#!/usr/bin/env python3
"""
Automatically update packs.json with correct emoji counts and metadata.
Also creates/updates individual pack.json files for each pack.
"""

import json
import os
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Any

def get_emoji_files(pack_dir: Path) -> List[str]:
    """Get list of emoji files in a pack directory with extensions."""
    emoji_files = []
    for file in pack_dir.iterdir():
        if file.suffix.lower() in ['.png', '.gif']:
            emoji_files.append(file.name)  # Include full filename with extension
    return sorted(emoji_files)

def load_existing_packs_json() -> Dict[str, Any]:
    """Load existing packs.json file."""
    packs_json_path = Path('packs.json')
    if packs_json_path.exists():
        with open(packs_json_path, 'r') as f:
            return json.load(f)
    
    # Default structure
    return {
        "version": "1.0.0",
        "lastUpdated": datetime.now().strftime("%Y-%m-%d"),
        "totalPacks": 0,
        "packs": []
    }

def load_pack_metadata(pack_dir: Path, pack_id: str) -> Dict[str, Any]:
    """Load metadata from pack.json or return defaults."""
    pack_json_path = pack_dir / 'pack.json'
    
    if pack_json_path.exists():
        with open(pack_json_path, 'r') as f:
            metadata = json.load(f)
    else:
        # Default metadata
        metadata = {}
    
    # Ensure required fields with defaults
    defaults = {
        "id": pack_id,
        "name": pack_id.replace('-', ' ').title(),
        "description": f"Emoji pack for {pack_id.replace('-', ' ')}",
        "category": "general",
        "author": "Community",
        "tags": [pack_id],
        "featured": False,
        "createdAt": datetime.now().strftime("%Y-%m-%d"),
        "updatedAt": datetime.now().strftime("%Y-%m-%d")
    }
    
    for key, value in defaults.items():
        if key not in metadata:
            metadata[key] = value
    
    return metadata

def generate_pack_preview(emoji_files: List[str], existing_preview: List[str] = None) -> List[str]:
    """Generate preview emoji list for a pack with extensions."""
    if existing_preview and len(existing_preview) >= 4:
        # Check if existing preview has extensions, if not add them
        valid_preview = []
        for preview_item in existing_preview:
            if '.' in preview_item:
                # Already has extension, check if file exists
                if preview_item in emoji_files:
                    valid_preview.append(preview_item)
            else:
                # No extension, try to find matching file
                for emoji_file in emoji_files:
                    if emoji_file.startswith(preview_item + '.'):
                        valid_preview.append(emoji_file)
                        break
        
        if len(valid_preview) >= 4:
            return valid_preview[:4]
    
    # Auto-generate preview from available emojis
    preview = []
    
    # Prioritize certain emoji names for preview
    priority_names = ['unicorn', 'rocket', 'fire', 'star', 'heart', 'party', 
                     'celebrate', 'wow', 'cool', 'awesome', 'loading', 'spinner']
    
    # Add priority emojis first
    for name in priority_names:
        for emoji in emoji_files:
            emoji_name = emoji.rsplit('.', 1)[0]  # Get name without extension
            if name in emoji_name.lower() and emoji not in preview:
                preview.append(emoji)
                if len(preview) >= 4:
                    return preview
    
    # Fill remaining with first available emojis
    for emoji in emoji_files:
        if emoji not in preview:
            preview.append(emoji)
            if len(preview) >= 4:
                return preview
    
    return preview

def update_pack_json_file(pack_dir: Path, metadata: Dict[str, Any], emoji_files: List[str]):
    """Create or update individual pack.json file."""
    pack_json_path = pack_dir / 'pack.json'
    
    # Add emoji list to metadata
    pack_metadata = {
        "id": metadata["id"],
        "name": metadata["name"],
        "description": metadata["description"],
        "category": metadata["category"],
        "author": metadata["author"],
        "tags": metadata["tags"],
        "emojis": emoji_files,
        "emojiCount": len(emoji_files),
        "preview": metadata.get("preview", []),
        "featured": metadata.get("featured", False),
        "createdAt": metadata.get("createdAt"),
        "updatedAt": datetime.now().strftime("%Y-%m-%d")
    }
    
    with open(pack_json_path, 'w') as f:
        json.dump(pack_metadata, f, indent=2)
    
    print(f"  ✅ Updated {pack_json_path}")

def main():
    """Main function to update packs.json."""
    images_dir = Path('images')
    
    if not images_dir.exists():
        print("❌ images/ directory not found")
        return
    
    # Load existing packs.json
    packs_data = load_existing_packs_json()
    existing_packs = {pack['id']: pack for pack in packs_data['packs']}
    
    # Process all pack directories
    updated_packs = []
    total_emoji_count = 0
    
    for pack_dir in sorted(images_dir.iterdir()):
        if not pack_dir.is_dir():
            continue
        
        pack_id = pack_dir.name
        print(f"\n📦 Processing pack: {pack_id}")
        
        # Get emoji files
        emoji_files = get_emoji_files(pack_dir)
        emoji_count = len(emoji_files)
        total_emoji_count += emoji_count
        
        print(f"  Found {emoji_count} emojis")
        
        # Get existing pack data or create new
        if pack_id in existing_packs:
            pack_info = existing_packs[pack_id]
            # Update count
            old_count = pack_info.get('emojiCount', 0)
            if old_count != emoji_count:
                print(f"  📊 Updated count: {old_count} → {emoji_count}")
            pack_info['emojiCount'] = emoji_count
        else:
            # New pack - load metadata from pack.json or use defaults
            pack_info = load_pack_metadata(pack_dir, pack_id)
            pack_info['emojiCount'] = emoji_count
            print(f"  🆕 New pack added")
        
        # Update preview
        pack_info['preview'] = generate_pack_preview(
            emoji_files, 
            pack_info.get('preview', [])
        )
        
        # Update timestamp
        pack_info['updatedAt'] = datetime.now().strftime("%Y-%m-%d")
        
        # Update individual pack.json file
        update_pack_json_file(pack_dir, pack_info, emoji_files)
        
        # Ensure pack has ID
        pack_info['id'] = pack_id
        
        updated_packs.append(pack_info)
    
    # Update packs.json
    packs_data['packs'] = updated_packs
    packs_data['totalPacks'] = len(updated_packs)
    packs_data['lastUpdated'] = datetime.now().strftime("%Y-%m-%d")
    
    # Write updated packs.json
    with open('packs.json', 'w') as f:
        json.dump(packs_data, f, indent=2)
    
    print(f"\n✅ Updated packs.json:")
    print(f"  - Total packs: {len(updated_packs)}")
    print(f"  - Total emojis: {total_emoji_count}")
    
    # Summary of changes
    new_packs = [p['id'] for p in updated_packs if p['id'] not in existing_packs]
    if new_packs:
        print(f"  - New packs: {', '.join(new_packs)}")

if __name__ == "__main__":
    main()
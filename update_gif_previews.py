#!/usr/bin/env python3
"""
Update preview arrays to include GIF files for better visibility
"""

import json
from pathlib import Path

# Load packs.json
packs_file = Path("packs.json")
with open(packs_file, 'r', encoding='utf-8') as f:
    packs_data = json.load(f)

# Update preview arrays for each pack
pack_updates = {
    "dev-essentials": ["loading_dots.gif", "compiling.gif", "shipit.png", "bug.png"],
    "korean-culture": ["bow.gif", "soju_pour.gif", "fighting.png", "heart-finger.png"],
    "korean-office": ["clock_6pm.gif", "overtime_meter.gif", "yagun.png", "hoesik.png"],
    "reactions": ["clapping.gif", "typing.gif", "mind_blown.gif", "thumbs_up.gif"],
    "startup-hustle": ["rocket_launch.gif", "loading_spinner.gif", "unicorn.png", "burn_rate.png"],
    "work-from-home": ["cat_walking.gif", "coffee_steam.gif", "connection_lost.gif", "pajamas.png"],
    "korean-words": ["loading.gif", "alert.gif", "ne.png", "hwaiting.png"]
}

# Update packs data
for pack in packs_data['packs']:
    pack_id = pack['id']
    if pack_id in pack_updates:
        # Check which files actually exist
        pack_dir = Path(f"images/{pack_id}")
        new_preview = []
        for file in pack_updates[pack_id]:
            if (pack_dir / file).exists():
                new_preview.append(file)
        
        # If we have valid files, update preview
        if new_preview:
            pack['preview'] = new_preview[:4]  # Keep max 4 items
            print(f"✅ Updated {pack_id} preview: {pack['preview']}")

# Save updated packs.json
with open(packs_file, 'w', encoding='utf-8') as f:
    json.dump(packs_data, f, indent=2, ensure_ascii=False)

print("\n✅ Updated packs.json with GIF previews")

# Also update individual pack.json files
for pack in packs_data['packs']:
    pack_id = pack['id']
    pack_json_path = Path(f"images/{pack_id}/pack.json")
    
    if pack_json_path.exists():
        with open(pack_json_path, 'r', encoding='utf-8') as f:
            pack_data = json.load(f)
        
        # Update preview in pack.json
        pack_data['preview'] = pack['preview']
        
        with open(pack_json_path, 'w', encoding='utf-8') as f:
            json.dump(pack_data, f, indent=2, ensure_ascii=False)
        
        print(f"✅ Updated images/{pack_id}/pack.json")
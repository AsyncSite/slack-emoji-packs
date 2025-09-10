#!/usr/bin/env python3
"""
Generate placeholder emoji images for all packs.
Creates 128x128 PNG images with emoji unicode characters.
"""

import json
import os
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
import hashlib

def get_color_from_name(name):
    """Generate a consistent color from emoji name."""
    hash_obj = hashlib.md5(name.encode())
    hash_hex = hash_obj.hexdigest()
    
    # Generate RGB from hash
    r = int(hash_hex[:2], 16)
    g = int(hash_hex[2:4], 16)
    b = int(hash_hex[4:6], 16)
    
    # Make colors more vibrant
    r = min(255, r + 50)
    g = min(255, g + 50)
    b = min(255, b + 50)
    
    return (r, g, b)

def create_emoji_image(unicode_char, name, output_path):
    """Create a 128x128 PNG with the emoji character."""
    size = 128
    img = Image.new('RGBA', (size, size), (255, 255, 255, 0))
    draw = ImageDraw.Draw(img)
    
    # Get background color based on name
    bg_color = get_color_from_name(name)
    
    # Draw circle background
    margin = 10
    draw.ellipse([margin, margin, size-margin, size-margin], 
                 fill=(*bg_color, 255))
    
    # Try to use system font that supports emoji
    font_size = 60
    try:
        # Try different fonts that might support emoji
        font_paths = [
            '/System/Library/Fonts/Apple Color Emoji.ttc',  # macOS
            '/usr/share/fonts/truetype/noto/NotoColorEmoji.ttf',  # Linux
            '/System/Library/Fonts/Helvetica.ttc',  # macOS fallback
            '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf',  # Linux fallback
        ]
        
        font = None
        for font_path in font_paths:
            if os.path.exists(font_path):
                try:
                    font = ImageFont.truetype(font_path, font_size)
                    break
                except:
                    continue
        
        if not font:
            font = ImageFont.load_default()
    except:
        font = ImageFont.load_default()
    
    # Draw text
    text = unicode_char
    
    # Get text bounding box for centering
    bbox = draw.textbbox((0, 0), text, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]
    
    x = (size - text_width) / 2
    y = (size - text_height) / 2 - bbox[1]
    
    # Draw white outline for better visibility
    outline_width = 2
    for dx in range(-outline_width, outline_width + 1):
        for dy in range(-outline_width, outline_width + 1):
            if dx != 0 or dy != 0:
                draw.text((x + dx, y + dy), text, fill=(255, 255, 255, 255), font=font)
    
    # Draw main text
    draw.text((x, y), text, fill=(0, 0, 0, 255), font=font)
    
    # Save image
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    img.save(output_path, 'PNG')
    print(f"Created: {output_path}")

def main():
    """Generate all emoji images based on pack data."""
    base_dir = Path(__file__).parent
    packs_dir = base_dir / 'packs'
    images_dir = base_dir / 'images'
    
    # Process each pack directory
    for pack_dir in packs_dir.iterdir():
        if pack_dir.is_dir():
            pack_json = pack_dir / 'pack.json'
            if pack_json.exists():
                with open(pack_json, 'r', encoding='utf-8') as f:
                    pack_data = json.load(f)
                
                pack_id = pack_data['id']
                print(f"\nProcessing pack: {pack_id}")
                
                # Create images for each emoji
                for emoji in pack_data['emojis']:
                    emoji_name = emoji['name']
                    unicode_char = emoji.get('unicode', '❓')
                    
                    # Create image path
                    image_path = images_dir / pack_id / f"{emoji_name}.png"
                    
                    # Generate image
                    create_emoji_image(unicode_char, emoji_name, str(image_path))
    
    print("\n✅ All emoji images generated!")
    
    # Create a simple index.html for preview
    preview_html = base_dir / 'preview.html'
    with open(preview_html, 'w') as f:
        f.write("""<!DOCTYPE html>
<html>
<head>
    <title>Emoji Pack Preview</title>
    <style>
        body { font-family: Arial, sans-serif; padding: 20px; }
        .pack { margin-bottom: 40px; }
        .pack h2 { color: #333; border-bottom: 2px solid #ccc; padding-bottom: 10px; }
        .emoji-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(150px, 1fr)); gap: 20px; }
        .emoji-item { text-align: center; }
        .emoji-item img { width: 64px; height: 64px; }
        .emoji-name { font-size: 12px; margin-top: 5px; }
    </style>
</head>
<body>
    <h1>Slack Emoji Packs Preview</h1>
""")
        
        # Add each pack
        for pack_dir in sorted(packs_dir.iterdir()):
            if pack_dir.is_dir():
                pack_json = pack_dir / 'pack.json'
                if pack_json.exists():
                    with open(pack_json, 'r', encoding='utf-8') as pf:
                        pack_data = json.load(pf)
                    
                    f.write(f'<div class="pack">\n')
                    f.write(f'<h2>{pack_data["name"]}</h2>\n')
                    f.write(f'<p>{pack_data["description"]}</p>\n')
                    f.write('<div class="emoji-grid">\n')
                    
                    for emoji in pack_data['emojis']:
                        img_path = f'images/{pack_data["id"]}/{emoji["name"]}.png'
                        f.write(f'<div class="emoji-item">\n')
                        f.write(f'<img src="{img_path}" alt="{emoji["name"]}">\n')
                        f.write(f'<div class="emoji-name">:{emoji["name"]}:</div>\n')
                        f.write('</div>\n')
                    
                    f.write('</div>\n')
                    f.write('</div>\n')
        
        f.write("""
</body>
</html>
""")
    
    print(f"Preview HTML created: {preview_html}")

if __name__ == '__main__':
    main()
#!/usr/bin/env python3

from PIL import Image, ImageDraw, ImageFont
import os

# Detailed emotion emojis
EMOTION_EMOJIS = [
    # Basic emotions expanded
    ("upset", "속상해", "#9E9E9E", "속상한 기분"),
    ("frustrated", "답답해", "#FF5722", "답답한 상태"),
    ("refreshed", "시원해", "#00BCD4", "시원한 느낌"),
    ("sweet_potato", "고구마", "#8D6E63", "답답함 (고구마)"),
    ("cider", "사이다", "#4CAF50", "시원함 (사이다)"),
    ("honey_jam", "꿀잼", "#FFC107", "매우 재밌음"),
    ("no_jam", "노잼", "#757575", "재미없음"),
    ("nuclear_honey", "핵꿀잼", "#FFD700", "극도로 재밌음"),
    
    # Detailed feelings
    ("touched", "감동", "#E91E63", "감동받음"),
    ("proud", "뿌듯", "#7C4DFF", "뿌듯함"),
    ("embarrassed", "민망", "#FF7043", "민망함"),
    ("awkward", "어색", "#78909C", "어색한 상황"),
    ("confused", "헷갈려", "#9C27B0", "헷갈림"),
    ("curious", "궁금", "#3F51B5", "궁금함"),
    ("relieved", "다행", "#66BB6A", "안도감"),
    ("disappointed", "실망", "#616161", "실망스러움"),
    ("amazed", "놀라워", "#FF6B6B", "놀라움"),
    ("jealous", "부러워", "#8BC34A", "부러움"),
    ("lonely", "외로워", "#607D8B", "외로움"),
    ("nervous", "긴장", "#FF9800", "긴장됨"),
    
    # Intensity expressions
    ("very_good", "개좋아", "#4CAF50", "매우 좋음"),
    ("crazy_good", "미쳤다", "#FF1744", "미친듯이 좋음"),
    ("goosebumps", "소름", "#7B1FA2", "소름돋음"),
    ("dying", "죽겠다", "#424242", "극한 상태"),
    ("exploding", "터진다", "#F44336", "폭발할 것 같음"),
    ("melting", "녹는다", "#FF80AB", "녹아내림"),
    ("flying", "날아간다", "#03A9F4", "날아갈 것 같음"),
    
    # Mood states
    ("hyped", "텐션업", "#FF6F00", "기분 상승"),
    ("down", "텐션다운", "#455A64", "기분 하락"),
    ("motivated", "의욕", "#4CAF50", "의욕 충만"),
    ("lazy", "귀찮", "#90A4AE", "귀찮음"),
    ("energetic", "활발", "#FFEB3B", "활발함"),
    ("tired", "피곤", "#795548", "피곤함"),
    ("sleepy", "졸려", "#9E9E9E", "졸림"),
    ("excited", "신나", "#FF4081", "신남"),
    ("bored", "심심", "#BDBDBD", "심심함"),
    ("focused", "집중", "#1565C0", "집중 상태"),
    
    # Reactions
    ("shocked", "충격", "#D32F2F", "충격받음"),
    ("mind_blown", "멘붕", "#6A1B9A", "멘탈 붕괴"),
    ("speechless", "할말없", "#546E7A", "할 말이 없음"),
    ("cant_believe", "믿기지않아", "#FF6E40", "믿을 수 없음"),
    ("expected", "예상했어", "#43A047", "예상한 대로"),
    ("unexpected", "예상밖", "#EF5350", "예상 밖"),
    ("understood", "이해됨", "#26A69A", "이해함"),
    ("dont_understand", "이해안됨", "#EC407A", "이해 못함"),
]

def create_simple_text_emoji(text, color, name, output_dir, bg_type="transparent"):
    """Create a simple text emoji with specified background"""
    scale = 4
    size = 128 * scale
    
    # Create image with specified background
    if bg_type == "white":
        img = Image.new('RGBA', (size, size), (255, 255, 255, 255))
    else:  # transparent
        img = Image.new('RGBA', (size, size), (255, 255, 255, 0))
    
    draw = ImageDraw.Draw(img)
    
    # Try to use a good Korean font
    font_paths = [
        "/System/Library/Fonts/AppleSDGothicNeo.ttc",
        "/Library/Fonts/NanumGothic.ttf",
        "/usr/share/fonts/truetype/nanum/NanumGothic.ttf",
    ]
    
    font = None
    # Adjust font size based on text length
    if len(text) <= 2:
        base_size = 48 * scale
    elif len(text) <= 3:
        base_size = 36 * scale
    elif len(text) <= 4:
        base_size = 28 * scale
    elif len(text) <= 5:
        base_size = 24 * scale
    elif len(text) <= 6:
        base_size = 20 * scale
    else:
        base_size = 18 * scale
    
    for font_path in font_paths:
        if os.path.exists(font_path):
            try:
                font = ImageFont.truetype(font_path, base_size)
                break
            except:
                continue
    
    if not font:
        font = ImageFont.load_default()
    
    # Get text dimensions
    bbox = draw.textbbox((0, 0), text, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]
    
    # Center the text
    x = (size - text_width) // 2
    y = (size - text_height) // 2 - bbox[1]
    
    # Draw shadow for better visibility (only on transparent bg)
    if bg_type == "transparent":
        shadow_offset = 3 * scale
        draw.text((x + shadow_offset, y + shadow_offset), text, 
                 fill=(0, 0, 0, 100), font=font)
    
    # Draw main text
    draw.text((x, y), text, fill=color, font=font)
    
    # Downscale for anti-aliasing
    img = img.resize((128, 128), Image.Resampling.LANCZOS)
    
    # Save with appropriate suffix
    suffix = "_white" if bg_type == "white" else ""
    filename = f"{name}{suffix}.png"
    filepath = os.path.join(output_dir, filename)
    img.save(filepath, 'PNG')
    print(f"Created: {filename}")
    return filename

def main():
    output_dir = "/Users/rene/asyncsite/slack-emoji-packs/images/korean-words"
    
    print("Creating detailed emotion emojis...")
    created_files = []
    
    for name, text, color, description in EMOTION_EMOJIS:
        # Create transparent background version
        created_files.append(create_simple_text_emoji(text, color, name, output_dir, "transparent"))
        # Create white background version  
        created_files.append(create_simple_text_emoji(text, color, name + "_bg", output_dir, "white"))
    
    print(f"\n✅ Created {len(created_files)} emotion emojis")
    print("\nCreated files:")
    for f in created_files[:10]:  # Show first 10 as sample
        print(f"  - {f}")
    print(f"  ... and {len(created_files) - 10} more")
    
    return created_files

if __name__ == "__main__":
    main()
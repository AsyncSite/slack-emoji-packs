#!/usr/bin/env python3

from PIL import Image, ImageDraw, ImageFont
import os

# Game/Internet culture emojis
GAME_CULTURE_EMOJIS = [
    # Common gaming/internet abbreviations
    ("gg", "ㅈㅈ", "#FF6B6B", "Good Game / 항복"),
    ("ss", "ㅅㅅ", "#4CAF50", "수고하셨습니다"),
    ("hi", "ㅎㅇ", "#2196F3", "하이 / 안녕"),
    ("bye", "ㅂㅇ", "#9C27B0", "바이 / 잘가"),
    ("ok_short", "ㅇㅋ", "#00BCD4", "오케이"),
    ("real_q", "ㄹㅇ?", "#FF9800", "리얼? / 진짜?"),
    ("agree", "ㅇㅈ", "#8BC34A", "인정"),
    ("grats", "ㅊㅋ", "#E91E63", "축하"),
    ("thanks_short", "ㄱㅅ", "#3F51B5", "감사"),
    ("sorry_short", "ㅈㅅ", "#795548", "죄송"),
    ("no_way", "ㄴㄴ", "#F44336", "노노 / 아니"),
    ("yes_yes", "ㅇㅇ", "#4CAF50", "응응 / 맞아"),
    ("fine", "ㄱㅊ", "#00ACC1", "괜찮아"),
    ("wait", "ㅈㄷ", "#FFC107", "잠시만"),
    ("go_go", "ㄱㄱ", "#FF5722", "고고 / 가자"),
    
    # Full gaming terms
    ("noob", "뉴비", "#9E9E9E", "초보자"),
    ("carry", "캐리", "#FFD700", "팀을 이끌다"),
    ("troll", "트롤", "#8B4513", "방해꾼"),
    ("op", "사기", "#FF1744", "Overpowered"),
    ("nerf", "너프", "#7B1FA2", "하향 조정"),
    ("buff", "버프", "#1976D2", "상향 조정"),
    ("inting", "던짐", "#424242", "일부러 지기"),
    ("dodge", "닷지", "#FF6F00", "게임 회피"),
    ("ban", "밴", "#D32F2F", "금지"),
    ("pick", "픽", "#388E3C", "선택"),
    ("mid", "미드", "#5E35B1", "중앙 라인"),
    ("top", "탑", "#0288D1", "상단 라인"),
    ("bot", "봇", "#C2185B", "하단 라인"),
    ("jungle", "정글", "#2E7D32", "정글러"),
    ("sup", "서폿", "#00838F", "서포터"),
    ("adc", "원딜", "#BF360C", "원거리 딜러"),
    ("tank", "탱커", "#37474F", "탱크"),
    ("dps", "딜러", "#B71C1C", "데미지 딜러"),
    
    # Gaming reactions
    ("ez", "이지", "#4CAF50", "쉬워"),
    ("hard", "하드", "#F44336", "어려워"),
    ("clutch", "클러치", "#FFD700", "극적인 플레이"),
    ("ace", "에이스", "#FF6B6B", "전원 처치"),
    ("penta", "펜타", "#9C27B0", "5연속 킬"),
    ("first", "퍼블", "#2196F3", "첫 킬"),
    ("comeback", "역전", "#FF9800", "컴백"),
    ("throw", "스로우", "#795548", "던지다"),
    ("rage", "빡겜", "#D32F2F", "화난 게임"),
    ("tryhard", "빡겜러", "#FF5722", "열심히 하는 사람"),
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
    base_size = 40 * scale if len(text) <= 2 else 32 * scale if len(text) <= 3 else 24 * scale
    
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
    
    print("Creating game/internet culture emojis...")
    created_files = []
    
    for name, text, color, description in GAME_CULTURE_EMOJIS:
        # Create transparent background version
        created_files.append(create_simple_text_emoji(text, color, name, output_dir, "transparent"))
        # Create white background version
        created_files.append(create_simple_text_emoji(text, color, name + "_bg", output_dir, "white"))
    
    print(f"\n✅ Created {len(created_files)} game/internet culture emojis")
    print("\nCreated files:")
    for f in created_files[:10]:  # Show first 10 as sample
        print(f"  - {f}")
    print(f"  ... and {len(created_files) - 10} more")
    
    return created_files

if __name__ == "__main__":
    main()
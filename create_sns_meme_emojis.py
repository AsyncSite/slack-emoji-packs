#!/usr/bin/env python3

from PIL import Image, ImageDraw, ImageFont
import os

# SNS/Meme emojis
SNS_MEME_EMOJIS = [
    # Popular memes
    ("tmi", "TMI", "#FF6B6B", "Too Much Information"),
    ("awkward_atmosphere", "갑분싸", "#9E9E9E", "갑자기 분위기 싸해짐"),
    ("whatever_tv", "어쩔티비", "#9C27B0", "어쩌라고 티비나 봐"),
    ("makes_me_mad", "킹받네", "#F44336", "킹받네 (화남)"),
    ("real_authentic", "찐", "#2196F3", "진짜/진정한"),
    ("legend", "레전드", "#FFD700", "전설적인"),
    ("goat", "역대급", "#FF6F00", "역대 최고"),
    ("flex", "플렉스", "#4CAF50", "자랑하기"),
    ("insane", "미친", "#E91E63", "미친/대박"),
    ("no_answer", "답없다", "#757575", "답이 없다"),
    
    # Internet slang
    ("lol", "ㅋㅋㅋㅋㅋ", "#FFC107", "크크크크크"),
    ("crying_laugh", "ㅠㅠ", "#03A9F4", "흑흑"),
    ("haha", "하하하", "#8BC34A", "하하하"),
    ("hehe", "히히", "#FF80AB", "히히"),
    ("hoho", "호호", "#CE93D8", "호호"),
    ("keke", "키키", "#FFAB91", "키키"),
    
    # Trendy expressions
    ("like", "좋아요", "#E91E63", "좋아요"),
    ("heart", "하트", "#F06292", "하트"),
    ("follow", "팔로우", "#2196F3", "팔로우"),
    ("subscribe", "구독", "#F44336", "구독"),
    ("notification", "알림", "#FF9800", "알림 설정"),
    ("share", "공유", "#4CAF50", "공유하기"),
    ("retweet", "리트윗", "#00BCD4", "리트윗"),
    ("dm", "디엠", "#9C27B0", "다이렉트 메시지"),
    ("mention", "멘션", "#3F51B5", "멘션/태그"),
    
    # Gen Z slang
    ("no_cap", "ㄹㅇ", "#FF5722", "진짜로"),
    ("facts", "팩트", "#607D8B", "사실"),
    ("vibe", "바이브", "#AB47BC", "분위기/느낌"),
    ("mood", "무드", "#7E57C2", "기분/분위기"),
    ("slay", "찢었다", "#E91E63", "완전 잘했다"),
    ("periodt", "그말", "#F44336", "그 말이야"),
    ("stan", "스탠", "#EC407A", "열렬히 지지"),
    ("ship", "커플링", "#F06292", "커플 응원"),
    ("bias", "최애", "#E91E63", "최고로 좋아하는"),
    ("ootd", "오오티디", "#9C27B0", "오늘의 옷"),
    
    # Reaction memes
    ("shocked_pikachu", "헐", "#FFEB3B", "헐/놀람"),
    ("confused", "???", "#9E9E9E", "뭐야/이해불가"),
    ("sus", "의심", "#FF5722", "수상함"),
    ("cap", "구라", "#424242", "거짓말"),
    ("bet", "ㅇㅇ", "#4CAF50", "알았어/좋아"),
    ("yeet", "던짐", "#FF9800", "던지다/버리다"),
    ("bruh", "형", "#795548", "브러/실망"),
    ("oof", "우프", "#607D8B", "아야/실수"),
    
    # Korean specific memes
    ("mz", "MZ", "#00BCD4", "MZ세대"),
    ("boomer", "꼰대", "#757575", "꼰대/부머"),
    ("insider", "인싸", "#4CAF50", "인사이더"),
    ("outsider", "아싸", "#9E9E9E", "아웃사이더"),
    ("youth_talk", "요즘말", "#FF6B6B", "요즘 말"),
    ("old_school", "라떼", "#8D6E63", "옛날 얘기"),
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
    elif len(text) <= 7:
        base_size = 20 * scale
    else:
        base_size = 16 * scale
    
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
    
    print("Creating SNS/meme emojis...")
    created_files = []
    
    for name, text, color, description in SNS_MEME_EMOJIS:
        # Create transparent background version
        created_files.append(create_simple_text_emoji(text, color, name, output_dir, "transparent"))
        # Create white background version  
        created_files.append(create_simple_text_emoji(text, color, name + "_bg", output_dir, "white"))
    
    print(f"\n✅ Created {len(created_files)} SNS/meme emojis")
    print("\nCreated files:")
    for f in created_files[:10]:  # Show first 10 as sample
        print(f"  - {f}")
    print(f"  ... and {len(created_files) - 10} more")
    
    return created_files

if __name__ == "__main__":
    main()
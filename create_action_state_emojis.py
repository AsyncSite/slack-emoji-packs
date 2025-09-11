#!/usr/bin/env python3

from PIL import Image, ImageDraw, ImageFont
import os

# Action/State emojis
ACTION_STATE_EMOJIS = [
    # Actions
    ("lets_go", "가보자고", "#FF6B6B", "가보자고!"),
    ("just_do_it", "일단고", "#4CAF50", "일단 하고 보자"),
    ("gaza", "가즈아", "#FF5722", "가즈아!"),
    ("developing", "개발중", "#2196F3", "개발 중"),
    ("deploying", "배포중", "#9C27B0", "배포 중"),
    ("rollback", "롤백", "#F44336", "롤백"),
    ("testing", "테스트중", "#FF9800", "테스트 중"),
    ("debugging", "디버깅", "#795548", "디버깅 중"),
    ("reviewing_code", "코드리뷰", "#00BCD4", "코드 리뷰"),
    ("merging", "머지중", "#4CAF50", "머지 중"),
    ("fixing", "수정중", "#FF7043", "수정 중"),
    ("building", "빌드중", "#3F51B5", "빌드 중"),
    
    # States
    ("loading", "로딩중", "#03A9F4", "로딩 중"),
    ("processing", "처리중", "#00ACC1", "처리 중"),
    ("waiting", "대기중", "#FFC107", "대기 중"),
    ("ready", "준비완료", "#8BC34A", "준비 완료"),
    ("done", "완료", "#4CAF50", "완료"),
    ("failed", "실패", "#F44336", "실패"),
    ("success", "성공", "#43A047", "성공"),
    ("error", "에러", "#D32F2F", "에러 발생"),
    ("warning", "경고", "#FF9800", "경고"),
    ("info", "정보", "#2196F3", "정보"),
    
    # Working states
    ("working", "작업중", "#1976D2", "작업 중"),
    ("thinking", "생각중", "#9C27B0", "생각 중"),
    ("searching", "검색중", "#00BCD4", "검색 중"),
    ("writing", "작성중", "#607D8B", "작성 중"),
    ("reading", "읽는중", "#455A64", "읽는 중"),
    ("listening", "듣는중", "#7B1FA2", "듣는 중"),
    ("watching", "보는중", "#5E35B1", "보는 중"),
    ("learning", "학습중", "#3949AB", "학습 중"),
    
    # Movement actions
    ("coming", "오는중", "#26A69A", "오는 중"),
    ("going", "가는중", "#26C6DA", "가는 중"),
    ("running", "뛰는중", "#FF5252", "뛰는 중"),
    ("walking", "걷는중", "#66BB6A", "걷는 중"),
    ("driving", "운전중", "#FFA726", "운전 중"),
    ("arriving", "도착", "#4CAF50", "도착"),
    ("departing", "출발", "#FF6F00", "출발"),
    
    # Communication actions
    ("calling", "통화중", "#4CAF50", "통화 중"),
    ("texting", "문자중", "#2196F3", "문자 중"),
    ("typing", "입력중", "#00BCD4", "입력 중"),
    ("recording", "녹음중", "#F44336", "녹음 중"),
    ("streaming", "방송중", "#E91E63", "스트리밍 중"),
    ("uploading", "업로드중", "#9C27B0", "업로드 중"),
    ("downloading", "다운로드중", "#3F51B5", "다운로드 중"),
    
    # Daily actions
    ("sleeping", "자는중", "#9E9E9E", "자는 중"),
    ("waking", "일어남", "#FFEB3B", "일어남"),
    ("eating", "먹는중", "#FF9800", "먹는 중"),
    ("drinking", "마시는중", "#03A9F4", "마시는 중"),
    ("exercising", "운동중", "#FF5722", "운동 중"),
    ("studying", "공부중", "#5C6BC0", "공부 중"),
    ("gaming", "게임중", "#7E57C2", "게임 중"),
    ("shopping", "쇼핑중", "#EC407A", "쇼핑 중"),
    ("cleaning", "청소중", "#26A69A", "청소 중"),
    ("cooking", "요리중", "#FF7043", "요리 중"),
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
    
    print("Creating action/state emojis...")
    created_files = []
    
    for name, text, color, description in ACTION_STATE_EMOJIS:
        # Skip lets_go since it already exists
        if name == "lets_go":
            continue
        # Create transparent background version
        created_files.append(create_simple_text_emoji(text, color, name, output_dir, "transparent"))
        # Create white background version  
        created_files.append(create_simple_text_emoji(text, color, name + "_bg", output_dir, "white"))
    
    print(f"\n✅ Created {len(created_files)} action/state emojis")
    print("\nCreated files:")
    for f in created_files[:10]:  # Show first 10 as sample
        print(f"  - {f}")
    print(f"  ... and {len(created_files) - 10} more")
    
    return created_files

if __name__ == "__main__":
    main()
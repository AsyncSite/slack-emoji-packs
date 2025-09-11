#!/usr/bin/env python3

from PIL import Image, ImageDraw, ImageFont
import os

# Office life extension emojis
OFFICE_EMOJIS = [
    # Common office terms
    ("approval_request", "결재부탁", "#2196F3", "결재 부탁드립니다"),
    ("reviewing", "검토중", "#FF9800", "검토 중"),
    ("approved", "승인", "#4CAF50", "승인됨"),
    ("rejected", "반려", "#F44336", "반려됨"),
    ("wfh", "재택", "#9C27B0", "재택근무"),
    ("business_trip", "출장", "#3F51B5", "출장 중"),
    ("meeting", "회의중", "#FF5722", "회의 중"),
    ("lunch", "점심", "#8BC34A", "점심시간"),
    ("overtime", "야근", "#795548", "야근 중"),
    ("leave_work", "퇴근", "#00BCD4", "퇴근"),
    ("vacation", "휴가", "#E91E63", "휴가 중"),
    ("sick_leave", "병가", "#607D8B", "병가"),
    
    # Office statuses
    ("busy", "바쁨", "#D32F2F", "바쁜 상태"),
    ("available", "가능", "#388E3C", "응대 가능"),
    ("in_progress", "진행중", "#1976D2", "진행 중"),
    ("completed", "완료", "#43A047", "완료됨"),
    ("pending", "대기", "#FFA726", "대기 중"),
    ("urgent", "긴급", "#E53935", "긴급 건"),
    ("important", "중요", "#AB47BC", "중요 표시"),
    ("deadline", "마감", "#EF5350", "마감일"),
    ("asap", "ASAP", "#FF1744", "가능한 빨리"),
    ("fyi", "참고", "#42A5F5", "참고용"),
    ("cc", "참조", "#26A69A", "참조"),
    
    # Meeting related
    ("standup", "스탠드업", "#5C6BC0", "스탠드업 미팅"),
    ("retro", "회고", "#7E57C2", "회고 미팅"),
    ("planning", "기획", "#29B6F6", "기획 회의"),
    ("sprint", "스프린트", "#26C6DA", "스프린트"),
    ("demo", "데모", "#66BB6A", "데모 시연"),
    ("presentation", "발표", "#FFA726", "프레젠테이션"),
    ("brainstorm", "브레인스토밍", "#FFCA28", "브레인스토밍"),
    ("sync", "싱크", "#8D6E63", "동기화 미팅"),
    ("1on1", "1대1", "#78909C", "1대1 미팅"),
    
    # Documents
    ("report", "보고서", "#546E7A", "보고서"),
    ("proposal", "제안서", "#5E35B1", "제안서"),
    ("contract", "계약서", "#43A047", "계약서"),
    ("invoice", "인보이스", "#FB8C00", "송장"),
    ("receipt", "영수증", "#6D4C41", "영수증"),
    ("draft", "초안", "#757575", "초안"),
    ("final", "최종", "#2E7D32", "최종본"),
    ("revision", "수정", "#F4511E", "수정 필요"),
    
    # Team related
    ("teamwork", "팀워크", "#4CAF50", "팀워크"),
    ("collaboration", "협업", "#2196F3", "협업"),
    ("handover", "인수인계", "#9C27B0", "인수인계"),
    ("onboarding", "온보딩", "#00ACC1", "온보딩"),
    ("training", "교육", "#7B1FA2", "교육/트레이닝"),
    ("workshop", "워크샵", "#FF6F00", "워크샵"),
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
    else:
        base_size = 20 * scale
    
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
    
    print("Creating office life extension emojis...")
    created_files = []
    
    for name, text, color, description in OFFICE_EMOJIS:
        # Create transparent background version
        created_files.append(create_simple_text_emoji(text, color, name, output_dir, "transparent"))
        # Create white background version  
        created_files.append(create_simple_text_emoji(text, color, name + "_bg", output_dir, "white"))
    
    print(f"\n✅ Created {len(created_files)} office life emojis")
    print("\nCreated files:")
    for f in created_files[:10]:  # Show first 10 as sample
        print(f"  - {f}")
    print(f"  ... and {len(created_files) - 10} more")
    
    return created_files

if __name__ == "__main__":
    main()
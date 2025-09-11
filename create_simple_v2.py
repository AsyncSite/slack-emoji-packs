#!/usr/bin/env python3
from PIL import Image, ImageDraw, ImageFont
import os
from pathlib import Path

# 출력 디렉토리
OUTPUT_DIR = Path("images/korean-words-simple")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# 심플 버전 이모지 정의
SIMPLE_EMOJIS = [
    # 필수 표현들
    ("ne_simple", "네", "#4CAF50", "white"),
    ("ne_trans", "네", "#4CAF50", "transparent"),
    ("ani_simple", "아니", "#F44336", "white"),
    ("ani_trans", "아니", "#F44336", "transparent"),
    ("okay_simple", "오케이", "#4CAF50", "white"),
    ("okay_trans", "오케이", "#4CAF50", "transparent"),
    
    # 인사
    ("annyeong_simple", "안녕", "#2196F3", "white"),
    ("annyeong_trans", "안녕", "#2196F3", "transparent"),
    ("gamsa_simple", "감사", "#E91E63", "white"),
    ("gamsa_trans", "감사", "#E91E63", "transparent"),
    
    # 응원/격려
    ("hwaiting_simple", "화이팅", "#FF6B6B", "white"),
    ("hwaiting_trans", "화이팅", "#FF6B6B", "transparent"),
    
    # 감정
    ("daebak_simple", "대박", "#FF1744", "white"),
    ("daebak_trans", "대박", "#FF1744", "transparent"),
    
    # 상태
    ("wanryo_simple", "완료", "#4CAF50", "white"),
    ("wanryo_trans", "완료", "#4CAF50", "transparent"),
    
    # 웃음
    ("kkk_simple", "ㅋㅋㅋ", "#FFD700", "white"),
    ("kkk_trans", "ㅋㅋㅋ", "#FFD700", "transparent"),
]

def hex_to_rgba(hex_color):
    """Convert hex color to RGBA tuple"""
    hex_color = hex_color.lstrip('#')
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4)) + (255,)

def create_simple_static(name, korean, color, bg_type):
    """Create a simple text emoji with larger text"""
    # 더 큰 캔버스에서 작업 후 축소
    scale = 4
    img = Image.new('RGBA', (128 * scale, 128 * scale), 
                    (255, 255, 255, 255) if bg_type == "white" else (255, 255, 255, 0))
    draw = ImageDraw.Draw(img)
    
    # 폰트 크기 (매우 크게)
    if len(korean) == 1:
        font_size = 400
    elif len(korean) == 2:
        font_size = 320
    elif len(korean) == 3:
        font_size = 240
    elif len(korean) == 4:
        font_size = 180
    else:
        font_size = 160
    
    # 여러 폰트 시도
    fonts_to_try = [
        "/System/Library/Fonts/AppleSDGothicNeo.ttc",
        "/System/Library/Fonts/Supplemental/AppleGothic.ttc",
        "/Library/Fonts/Arial Unicode.ttf",
        "/System/Library/Fonts/Helvetica.ttc"
    ]
    
    font = None
    for font_path in fonts_to_try:
        try:
            font = ImageFont.truetype(font_path, font_size)
            break
        except:
            continue
    
    # 폰트를 찾지 못한 경우 기본 처리
    if not font:
        # 직접 텍스트 그리기 (큰 크기로)
        text_color = hex_to_rgba(color)
        # 간단한 박스로 표현
        box_size = 300
        x = (128 * scale - box_size) // 2
        y = (128 * scale - box_size) // 2
        
        # 텍스트 대신 색상 박스
        if bg_type == "white":
            draw.rectangle([x, y, x + box_size, y + box_size], outline=text_color, width=20)
        else:
            draw.rectangle([x, y, x + box_size, y + box_size], fill=(*text_color[:3], 50))
        
        # 임시 텍스트
        draw.text((128 * scale // 2, 128 * scale // 2), korean, 
                 fill=text_color, anchor="mm")
    else:
        # 폰트가 있는 경우
        bbox = draw.textbbox((0, 0), korean, font=font)
        text_width = bbox[2] - bbox[0]
        text_height = bbox[3] - bbox[1]
        x = (128 * scale - text_width) // 2
        y = (128 * scale - text_height) // 2
        
        text_color = hex_to_rgba(color)
        
        # 배경이 흰색인 경우 약간의 그림자 효과
        if bg_type == "white":
            shadow_offset = 8
            draw.text((x + shadow_offset, y + shadow_offset), korean, 
                     fill=(200, 200, 200, 255), font=font)
        
        # 메인 텍스트
        draw.text((x, y), korean, fill=text_color, font=font)
    
    # 축소해서 부드럽게
    img = img.resize((128, 128), Image.Resampling.LANCZOS)
    
    return img

def create_simple_gif(name, korean, color, anim_type):
    """Create simple animated text GIF"""
    frames = []
    scale = 4
    
    for frame_idx in range(4):
        img = Image.new('RGBA', (128 * scale, 128 * scale), (255, 255, 255, 0))
        draw = ImageDraw.Draw(img)
        
        # 폰트 설정
        base_size = 320 if len(korean) <= 2 else 240 if len(korean) <= 3 else 180
        
        # 애니메이션 효과
        if anim_type == "pulse":
            font_size = base_size + int(40 * (1 if frame_idx % 2 == 0 else -1))
        elif anim_type == "bounce":
            y_offset = [0, -40, 0, 40][frame_idx]
            font_size = base_size
        else:
            font_size = base_size
            y_offset = 0
        
        try:
            font = ImageFont.truetype("/System/Library/Fonts/AppleSDGothicNeo.ttc", font_size)
        except:
            font = None
        
        text_color = hex_to_rgba(color)
        
        if font:
            bbox = draw.textbbox((0, 0), korean, font=font)
            text_width = bbox[2] - bbox[0]
            text_height = bbox[3] - bbox[1]
            x = (128 * scale - text_width) // 2
            y = (128 * scale - text_height) // 2 + (y_offset if 'y_offset' in locals() else 0)
            
            draw.text((x, y), korean, fill=text_color, font=font)
        
        # 축소
        img = img.resize((128, 128), Image.Resampling.LANCZOS)
        frames.append(img)
    
    return frames

# 메인 실행
print("심플한 한국어 이모지 생성 (v2)...")

# 정적 이모지 생성
for name, korean, color, bg_type in SIMPLE_EMOJIS:
    try:
        img = create_simple_static(name, korean, color, bg_type)
        filepath = OUTPUT_DIR / f"{name}.png"
        img.save(filepath, "PNG")
        bg_desc = "white bg" if bg_type == "white" else "transparent"
        print(f"✓ {name}.png - {korean} ({bg_desc})")
    except Exception as e:
        print(f"✗ {name} 생성 실패: {e}")

# GIF 샘플
GIF_SAMPLES = [
    ("loading_simple", "로딩", "#2196F3", "pulse"),
    ("hwaiting_gif", "화이팅", "#FF6B6B", "bounce"),
    ("kkk_gif", "ㅋㅋㅋ", "#FFD700", "pulse"),
]

for name, korean, color, anim_type in GIF_SAMPLES:
    try:
        frames = create_simple_gif(name, korean, color, anim_type)
        if frames:
            filepath = OUTPUT_DIR / f"{name}.gif"
            frames[0].save(
                filepath,
                save_all=True,
                append_images=frames[1:],
                duration=250,
                loop=0,
                disposal=2
            )
            print(f"✓ {name}.gif - {korean} ({anim_type})")
    except Exception as e:
        print(f"✗ {name} 생성 실패: {e}")

print(f"\n완료! {OUTPUT_DIR}에 생성됨")
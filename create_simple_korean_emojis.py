#!/usr/bin/env python3
from PIL import Image, ImageDraw, ImageFont
import os
from pathlib import Path

# 출력 디렉토리
OUTPUT_DIR = Path("images/korean-words-simple")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# 심플 버전 이모지 정의 (이름, 한글, 색상, 배경타입)
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
    ("jjang_simple", "짱", "#FFD700", "white"),
    ("jjang_trans", "짱", "#FFD700", "transparent"),
    
    # 감정
    ("daebak_simple", "대박", "#FF1744", "white"),
    ("daebak_trans", "대박", "#FF1744", "transparent"),
    ("heol_simple", "헐", "#FF5722", "white"),
    ("heol_trans", "헐", "#FF5722", "transparent"),
    
    # 상태
    ("wanryo_simple", "완료", "#4CAF50", "white"),
    ("wanryo_trans", "완료", "#4CAF50", "transparent"),
    ("hwagin_simple", "확인", "#4CAF50", "white"),
    ("hwagin_trans", "확인", "#4CAF50", "transparent"),
    
    # 웃음
    ("kkk_simple", "ㅋㅋㅋ", "#FFD700", "white"),
    ("kkk_trans", "ㅋㅋㅋ", "#FFD700", "transparent"),
    
    # 업무
    ("toegeun_simple", "퇴근", "#4CAF50", "white"),
    ("toegeun_trans", "퇴근", "#4CAF50", "transparent"),
    ("yageun_simple", "야근", "#424242", "white"),
    ("yageun_trans", "야근", "#424242", "transparent"),
    
    # 인터넷 밈
    ("oo_simple", "ㅇㅇ", "#4CAF50", "white"),
    ("oo_trans", "ㅇㅇ", "#4CAF50", "transparent"),
    ("nn_simple", "ㄴㄴ", "#F44336", "white"),
    ("nn_trans", "ㄴㄴ", "#F44336", "transparent"),
]

# GIF 버전 (심플 애니메이션)
GIF_EMOJIS = [
    ("loading_simple", "로딩중", "#2196F3", "pulse"),
    ("alert_simple", "알림", "#FF9800", "blink"),
    ("hwaiting_gif", "화이팅!", "#FF6B6B", "bounce"),
    ("daebak_gif", "대박", "#FF1744", "zoom"),
    ("kkk_gif", "ㅋㅋㅋ", "#FFD700", "shake"),
    ("toegeun_gif", "퇴근!", "#4CAF50", "slide"),
    ("yageun_gif", "야근", "#424242", "fade"),
    ("okay_gif", "OK", "#4CAF50", "rotate"),
    ("jjang_gif", "짱!", "#FFD700", "sparkle"),
    ("sarang_simple", "사랑", "#E91E63", "heart"),
]

def hex_to_rgba(hex_color):
    """Convert hex color to RGBA tuple"""
    hex_color = hex_color.lstrip('#')
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4)) + (255,)

def create_simple_static(name, korean, color, bg_type):
    """Create a simple text emoji - just text, no decorations"""
    img = Image.new('RGBA', (128, 128), 
                    (255, 255, 255, 255) if bg_type == "white" else (255, 255, 255, 0))
    draw = ImageDraw.Draw(img)
    
    # 폰트 크기 (심플하게 크게)
    if len(korean) == 1:
        font_size = 100
    elif len(korean) == 2:
        font_size = 86
    elif len(korean) == 3:
        font_size = 68
    elif len(korean) == 4:
        font_size = 52
    else:
        font_size = 44
    
    try:
        font = ImageFont.truetype("/System/Library/Fonts/AppleSDGothicNeo.ttc", font_size)
    except:
        try:
            font = ImageFont.truetype("/Library/Fonts/Arial Unicode.ttf", font_size)
        except:
            # 기본 폰트 사용
            from PIL import ImageFont
            font = ImageFont.load_default()
    
    # 텍스트 위치 계산 (정중앙)
    bbox = draw.textbbox((0, 0), korean, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]
    x = (128 - text_width) // 2
    y = (128 - text_height) // 2
    
    # 텍스트만 그리기 (심플!)
    text_color = hex_to_rgba(color)
    draw.text((x, y), korean, fill=text_color, font=font)
    
    return img

def create_simple_gif(name, korean, color, anim_type):
    """Create simple animated text GIF"""
    frames = []
    
    for frame_idx in range(4):
        img = Image.new('RGBA', (128, 128), (255, 255, 255, 0))
        draw = ImageDraw.Draw(img)
        
        # 폰트 설정
        base_size = 86 if len(korean) <= 2 else 68 if len(korean) <= 3 else 52
        
        # 애니메이션 타입별 처리
        if anim_type == "pulse":  # 크기 변화
            font_size = base_size + int(10 * (1 if frame_idx % 2 == 0 else 0))
        elif anim_type == "blink":  # 깜빡임
            alpha = 255 if frame_idx % 2 == 0 else 100
            text_color = (*hex_to_rgba(color)[:3], alpha)
        elif anim_type == "bounce":  # 위아래 움직임
            y_offset = [0, -10, 0, 10][frame_idx]
        elif anim_type == "zoom":  # 확대/축소
            font_size = base_size + [-10, 0, 10, 0][frame_idx]
        elif anim_type == "shake":  # 좌우 흔들기
            x_offset = [0, 5, 0, -5][frame_idx]
        elif anim_type == "slide":  # 슬라이드
            x_offset = [-20, -10, 10, 20][frame_idx]
        elif anim_type == "fade":  # 페이드
            alpha = [255, 200, 150, 200][frame_idx]
            text_color = (*hex_to_rgba(color)[:3], alpha)
        elif anim_type == "rotate":  # 회전 효과 (위치 변경으로 시뮬레이션)
            positions = [(64, 54), (74, 64), (64, 74), (54, 64)]
            x_base, y_base = positions[frame_idx]
        elif anim_type == "sparkle":  # 반짝임
            # 별 추가
            if frame_idx % 2 == 0:
                for i in range(3):
                    star_x = 20 + i * 40
                    star_y = 20
                    draw.text((star_x, star_y), "✨", fill=hex_to_rgba(color))
        elif anim_type == "heart":  # 하트 비트
            if frame_idx % 2 == 0:
                draw.text((10, 10), "❤️", fill=hex_to_rgba(color))
                draw.text((100, 10), "❤️", fill=hex_to_rgba(color))
        
        # 기본값 설정
        if 'font_size' not in locals():
            font_size = base_size
        if 'text_color' not in locals():
            text_color = hex_to_rgba(color)
        if 'x_offset' not in locals():
            x_offset = 0
        if 'y_offset' not in locals():
            y_offset = 0
        
        try:
            font = ImageFont.truetype("/System/Library/Fonts/AppleSDGothicNeo.ttc", font_size)
        except:
            font = ImageFont.load_default()
        
        # 텍스트 위치 계산
        bbox = draw.textbbox((0, 0), korean, font=font)
        text_width = bbox[2] - bbox[0]
        text_height = bbox[3] - bbox[1]
        
        if 'x_base' in locals():
            x = x_base - text_width // 2
            y = y_base - text_height // 2
        else:
            x = (128 - text_width) // 2 + x_offset
            y = (128 - text_height) // 2 + y_offset
        
        # 텍스트 그리기
        draw.text((x, y), korean, fill=text_color, font=font)
        
        frames.append(img)
    
    return frames

# 메인 실행
print("심플한 한국어 이모지 생성 시작...")
print(f"정적 이모지 {len(SIMPLE_EMOJIS)}개, GIF {len(GIF_EMOJIS)}개 생성 예정")

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

# GIF 이모지 생성
for name, korean, color, anim_type in GIF_EMOJIS:
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
            print(f"✓ {name}.gif - {korean} ({anim_type} animation)")
    except Exception as e:
        print(f"✗ {name} 생성 실패: {e}")

print(f"\n완료! {OUTPUT_DIR}에 심플 버전 이모지 생성됨")
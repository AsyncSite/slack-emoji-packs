#!/usr/bin/env python3
from PIL import Image, ImageDraw, ImageFont
import os
from pathlib import Path
import math

# 출력 디렉토리
OUTPUT_DIR = Path("images/korean-words")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# 다양한 느낌의 GIF 정의 (이름, 텍스트, 색상, 애니메이션 타입, 설명)
EXPRESSIVE_GIFS = [
    # 넵 시리즈
    ("nep_excited", "넵!", "#FF6B6B", "bounce", "신나는 넵"),
    ("nep_calm", "넵", "#4CAF50", "fade", "차분한 넵"),
    ("nep_fast", "넵!!", "#FFD700", "shake", "급한 넵"),
    
    # 옙 시리즈
    ("yep_happy", "옙!", "#FF1744", "zoom", "기쁜 옙"),
    ("yep_cute", "옙~", "#E91E63", "wiggle", "귀여운 옙"),
    
    # 에이 시리즈
    ("ei_annoyed", "에이!", "#FF5722", "shake", "짜증난 에이"),
    ("ei_dismissive", "에이~", "#9C27B0", "slide", "무시하는 에이"),
    ("ei_surprised", "에이?!", "#FF9800", "bounce", "놀란 에이"),
    
    # 네 시리즈
    ("ne_excited", "네!", "#4CAF50", "pulse", "신난 네"),
    ("ne_double", "네네!", "#00BCD4", "double_bounce", "빠른 네네"),
    ("ne_question", "네?", "#2196F3", "tilt", "의문의 네"),
    
    # 오 시리즈
    ("oh_surprised", "오!", "#FF6B6B", "explode", "놀란 오"),
    ("oh_thinking", "오...", "#607D8B", "dots", "생각하는 오"),
    ("oh_impressed", "오~", "#FFD700", "wave", "감탄하는 오"),
    ("oh_confused", "오?", "#9C27B0", "question", "혼란스러운 오"),
    
    # ㅋㅋㅋ 시리즈
    ("kkk_loud", "ㅋㅋㅋ", "#FFD700", "shake_crazy", "빵터진 웃음"),
    ("kkk_subtle", "ㅋㅋ", "#FFC107", "gentle", "은은한 웃음"),
    ("kkk_many", "ㅋㅋㅋㅋㅋ", "#FF6B6B", "scroll", "많이 웃음"),
    ("kkk_sarcastic", "ㅋ", "#795548", "slow_fade", "비웃음"),
    
    # 추가 표현들
    ("ahh_realize", "아!", "#FF1744", "lightbulb", "깨달음"),
    ("hmm_thinking", "흠...", "#607D8B", "dots", "고민중"),
    ("wow_amazed", "와!", "#FFD700", "sparkle", "감탄"),
    ("heok_shocked", "헉!", "#F44336", "shock", "충격"),
    ("ang_angry", "앙!", "#E91E63", "angry", "화남"),
]

def hex_to_rgba(hex_color):
    """Convert hex color to RGBA tuple"""
    hex_color = hex_color.lstrip('#')
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4)) + (255,)

def create_expressive_gif(name, text, color, anim_type, description):
    """Create expressive animated text GIF with white background"""
    frames = []
    scale = 4  # 고해상도 작업
    
    for frame_idx in range(6):  # 6프레임으로 더 부드럽게
        # 흰색 배경
        img = Image.new('RGBA', (128 * scale, 128 * scale), (255, 255, 255, 255))
        draw = ImageDraw.Draw(img)
        
        # 기본 폰트 크기
        base_size = 380 if len(text) <= 2 else 280 if len(text) <= 3 else 200
        font_size = base_size
        x_offset = 0
        y_offset = 0
        rotation = 0
        alpha = 255
        
        # 애니메이션 타입별 효과
        if anim_type == "bounce":  # 위아래 통통
            y_offset = [0, -30, -50, -30, 0, 20][frame_idx] * scale
            
        elif anim_type == "shake":  # 좌우 흔들기
            x_offset = [0, 20, -20, 20, -20, 0][frame_idx] * scale
            
        elif anim_type == "fade":  # 페이드 인/아웃
            alpha = [100, 150, 200, 255, 200, 150][frame_idx]
            
        elif anim_type == "zoom":  # 확대/축소
            font_size = base_size + [0, 20, 40, 60, 40, 20][frame_idx]
            
        elif anim_type == "wiggle":  # 귀여운 흔들기
            rotation = [0, 5, -5, 5, -5, 0][frame_idx]
            y_offset = [0, -10, 0, -10, 0, 0][frame_idx] * scale
            
        elif anim_type == "slide":  # 슬라이드
            x_offset = [-100, -60, -20, 20, 60, 100][frame_idx] * scale
            
        elif anim_type == "pulse":  # 맥박
            font_size = base_size + [0, 10, 20, 10, 0, -10][frame_idx]
            alpha = [255, 230, 200, 230, 255, 230][frame_idx]
            
        elif anim_type == "double_bounce":  # 두 번 통통
            y_offset = [0, -40, 0, -40, 0, 0][frame_idx] * scale
            
        elif anim_type == "tilt":  # 기울기
            rotation = [0, -10, 0, 10, 0, 0][frame_idx]
            
        elif anim_type == "explode":  # 폭발
            font_size = base_size + [0, 40, 80, 60, 30, 10][frame_idx]
            if frame_idx == 2:  # 최대 크기일 때 효과
                # 방사형 선 그리기
                center = 64 * scale
                for angle in range(0, 360, 30):
                    rad = math.radians(angle)
                    x1 = center + int(30 * scale * math.cos(rad))
                    y1 = center + int(30 * scale * math.sin(rad))
                    x2 = center + int(50 * scale * math.cos(rad))
                    y2 = center + int(50 * scale * math.sin(rad))
                    draw.line([x1, y1, x2, y2], fill=hex_to_rgba(color), width=4)
                    
        elif anim_type == "dots":  # 점점점 애니메이션
            dots = ["", ".", "..", "...", "..", "."][frame_idx]
            text_to_draw = text.rstrip('.') + dots
            
        elif anim_type == "wave":  # 물결
            y_offset = int(30 * scale * math.sin(frame_idx * math.pi / 3))
            
        elif anim_type == "question":  # 물음표 효과
            if frame_idx >= 3:
                text_to_draw = text + "?"
                
        elif anim_type == "shake_crazy":  # 미친듯이 흔들기
            x_offset = [0, 40, -40, 30, -30, 0][frame_idx] * scale
            y_offset = [0, -20, 20, -10, 10, 0][frame_idx] * scale
            rotation = [0, 10, -10, 5, -5, 0][frame_idx]
            
        elif anim_type == "gentle":  # 부드러운 움직임
            y_offset = int(10 * scale * math.sin(frame_idx * math.pi / 3))
            
        elif anim_type == "scroll":  # 스크롤
            # 텍스트가 길어지는 효과
            text_to_draw = text[:min(len(text), frame_idx + 1)]
            
        elif anim_type == "slow_fade":  # 천천히 페이드
            alpha = [50, 100, 150, 200, 150, 100][frame_idx]
            
        elif anim_type == "lightbulb":  # 전구 켜지는 효과
            if frame_idx >= 3:
                # 반짝임 효과
                draw.ellipse([50*scale, 10*scale, 78*scale, 38*scale], 
                           fill=(255, 255, 0, 100))
                
        elif anim_type == "sparkle":  # 반짝임
            if frame_idx % 2 == 0:
                # 별 그리기
                for i in range(3):
                    x = (30 + i * 30) * scale
                    y = 20 * scale
                    draw.text((x, y), "✨", fill=hex_to_rgba(color))
                    
        elif anim_type == "shock":  # 충격
            font_size = base_size + [0, 60, 40, 20, 10, 0][frame_idx]
            if frame_idx == 1:
                # 충격 선
                for angle in range(0, 360, 45):
                    rad = math.radians(angle)
                    x1 = 64 * scale + int(40 * scale * math.cos(rad))
                    y1 = 64 * scale + int(40 * scale * math.sin(rad))
                    x2 = 64 * scale + int(60 * scale * math.cos(rad))
                    y2 = 64 * scale + int(60 * scale * math.sin(rad))
                    draw.line([x1, y1, x2, y2], fill=(255, 0, 0, 200), width=6)
                    
        elif anim_type == "angry":  # 화남
            x_offset = [0, 10, -10, 10, -10, 0][frame_idx] * scale
            # 빨간 배경 효과
            if frame_idx % 2 == 0:
                draw.rectangle([0, 0, 128*scale, 128*scale], 
                             fill=(255, 200, 200, 50))
        
        # 텍스트 그리기
        if 'text_to_draw' not in locals():
            text_to_draw = text
            
        try:
            font = ImageFont.truetype("/System/Library/Fonts/AppleSDGothicNeo.ttc", font_size)
        except:
            try:
                font = ImageFont.truetype("/Library/Fonts/Arial Unicode.ttf", font_size)
            except:
                font = None
        
        if font:
            bbox = draw.textbbox((0, 0), text_to_draw, font=font)
            text_width = bbox[2] - bbox[0]
            text_height = bbox[3] - bbox[1]
            x = (128 * scale - text_width) // 2 + x_offset
            y = (128 * scale - text_height) // 2 + y_offset
            
            text_color = (*hex_to_rgba(color)[:3], alpha)
            
            # 회전이 있는 경우
            if rotation != 0:
                # 텍스트를 별도 이미지에 그리고 회전
                txt_img = Image.new('RGBA', (text_width + 100, text_height + 100), (255, 255, 255, 0))
                txt_draw = ImageDraw.Draw(txt_img)
                txt_draw.text((50, 50), text_to_draw, fill=text_color, font=font)
                txt_img = txt_img.rotate(rotation, expand=1, fillcolor=(255, 255, 255, 0))
                img.paste(txt_img, (int(x - 50), int(y - 50)), txt_img)
            else:
                draw.text((x, y), text_to_draw, fill=text_color, font=font)
        
        # 로컬 변수 초기화
        if 'text_to_draw' in locals():
            del text_to_draw
            
        # 축소
        img = img.resize((128, 128), Image.Resampling.LANCZOS)
        frames.append(img)
    
    return frames

# 메인 실행
print("다양한 느낌의 한국어 GIF 생성 시작...")
print(f"총 {len(EXPRESSIVE_GIFS)}개 GIF 생성 예정")

created_count = 0
for name, text, color, anim_type, description in EXPRESSIVE_GIFS:
    try:
        frames = create_expressive_gif(name, text, color, anim_type, description)
        if frames:
            filepath = OUTPUT_DIR / f"{name}.gif"
            frames[0].save(
                filepath,
                save_all=True,
                append_images=frames[1:],
                duration=150,  # 더 빠른 애니메이션
                loop=0,
                disposal=2
            )
            created_count += 1
            print(f"✓ {name}.gif - {text} ({description})")
    except Exception as e:
        print(f"✗ {name} 생성 실패: {e}")

print(f"\n완료! {created_count}개 GIF 생성됨")
print(f"위치: {OUTPUT_DIR}")
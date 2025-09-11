#!/usr/bin/env python3
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import os
from pathlib import Path
import math

# 출력 디렉토리
OUTPUT_DIR = Path("images/korean-words")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

def create_layered_shadow_text(draw, x, y, text, font, main_color, scale=1):
    """다층 그림자 효과를 가진 텍스트 생성"""
    # 여러 레이어의 그림자 (멀리서부터 가까이)
    shadow_layers = [
        (12*scale, 12*scale, (0, 0, 0, 80)),   # 가장 멀고 흐린 그림자
        (9*scale, 9*scale, (0, 0, 0, 120)),
        (6*scale, 6*scale, (0, 0, 0, 160)),
        (4*scale, 4*scale, (0, 0, 0, 200)),    # 가장 가깝고 진한 그림자
        (2*scale, 2*scale, (0, 0, 0, 240)),
    ]
    
    # 그림자 그리기
    for offset_x, offset_y, shadow_color in shadow_layers:
        draw.text((x + offset_x, y + offset_y), text, fill=shadow_color, font=font)
    
    # 외곽선 (아웃라인)
    outline_width = 3 * scale
    for dx in range(-outline_width, outline_width + 1):
        for dy in range(-outline_width, outline_width + 1):
            if dx != 0 or dy != 0:
                draw.text((x + dx, y + dy), text, fill=(50, 50, 50, 255), font=font)
    
    # 메인 텍스트
    draw.text((x, y), text, fill=main_color, font=font)
    
    # 하이라이트 (빛 반사 효과)
    highlight = Image.new('RGBA', draw.im.size, (255, 255, 255, 0))
    h_draw = ImageDraw.Draw(highlight)
    h_draw.text((x - 2*scale, y - 2*scale), text, fill=(255, 255, 255, 80), font=font)
    
    return highlight

def create_kkk4_static(name, style):
    """2x2 레이아웃의 정적 ㅋㅋㅋㅋ 이모지 생성"""
    scale = 4
    size = 128 * scale
    
    # 배경 설정
    if style == "classic":
        img = Image.new('RGBA', (size, size), (255, 255, 255, 255))
        text_color = (255, 215, 0, 255)  # 골드
    elif style == "gold":
        # 그라데이션 배경
        img = Image.new('RGBA', (size, size), (255, 255, 255, 255))
        draw = ImageDraw.Draw(img)
        # 방사형 그라데이션 효과
        center = size // 2
        for i in range(100):
            alpha = int(255 * (1 - i/100))
            radius = size // 2 - i * 2
            if radius > 0:
                draw.ellipse([center - radius, center - radius, 
                            center + radius, center + radius],
                            fill=(255, 250, 200, alpha // 4))
        text_color = (255, 195, 0, 255)
    elif style == "bold":
        img = Image.new('RGBA', (size, size), (255, 255, 255, 255))
        text_color = (255, 200, 0, 255)
    else:  # 3d
        img = Image.new('RGBA', (size, size), (250, 250, 250, 255))
        text_color = (255, 180, 0, 255)
    
    draw = ImageDraw.Draw(img)
    
    # 폰트 설정
    font_size = 180
    try:
        font = ImageFont.truetype("/System/Library/Fonts/AppleSDGothicNeo.ttc", font_size)
    except:
        try:
            font = ImageFont.truetype("/Library/Fonts/Arial Unicode.ttf", font_size)
        except:
            font = None
    
    if font:
        # 2x2 그리드 위치 계산
        positions = [
            (size * 0.25, size * 0.25),  # 좌상
            (size * 0.75, size * 0.25),  # 우상
            (size * 0.25, size * 0.75),  # 좌하
            (size * 0.75, size * 0.75),  # 우하
        ]
        
        for pos_x, pos_y in positions:
            # 각 ㅋ 그리기
            bbox = draw.textbbox((0, 0), "ㅋ", font=font)
            text_width = bbox[2] - bbox[0]
            text_height = bbox[3] - bbox[1]
            x = pos_x - text_width // 2
            y = pos_y - text_height // 2
            
            if style == "bold":
                # 극도로 두꺼운 그림자
                for i in range(20, 0, -2):
                    alpha = min(255, 100 + i * 8)
                    draw.text((x + i, y + i), "ㅋ", 
                            fill=(0, 0, 0, alpha), font=font)
            elif style == "3d":
                # 3D 효과
                for i in range(15, 0, -1):
                    gray = 50 + i * 10
                    draw.text((x + i*2, y + i*2), "ㅋ", 
                            fill=(gray, gray, gray, 255), font=font)
            else:
                # 기본 다층 그림자
                create_layered_shadow_text(draw, x, y, "ㅋ", font, text_color, scale)
                continue
            
            # 메인 텍스트
            draw.text((x, y), "ㅋ", fill=text_color, font=font)
            
            # 광택 효과
            if style in ["gold", "3d"]:
                draw.text((x - 3, y - 3), "ㅋ", 
                        fill=(255, 255, 255, 60), font=font)
    
    # 축소
    img = img.resize((128, 128), Image.Resampling.LANCZOS)
    
    # 후처리 효과
    if style == "gold":
        # 약간의 블러로 부드럽게
        img = img.filter(ImageFilter.SMOOTH_MORE)
    
    return img

def create_kkk4_animated(name, anim_type):
    """2x2 레이아웃의 애니메이션 ㅋㅋㅋㅋ GIF 생성"""
    frames = []
    scale = 4
    size = 128 * scale
    
    for frame_idx in range(8):  # 8프레임으로 부드럽게
        img = Image.new('RGBA', (size, size), (255, 255, 255, 255))
        draw = ImageDraw.Draw(img)
        
        # 폰트 설정
        base_font_size = 180
        try:
            font = ImageFont.truetype("/System/Library/Fonts/AppleSDGothicNeo.ttc", base_font_size)
        except:
            font = None
        
        if font:
            # 2x2 그리드 위치
            base_positions = [
                (size * 0.25, size * 0.25),  # 좌상
                (size * 0.75, size * 0.25),  # 우상
                (size * 0.25, size * 0.75),  # 좌하
                (size * 0.75, size * 0.75),  # 우하
            ]
            
            for i, (base_x, base_y) in enumerate(base_positions):
                pos_x, pos_y = base_x, base_y
                font_size = base_font_size
                text_color = (255, 200, 0, 255)
                rotation = 0
                
                # 애니메이션 타입별 효과
                if anim_type == "wave":
                    # 파도타기 효과
                    wave_offset = math.sin((frame_idx + i * 2) * math.pi / 4) * 30
                    pos_y = base_y + wave_offset
                    
                elif anim_type == "bounce":
                    # 동시 바운스
                    bounce = abs(math.sin(frame_idx * math.pi / 4)) * 40
                    pos_y = base_y - bounce
                    
                elif anim_type == "glow":
                    # 빛나는 효과
                    glow_intensity = abs(math.sin(frame_idx * math.pi / 4))
                    # 광원 효과
                    glow_radius = int(60 + glow_intensity * 40)
                    draw.ellipse([pos_x - glow_radius, pos_y - glow_radius,
                                pos_x + glow_radius, pos_y + glow_radius],
                               fill=(255, 250, 200, int(50 * glow_intensity)))
                    
                elif anim_type == "party":
                    # 파티 모드
                    rotation = frame_idx * 45 + i * 90
                    # 색상 변화
                    hue_shift = (frame_idx * 45 + i * 90) % 360
                    if hue_shift < 120:
                        text_color = (255, 200, 0, 255)  # 노랑
                    elif hue_shift < 240:
                        text_color = (255, 100, 100, 255)  # 빨강
                    else:
                        text_color = (100, 200, 255, 255)  # 파랑
                    
                    # 크기 변화
                    font_size = base_font_size + int(20 * math.sin(frame_idx * math.pi / 4))
                
                # 폰트 재설정 (크기 변경된 경우)
                if font_size != base_font_size:
                    try:
                        font = ImageFont.truetype("/System/Library/Fonts/AppleSDGothicNeo.ttc", font_size)
                    except:
                        pass
                
                # 텍스트 그리기
                bbox = draw.textbbox((0, 0), "ㅋ", font=font)
                text_width = bbox[2] - bbox[0]
                text_height = bbox[3] - bbox[1]
                x = pos_x - text_width // 2
                y = pos_y - text_height // 2
                
                # 그림자
                for offset in range(8, 0, -2):
                    draw.text((x + offset, y + offset), "ㅋ", 
                            fill=(0, 0, 0, 100), font=font)
                
                # 메인 텍스트
                if rotation != 0:
                    # 회전이 필요한 경우
                    txt_img = Image.new('RGBA', (text_width + 100, text_height + 100), (255, 255, 255, 0))
                    txt_draw = ImageDraw.Draw(txt_img)
                    txt_draw.text((50, 50), "ㅋ", fill=text_color, font=font)
                    txt_img = txt_img.rotate(rotation, expand=1, fillcolor=(255, 255, 255, 0))
                    img.paste(txt_img, (int(x - 50), int(y - 50)), txt_img)
                else:
                    draw.text((x, y), "ㅋ", fill=text_color, font=font)
        
        # 축소
        img = img.resize((128, 128), Image.Resampling.LANCZOS)
        frames.append(img)
    
    return frames

# 메인 실행
print("ㅋㅋㅋㅋ 2x2 고급 버전 생성 시작...")

# 정적 버전
static_versions = [
    ("kkk4_classic", "classic"),
    ("kkk4_gold", "gold"),
    ("kkk4_bold", "bold"),
    ("kkk4_3d", "3d"),
]

for name, style in static_versions:
    try:
        img = create_kkk4_static(name, style)
        filepath = OUTPUT_DIR / f"{name}.png"
        img.save(filepath, "PNG")
        print(f"✓ {name}.png - {style} 스타일")
    except Exception as e:
        print(f"✗ {name} 생성 실패: {e}")

# 애니메이션 버전
animated_versions = [
    ("kkk4_wave", "wave"),
    ("kkk4_bounce", "bounce"),
    ("kkk4_glow", "glow"),
    ("kkk4_party", "party"),
]

for name, anim_type in animated_versions:
    try:
        frames = create_kkk4_animated(name, anim_type)
        if frames:
            filepath = OUTPUT_DIR / f"{name}.gif"
            frames[0].save(
                filepath,
                save_all=True,
                append_images=frames[1:],
                duration=150,
                loop=0,
                disposal=2
            )
            print(f"✓ {name}.gif - {anim_type} 애니메이션")
    except Exception as e:
        print(f"✗ {name} 생성 실패: {e}")

print("\n완료! 총 8개의 ㅋㅋㅋㅋ 2x2 버전 생성됨")
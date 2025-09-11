#!/usr/bin/env python3
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import os
from pathlib import Path
import math

# 출력 디렉토리
OUTPUT_DIR = Path("images/korean-words")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# 이모지 정의 (이름, 한글, 영문, 색상, 타입)
EMOJIS = [
    # 긍정/동의
    ("ne", "네", "Yes", "#4CAF50", "static"),
    ("nep", "넵", "Yes!", "#4CAF50", "static"),
    ("ye", "예", "Yes", "#4CAF50", "static"),
    ("good", "굿", "Good", "#2196F3", "static"),
    ("choego", "최고", "Best", "#FFD700", "static"),
    ("jjang", "짱", "Best!", "#FF6B6B", "gif"),
    
    # 부정/거부
    ("ani", "아니", "No", "#F44336", "static"),
    ("ani_alt", "아니요", "No", "#F44336", "static"),
    ("sileo", "싫어", "Dislike", "#E91E63", "static"),
    ("nono", "노노", "No No", "#F44336", "gif"),
    
    # 감탄사
    ("aha", "아하", "Aha", "#9C27B0", "static"),
    ("eoheo", "어허", "Oh my", "#FF9800", "static"),
    ("heol", "헐", "OMG", "#FF5722", "static"),
    ("heum", "흠", "Hmm", "#607D8B", "static"),
    ("oh", "오", "Oh", "#3F51B5", "static"),
    ("daebak", "대박", "Awesome", "#FF1744", "gif"),
    
    # 응원/격려
    ("hwaiting", "화이팅", "Fighting", "#FF6B6B", "static"),
    ("ilhae", "일해", "Work!", "#795548", "static"),
    ("sugo", "수고", "Good job", "#00BCD4", "static"),
    
    # 상태/진행
    ("hwagin", "확인", "Check", "#4CAF50", "static"),
    ("hwagin_jung", "확인중", "Checking", "#FFC107", "static"),
    ("wanryo", "완료", "Done", "#4CAF50", "static"),
    ("loading", "로딩중", "Loading", "#2196F3", "gif"),
    ("alert", "알림", "Alert", "#FF9800", "gif"),
    
    # 웃음/재미
    ("kkk", "ㅋㅋㅋ", "LOL", "#FFD700", "static"),
    ("hh", "ㅎㅎ", "hehe", "#FFC107", "static"),
    
    # 인사
    ("annyeong", "안녕", "Hello", "#00BCD4", "static"),
    ("gamsa", "감사", "Thanks", "#E91E63", "static"),
    ("gomawo", "고마워", "Thanks", "#E91E63", "static"),
    ("mian", "미안", "Sorry", "#9C27B0", "static"),
    ("joesong", "죄송", "Sorry", "#9C27B0", "static"),
    ("jalga", "잘가", "Bye", "#607D8B", "static"),
    ("bbai", "빠이", "Bye bye", "#607D8B", "gif"),
    
    # 감정
    ("joa", "좋아", "Like", "#E91E63", "gif"),
    ("sarang", "사랑", "Love", "#E91E63", "gif"),
    ("hwanam", "화남", "Angry", "#F44336", "gif"),
    ("seulpeum", "슬픔", "Sad", "#3F51B5", "static"),
    ("haengbok", "행복", "Happy", "#FFD700", "static"),
    
    # 리액션
    ("okay", "오케이", "OK", "#4CAF50", "gif"),
    ("moreugesseo", "모르겠어", "IDK", "#9E9E9E", "static"),
    ("geulsse", "글쎄", "Well", "#607D8B", "static"),
    ("eum", "음", "Umm", "#9E9E9E", "static"),
    ("at", "앗", "Oops", "#FF9800", "static"),
    
    # 업무
    ("hoeui", "회의", "Meeting", "#795548", "gif"),
    ("jeomsim", "점심", "Lunch", "#FF9800", "static"),
    ("toegeun", "퇴근", "Leave", "#4CAF50", "gif"),
    ("chulgeun", "출근", "Work", "#2196F3", "static"),
    ("yageun", "야근", "Overtime", "#424242", "gif"),
    ("kaltoe", "칼퇴", "On time!", "#4CAF50", "gif"),
    
    # 인터넷/밈
    ("oo", "ㅇㅇ", "yep", "#4CAF50", "static"),
    ("nn", "ㄴㄴ", "nope", "#F44336", "static"),
    ("yuyu", "ㅠㅠ", "crying", "#2196F3", "static"),
    ("uu", "ㅜㅜ", "tears", "#2196F3", "static"),
    ("dd", "ㄷㄷ", "shiver", "#9C27B0", "static"),
    ("bb", "ㅂㅂ", "bye", "#607D8B", "static"),
    ("gg", "ㄱㄱ", "go go", "#FF6B6B", "gif"),
    
    # 특수
    ("gingeup", "긴급", "Urgent", "#F44336", "gif"),
    ("jungyо", "중요", "Important", "#FFD700", "gif"),
    ("juui", "주의", "Caution", "#FFC107", "gif"),
    ("chukha", "축하", "Congrats", "#E91E63", "gif"),
    ("hwanyeong", "환영", "Welcome", "#00BCD4", "gif"),
]

def hex_to_rgba(hex_color):
    """Convert hex color to RGBA tuple"""
    hex_color = hex_color.lstrip('#')
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4)) + (255,)

def create_rounded_rect(draw, coords, radius, fill):
    """Draw a rounded rectangle"""
    x1, y1, x2, y2 = coords
    draw.ellipse([x1, y1, x1 + 2*radius, y1 + 2*radius], fill=fill)
    draw.ellipse([x2 - 2*radius, y1, x2, y1 + 2*radius], fill=fill)
    draw.ellipse([x1, y2 - 2*radius, x1 + 2*radius, y2], fill=fill)
    draw.ellipse([x2 - 2*radius, y2 - 2*radius, x2, y2], fill=fill)
    draw.rectangle([x1 + radius, y1, x2 - radius, y2], fill=fill)
    draw.rectangle([x1, y1 + radius, x2, y2 - radius], fill=fill)

def create_static_emoji(name, korean, english, color):
    """Create a static PNG emoji with better design"""
    # 더 큰 크기로 그린 후 축소 (안티앨리어싱)
    scale = 4
    img = Image.new('RGBA', (128 * scale, 128 * scale), (255, 255, 255, 0))
    draw = ImageDraw.Draw(img)
    
    # 색상 정의
    bg_color = (*hex_to_rgba(color)[:3], 25)
    text_color = hex_to_rgba(color)
    
    # 배경 그라데이션 원
    center = 64 * scale
    for i in range(50):
        alpha = int(25 * (1 - i/50))
        radius = (60 - i) * scale
        draw.ellipse([center - radius, center - radius, center + radius, center + radius],
                    fill=(*hex_to_rgba(color)[:3], alpha))
    
    # 폰트 크기 (크게!)
    if len(korean) <= 2:
        font_size = 200
    elif len(korean) <= 3:
        font_size = 150
    elif len(korean) <= 4:
        font_size = 120
    else:
        font_size = 100
    
    # 텍스트 그리기 (비트맵 폰트 대신 도형으로 근사)
    text = korean
    
    # 간단한 텍스트 렌더링
    try:
        font = ImageFont.truetype("/System/Library/Fonts/AppleSDGothicNeo.ttc", font_size)
    except:
        try:
            font = ImageFont.truetype("/Library/Fonts/Arial Unicode.ttf", font_size)
        except:
            # 폰트가 없으면 도형으로 표현
            font = None
    
    if font:
        # 텍스트 위치 계산
        bbox = draw.textbbox((0, 0), text, font=font)
        text_width = bbox[2] - bbox[0]
        text_height = bbox[3] - bbox[1]
        x = (128 * scale - text_width) // 2
        y = (128 * scale - text_height) // 2 - 20
        
        # 외곽선 효과
        outline_width = 4
        for dx in range(-outline_width, outline_width + 1):
            for dy in range(-outline_width, outline_width + 1):
                if dx != 0 or dy != 0:
                    draw.text((x + dx, y + dy), text, 
                            fill=(255, 255, 255, 200), font=font)
        
        # 메인 텍스트
        draw.text((x, y), text, fill=text_color, font=font)
    else:
        # 폰트가 없을 때 기본 렌더링
        draw.text((center - 50, center - 50), text, fill=text_color)
    
    # 축소해서 부드럽게
    img = img.resize((128, 128), Image.Resampling.LANCZOS)
    
    return img

def create_gif_emoji(name, korean, english, color):
    """Create an animated GIF emoji with effects"""
    frames = []
    scale = 4
    
    for frame_idx in range(4):
        img = Image.new('RGBA', (128 * scale, 128 * scale), (255, 255, 255, 0))
        draw = ImageDraw.Draw(img)
        
        # 애니메이션 효과별 처리
        if name in ["loading", "hoeui"]:  # 회전 로딩
            angle = frame_idx * 90
            for i in range(8):
                a = math.radians(angle + i * 45)
                x = 64 * scale + int(40 * scale * math.cos(a))
                y = 64 * scale + int(40 * scale * math.sin(a))
                size = 15 * scale if i == 0 else 10 * scale
                alpha = 255 if i == 0 else 100
                draw.ellipse([x - size, y - size, x + size, y + size],
                           fill=(*hex_to_rgba(color)[:3], alpha))
            
        elif name in ["alert", "gingeup"]:  # 펄스 효과
            pulse = 1 + 0.2 * math.sin(frame_idx * math.pi / 2)
            radius = int(50 * scale * pulse)
            alpha = int(255 * (0.7 + 0.3 * math.sin(frame_idx * math.pi / 2)))
            draw.ellipse([64*scale - radius, 64*scale - radius, 
                         64*scale + radius, 64*scale + radius],
                        fill=(*hex_to_rgba(color)[:3], alpha // 4))
            
        elif name in ["sarang", "joa"]:  # 하트 비트
            beat = 1 + 0.15 * math.sin(frame_idx * math.pi / 2)
            size = int(30 * scale * beat)
            # 하트 그리기
            draw.ellipse([64*scale - size - 10*scale, 50*scale, 
                         64*scale - size + 10*scale, 50*scale + size*2],
                        fill=hex_to_rgba(color))
            draw.ellipse([64*scale + size - 10*scale, 50*scale,
                         64*scale + size + 10*scale, 50*scale + size*2],
                        fill=hex_to_rgba(color))
            draw.polygon([(64*scale, 50*scale + size),
                         (64*scale - size, 60*scale),
                         (64*scale, 90*scale),
                         (64*scale + size, 60*scale)],
                        fill=hex_to_rgba(color))
        
        elif name in ["daebak", "chukha"]:  # 폭발 효과
            for i in range(8):
                angle = i * 45 + frame_idx * 15
                distance = 20 + frame_idx * 10
                x = 64 * scale + int(distance * scale * math.cos(math.radians(angle)))
                y = 64 * scale + int(distance * scale * math.sin(math.radians(angle)))
                size = (10 - frame_idx * 2) * scale
                if size > 0:
                    draw.ellipse([x - size, y - size, x + size, y + size],
                               fill=hex_to_rgba(color))
        
        # 텍스트 추가
        font_size = 150 if len(korean) <= 3 else 120
        try:
            font = ImageFont.truetype("/System/Library/Fonts/AppleSDGothicNeo.ttc", font_size)
        except:
            font = None
        
        if font:
            bbox = draw.textbbox((0, 0), korean, font=font)
            text_width = bbox[2] - bbox[0]
            text_height = bbox[3] - bbox[1]
            x = (128 * scale - text_width) // 2
            y = (128 * scale - text_height) // 2
            
            # 배경 효과
            if name in ["nono", "dd"]:  # 흔들기
                x += (10 if frame_idx % 2 == 0 else -10) * scale
            
            # 텍스트 그리기
            draw.text((x, y), korean, fill=hex_to_rgba(color), font=font)
        
        # 축소
        img = img.resize((128, 128), Image.Resampling.LANCZOS)
        frames.append(img)
    
    return frames

# 메인 실행
print("한국어 이모지 생성 시작 (개선된 버전)...")
print(f"총 {len(EMOJIS)}개 이모지 생성 예정")

created_files = []

for name, korean, english, color, emoji_type in EMOJIS:
    try:
        if emoji_type == "static":
            img = create_static_emoji(name, korean, english, color)
            filepath = OUTPUT_DIR / f"{name}.png"
            img.save(filepath, "PNG")
            created_files.append(f"{name}.png")
            print(f"✓ {name}.png - {korean} ({english})")
        else:  # gif
            frames = create_gif_emoji(name, korean, english, color)
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
                created_files.append(f"{name}.gif")
                print(f"✓ {name}.gif - {korean} ({english}) [animated]")
    except Exception as e:
        print(f"✗ {name} 생성 실패: {e}")

# 추가 이모지 (기존에 없던 것들)
ADDITIONAL = [
    ("jinjja", "진짜", "Really", "#FF5722", "static"),
    ("jebalyo", "제발요", "Please", "#9C27B0", "static"),
    ("don", "돈", "Money", "#4CAF50", "static"),
    ("neng", "냉", "Cold", "#2196F3", "static"),
    ("nimah", "니마", "WTF", "#F44336", "static"),
    ("documento", "도큐멘토", "Doc", "#2196F3", "static"),
    ("daebang_donggeon", "대방동건", "DBDG", "#9C27B0", "static"),
]

for name, korean, english, color, emoji_type in ADDITIONAL:
    try:
        img = create_static_emoji(name, korean, english, color)
        filepath = OUTPUT_DIR / f"{name}.png"
        img.save(filepath, "PNG")
        created_files.append(f"{name}.png")
        print(f"✓ {name}.png - {korean} ({english})")
    except Exception as e:
        print(f"✗ {name} 생성 실패: {e}")

print(f"\n완료! {len(created_files)}개 파일 생성됨")
print(f"위치: {OUTPUT_DIR}")
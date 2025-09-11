#!/usr/bin/env python3
from PIL import Image, ImageDraw, ImageFont
import os
from pathlib import Path

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
    
    # 기타 기존
    ("jinjja", "진짜", "Really", "#FF5722", "static"),
    ("jebalyo", "제발요", "Please", "#9C27B0", "static"),
    ("don", "돈", "Money", "#4CAF50", "static"),
    ("neng", "냉", "Cold", "#2196F3", "static"),
    ("nimah", "니마", "WTF", "#F44336", "static"),
    ("documento", "도큐멘토", "Doc", "#2196F3", "static"),
    ("daebang_donggeon", "대방동건", "DBDG", "#9C27B0", "static"),
]

def hex_to_rgba(hex_color):
    """Convert hex color to RGBA tuple"""
    hex_color = hex_color.lstrip('#')
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4)) + (255,)

def create_static_emoji(name, korean, english, color):
    """Create a static PNG emoji with transparent background"""
    # 이미지 생성 (투명 배경)
    img = Image.new('RGBA', (128, 128), (255, 255, 255, 0))
    draw = ImageDraw.Draw(img)
    
    # 부드러운 원형 배경
    draw.ellipse([8, 8, 120, 120], fill=(*hex_to_rgba(color)[:3], 40))
    
    # 텍스트 색상
    text_color = hex_to_rgba(color)
    
    # 폰트 크기 조정 (한글 길이에 따라) - 더 크게!
    if len(korean) <= 2:
        font_size = 72
    elif len(korean) <= 3:
        font_size = 56
    elif len(korean) <= 4:
        font_size = 42
    else:
        font_size = 36
    
    try:
        # 시스템 폰트 시도
        font = ImageFont.truetype("/System/Library/Fonts/Supplemental/AppleGothic.ttc", font_size)
    except:
        try:
            # 대체 폰트
            font = ImageFont.truetype("/System/Library/Fonts/AppleSDGothicNeo.ttc", font_size)
        except:
            # 기본 폰트를 더 크게
            from PIL import ImageFont
            font = ImageFont.load_default()
            # 기본 폰트는 작으므로 크기 재조정
            font_size = font_size * 2
    
    # 텍스트 위치 계산
    bbox = draw.textbbox((0, 0), korean, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]
    x = (128 - text_width) // 2
    y = (128 - text_height) // 2 - 10
    
    # 텍스트 그리기 (더 진한 그림자)
    shadow_offset = 3
    draw.text((x + shadow_offset, y + shadow_offset), korean, 
              fill=(0, 0, 0, 120), font=font)
    draw.text((x, y), korean, fill=text_color, font=font)
    
    # 영문 서브텍스트 (더 크게)
    if len(english) <= 10:
        sub_font_size = 18
        try:
            sub_font = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", sub_font_size)
        except:
            sub_font = font  # 같은 폰트 사용
        
        sub_bbox = draw.textbbox((0, 0), english, font=sub_font)
        sub_width = sub_bbox[2] - sub_bbox[0]
        sub_x = (128 - sub_width) // 2
        sub_y = y + text_height + 8
        
        if sub_y < 110:  # 화면 안에 들어오는 경우만
            draw.text((sub_x, sub_y), english, fill=(80, 80, 80, 255), font=sub_font)
    
    return img

def create_gif_emoji(name, korean, english, color):
    """Create an animated GIF emoji"""
    frames = []
    
    for i in range(4):
        # 기본 이미지 생성
        img = Image.new('RGBA', (128, 128), (255, 255, 255, 0))
        draw = ImageDraw.Draw(img)
        
        # 애니메이션 효과
        if name in ["loading", "hoeui", "gg"]:  # 회전
            angle = i * 90
            temp_img = Image.new('RGBA', (128, 128), (255, 255, 255, 0))
            temp_draw = ImageDraw.Draw(temp_img)
            
            # 원형 프로그레스
            start = angle
            end = angle + 270
            temp_draw.arc([20, 20, 108, 108], start, end, 
                         fill=hex_to_rgba(color), width=8)
            
            img = temp_img
            draw = ImageDraw.Draw(img)
            
        elif name in ["alert", "gingeup", "juui"]:  # 깜빡임
            alpha = 255 if i % 2 == 0 else 180
            text_color = (*hex_to_rgba(color)[:3], alpha)
            
        elif name in ["daebak", "chukha", "hwanyeong"]:  # 크기 변화
            scale = 1.0 + (i * 0.1)
            font_size = int(36 * scale)
            
        elif name in ["joa", "sarang"]:  # 하트 애니메이션
            # 하트 그리기
            heart_size = 20 + (i * 5)
            heart_y = 20 - (i * 3)
            draw.ellipse([54 - heart_size//2, heart_y, 54 + heart_size//2, heart_y + heart_size], 
                        fill=hex_to_rgba(color))
            draw.ellipse([74 - heart_size//2, heart_y, 74 + heart_size//2, heart_y + heart_size], 
                        fill=hex_to_rgba(color))
            points = [(64, heart_y + heart_size//2), 
                     (54 - heart_size//2, heart_y + heart_size//4),
                     (74 + heart_size//2, heart_y + heart_size//4),
                     (64, heart_y + heart_size + 10)]
            draw.polygon(points, fill=hex_to_rgba(color))
            
        elif name in ["nono", "dd"]:  # 좌우 흔들기
            offset = 5 if i % 2 == 0 else -5
            x_offset = offset
        else:
            # 기본 펄스 효과
            alpha = 255 - (i * 20)
            text_color = (*hex_to_rgba(color)[:3], alpha)
        
        # 텍스트 추가
        if 'text_color' not in locals():
            text_color = hex_to_rgba(color)
        if 'font_size' not in locals():
            font_size = 56 if len(korean) <= 3 else 42
        if 'x_offset' not in locals():
            x_offset = 0
            
        try:
            font = ImageFont.truetype("/System/Library/Fonts/Supplemental/AppleGothic.ttc", font_size)
        except:
            font = ImageFont.load_default()
        
        bbox = draw.textbbox((0, 0), korean, font=font)
        text_width = bbox[2] - bbox[0]
        text_height = bbox[3] - bbox[1]
        x = (128 - text_width) // 2 + x_offset
        y = (128 - text_height) // 2
        
        draw.text((x, y), korean, fill=text_color, font=font)
        
        # 프레임 추가
        frames.append(img)
    
    return frames

# 메인 실행
print("한국어 이모지 생성 시작...")
print(f"총 {len(EMOJIS)}개 이모지 생성 예정")

for name, korean, english, color, emoji_type in EMOJIS:
    if emoji_type == "static":
        img = create_static_emoji(name, korean, english, color)
        img.save(OUTPUT_DIR / f"{name}.png", "PNG")
        print(f"✓ {name}.png - {korean} ({english})")
    else:  # gif
        frames = create_gif_emoji(name, korean, english, color)
        if frames:
            frames[0].save(
                OUTPUT_DIR / f"{name}.gif",
                save_all=True,
                append_images=frames[1:],
                duration=200,
                loop=0,
                disposal=2
            )
            print(f"✓ {name}.gif - {korean} ({english}) [animated]")

print(f"\n완료! {OUTPUT_DIR}에 이모지 생성됨")
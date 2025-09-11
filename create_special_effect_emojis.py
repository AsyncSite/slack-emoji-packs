#!/usr/bin/env python3

from PIL import Image, ImageDraw, ImageFont
import os
import math

# Special effect GIF emojis
SPECIAL_EFFECT_EMOJIS = [
    # Sparkle effects
    ("sparkle_yes", "네✨", "#FFD700", "sparkle", "반짝이는 네"),
    ("sparkle_ok", "오케이✨", "#4CAF50", "sparkle", "반짝이는 오케이"),
    ("sparkle_good", "좋아✨", "#FF6B6B", "sparkle", "반짝이는 좋아"),
    ("sparkle_love", "사랑해✨", "#E91E63", "sparkle", "반짝이는 사랑해"),
    
    # Rainbow effects
    ("rainbow_fighting", "화이팅", None, "rainbow", "무지개 화이팅"),
    ("rainbow_congrats", "축하", None, "rainbow", "무지개 축하"),
    ("rainbow_awesome", "대박", None, "rainbow", "무지개 대박"),
    ("rainbow_legend", "레전드", None, "rainbow", "무지개 레전드"),
    
    # Pulse effects
    ("pulse_urgent", "긴급!", "#FF1744", "pulse", "펄스 긴급"),
    ("pulse_important", "중요!", "#9C27B0", "pulse", "펄스 중요"),
    ("pulse_notice", "공지!", "#2196F3", "pulse", "펄스 공지"),
    ("pulse_alert", "알림!", "#FF9800", "pulse", "펄스 알림"),
    
    # Glow effects
    ("glow_hot", "핫!", "#FF5722", "glow", "빛나는 핫"),
    ("glow_new", "NEW", "#4CAF50", "glow", "빛나는 뉴"),
    ("glow_best", "최고", "#FFD700", "glow", "빛나는 최고"),
    ("glow_premium", "프리미엄", "#9C27B0", "glow", "빛나는 프리미엄"),
    
    # Shake effects  
    ("shake_no", "아니!", "#F44336", "shake", "흔들리는 아니"),
    ("shake_stop", "멈춰!", "#FF5722", "shake", "흔들리는 멈춰"),
    ("shake_wait", "잠깐!", "#FF9800", "shake", "흔들리는 잠깐"),
    ("shake_help", "도와줘!", "#E91E63", "shake", "흔들리는 도와줘"),
    
    # Bounce effects
    ("bounce_hello", "안녕!", "#2196F3", "bounce", "통통 튀는 안녕"),
    ("bounce_bye", "잘가!", "#9C27B0", "bounce", "통통 튀는 잘가"),
    ("bounce_thanks", "감사!", "#4CAF50", "bounce", "통통 튀는 감사"),
    ("bounce_sorry", "미안!", "#FF9800", "bounce", "통통 튀는 미안"),
    
    # Rotate effects
    ("rotate_loading", "로딩중", "#03A9F4", "rotate", "회전하는 로딩중"),
    ("rotate_thinking", "생각중", "#9C27B0", "rotate", "회전하는 생각중"),
    ("rotate_processing", "처리중", "#00ACC1", "rotate", "회전하는 처리중"),
    
    # Fade effects
    ("fade_maybe", "아마도", "#607D8B", "fade", "페이드 아마도"),
    ("fade_secret", "비밀", "#795548", "fade", "페이드 비밀"),
    ("fade_quiet", "조용", "#9E9E9E", "fade", "페이드 조용"),
]

def create_special_effect_gif(text, color, name, effect_type, output_dir):
    """Create a special effect GIF emoji"""
    scale = 4
    size = 128 * scale
    frames = []
    
    # Try to use a good Korean font
    font_paths = [
        "/System/Library/Fonts/AppleSDGothicNeo.ttc",
        "/Library/Fonts/NanumGothic.ttf",
        "/usr/share/fonts/truetype/nanum/NanumGothic.ttf",
    ]
    
    font = None
    # Adjust font size based on text length (remove emoji for length calc)
    clean_text = text.replace("✨", "").replace("!", "")
    if len(clean_text) <= 2:
        base_size = 40 * scale
    elif len(clean_text) <= 3:
        base_size = 32 * scale
    elif len(clean_text) <= 4:
        base_size = 26 * scale
    else:
        base_size = 22 * scale
    
    for font_path in font_paths:
        if os.path.exists(font_path):
            try:
                font = ImageFont.truetype(font_path, base_size)
                break
            except:
                continue
    
    if not font:
        font = ImageFont.load_default()
    
    # Create frames based on effect type
    if effect_type == "sparkle":
        sparkle_positions = [(0.2, 0.2), (0.8, 0.2), (0.5, 0.8), (0.2, 0.8), (0.8, 0.8)]
        for i in range(10):
            img = Image.new('RGBA', (size, size), (255, 255, 255, 0))
            draw = ImageDraw.Draw(img)
            
            # Draw text
            bbox = draw.textbbox((0, 0), text, font=font)
            text_width = bbox[2] - bbox[0]
            text_height = bbox[3] - bbox[1]
            x = (size - text_width) // 2
            y = (size - text_height) // 2 - bbox[1]
            
            draw.text((x, y), text, fill=color, font=font)
            
            # Add sparkles
            sparkle_idx = i % len(sparkle_positions)
            sx, sy = sparkle_positions[sparkle_idx]
            sparkle_x = int(sx * size)
            sparkle_y = int(sy * size)
            sparkle_size = 15 * scale
            draw.ellipse([sparkle_x - sparkle_size, sparkle_y - sparkle_size,
                         sparkle_x + sparkle_size, sparkle_y + sparkle_size],
                        fill=(255, 255, 255, 200))
            
            img = img.resize((128, 128), Image.Resampling.LANCZOS)
            frames.append(img)
    
    elif effect_type == "rainbow":
        rainbow_colors = ["#FF0000", "#FF7F00", "#FFFF00", "#00FF00", "#0000FF", "#4B0082", "#9400D3"]
        for i in range(14):
            img = Image.new('RGBA', (size, size), (255, 255, 255, 0))
            draw = ImageDraw.Draw(img)
            
            color_idx = i % len(rainbow_colors)
            current_color = rainbow_colors[color_idx]
            
            bbox = draw.textbbox((0, 0), text, font=font)
            text_width = bbox[2] - bbox[0]
            text_height = bbox[3] - bbox[1]
            x = (size - text_width) // 2
            y = (size - text_height) // 2 - bbox[1]
            
            draw.text((x, y), text, fill=current_color, font=font)
            
            img = img.resize((128, 128), Image.Resampling.LANCZOS)
            frames.append(img)
    
    elif effect_type == "pulse":
        for i in range(8):
            img = Image.new('RGBA', (size, size), (255, 255, 255, 0))
            draw = ImageDraw.Draw(img)
            
            # Calculate pulse scale
            scale_factor = 1 + 0.2 * math.sin(i * math.pi / 4)
            pulse_font_size = int(base_size * scale_factor)
            
            try:
                pulse_font = ImageFont.truetype(font.path, pulse_font_size)
            except:
                pulse_font = font
            
            bbox = draw.textbbox((0, 0), text, font=pulse_font)
            text_width = bbox[2] - bbox[0]
            text_height = bbox[3] - bbox[1]
            x = (size - text_width) // 2
            y = (size - text_height) // 2 - bbox[1]
            
            draw.text((x, y), text, fill=color, font=pulse_font)
            
            img = img.resize((128, 128), Image.Resampling.LANCZOS)
            frames.append(img)
    
    elif effect_type == "glow":
        for i in range(8):
            img = Image.new('RGBA', (size, size), (255, 255, 255, 0))
            draw = ImageDraw.Draw(img)
            
            # Draw glow effect
            glow_intensity = int(100 + 155 * abs(math.sin(i * math.pi / 4)))
            for offset in range(3, 0, -1):
                glow_alpha = glow_intensity // (offset + 1)
                bbox = draw.textbbox((0, 0), text, font=font)
                text_width = bbox[2] - bbox[0]
                text_height = bbox[3] - bbox[1]
                x = (size - text_width) // 2
                y = (size - text_height) // 2 - bbox[1]
                
                for dx in [-offset*scale, 0, offset*scale]:
                    for dy in [-offset*scale, 0, offset*scale]:
                        if dx != 0 or dy != 0:
                            draw.text((x + dx, y + dy), text, 
                                    fill=color[:7] + f"{glow_alpha:02x}", font=font)
            
            # Draw main text
            draw.text((x, y), text, fill=color, font=font)
            
            img = img.resize((128, 128), Image.Resampling.LANCZOS)
            frames.append(img)
    
    elif effect_type == "shake":
        for i in range(8):
            img = Image.new('RGBA', (size, size), (255, 255, 255, 0))
            draw = ImageDraw.Draw(img)
            
            # Calculate shake offset
            offset_x = int(5 * scale * math.sin(i * math.pi))
            offset_y = 0
            
            bbox = draw.textbbox((0, 0), text, font=font)
            text_width = bbox[2] - bbox[0]
            text_height = bbox[3] - bbox[1]
            x = (size - text_width) // 2 + offset_x
            y = (size - text_height) // 2 - bbox[1] + offset_y
            
            draw.text((x, y), text, fill=color, font=font)
            
            img = img.resize((128, 128), Image.Resampling.LANCZOS)
            frames.append(img)
    
    elif effect_type == "bounce":
        for i in range(8):
            img = Image.new('RGBA', (size, size), (255, 255, 255, 0))
            draw = ImageDraw.Draw(img)
            
            # Calculate bounce offset
            bounce_height = abs(math.sin(i * math.pi / 4)) * 20 * scale
            
            bbox = draw.textbbox((0, 0), text, font=font)
            text_width = bbox[2] - bbox[0]
            text_height = bbox[3] - bbox[1]
            x = (size - text_width) // 2
            y = (size - text_height) // 2 - bbox[1] - int(bounce_height)
            
            draw.text((x, y), text, fill=color, font=font)
            
            img = img.resize((128, 128), Image.Resampling.LANCZOS)
            frames.append(img)
    
    elif effect_type == "rotate":
        for i in range(12):
            img = Image.new('RGBA', (size, size), (255, 255, 255, 0))
            
            # Create text image
            text_img = Image.new('RGBA', (size, size), (255, 255, 255, 0))
            draw = ImageDraw.Draw(text_img)
            
            bbox = draw.textbbox((0, 0), text, font=font)
            text_width = bbox[2] - bbox[0]
            text_height = bbox[3] - bbox[1]
            x = (size - text_width) // 2
            y = (size - text_height) // 2 - bbox[1]
            
            draw.text((x, y), text, fill=color, font=font)
            
            # Rotate
            angle = i * 30
            rotated = text_img.rotate(-angle, expand=False, fillcolor=(255, 255, 255, 0))
            
            img.paste(rotated, (0, 0), rotated)
            img = img.resize((128, 128), Image.Resampling.LANCZOS)
            frames.append(img)
    
    elif effect_type == "fade":
        for i in range(8):
            img = Image.new('RGBA', (size, size), (255, 255, 255, 0))
            draw = ImageDraw.Draw(img)
            
            # Calculate fade alpha
            alpha = int(100 + 155 * abs(math.sin(i * math.pi / 4)))
            
            bbox = draw.textbbox((0, 0), text, font=font)
            text_width = bbox[2] - bbox[0]
            text_height = bbox[3] - bbox[1]
            x = (size - text_width) // 2
            y = (size - text_height) // 2 - bbox[1]
            
            # Apply alpha to color
            if color:
                fade_color = color[:7] + f"{alpha:02x}"
            else:
                fade_color = f"#000000{alpha:02x}"
            
            draw.text((x, y), text, fill=fade_color, font=font)
            
            img = img.resize((128, 128), Image.Resampling.LANCZOS)
            frames.append(img)
    
    # Save GIF
    filename = f"{name}.gif"
    filepath = os.path.join(output_dir, filename)
    frames[0].save(filepath, save_all=True, append_images=frames[1:], 
                  duration=100, loop=0, disposal=2)
    print(f"Created: {filename}")
    return filename

def main():
    output_dir = "/Users/rene/asyncsite/slack-emoji-packs/images/korean-words"
    
    print("Creating special effect GIF emojis...")
    created_files = []
    
    for name, text, color, effect_type, description in SPECIAL_EFFECT_EMOJIS:
        created_files.append(create_special_effect_gif(text, color, name, effect_type, output_dir))
    
    print(f"\n✅ Created {len(created_files)} special effect GIF emojis")
    print("\nCreated files:")
    for f in created_files[:10]:  # Show first 10 as sample
        print(f"  - {f}")
    if len(created_files) > 10:
        print(f"  ... and {len(created_files) - 10} more")
    
    return created_files

if __name__ == "__main__":
    main()
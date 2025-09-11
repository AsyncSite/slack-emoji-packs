#!/usr/bin/env python3
"""
Create Korean word emojis for korean-words pack
"""

from PIL import Image, ImageDraw, ImageFont
import os

output_dir = "images/korean-words"
os.makedirs(output_dir, exist_ok=True)

def create_text_emoji(text, filename, bg_color=(255, 255, 255, 0), text_color=(33, 33, 33, 255), font_size=48):
    """Create a text-based emoji with Korean text"""
    size = 128
    img = Image.new('RGBA', (size, size), bg_color)
    draw = ImageDraw.Draw(img)
    
    # Try to use a Korean font, fallback to default if not available
    try:
        # Try common Korean fonts on macOS
        font = ImageFont.truetype("/System/Library/Fonts/AppleSDGothicNeo.ttc", font_size)
    except:
        try:
            font = ImageFont.truetype("/System/Library/Fonts/Supplemental/AppleGothicRegular.ttf", font_size)
        except:
            # Fallback to default font
            font = ImageFont.load_default()
    
    # Get text bounding box
    bbox = draw.textbbox((0, 0), text, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]
    
    # Center the text
    x = (size - text_width) // 2
    y = (size - text_height) // 2
    
    # Draw text
    draw.text((x, y), text, fill=text_color, font=font)
    
    return img

def create_styled_text_emoji(text, filename, style="default"):
    """Create styled text emojis with different backgrounds and effects"""
    size = 128
    
    if style == "positive":
        # Green background for positive words
        img = Image.new('RGBA', (size, size), (76, 175, 80, 255))
        text_color = (255, 255, 255, 255)
    elif style == "negative":
        # Red background for negative words  
        img = Image.new('RGBA', (size, size), (244, 67, 54, 255))
        text_color = (255, 255, 255, 255)
    elif style == "emphasis":
        # Yellow background for emphasis
        img = Image.new('RGBA', (size, size), (255, 235, 59, 255))
        text_color = (33, 33, 33, 255)
    elif style == "question":
        # Blue background for questions
        img = Image.new('RGBA', (size, size), (33, 150, 243, 255))
        text_color = (255, 255, 255, 255)
    elif style == "casual":
        # Purple gradient for casual words
        img = Image.new('RGBA', (size, size), (156, 39, 176, 255))
        text_color = (255, 255, 255, 255)
    else:
        # Default transparent background
        img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
        text_color = (33, 33, 33, 255)
    
    draw = ImageDraw.Draw(img)
    
    # Add rounded corners if has background
    if style != "default":
        # Create rounded rectangle
        mask = Image.new('L', (size, size), 0)
        mask_draw = ImageDraw.Draw(mask)
        mask_draw.rounded_rectangle([0, 0, size, size], radius=20, fill=255)
        
        # Apply mask
        img.putalpha(mask)
        draw = ImageDraw.Draw(img)
    
    # Try to use a Korean font
    font_size = 48 if len(text) <= 2 else 36 if len(text) <= 3 else 28
    try:
        font = ImageFont.truetype("/System/Library/Fonts/AppleSDGothicNeo.ttc", font_size)
    except:
        try:
            font = ImageFont.truetype("/System/Library/Fonts/Supplemental/AppleGothicRegular.ttf", font_size)
        except:
            font = ImageFont.load_default()
    
    # Get text bounding box
    bbox = draw.textbbox((0, 0), text, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]
    
    # Center the text
    x = (size - text_width) // 2
    y = (size - text_height) // 2
    
    # Draw text
    draw.text((x, y), text, fill=text_color, font=font)
    
    return img

# Korean words to create
korean_words = [
    # Positive responses
    ("굿", "positive"),
    ("네", "positive"),
    ("네_", "positive"),  # Alternative 네
    ("넵", "positive"),
    ("넹", "casual"),
    ("예", "positive"),
    ("완료", "positive"),
    ("최고", "positive"),
    ("화이팅", "positive"),
    ("확인", "positive"),
    
    # Negative/Question
    ("아니", "negative"),
    ("아니_", "negative"),  # Alternative 아니
    ("헐", "emphasis"),
    ("님아", "emphasis"),
    ("제발요", "emphasis"),
    
    # Reactions
    ("아하", "default"),
    ("어허", "question"),
    ("ㅇㅎ", "casual"),
    ("진짜", "emphasis"),
    ("흠", "question"),
    
    # Casual/Fun
    ("ㅋㅋㅋ_ㅋㅋㅋ", "casual"),
    ("대빵_동건", "casual"),
    
    # Work related
    ("일해", "negative"),
    ("확인중", "default"),
    ("도큐멘토", "default"),
    ("돈", "positive"),
]

# Create static PNG emojis
print("Creating Korean word emojis...")
for word, style in korean_words:
    filename = f"{word}.png"
    img = create_styled_text_emoji(word, filename, style)
    img.save(f"{output_dir}/{filename}")
    print(f"  Created {filename}")

# Create animated GIF emojis (reuse some from reactions pack)
print("\nCreating animated GIF emojis...")

# Import functions from other scripts for consistency
def create_simple_loading_frame(frame_num, total_frames=8):
    """Create simple loading animation"""
    size = 128
    img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # Loading circle
    angle = (frame_num / total_frames) * 360
    start_angle = angle - 30
    end_angle = angle + 30
    
    draw.arc([40, 40, 88, 88], start=start_angle, end=end_angle, 
             fill=(33, 150, 243, 255), width=6)
    
    return img

def create_alert_frame(frame_num, total_frames=6):
    """Create alert/warning animation"""
    size = 128
    img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # Flashing alert triangle
    if frame_num % 2 == 0:
        color = (244, 67, 54, 255)  # Red
    else:
        color = (255, 152, 0, 255)  # Orange
    
    # Draw triangle
    draw.polygon([(64, 30), (94, 80), (34, 80)], fill=color)
    
    # Exclamation mark
    draw.rectangle([60, 45, 68, 60], fill=(255, 255, 255, 255))
    draw.ellipse([60, 65, 68, 73], fill=(255, 255, 255, 255))
    
    return img

# Create animated GIFs
gif_emojis = [
    ("loading", create_simple_loading_frame, 8, 150),
    ("alert", create_alert_frame, 6, 200),
]

for name, create_frame_func, total_frames, duration in gif_emojis:
    frames = []
    for i in range(total_frames):
        frame = create_frame_func(i, total_frames)
        frames.append(frame)
    
    frames[0].save(f"{output_dir}/{name}.gif", save_all=True,
                   append_images=frames[1:], duration=duration, loop=0)
    print(f"  Created {name}.gif")

# Copy/link some existing GIFs that match Korean words
existing_gifs = [
    ("clapping", "../reactions/clapping.gif"),
    ("excited", "../reactions/heart_beat.gif"),
    ("thinking", "../reactions/typing.gif"),
    ("surprise", "../reactions/mind_blown.gif"),
    ("party", "../reactions/thumbs_up.gif"),
    ("typingcat", "../work-from-home/cat_walking.gif"),
    ("scroll", "../dev-essentials/loading_dots.gif"),
    ("lol", "../reactions/clapping.gif"),
    ("fb-wow", "../reactions/mind_blown.gif"),
    ("cool-doge", "../startup-hustle/rocket_launch.gif"),
]

print("\nCopying existing GIFs...")
for name, source in existing_gifs:
    source_path = f"images/{source}"
    if os.path.exists(source_path):
        # Read and save as new file
        img = Image.open(source_path)
        img.save(f"{output_dir}/{name}.gif")
        print(f"  Copied {name}.gif from {source}")

print(f"\n✅ Created Korean words emoji pack with {len(korean_words)} PNGs and {len(gif_emojis) + len(existing_gifs)} GIFs!")
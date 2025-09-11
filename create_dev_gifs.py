#!/usr/bin/env python3
"""
Create animated GIF emojis for dev-essentials pack
"""

from PIL import Image, ImageDraw, ImageFont
import os
import math

output_dir = "images/dev-essentials"
os.makedirs(output_dir, exist_ok=True)

def create_loading_dots_frame(frame_num, total_frames=8):
    """Create loading dots animation frame"""
    size = 128
    img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # Three dots that animate
    dot_size = 12
    y = 64
    spacing = 30
    start_x = 34
    
    for i in range(3):
        x = start_x + i * spacing
        # Animate each dot with a phase offset
        phase = (frame_num + i * 2) % total_frames
        opacity = int(100 + 155 * (0.5 + 0.5 * math.sin(phase * 2 * math.pi / total_frames)))
        scale = 0.8 + 0.2 * math.sin(phase * 2 * math.pi / total_frames)
        current_size = int(dot_size * scale)
        
        color = (33, 150, 243, opacity)  # Blue
        draw.ellipse([x-current_size, y-current_size, x+current_size, y+current_size], fill=color)
    
    return img

def create_compiling_frame(frame_num, total_frames=10):
    """Create compiling progress animation"""
    size = 128
    img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # Terminal window outline
    terminal_color = (40, 44, 52, 255)  # Dark terminal
    draw.rounded_rectangle([20, 30, 108, 98], radius=5, fill=terminal_color)
    
    # Terminal header
    header_color = (61, 67, 79, 255)
    draw.rectangle([20, 30, 108, 45], fill=header_color)
    
    # Terminal buttons
    button_colors = [(237, 106, 94), (245, 191, 79), (97, 197, 84)]
    for i, color in enumerate(button_colors):
        draw.ellipse([27 + i*12, 36, 33 + i*12, 42], fill=color)
    
    # Progress bar background
    draw.rectangle([30, 60, 98, 70], fill=(61, 67, 79, 255))
    
    # Animated progress bar
    progress = (frame_num / total_frames) * 68
    if progress > 0:
        draw.rectangle([30, 60, 30 + progress, 70], fill=(97, 197, 84, 255))
    
    # Progress text
    text_color = (171, 178, 191, 255)
    percent = int((frame_num / total_frames) * 100)
    draw.text((55, 75), f"{percent}%", fill=text_color)
    
    return img

def create_deploying_frame(frame_num, total_frames=12):
    """Create deploying rocket animation"""
    size = 128
    img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # Cloud/server at top
    cloud_color = (100, 181, 246, 255)
    draw.ellipse([45, 15, 83, 35], fill=cloud_color)
    draw.ellipse([35, 20, 60, 38], fill=cloud_color)
    draw.ellipse([68, 20, 93, 38], fill=cloud_color)
    
    # Package/box moving up
    progress = frame_num / total_frames
    box_y = 90 - (progress * 50)  # Moves from y=90 to y=40
    
    # Box
    box_color = (255, 167, 38, 255)
    draw.rectangle([54, box_y, 74, box_y + 20], fill=box_color)
    
    # Box tape
    tape_color = (230, 126, 34, 255)
    draw.rectangle([54, box_y + 8, 74, box_y + 12], fill=tape_color)
    draw.rectangle([62, box_y, 66, box_y + 20], fill=tape_color)
    
    # Motion lines below box
    if progress > 0.1:
        line_color = (189, 189, 189, 100)
        for i in range(3):
            line_y = box_y + 25 + i * 5
            if line_y < 110:
                draw.rectangle([60 - i*3, line_y, 68 + i*3, line_y + 2], fill=line_color)
    
    return img

def create_debugging_frame(frame_num, total_frames=8):
    """Create debugging bug animation"""
    size = 128
    img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # Magnifying glass (static)
    glass_color = (66, 66, 66, 255)
    # Glass circle
    draw.ellipse([30, 30, 70, 70], outline=glass_color, width=4)
    # Glass handle
    draw.line([(68, 68), (88, 88)], fill=glass_color, width=6)
    
    # Bug moving around
    angle = (frame_num / total_frames) * 2 * math.pi
    bug_x = 50 + 12 * math.cos(angle)
    bug_y = 50 + 12 * math.sin(angle)
    
    # Bug body
    bug_color = (244, 67, 54, 255)
    draw.ellipse([bug_x-8, bug_y-6, bug_x+8, bug_y+6], fill=bug_color)
    
    # Bug spots
    spot_color = (183, 28, 28, 255)
    draw.ellipse([bug_x-5, bug_y-3, bug_x-1, bug_y+1], fill=spot_color)
    draw.ellipse([bug_x+1, bug_y-3, bug_x+5, bug_y+1], fill=spot_color)
    
    # Bug legs (simplified)
    leg_color = (33, 33, 33, 255)
    for i in range(-1, 2):
        draw.line([(bug_x-6, bug_y+i*3), (bug_x-10, bug_y+i*4)], fill=leg_color, width=1)
        draw.line([(bug_x+6, bug_y+i*3), (bug_x+10, bug_y+i*4)], fill=leg_color, width=1)
    
    return img

def create_code_typing_frame(frame_num, total_frames=12):
    """Create code typing animation"""
    size = 128
    img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # Editor background
    editor_bg = (40, 44, 52, 255)
    draw.rounded_rectangle([15, 20, 113, 108], radius=5, fill=editor_bg)
    
    # Line numbers background
    line_bg = (49, 54, 63, 255)
    draw.rectangle([15, 20, 35, 108], fill=line_bg)
    
    # Line numbers
    line_color = (121, 129, 142, 255)
    for i in range(5):
        draw.text((22, 30 + i*15), str(i+1), fill=line_color)
    
    # Code colors
    keyword_color = (198, 120, 221, 255)  # Purple
    string_color = (152, 195, 121, 255)   # Green
    func_color = (97, 175, 239, 255)      # Blue
    text_color = (171, 178, 191, 255)     # Gray
    
    # Animated typing effect
    code_lines = [
        ("function", keyword_color, "hello", func_color),
        ("  console", text_color, ".log", func_color),
        ("  return", keyword_color, "true", string_color),
        ("}", text_color, "", None)
    ]
    
    # Calculate how many characters to show
    chars_per_frame = 3
    total_chars = frame_num * chars_per_frame
    
    y_pos = 30
    chars_shown = 0
    
    for line in code_lines[:min(frame_num // 3 + 1, len(code_lines))]:
        x_pos = 40
        if chars_shown < total_chars:
            # First part
            if line[0] and chars_shown + len(line[0]) <= total_chars:
                draw.text((x_pos, y_pos), line[0], fill=line[1])
                x_pos += len(line[0]) * 6
                chars_shown += len(line[0])
            
            # Second part
            if line[2] and chars_shown + len(line[2]) <= total_chars:
                draw.text((x_pos + 5, y_pos), line[2], fill=line[3])
                chars_shown += len(line[2])
        
        y_pos += 15
    
    # Blinking cursor
    if frame_num % 4 < 2:
        cursor_x = 40 + min(total_chars * 6, 60)
        cursor_y = min(30 + (frame_num // 3) * 15, 75)
        draw.rectangle([cursor_x, cursor_y, cursor_x + 2, cursor_y + 12], fill=(255, 255, 255, 255))
    
    return img

# Generate all GIF animations
if __name__ == "__main__":
    print("Creating dev-essentials GIF emojis...")
    
    # 1. Loading dots
    print("Creating loading_dots.gif...")
    frames = []
    for i in range(8):
        frame = create_loading_dots_frame(i, 8)
        frames.append(frame)
    frames[0].save(
        f"{output_dir}/loading_dots.gif",
        save_all=True,
        append_images=frames[1:],
        duration=150,
        loop=0
    )
    
    # 2. Compiling
    print("Creating compiling.gif...")
    frames = []
    for i in range(10):
        frame = create_compiling_frame(i, 10)
        frames.append(frame)
    frames[0].save(
        f"{output_dir}/compiling.gif",
        save_all=True,
        append_images=frames[1:],
        duration=200,
        loop=0
    )
    
    # 3. Deploying
    print("Creating deploying.gif...")
    frames = []
    for i in range(12):
        frame = create_deploying_frame(i, 12)
        frames.append(frame)
    frames[0].save(
        f"{output_dir}/deploying.gif",
        save_all=True,
        append_images=frames[1:],
        duration=100,
        loop=0
    )
    
    # 4. Debugging
    print("Creating debugging.gif...")
    frames = []
    for i in range(8):
        frame = create_debugging_frame(i, 8)
        frames.append(frame)
    frames[0].save(
        f"{output_dir}/debugging.gif",
        save_all=True,
        append_images=frames[1:],
        duration=150,
        loop=0
    )
    
    # 5. Code typing
    print("Creating code_typing.gif...")
    frames = []
    for i in range(12):
        frame = create_code_typing_frame(i, 12)
        frames.append(frame)
    frames[0].save(
        f"{output_dir}/code_typing.gif",
        save_all=True,
        append_images=frames[1:],
        duration=150,
        loop=0
    )
    
    print("\n✅ Created 5 GIF emojis for dev-essentials pack!")
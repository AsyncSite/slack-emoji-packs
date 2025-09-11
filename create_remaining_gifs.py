#!/usr/bin/env python3
"""
Create animated GIF emojis for korean-culture, work-from-home, and korean-office packs
"""

from PIL import Image, ImageDraw
import os
import math

# Korean Culture GIFs
def create_bow_frame(frame_num, total_frames=8):
    """Create bowing animation (Korean greeting)"""
    size = 128
    img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # Bow angle based on frame
    bow_angle = abs(math.sin(frame_num * math.pi / total_frames)) * 30
    
    # Head
    head_y = 35 + bow_angle
    draw.ellipse([54, head_y, 74, head_y + 20], fill=(255, 220, 177, 255))
    
    # Hair
    draw.ellipse([54, head_y-5, 74, head_y+10], fill=(33, 33, 33, 255))
    
    # Body (bending)
    body_top_y = head_y + 20
    body_bend = bow_angle * 0.5
    draw.ellipse([50, body_top_y, 78, body_top_y + 40 - body_bend], fill=(100, 181, 246, 255))
    
    # Arms (hands together in front when bowing)
    if bow_angle > 10:
        # Hands in front
        draw.ellipse([58, body_top_y + 25, 70, body_top_y + 35], fill=(255, 220, 177, 255))
    else:
        # Arms at sides
        draw.ellipse([45, body_top_y + 10, 52, body_top_y + 30], fill=(100, 181, 246, 255))
        draw.ellipse([76, body_top_y + 10, 83, body_top_y + 30], fill=(100, 181, 246, 255))
    
    # Legs
    leg_top = min(body_top_y + 35, 85)
    draw.rectangle([56, leg_top, 62, 95], fill=(66, 66, 66, 255))
    draw.rectangle([66, leg_top, 72, 95], fill=(66, 66, 66, 255))
    
    return img

def create_soju_pour_frame(frame_num, total_frames=10):
    """Create soju pouring animation"""
    size = 128
    img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # Soju bottle (green)
    bottle_angle = -30 + (frame_num / total_frames) * 60  # Tilt animation
    bottle_color = (76, 175, 80, 255)
    
    # Bottle body
    draw.polygon([
        (30, 30), (40, 30), (38, 60), (32, 60)
    ], fill=bottle_color)
    # Bottle neck
    draw.rectangle([34, 25, 36, 30], fill=bottle_color)
    
    # Shot glass
    glass_color = (224, 224, 224, 200)
    draw.polygon([
        (70, 70), (80, 70), (78, 85), (72, 85)
    ], fill=glass_color)
    
    # Liquid pouring (if bottle is tilted enough)
    if frame_num > 2 and frame_num < 8:
        liquid_color = (224, 247, 250, 200)
        # Pour stream
        pour_progress = (frame_num - 2) / 5
        stream_y = 60 + pour_progress * 25
        draw.rectangle([36, 60, 38, stream_y], fill=liquid_color)
        
        # Liquid in glass
        liquid_level = 80 - (pour_progress * 8)
        draw.polygon([
            (72, liquid_level), (78, liquid_level), 
            (78, 85), (72, 85)
        ], fill=liquid_color)
    
    return img

# Work From Home GIFs
def create_coffee_steam_frame(frame_num, total_frames=12):
    """Create steaming coffee mug animation"""
    size = 128
    img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # Coffee mug
    mug_color = (121, 85, 72, 255)
    draw.rounded_rectangle([45, 60, 75, 90], radius=5, fill=mug_color)
    # Handle
    draw.ellipse([72, 68, 82, 82], outline=mug_color, width=4)
    
    # Coffee inside
    coffee_color = (62, 39, 35, 255)
    draw.rectangle([48, 63, 72, 87], fill=coffee_color)
    
    # Steam animation
    for i in range(3):
        # Each steam line has different phase
        phase = (frame_num + i * 4) % total_frames
        steam_x = 52 + i * 8
        
        # Steam rises and wiggles
        for j in range(5):
            y_pos = 60 - j * 8 - phase * 2
            if y_pos > 20:
                wiggle = math.sin((phase + j) * 0.5) * 3
                opacity = int(150 - j * 20 - phase * 10)
                if opacity > 0:
                    steam_color = (189, 189, 189, opacity)
                    draw.ellipse([steam_x + wiggle - 3, y_pos - 3,
                                 steam_x + wiggle + 3, y_pos + 3], 
                                fill=steam_color)
    
    return img

def create_cat_walking_frame(frame_num, total_frames=12):
    """Create cat walking on keyboard animation"""
    size = 128
    img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # Keyboard
    keyboard_color = (189, 189, 189, 255)
    draw.rounded_rectangle([20, 80, 108, 100], radius=3, fill=keyboard_color)
    # Keys
    key_color = (158, 158, 158, 255)
    for i in range(8):
        for j in range(2):
            draw.rectangle([25 + i*10, 83 + j*8, 32 + i*10, 88 + j*8], fill=key_color)
    
    # Cat walking across
    cat_x = 20 + (frame_num / total_frames) * 88
    
    # Cat body
    cat_color = (255, 152, 0, 255)
    draw.ellipse([cat_x - 15, 60, cat_x + 15, 75], fill=cat_color)
    
    # Cat head
    draw.ellipse([cat_x + 10, 55, cat_x + 25, 70], fill=cat_color)
    
    # Cat ears
    draw.polygon([
        (cat_x + 12, 58), (cat_x + 10, 50), (cat_x + 15, 55)
    ], fill=cat_color)
    draw.polygon([
        (cat_x + 20, 55), (cat_x + 25, 50), (cat_x + 23, 58)
    ], fill=cat_color)
    
    # Cat tail (swaying)
    tail_sway = math.sin(frame_num * 0.5) * 10
    draw.ellipse([cat_x - 20, 55 + tail_sway, cat_x - 10, 65 + tail_sway], fill=cat_color)
    
    # Cat legs (animated walking)
    leg_phase = frame_num % 4
    for i in range(4):
        leg_x = cat_x - 10 + i * 8
        if (i + leg_phase) % 2 == 0:
            leg_y = 73
        else:
            leg_y = 75
        draw.rectangle([leg_x - 2, leg_y, leg_x + 2, 80], fill=cat_color)
    
    return img

def create_connection_lost_frame(frame_num, total_frames=8):
    """Create WiFi connection lost animation"""
    size = 128
    img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # WiFi icon base
    center_x, center_y = 64, 70
    
    # WiFi waves (blinking on/off)
    if frame_num < 4:
        # Show WiFi signal
        wifi_color = (76, 175, 80, 255)
        for i in range(3):
            radius = 15 + i * 12
            draw.arc([center_x - radius, center_y - radius,
                     center_x + radius, center_y],
                    start=225, end=315, fill=wifi_color, width=3)
    else:
        # Show disconnected
        wifi_color = (244, 67, 54, 255)
        for i in range(3):
            radius = 15 + i * 12
            draw.arc([center_x - radius, center_y - radius,
                     center_x + radius, center_y],
                    start=225, end=315, fill=wifi_color, width=2)
        
        # Red X over WiFi
        draw.line([(center_x - 15, center_y - 25), 
                  (center_x + 15, center_y + 5)], 
                 fill=(244, 67, 54, 255), width=4)
        draw.line([(center_x - 15, center_y + 5), 
                  (center_x + 15, center_y - 25)], 
                 fill=(244, 67, 54, 255), width=4)
    
    # Router dot
    draw.ellipse([center_x - 5, center_y - 5, 
                  center_x + 5, center_y + 5], 
                 fill=(66, 66, 66, 255))
    
    return img

# Korean Office GIFs
def create_clock_6pm_frame(frame_num, total_frames=12):
    """Create 6PM clock animation (칼퇴 time)"""
    size = 128
    img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # Clock face
    clock_color = (255, 255, 255, 255)
    draw.ellipse([30, 30, 98, 98], fill=clock_color)
    draw.ellipse([30, 30, 98, 98], outline=(66, 66, 66, 255), width=3)
    
    # Hour markers
    for i in range(12):
        angle = i * 30 * math.pi / 180
        x1 = 64 + 28 * math.sin(angle)
        y1 = 64 - 28 * math.cos(angle)
        x2 = 64 + 32 * math.sin(angle)
        y2 = 64 - 32 * math.cos(angle)
        draw.line([(x1, y1), (x2, y2)], fill=(66, 66, 66, 255), width=2)
    
    # Hour hand (pointing to 6)
    draw.line([(64, 64), (64, 85)], fill=(33, 33, 33, 255), width=4)
    
    # Minute hand (moving to 12 for 6:00)
    minute_angle = (frame_num / total_frames) * 30 - 90  # Move from 11:30 to 12:00
    minute_x = 64 + 25 * math.cos(minute_angle * math.pi / 180)
    minute_y = 64 + 25 * math.sin(minute_angle * math.pi / 180)
    draw.line([(64, 64), (minute_x, minute_y)], fill=(33, 33, 33, 255), width=3)
    
    # Celebration effects at 6:00
    if frame_num >= 10:
        # Sparkles
        sparkle_color = (255, 215, 0, 200)
        sparkle_positions = [(40, 35), (88, 35), (35, 90), (93, 90)]
        for x, y in sparkle_positions:
            draw.polygon([(x, y-3), (x-2, y), (x, y+3), (x+2, y)], 
                        fill=sparkle_color)
    
    return img

def create_overtime_meter_frame(frame_num, total_frames=10):
    """Create overtime meter filling up (야근 gauge)"""
    size = 128
    img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # Meter background
    meter_bg = (224, 224, 224, 255)
    draw.rounded_rectangle([30, 40, 98, 80], radius=5, fill=meter_bg)
    
    # Meter frame
    draw.rounded_rectangle([30, 40, 98, 80], radius=5, outline=(66, 66, 66, 255), width=2)
    
    # Fill level based on frame
    fill_progress = frame_num / total_frames
    fill_width = int(65 * fill_progress)
    
    # Color changes from green to red as it fills
    if fill_progress < 0.3:
        fill_color = (76, 175, 80, 255)  # Green
    elif fill_progress < 0.6:
        fill_color = (255, 193, 7, 255)  # Yellow
    else:
        fill_color = (244, 67, 54, 255)  # Red
    
    if fill_width > 0:
        draw.rounded_rectangle([33, 43, 33 + fill_width, 77], 
                               radius=3, fill=fill_color)
    
    # Text label
    text_color = (33, 33, 33, 255)
    draw.text((45, 85), "OVERTIME", fill=text_color)
    
    # Warning icon if meter is high
    if fill_progress > 0.7:
        warning_color = (244, 67, 54, 255) if frame_num % 2 == 0 else (255, 152, 0, 255)
        draw.polygon([(64, 20), (58, 32), (70, 32)], fill=warning_color)
        draw.text((61, 22), "!", fill=(255, 255, 255, 255))
    
    return img

# Main execution
if __name__ == "__main__":
    print("Creating GIF emojis for remaining packs...")
    
    # Korean Culture
    print("\n=== Korean Culture Pack ===")
    output_dir = "images/korean-culture"
    
    print("Creating bow.gif...")
    frames = []
    for i in range(8):
        frame = create_bow_frame(i, 8)
        frames.append(frame)
    frames[0].save(f"{output_dir}/bow.gif", save_all=True, 
                   append_images=frames[1:], duration=150, loop=0)
    
    print("Creating soju_pour.gif...")
    frames = []
    for i in range(10):
        frame = create_soju_pour_frame(i, 10)
        frames.append(frame)
    frames[0].save(f"{output_dir}/soju_pour.gif", save_all=True,
                   append_images=frames[1:], duration=150, loop=0)
    
    # Work From Home
    print("\n=== Work From Home Pack ===")
    output_dir = "images/work-from-home"
    
    print("Creating coffee_steam.gif...")
    frames = []
    for i in range(12):
        frame = create_coffee_steam_frame(i, 12)
        frames.append(frame)
    frames[0].save(f"{output_dir}/coffee_steam.gif", save_all=True,
                   append_images=frames[1:], duration=150, loop=0)
    
    print("Creating cat_walking.gif...")
    frames = []
    for i in range(12):
        frame = create_cat_walking_frame(i, 12)
        frames.append(frame)
    frames[0].save(f"{output_dir}/cat_walking.gif", save_all=True,
                   append_images=frames[1:], duration=100, loop=0)
    
    print("Creating connection_lost.gif...")
    frames = []
    for i in range(8):
        frame = create_connection_lost_frame(i, 8)
        frames.append(frame)
    frames[0].save(f"{output_dir}/connection_lost.gif", save_all=True,
                   append_images=frames[1:], duration=300, loop=0)
    
    # Korean Office  
    print("\n=== Korean Office Pack ===")
    output_dir = "images/korean-office"
    
    print("Creating clock_6pm.gif...")
    frames = []
    for i in range(12):
        frame = create_clock_6pm_frame(i, 12)
        frames.append(frame)
    frames[0].save(f"{output_dir}/clock_6pm.gif", save_all=True,
                   append_images=frames[1:], duration=100, loop=0)
    
    print("Creating overtime_meter.gif...")
    frames = []
    for i in range(10):
        frame = create_overtime_meter_frame(i, 10)
        frames.append(frame)
    frames[0].save(f"{output_dir}/overtime_meter.gif", save_all=True,
                   append_images=frames[1:], duration=200, loop=0)
    
    print("\n✅ Created all remaining GIF emojis!")
    print("  - Korean Culture: 2 GIFs")
    print("  - Work From Home: 3 GIFs") 
    print("  - Korean Office: 2 GIFs")
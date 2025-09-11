#!/usr/bin/env python3
"""
Test creating animated GIF emoji
Creating a loading spinner GIF for startup-hustle pack
"""

from PIL import Image, ImageDraw
import os
import math

# Create output directory
output_dir = "images/startup-hustle"
os.makedirs(output_dir, exist_ok=True)

def create_loading_frame(frame_num, total_frames=8):
    """Create a single frame of the loading spinner"""
    size = 128
    img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # Center point
    center_x = 64
    center_y = 64
    
    # Draw circular loading dots
    num_dots = 8
    radius = 25  # Distance from center
    dot_size = 8  # Size of each dot
    
    for i in range(num_dots):
        # Calculate angle for each dot
        angle = (360 / num_dots) * i
        rad = math.radians(angle)
        
        # Calculate dot position
        x = center_x + radius * math.cos(rad)
        y = center_y + radius * math.sin(rad)
        
        # Calculate opacity based on frame (creates spinning effect)
        # The "active" dot position rotates with frame_num
        active_position = frame_num % num_dots
        distance_from_active = min(
            abs(i - active_position),
            num_dots - abs(i - active_position)
        )
        
        # Opacity decreases with distance from active position
        opacity = int(255 - (distance_from_active * 30))
        opacity = max(50, opacity)  # Minimum opacity
        
        # Color with varying opacity (startup purple/blue)
        if distance_from_active == 0:
            color = (63, 81, 181, opacity)  # Blue for active
        else:
            color = (156, 39, 176, opacity)  # Purple for others
        
        # Draw dot
        draw.ellipse([x-dot_size, y-dot_size, x+dot_size, y+dot_size], fill=color)
    
    # Add "LOADING" text below (optional)
    text_color = (66, 66, 66, 200)
    draw.text((45, 95), "LOADING", fill=text_color, font=None)
    
    return img

def create_rocket_launch_frame(frame_num, total_frames=12):
    """Create a frame of rocket launching animation"""
    size = 128
    img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # Rocket moves up over time
    progress = frame_num / total_frames
    
    # Rocket starting at bottom, moving up
    rocket_y = 90 - (progress * 70)  # Moves from y=90 to y=20
    rocket_x = 64
    
    # Rocket body
    rocket_color = (244, 67, 54)
    draw.polygon([
        (rocket_x-8, rocket_y+15),  # Bottom left
        (rocket_x+8, rocket_y+15),   # Bottom right
        (rocket_x+8, rocket_y-5),    # Top right
        (rocket_x, rocket_y-15),     # Tip
        (rocket_x-8, rocket_y-5)     # Top left
    ], fill=rocket_color)
    
    # Rocket window
    window_color = (135, 206, 250)
    draw.ellipse([rocket_x-4, rocket_y-5, rocket_x+4, rocket_y+3], fill=window_color)
    
    # Rocket fins
    fin_color = (198, 40, 40)
    # Left fin
    draw.polygon([
        (rocket_x-8, rocket_y+10),
        (rocket_x-15, rocket_y+15),
        (rocket_x-8, rocket_y+5)
    ], fill=fin_color)
    # Right fin
    draw.polygon([
        (rocket_x+8, rocket_y+10),
        (rocket_x+15, rocket_y+15),
        (rocket_x+8, rocket_y+5)
    ], fill=fin_color)
    
    # Flames (get bigger as rocket goes up)
    flame_size = 1 + progress * 0.5
    
    # Outer flame (orange)
    flame_outer = (255, 152, 0, 200)
    for i in range(3):
        offset = (i - 1) * 5
        flame_y = rocket_y + 15
        # Flame flickers by alternating size based on frame
        flicker = 1 + 0.3 * math.sin(frame_num * 0.5 + i)
        flame_height = 15 * flame_size * flicker
        
        draw.polygon([
            (rocket_x + offset - 3, flame_y),
            (rocket_x + offset, flame_y + flame_height),
            (rocket_x + offset + 3, flame_y)
        ], fill=flame_outer)
    
    # Inner flame (yellow)
    flame_inner = (255, 235, 59, 220)
    flame_y = rocket_y + 15
    flame_height = 10 * flame_size
    draw.polygon([
        (rocket_x - 2, flame_y),
        (rocket_x, flame_y + flame_height),
        (rocket_x + 2, flame_y)
    ], fill=flame_inner)
    
    # Smoke trails (fade over time)
    smoke_color = (158, 158, 158, int(100 * (1 - progress)))
    if progress > 0.2:  # Start showing smoke after initial launch
        for i in range(3):
            smoke_y = 95 - (i * 10 * progress)
            smoke_x = rocket_x + (i - 1) * 8
            if smoke_y > rocket_y + 20:  # Only show smoke below rocket
                draw.ellipse([smoke_x-6, smoke_y-4, smoke_x+6, smoke_y+4], fill=smoke_color)
    
    # Stars in background (appear as rocket goes higher)
    if progress > 0.5:
        star_opacity = int((progress - 0.5) * 2 * 255)
        star_color = (255, 255, 255, star_opacity)
        stars = [(30, 25), (90, 30), (40, 45), (85, 50)]
        for x, y in stars:
            draw.polygon([
                (x, y-2), (x-1, y), (x, y+2), (x+1, y)
            ], fill=star_color)
    
    return img

def create_celebrating_parrot_frame(frame_num, total_frames=10):
    """Create a frame of party parrot animation"""
    size = 128
    img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # Parrot colors cycle through rainbow
    colors = [
        (244, 67, 54),   # Red
        (255, 152, 0),   # Orange
        (255, 235, 59),  # Yellow
        (76, 175, 80),   # Green
        (33, 150, 243),  # Blue
        (156, 39, 176),  # Purple
    ]
    
    # Current color based on frame
    color_index = frame_num % len(colors)
    parrot_color = colors[color_index]
    
    # Parrot bounces up and down
    bounce = math.sin(frame_num * 0.6) * 5
    base_y = 64 + bounce
    
    # Body
    draw.ellipse([45, base_y-20, 83, base_y+20], fill=parrot_color)
    
    # Head (also bounces)
    head_y = base_y - 25 + bounce * 0.5
    draw.ellipse([50, head_y-15, 78, head_y+13], fill=parrot_color)
    
    # Beak
    beak_color = (255, 193, 7)
    draw.polygon([
        (50, head_y),
        (40, head_y+3),
        (50, head_y+6)
    ], fill=beak_color)
    
    # Eye
    eye_white = (255, 255, 255)
    draw.ellipse([55, head_y-5, 63, head_y+3], fill=eye_white)
    draw.ellipse([57, head_y-3, 61, head_y+1], fill=(0, 0, 0))
    
    # Wing (flaps)
    wing_angle = math.sin(frame_num * 0.8) * 20
    wing_y = base_y + wing_angle
    
    # Darker shade for wing
    wing_color = tuple(int(c * 0.8) for c in parrot_color[:3])
    draw.ellipse([75, wing_y-10, 95, wing_y+10], fill=wing_color)
    
    # Party elements - confetti
    confetti_colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0)]
    for i in range(8):
        # Confetti falls and rotates
        conf_y = (frame_num * 5 + i * 15) % 128
        conf_x = 20 + i * 12
        conf_color = confetti_colors[i % len(confetti_colors)]
        
        # Rotate confetti
        angle = frame_num * 20 + i * 45
        size_mod = 3 + math.sin(angle * 0.1) * 2
        
        draw.rectangle([conf_x, conf_y, conf_x+size_mod, conf_y+size_mod*2], 
                      fill=conf_color)
    
    return img

# Generate test GIFs
if __name__ == "__main__":
    print("Creating animated GIF emojis...")
    
    # 1. Loading spinner
    print("Creating loading spinner GIF...")
    frames = []
    for i in range(8):
        frame = create_loading_frame(i, 8)
        frames.append(frame)
    
    # Save as animated GIF
    frames[0].save(
        f"{output_dir}/loading_spinner.gif",
        save_all=True,
        append_images=frames[1:],
        duration=100,  # 100ms per frame
        loop=0  # Infinite loop
    )
    print("Created loading_spinner.gif")
    
    # 2. Rocket launch
    print("Creating rocket launch GIF...")
    frames = []
    for i in range(12):
        frame = create_rocket_launch_frame(i, 12)
        frames.append(frame)
    
    frames[0].save(
        f"{output_dir}/rocket_launch.gif",
        save_all=True,
        append_images=frames[1:],
        duration=80,
        loop=0
    )
    print("Created rocket_launch.gif")
    
    # 3. Party parrot
    print("Creating party parrot GIF...")
    frames = []
    for i in range(10):
        frame = create_celebrating_parrot_frame(i, 10)
        frames.append(frame)
    
    frames[0].save(
        f"{output_dir}/party_parrot.gif",
        save_all=True,
        append_images=frames[1:],
        duration=60,  # Faster for party effect
        loop=0
    )
    print("Created party_parrot.gif")
    
    print("\nAll test GIF emojis created successfully!")
    print("Files saved in:", output_dir)
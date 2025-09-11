#!/usr/bin/env python3
"""
Create animated GIF emojis for reactions pack
"""

from PIL import Image, ImageDraw
import os
import math

output_dir = "images/reactions"
os.makedirs(output_dir, exist_ok=True)

def create_clapping_frame(frame_num, total_frames=8):
    """Create clapping hands animation"""
    size = 128
    img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # Hands clapping animation
    clap_phase = abs(math.sin(frame_num * math.pi / (total_frames / 2)))
    separation = 5 + 25 * clap_phase  # Hands separate and come together
    
    # Left hand
    left_x = 64 - separation
    draw.ellipse([left_x-20, 50, left_x, 78], fill=(255, 220, 177, 255))
    # Left thumb
    draw.ellipse([left_x-5, 55, left_x+3, 65], fill=(255, 220, 177, 255))
    
    # Right hand
    right_x = 64 + separation  
    draw.ellipse([right_x, 50, right_x+20, 78], fill=(255, 220, 177, 255))
    # Right thumb
    draw.ellipse([right_x-3, 55, right_x+5, 65], fill=(255, 220, 177, 255))
    
    # Impact lines when hands are close
    if separation < 15:
        impact_color = (255, 193, 7, 150)
        for i in range(3):
            angle = (i * 120 + frame_num * 30) * math.pi / 180
            x1 = 64 + 30 * math.cos(angle)
            y1 = 64 + 30 * math.sin(angle)
            x2 = 64 + 40 * math.cos(angle)
            y2 = 64 + 40 * math.sin(angle)
            draw.line([(x1, y1), (x2, y2)], fill=impact_color, width=3)
    
    return img

def create_typing_frame(frame_num, total_frames=6):
    """Create typing indicator animation"""
    size = 128
    img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # Chat bubble
    bubble_color = (229, 229, 229, 255)
    draw.rounded_rectangle([25, 40, 103, 80], radius=15, fill=bubble_color)
    # Bubble tail
    draw.polygon([(30, 75), (20, 90), (40, 75)], fill=bubble_color)
    
    # Three animated dots
    dot_color = (117, 117, 117, 255)
    for i in range(3):
        x = 45 + i * 20
        y = 60
        # Each dot bounces with phase offset
        phase = (frame_num + i * 2) % total_frames
        bounce = abs(math.sin(phase * math.pi / total_frames)) * 8
        current_y = y - bounce
        
        draw.ellipse([x-5, current_y-5, x+5, current_y+5], fill=dot_color)
    
    return img

def create_mind_blown_frame(frame_num, total_frames=10):
    """Create mind blown explosion animation"""
    size = 128
    img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # Head silhouette
    head_color = (97, 97, 97, 255)
    draw.ellipse([45, 50, 83, 88], fill=head_color)
    
    # Explosion from top of head
    if frame_num > 2:
        explosion_progress = (frame_num - 2) / (total_frames - 2)
        
        # Explosion particles
        colors = [(255, 87, 34), (255, 193, 7), (255, 152, 0), (244, 67, 54)]
        num_particles = 8
        
        for i in range(num_particles):
            angle = (i * 360 / num_particles) * math.pi / 180
            # Particles move outward
            distance = explosion_progress * 30
            x = 64 + distance * math.cos(angle)
            y = 45 + distance * math.sin(angle) * 0.7  # Elliptical explosion
            
            # Particle size decreases over time
            particle_size = max(1, 8 - explosion_progress * 6)
            color_idx = i % len(colors)
            opacity = int(255 * (1 - explosion_progress * 0.7))
            color = colors[color_idx] + (opacity,)
            
            draw.ellipse([x-particle_size, y-particle_size, 
                         x+particle_size, y+particle_size], fill=color)
        
        # Central burst
        if explosion_progress < 0.5:
            burst_size = int(20 * explosion_progress * 2)
            burst_opacity = int(255 * (1 - explosion_progress * 2))
            draw.ellipse([64-burst_size, 45-burst_size, 
                         64+burst_size, 45+burst_size], 
                        fill=(255, 255, 255, burst_opacity))
    
    # Eyes (wide with shock)
    if frame_num < 8:
        eye_color = (255, 255, 255, 255)
        pupil_color = (33, 33, 33, 255)
        # Left eye
        draw.ellipse([52, 62, 62, 72], fill=eye_color)
        draw.ellipse([55, 65, 59, 69], fill=pupil_color)
        # Right eye
        draw.ellipse([66, 62, 76, 72], fill=eye_color)
        draw.ellipse([69, 65, 73, 69], fill=pupil_color)
    
    return img

def create_thumbs_up_frame(frame_num, total_frames=8):
    """Create animated thumbs up"""
    size = 128
    img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # Thumb rotation animation
    rotation = math.sin(frame_num * 2 * math.pi / total_frames) * 10
    
    # Hand/fist
    hand_color = (255, 220, 177, 255)
    draw.rounded_rectangle([50, 55, 78, 85], radius=10, fill=hand_color)
    
    # Thumb
    thumb_y = 55 - 15 + rotation
    draw.ellipse([58, thumb_y, 70, thumb_y + 25], fill=hand_color)
    # Thumb tip
    draw.ellipse([60, thumb_y-5, 68, thumb_y+5], fill=hand_color)
    
    # Sparkles around thumb
    if frame_num % 2 == 0:
        sparkle_color = (255, 215, 0, 200)
        sparkle_positions = [(48, 40), (80, 40), (45, 50), (83, 50)]
        for x, y in sparkle_positions:
            # Rotate sparkles
            angle = frame_num * 45
            draw.polygon([
                (x, y-4), (x-2, y), (x, y+4), (x+2, y)
            ], fill=sparkle_color)
            draw.polygon([
                (x-3, y-3), (x, y), (x+3, y+3), (x, y)
            ], fill=sparkle_color)
    
    return img

def create_heart_beat_frame(frame_num, total_frames=10):
    """Create beating heart animation"""
    size = 128
    img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # Heart beat pattern (like ECG)
    beat_pattern = [1.0, 1.1, 1.0, 0.95, 1.2, 1.3, 1.2, 1.0, 0.95, 1.0]
    scale = beat_pattern[frame_num % len(beat_pattern)]
    
    # Calculate heart size based on beat
    base_size = 35
    current_size = int(base_size * scale)
    
    # Draw heart shape
    heart_color = (244, 67, 54, 255)
    cx, cy = 64, 60
    
    # Left curve of heart
    left_x = cx - current_size // 2
    left_y = cy - current_size // 4
    draw.ellipse([left_x - current_size//3, left_y,
                  left_x + current_size//3, left_y + current_size//2], 
                 fill=heart_color)
    
    # Right curve of heart
    right_x = cx + current_size // 2
    right_y = cy - current_size // 4
    draw.ellipse([right_x - current_size//3, right_y,
                  right_x + current_size//3, right_y + current_size//2], 
                 fill=heart_color)
    
    # Bottom point of heart
    draw.polygon([
        (cx - current_size//2, cy),
        (cx + current_size//2, cy),
        (cx, cy + current_size)
    ], fill=heart_color)
    
    # Pulse lines when beating hard
    if scale > 1.15:
        pulse_color = (255, 138, 128, 100)
        pulse_size = current_size + 10
        draw.ellipse([cx-pulse_size, cy-pulse_size//2, 
                     cx+pulse_size, cy+pulse_size], 
                    outline=pulse_color, width=2)
    
    return img

# Generate all GIF animations
if __name__ == "__main__":
    print("Creating reactions GIF emojis...")
    
    # 1. Clapping
    print("Creating clapping.gif...")
    frames = []
    for i in range(8):
        frame = create_clapping_frame(i, 8)
        frames.append(frame)
    frames[0].save(
        f"{output_dir}/clapping.gif",
        save_all=True,
        append_images=frames[1:],
        duration=100,
        loop=0
    )
    
    # 2. Typing
    print("Creating typing.gif...")
    frames = []
    for i in range(6):
        frame = create_typing_frame(i, 6)
        frames.append(frame)
    frames[0].save(
        f"{output_dir}/typing.gif",
        save_all=True,
        append_images=frames[1:],
        duration=200,
        loop=0
    )
    
    # 3. Mind blown
    print("Creating mind_blown.gif...")
    frames = []
    for i in range(10):
        frame = create_mind_blown_frame(i, 10)
        frames.append(frame)
    frames[0].save(
        f"{output_dir}/mind_blown.gif",
        save_all=True,
        append_images=frames[1:],
        duration=100,
        loop=0
    )
    
    # 4. Thumbs up
    print("Creating thumbs_up.gif...")
    frames = []
    for i in range(8):
        frame = create_thumbs_up_frame(i, 8)
        frames.append(frame)
    frames[0].save(
        f"{output_dir}/thumbs_up.gif",
        save_all=True,
        append_images=frames[1:],
        duration=150,
        loop=0
    )
    
    # 5. Heart beat
    print("Creating heart_beat.gif...")
    frames = []
    for i in range(10):
        frame = create_heart_beat_frame(i, 10)
        frames.append(frame)
    frames[0].save(
        f"{output_dir}/heart_beat.gif",
        save_all=True,
        append_images=frames[1:],
        duration=100,
        loop=0
    )
    
    print("\n✅ Created 5 GIF emojis for reactions pack!")
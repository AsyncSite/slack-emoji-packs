#!/usr/bin/env python3
"""
Create Korean culture emoji images for Slack emoji packs
"""

from PIL import Image, ImageDraw, ImageFont
import os

def create_annyeong_emoji():
    """Create annyeong (hello) emoji - waving hand"""
    size = 128
    img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # Hand color (skin tone)
    hand_color = (255, 220, 177)  # Peach
    
    # Palm
    draw.ellipse([40, 35, 85, 85], fill=hand_color)
    
    # Fingers
    # Thumb
    draw.ellipse([35, 55, 50, 75], fill=hand_color)
    
    # Index finger
    draw.rectangle([70, 30, 80, 50], fill=hand_color)
    draw.ellipse([70, 25, 80, 35], fill=hand_color)
    
    # Middle finger
    draw.rectangle([60, 28, 70, 48], fill=hand_color)
    draw.ellipse([60, 23, 70, 33], fill=hand_color)
    
    # Ring finger
    draw.rectangle([50, 30, 60, 50], fill=hand_color)
    draw.ellipse([50, 25, 60, 35], fill=hand_color)
    
    # Pinky
    draw.rectangle([40, 33, 50, 50], fill=hand_color)
    draw.ellipse([40, 28, 50, 38], fill=hand_color)
    
    # Wave lines (to show motion)
    wave_color = (100, 100, 100, 100)  # Semi-transparent gray
    draw.arc([85, 40, 100, 60], start=120, end=240, fill=wave_color, width=2)
    draw.arc([90, 45, 105, 65], start=120, end=240, fill=wave_color, width=2)
    
    return img

def create_fighting_emoji():
    """Create fighting/hwaiting emoji - fist pump"""
    size = 128
    img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # Arm/sleeve (blue - Korean flag colors)
    sleeve_color = (0, 56, 168)  # Korean blue
    draw.polygon([(50, 90), (75, 90), (70, 50), (55, 50)], fill=sleeve_color)
    
    # Fist (skin tone)
    fist_color = (255, 220, 177)  # Peach
    draw.ellipse([48, 35, 78, 65], fill=fist_color)
    
    # Knuckle lines
    knuckle_color = (230, 190, 150)
    draw.line([55, 45, 55, 55], fill=knuckle_color, width=2)
    draw.line([63, 45, 63, 55], fill=knuckle_color, width=2)
    draw.line([71, 45, 71, 55], fill=knuckle_color, width=2)
    
    # Energy lines (to show power)
    energy_color = (255, 0, 0)  # Red
    draw.line([45, 30, 40, 20], fill=energy_color, width=3)
    draw.line([63, 28, 63, 18], fill=energy_color, width=3)
    draw.line([80, 30, 85, 20], fill=energy_color, width=3)
    
    return img

def create_heart_finger_emoji():
    """Create heart finger emoji - Korean finger heart"""
    size = 128
    img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # Hand (skin tone)
    hand_color = (255, 220, 177)  # Peach
    
    # Palm base
    draw.ellipse([45, 50, 85, 90], fill=hand_color)
    
    # Thumb crossing over index finger to make heart
    # Index finger
    draw.polygon([(55, 50), (60, 30), (68, 30), (65, 50)], fill=hand_color)
    
    # Thumb
    draw.polygon([(65, 45), (75, 35), (80, 38), (70, 50)], fill=hand_color)
    
    # Heart shape where they meet (pink)
    heart_color = (255, 182, 193)  # Light pink
    draw.polygon([(63, 35), (58, 30), (55, 35), (63, 42), 
                  (71, 35), (68, 30), (63, 35)], fill=heart_color)
    
    # Other fingers
    draw.rectangle([50, 55, 58, 75], fill=hand_color)
    draw.rectangle([60, 55, 68, 78], fill=hand_color)
    draw.rectangle([70, 55, 78, 75], fill=hand_color)
    
    return img

def create_kimchi_emoji():
    """Create kimchi emoji - Korean fermented cabbage"""
    size = 128
    img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # Cabbage leaves (red from chili paste)
    kimchi_red = (220, 38, 38)  # Deep red
    
    # Multiple cabbage leaves layered
    # Leaf 1
    leaf1_points = [(40, 40), (45, 30), (55, 28), (65, 32), 
                     (70, 45), (65, 70), (50, 75), (40, 65)]
    draw.polygon(leaf1_points, fill=kimchi_red)
    
    # Leaf 2
    leaf2_points = [(55, 45), (60, 35), (70, 33), (80, 38), 
                     (85, 50), (80, 75), (65, 80), (55, 70)]
    draw.polygon(leaf2_points, fill=(200, 28, 28))  # Slightly darker
    
    # Leaf veins (darker red)
    vein_color = (150, 20, 20)
    draw.line([47, 35, 52, 65], fill=vein_color, width=2)
    draw.line([62, 40, 67, 70], fill=vein_color, width=2)
    draw.line([75, 40, 77, 70], fill=vein_color, width=2)
    
    # Sesame seeds on top
    sesame_color = (255, 248, 220)  # Light yellow
    draw.ellipse([50, 45, 53, 48], fill=sesame_color)
    draw.ellipse([65, 50, 68, 53], fill=sesame_color)
    draw.ellipse([58, 55, 61, 58], fill=sesame_color)
    draw.ellipse([70, 60, 73, 63], fill=sesame_color)
    
    return img

def create_soju_emoji():
    """Create soju emoji - Korean alcohol bottle"""
    size = 128
    img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # Bottle (green - classic soju color)
    bottle_color = (34, 197, 94)  # Green
    
    # Bottle neck
    draw.rectangle([58, 25, 70, 45], fill=bottle_color)
    
    # Bottle body
    draw.rounded_rectangle([50, 45, 78, 95], radius=5, fill=bottle_color)
    
    # Cap (silver/gray)
    cap_color = (192, 192, 192)
    draw.rectangle([56, 20, 72, 30], fill=cap_color)
    draw.ellipse([56, 18, 72, 25], fill=cap_color)
    
    # Label (white)
    label_color = (255, 255, 255)
    draw.rectangle([54, 55, 74, 75], fill=label_color)
    
    # Korean text simulation (green lines on label)
    text_color = bottle_color
    draw.rectangle([57, 60, 71, 62], fill=text_color)
    draw.rectangle([57, 65, 68, 67], fill=text_color)
    draw.rectangle([57, 70, 71, 72], fill=text_color)
    
    return img

def create_bibimbap_emoji():
    """Create bibimbap emoji - Korean mixed rice bowl"""
    size = 128
    img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # Bowl (dark gray/black)
    bowl_color = (64, 64, 64)
    draw.ellipse([25, 55, 103, 95], fill=bowl_color)
    draw.chord([25, 50, 103, 85], start=0, end=180, fill=bowl_color)
    
    # Rice (white)
    rice_color = (255, 255, 255)
    draw.ellipse([30, 52, 98, 80], fill=rice_color)
    
    # Toppings arranged in circle
    # Egg yolk in center (yellow)
    draw.ellipse([58, 58, 70, 70], fill=(255, 204, 0))
    
    # Vegetables around the egg
    # Spinach (green)
    draw.polygon([(45, 55), (50, 52), (55, 55), (50, 58)], fill=(34, 139, 34))
    
    # Carrot (orange)
    draw.polygon([(73, 55), (78, 52), (83, 55), (78, 58)], fill=(255, 140, 0))
    
    # Mushroom (brown)
    draw.polygon([(58, 50), (63, 47), (68, 50), (63, 53)], fill=(139, 69, 19))
    
    # Bean sprouts (light yellow)
    draw.polygon([(58, 75), (63, 72), (68, 75), (63, 78)], fill=(255, 248, 220))
    
    # Meat (brown)
    draw.polygon([(45, 65), (50, 62), (55, 65), (50, 68)], fill=(160, 82, 45))
    
    # Gochujang (red paste) dots
    draw.ellipse([48, 60, 52, 64], fill=(220, 38, 38))
    draw.ellipse([76, 60, 80, 64], fill=(220, 38, 38))
    
    return img

def create_daebak_emoji():
    """Create daebak emoji - awesome/jackpot with star"""
    size = 128
    img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # Large star (gold)
    star_color = (255, 215, 0)  # Gold
    
    # Star points (5-pointed star)
    star_points = [
        (64, 20),    # Top
        (74, 45),    # Top right inner
        (100, 45),   # Right
        (80, 62),    # Bottom right inner
        (88, 88),    # Bottom right
        (64, 72),    # Bottom center
        (40, 88),    # Bottom left
        (48, 62),    # Bottom left inner
        (28, 45),    # Left
        (54, 45),    # Top left inner
    ]
    draw.polygon(star_points, fill=star_color)
    
    # Inner star shadow (darker gold)
    inner_star = [
        (64, 35),
        (70, 48),
        (80, 48),
        (72, 58),
        (75, 70),
        (64, 62),
        (53, 70),
        (56, 58),
        (48, 48),
        (58, 48),
    ]
    draw.polygon(inner_star, fill=(255, 193, 37))
    
    # Sparkles around
    sparkle_color = (255, 255, 0)  # Bright yellow
    # Small stars
    draw.polygon([(95, 25), (97, 30), (102, 28), (97, 32), (99, 37),
                  (94, 33), (89, 37), (91, 32), (87, 28), (92, 30)], fill=sparkle_color)
    
    draw.polygon([(35, 25), (37, 30), (42, 28), (37, 32), (39, 37),
                  (34, 33), (29, 37), (31, 32), (27, 28), (32, 30)], fill=sparkle_color)
    
    return img

def create_jjang_emoji():
    """Create jjang emoji - thumbs up/best"""
    size = 128
    img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # Hand/fist (skin tone)
    hand_color = (255, 220, 177)  # Peach
    
    # Fist part
    draw.ellipse([45, 50, 85, 90], fill=hand_color)
    
    # Thumb up
    draw.rectangle([58, 30, 72, 55], fill=hand_color)
    draw.ellipse([58, 25, 72, 40], fill=hand_color)
    
    # Knuckle details
    knuckle_color = (230, 190, 150)
    draw.line([50, 65, 55, 65], fill=knuckle_color, width=2)
    draw.line([60, 65, 65, 65], fill=knuckle_color, width=2)
    draw.line([70, 65, 75, 65], fill=knuckle_color, width=2)
    
    # Shine effect (to show it's awesome)
    shine_color = (255, 255, 0, 150)  # Semi-transparent yellow
    draw.ellipse([75, 30, 85, 40], fill=shine_color)
    draw.ellipse([40, 35, 50, 45], fill=shine_color)
    
    return img

# Main execution
if __name__ == "__main__":
    output_dir = "images/korean-culture"
    
    # Create first batch of Korean emojis
    emojis = [
        ("annyeong", create_annyeong_emoji),
        ("fighting", create_fighting_emoji),
        ("heart-finger", create_heart_finger_emoji),
        ("kimchi", create_kimchi_emoji),
        ("soju", create_soju_emoji),
        ("bibimbap", create_bibimbap_emoji),
        ("daebak", create_daebak_emoji),
        ("jjang", create_jjang_emoji),
    ]
    
    for name, create_func in emojis:
        img = create_func()
        img.save(os.path.join(output_dir, f"{name}.png"))
        print(f"Created: {name}.png")
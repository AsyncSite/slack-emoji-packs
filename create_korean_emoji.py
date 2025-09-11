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

def create_aegyo_emoji():
    """Create aegyo emoji - cute expression with hearts"""
    size = 128
    img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # Face (yellow circle)
    face_color = (255, 223, 0)  # Yellow
    draw.ellipse([30, 30, 98, 98], fill=face_color)
    
    # Eyes (crescents for cute expression)
    eye_color = (0, 0, 0)
    # Left eye (crescent)
    draw.arc([40, 45, 55, 60], start=200, end=340, fill=eye_color, width=3)
    # Right eye (crescent)
    draw.arc([73, 45, 88, 60], start=200, end=340, fill=eye_color, width=3)
    
    # Blush (pink circles)
    blush_color = (255, 192, 203)
    draw.ellipse([32, 60, 42, 70], fill=blush_color)
    draw.ellipse([86, 60, 96, 70], fill=blush_color)
    
    # Cute mouth (small)
    draw.arc([55, 65, 73, 80], start=0, end=180, fill=eye_color, width=2)
    
    # Hearts around face
    heart_color = (255, 0, 127)  # Deep pink
    # Small heart top-left
    draw.polygon([(25, 25), (22, 22), (20, 25), (25, 30),
                  (30, 25), (28, 22), (25, 25)], fill=heart_color)
    # Small heart top-right
    draw.polygon([(103, 25), (100, 22), (98, 25), (103, 30),
                  (108, 25), (106, 22), (103, 25)], fill=heart_color)
    
    return img

def create_ppalli_emoji():
    """Create ppalli emoji - hurry/fast with speed lines"""
    size = 128
    img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # Running figure (simplified)
    body_color = (0, 123, 255)  # Blue
    
    # Body
    draw.ellipse([50, 45, 70, 75], fill=body_color)
    
    # Head
    head_color = (255, 220, 177)  # Skin
    draw.ellipse([55, 30, 70, 45], fill=head_color)
    
    # Legs in running position
    # Front leg
    draw.polygon([(60, 70), (65, 70), (70, 90), (65, 90)], fill=body_color)
    # Back leg
    draw.polygon([(55, 70), (60, 70), (50, 85), (45, 85)], fill=body_color)
    
    # Arms
    # Front arm
    draw.polygon([(65, 50), (70, 50), (80, 45), (80, 40)], fill=head_color)
    # Back arm
    draw.polygon([(55, 50), (50, 50), (40, 55), (40, 60)], fill=head_color)
    
    # Speed lines
    speed_color = (100, 100, 100)
    draw.line([25, 35, 45, 35], fill=speed_color, width=3)
    draw.line([20, 50, 40, 50], fill=speed_color, width=3)
    draw.line([25, 65, 45, 65], fill=speed_color, width=3)
    draw.line([30, 80, 50, 80], fill=speed_color, width=3)
    
    # Motion blur effect
    blur_color = (0, 123, 255, 100)  # Semi-transparent blue
    draw.ellipse([35, 45, 50, 70], fill=blur_color)
    
    return img

def create_kkkk_emoji():
    """Create kkkk emoji - Korean laughing (ㅋㅋㅋㅋ)"""
    size = 128
    img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # Korean character ㅋ repeated
    k_color = (0, 0, 0)  # Black
    
    # First ㅋ
    draw.rectangle([25, 40, 30, 70], fill=k_color)  # Vertical line
    draw.rectangle([30, 45, 40, 50], fill=k_color)  # Top horizontal
    draw.rectangle([30, 60, 40, 65], fill=k_color)  # Bottom horizontal
    
    # Second ㅋ
    draw.rectangle([45, 40, 50, 70], fill=k_color)  # Vertical line
    draw.rectangle([50, 45, 60, 50], fill=k_color)  # Top horizontal
    draw.rectangle([50, 60, 60, 65], fill=k_color)  # Bottom horizontal
    
    # Third ㅋ
    draw.rectangle([65, 40, 70, 70], fill=k_color)  # Vertical line
    draw.rectangle([70, 45, 80, 50], fill=k_color)  # Top horizontal
    draw.rectangle([70, 60, 80, 65], fill=k_color)  # Bottom horizontal
    
    # Fourth ㅋ
    draw.rectangle([85, 40, 90, 70], fill=k_color)  # Vertical line
    draw.rectangle([90, 45, 100, 50], fill=k_color)  # Top horizontal
    draw.rectangle([90, 60, 100, 65], fill=k_color)  # Bottom horizontal
    
    # Laugh tears (optional)
    tear_color = (135, 206, 235)  # Sky blue
    draw.ellipse([35, 75, 40, 85], fill=tear_color)
    draw.ellipse([88, 75, 93, 85], fill=tear_color)
    
    return img

def create_omo_emoji():
    """Create omo emoji - oh my! surprised face"""
    size = 128
    img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # Face (yellow)
    face_color = (255, 223, 0)
    draw.ellipse([30, 30, 98, 98], fill=face_color)
    
    # Wide eyes (surprised)
    eye_color = (0, 0, 0)
    # Left eye (big circle)
    draw.ellipse([40, 45, 55, 60], fill=eye_color)
    draw.ellipse([43, 48, 52, 57], fill=(255, 255, 255))  # Shine
    
    # Right eye (big circle)
    draw.ellipse([73, 45, 88, 60], fill=eye_color)
    draw.ellipse([76, 48, 85, 57], fill=(255, 255, 255))  # Shine
    
    # Mouth (O shape for "Oh!")
    draw.ellipse([54, 70, 74, 90], fill=eye_color)
    draw.ellipse([57, 73, 71, 87], fill=(255, 100, 100))  # Inner mouth
    
    # Surprise lines around head
    surprise_color = (255, 0, 0)
    draw.line([64, 20, 64, 10], fill=surprise_color, width=3)
    draw.line([40, 25, 30, 15], fill=surprise_color, width=3)
    draw.line([88, 25, 98, 15], fill=surprise_color, width=3)
    
    return img

def create_sarang_emoji():
    """Create sarang emoji - love with heart"""
    size = 128
    img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # Large heart
    heart_color = (255, 20, 147)  # Deep pink
    
    # Heart shape (two circles and triangle)
    # Left curve
    draw.ellipse([35, 35, 65, 65], fill=heart_color)
    # Right curve
    draw.ellipse([63, 35, 93, 65], fill=heart_color)
    # Bottom triangle
    draw.polygon([(35, 52), (93, 52), (64, 90)], fill=heart_color)
    
    # Inner shine (lighter pink)
    shine_color = (255, 182, 193)
    draw.ellipse([45, 45, 55, 55], fill=shine_color)
    
    # Small hearts floating around
    small_heart_color = (255, 105, 180)  # Hot pink
    # Top left small heart
    draw.polygon([(25, 30), (23, 28), (22, 30), (25, 33),
                  (28, 30), (27, 28), (25, 30)], fill=small_heart_color)
    # Bottom right small heart
    draw.polygon([(100, 80), (98, 78), (97, 80), (100, 83),
                  (103, 80), (102, 78), (100, 80)], fill=small_heart_color)
    
    return img

def create_hanbok_emoji():
    """Create hanbok emoji - traditional Korean dress"""
    size = 128
    img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # Jeogori (top part) - pink
    jeogori_color = (255, 192, 203)  # Pink
    draw.polygon([(40, 40), (88, 40), (85, 60), (43, 60)], fill=jeogori_color)
    
    # Collar (white)
    collar_color = (255, 255, 255)
    draw.polygon([(50, 40), (78, 40), (75, 45), (53, 45)], fill=collar_color)
    
    # Ribbon/bow (red)
    ribbon_color = (220, 20, 60)  # Crimson
    draw.ellipse([60, 45, 68, 53], fill=ribbon_color)
    # Ribbon tails
    draw.polygon([(60, 49), (55, 55), (57, 57), (62, 51)], fill=ribbon_color)
    draw.polygon([(68, 49), (73, 55), (71, 57), (66, 51)], fill=ribbon_color)
    
    # Chima (skirt) - traditional blue
    chima_color = (0, 56, 168)  # Korean blue
    draw.polygon([(43, 60), (85, 60), (95, 95), (33, 95)], fill=chima_color)
    
    # Skirt decoration lines
    deco_color = (255, 215, 0)  # Gold
    draw.line([40, 85, 88, 85], fill=deco_color, width=2)
    draw.line([38, 90, 90, 90], fill=deco_color, width=2)
    
    return img

def create_oppa_emoji():
    """Create oppa emoji - older brother/male with heart"""
    size = 128
    img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # Face (skin tone)
    face_color = (255, 220, 177)
    draw.ellipse([40, 35, 88, 85], fill=face_color)
    
    # Hair (black, K-pop style)
    hair_color = (0, 0, 0)
    draw.arc([38, 30, 90, 60], start=180, end=0, fill=hair_color, width=20)
    draw.polygon([(40, 45), (45, 35), (55, 33), (50, 45)], fill=hair_color)  # Bangs
    draw.polygon([(78, 45), (73, 33), (83, 35), (88, 45)], fill=hair_color)  # Bangs
    
    # Eyes (simple dots)
    draw.ellipse([50, 50, 56, 56], fill=hair_color)
    draw.ellipse([72, 50, 78, 56], fill=hair_color)
    
    # Cool smile
    draw.arc([55, 60, 73, 75], start=0, end=180, fill=hair_color, width=2)
    
    # Heart next to face (fan love)
    heart_color = (255, 20, 147)
    draw.polygon([(95, 50), (92, 47), (90, 50), (95, 55),
                  (100, 50), (98, 47), (95, 50)], fill=heart_color)
    
    return img

def create_heol_emoji():
    """Create heol emoji - shocked/what expression"""
    size = 128
    img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # Face (pale/shocked)
    face_color = (255, 245, 200)  # Pale yellow
    draw.ellipse([30, 30, 98, 98], fill=face_color)
    
    # Wide shocked eyes
    eye_color = (0, 0, 0)
    # Left eye (very wide)
    draw.ellipse([38, 45, 58, 65], fill=eye_color)
    draw.ellipse([41, 48, 55, 62], fill=(255, 255, 255))  # White
    draw.ellipse([45, 52, 51, 58], fill=eye_color)  # Pupil
    
    # Right eye (very wide)
    draw.ellipse([70, 45, 90, 65], fill=eye_color)
    draw.ellipse([73, 48, 87, 62], fill=(255, 255, 255))  # White
    draw.ellipse([77, 52, 83, 58], fill=eye_color)  # Pupil
    
    # Shocked mouth (wide open)
    draw.ellipse([52, 72, 76, 92], fill=eye_color)
    draw.ellipse([55, 75, 73, 89], fill=(100, 50, 50))  # Dark red inside
    
    # Sweat drops (showing nervousness)
    sweat_color = (173, 216, 230)  # Light blue
    draw.ellipse([25, 40, 33, 50], fill=sweat_color)
    draw.polygon([(29, 40), (27, 35), (31, 35)], fill=sweat_color)
    
    draw.ellipse([95, 40, 103, 50], fill=sweat_color)
    draw.polygon([(99, 40), (97, 35), (101, 35)], fill=sweat_color)
    
    return img

def create_noona_emoji():
    """Create noona emoji - older sister with feminine features"""
    size = 128
    img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # Face (skin tone)
    face_color = (255, 235, 205)  # Lighter skin tone
    draw.ellipse([40, 40, 88, 90], fill=face_color)
    
    # Hair (long, feminine style)
    hair_color = (101, 67, 33)  # Dark brown
    # Top hair
    draw.ellipse([35, 30, 93, 65], fill=hair_color)
    # Side hair (longer)
    draw.ellipse([33, 45, 48, 85], fill=hair_color)
    draw.ellipse([80, 45, 95, 85], fill=hair_color)
    
    # Bangs
    draw.arc([40, 35, 88, 55], start=180, end=0, fill=hair_color, width=8)
    
    # Eyes (feminine, with lashes)
    eye_color = (0, 0, 0)
    # Left eye
    draw.ellipse([48, 52, 56, 58], fill=eye_color)
    # Eyelash
    draw.line([48, 52, 46, 50], fill=eye_color, width=1)
    draw.line([52, 52, 52, 50], fill=eye_color, width=1)
    draw.line([56, 52, 58, 50], fill=eye_color, width=1)
    
    # Right eye
    draw.ellipse([72, 52, 80, 58], fill=eye_color)
    # Eyelash
    draw.line([72, 52, 70, 50], fill=eye_color, width=1)
    draw.line([76, 52, 76, 50], fill=eye_color, width=1)
    draw.line([80, 52, 82, 50], fill=eye_color, width=1)
    
    # Gentle smile
    draw.arc([56, 65, 72, 78], start=0, end=180, fill=(255, 105, 180), width=2)
    
    # Blush
    blush_color = (255, 192, 203, 100)  # Semi-transparent pink
    draw.ellipse([42, 62, 50, 68], fill=blush_color)
    draw.ellipse([78, 62, 86, 68], fill=blush_color)
    
    # Small heart (sisterly love)
    heart_color = (255, 182, 193)
    draw.polygon([(95, 55), (93, 53), (92, 55), (95, 58),
                  (98, 55), (97, 53), (95, 55)], fill=heart_color)
    
    return img

def create_kamsahamnida_emoji():
    """Create kamsahamnida emoji - deep bow of gratitude"""
    size = 128
    img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # Body (bowing position)
    body_color = (100, 149, 237)  # Cornflower blue
    # Torso bent forward
    draw.ellipse([45, 55, 85, 85], fill=body_color)
    
    # Head (bowed down)
    head_color = (255, 220, 177)  # Skin tone
    draw.ellipse([50, 35, 75, 60], fill=head_color)
    
    # Hair (top of head visible)
    hair_color = (0, 0, 0)
    draw.arc([48, 33, 77, 50], start=180, end=0, fill=hair_color, width=10)
    
    # Arms (folded in front)
    # Left arm
    draw.polygon([(50, 65), (45, 70), (48, 80), (53, 75)], fill=head_color)
    # Right arm
    draw.polygon([(75, 65), (80, 70), (77, 80), (72, 75)], fill=head_color)
    
    # Hands together (prayer position)
    draw.ellipse([58, 72, 67, 82], fill=head_color)
    
    # Motion lines (showing bowing motion)
    motion_color = (150, 150, 150, 100)  # Semi-transparent gray
    draw.arc([40, 25, 85, 45], start=20, end=160, fill=motion_color, width=2)
    draw.arc([35, 30, 90, 50], start=20, end=160, fill=motion_color, width=2)
    
    # Gratitude sparkles
    sparkle_color = (255, 215, 0)  # Gold
    draw.polygon([(30, 35), (32, 40), (34, 35), (32, 30)], fill=sparkle_color)
    draw.polygon([(94, 35), (96, 40), (98, 35), (96, 30)], fill=sparkle_color)
    
    return img

def create_mianhae_emoji():
    """Create mianhae emoji - sorry/apologetic expression"""
    size = 128
    img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # Face (slightly pale from guilt)
    face_color = (255, 248, 220)  # Light yellow
    draw.ellipse([30, 30, 98, 98], fill=face_color)
    
    # Sad downturned eyes
    eye_color = (0, 0, 0)
    # Left eye (downcast)
    draw.arc([42, 48, 56, 62], start=20, end=160, fill=eye_color, width=3)
    # Tear
    tear_color = (135, 206, 235)  # Sky blue
    draw.ellipse([48, 63, 53, 70], fill=tear_color)
    
    # Right eye (downcast)
    draw.arc([72, 48, 86, 62], start=20, end=160, fill=eye_color, width=3)
    # Tear
    draw.ellipse([78, 63, 83, 70], fill=tear_color)
    
    # Eyebrows (worried/sorry)
    brow_color = (100, 100, 100)
    draw.line([45, 43, 53, 40], fill=brow_color, width=2)  # Left brow up
    draw.line([75, 40, 83, 43], fill=brow_color, width=2)  # Right brow up
    
    # Sad mouth (downturned)
    draw.arc([52, 72, 76, 88], start=180, end=0, fill=eye_color, width=2)
    
    # Blush of embarrassment
    blush_color = (255, 182, 193, 120)  # Semi-transparent pink
    draw.ellipse([35, 65, 45, 73], fill=blush_color)
    draw.ellipse([83, 65, 93, 73], fill=blush_color)
    
    # Sorry gesture lines
    gesture_color = (200, 200, 200, 80)  # Light gray
    draw.line([25, 95, 35, 90], fill=gesture_color, width=2)
    draw.line([93, 90, 103, 95], fill=gesture_color, width=2)
    
    return img

def create_gwiyomi_emoji():
    """Create gwiyomi emoji - super cute with finger gesture"""
    size = 128
    img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # Face (extra cute style)
    face_color = (255, 239, 213)  # Papaya whip
    draw.ellipse([35, 35, 93, 93], fill=face_color)
    
    # Big sparkling eyes
    eye_color = (0, 0, 0)
    # Left eye
    draw.ellipse([45, 50, 58, 63], fill=eye_color)
    draw.ellipse([48, 53, 55, 60], fill=(139, 69, 19))  # Brown iris
    draw.ellipse([50, 54, 53, 57], fill=(0, 0, 0))  # Pupil
    draw.ellipse([51, 55, 52, 56], fill=(255, 255, 255))  # Shine
    
    # Right eye
    draw.ellipse([70, 50, 83, 63], fill=eye_color)
    draw.ellipse([73, 53, 80, 60], fill=(139, 69, 19))  # Brown iris
    draw.ellipse([75, 54, 78, 57], fill=(0, 0, 0))  # Pupil
    draw.ellipse([76, 55, 77, 56], fill=(255, 255, 255))  # Shine
    
    # Cute small mouth
    draw.arc([58, 68, 70, 78], start=0, end=180, fill=(255, 105, 180), width=2)
    
    # Finger pointing to cheek (gwiyomi gesture)
    finger_color = (255, 220, 177)
    draw.polygon([(30, 65), (35, 60), (38, 62), (33, 67)], fill=finger_color)
    draw.ellipse([35, 58, 40, 63], fill=finger_color)  # Fingertip
    
    # Blush
    blush_color = (255, 182, 193, 180)  # Semi-transparent pink
    draw.ellipse([38, 65, 48, 73], fill=blush_color)
    draw.ellipse([80, 65, 90, 73], fill=blush_color)
    
    # Stars for extra cuteness
    star_color = (255, 215, 0)
    draw.polygon([(25, 25), (26, 28), (29, 28), (27, 30), (28, 33),
                  (25, 31), (22, 33), (23, 30), (21, 28), (24, 28)], fill=star_color)
    
    return img

# Main execution
if __name__ == "__main__":
    output_dir = "images/korean-culture"
    
    # Create all Korean emojis
    emojis = [
        ("annyeong", create_annyeong_emoji),
        ("fighting", create_fighting_emoji),
        ("heart-finger", create_heart_finger_emoji),
        ("kimchi", create_kimchi_emoji),
        ("soju", create_soju_emoji),
        ("bibimbap", create_bibimbap_emoji),
        ("daebak", create_daebak_emoji),
        ("jjang", create_jjang_emoji),
        ("aegyo", create_aegyo_emoji),
        ("ppalli", create_ppalli_emoji),
        ("kkkk", create_kkkk_emoji),
        ("omo", create_omo_emoji),
        ("sarang", create_sarang_emoji),
        ("hanbok", create_hanbok_emoji),
        ("oppa", create_oppa_emoji),
        ("gwiyomi", create_gwiyomi_emoji),
        ("heol", create_heol_emoji),
        ("noona", create_noona_emoji),
        ("kamsahamnida", create_kamsahamnida_emoji),
        ("mianhae", create_mianhae_emoji),
    ]
    
    for name, create_func in emojis:
        img = create_func()
        img.save(os.path.join(output_dir, f"{name}.png"))
        print(f"Created: {name}.png")
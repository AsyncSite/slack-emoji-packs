#!/usr/bin/env python3
"""
Create reaction emoji images for Slack emoji packs
"""

from PIL import Image, ImageDraw, ImageFont
import os

def create_mindblown_emoji():
    """Create mindblown emoji - head exploding with amazement"""
    size = 128
    img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # Face (yellow)
    face_color = (255, 223, 0)
    draw.ellipse([30, 35, 98, 103], fill=face_color)
    
    # Wide eyes
    eye_color = (0, 0, 0)
    draw.ellipse([40, 55, 55, 70], fill=eye_color)
    draw.ellipse([43, 58, 52, 67], fill=(255, 255, 255))
    
    draw.ellipse([73, 55, 88, 70], fill=eye_color)
    draw.ellipse([76, 58, 85, 67], fill=(255, 255, 255))
    
    # Open mouth (shocked)
    draw.ellipse([54, 75, 74, 90], fill=eye_color)
    
    # Explosion effect around head
    explosion_color = (255, 165, 0)  # Orange
    # Top explosion
    draw.polygon([(64, 20), (60, 30), (68, 30)], fill=explosion_color)
    draw.polygon([(50, 25), (45, 35), (55, 33)], fill=explosion_color)
    draw.polygon([(78, 25), (73, 33), (83, 35)], fill=explosion_color)
    
    # Side explosions
    draw.polygon([(20, 60), (30, 55), (30, 65)], fill=(255, 0, 0))
    draw.polygon([(108, 60), (98, 55), (98, 65)], fill=(255, 0, 0))
    
    return img

def create_facepalm_emoji():
    """Create facepalm emoji - hand covering face in frustration"""
    size = 128
    img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # Face (yellow, partially visible)
    face_color = (255, 223, 0)
    draw.ellipse([30, 30, 98, 98], fill=face_color)
    
    # Hand covering face (skin tone)
    hand_color = (255, 220, 177)
    # Palm covering face
    draw.ellipse([35, 40, 85, 85], fill=hand_color)
    
    # Fingers
    draw.rectangle([40, 35, 48, 55], fill=hand_color)
    draw.rectangle([50, 32, 58, 52], fill=hand_color)
    draw.rectangle([60, 30, 68, 50], fill=hand_color)
    draw.rectangle([70, 32, 78, 52], fill=hand_color)
    
    # Finger tips
    draw.ellipse([40, 30, 48, 38], fill=hand_color)
    draw.ellipse([50, 27, 58, 35], fill=hand_color)
    draw.ellipse([60, 25, 68, 33], fill=hand_color)
    draw.ellipse([70, 27, 78, 35], fill=hand_color)
    
    # Visible mouth (frustrated)
    draw.arc([50, 85, 78, 95], start=180, end=0, fill=(0, 0, 0), width=2)
    
    return img

def create_party_parrot_emoji():
    """Create party parrot emoji - colorful dancing parrot"""
    size = 128
    img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # Body (green)
    body_color = (0, 255, 0)
    draw.ellipse([45, 50, 85, 95], fill=body_color)
    
    # Head (red)
    head_color = (255, 0, 0)
    draw.ellipse([50, 30, 80, 60], fill=head_color)
    
    # Beak (orange)
    beak_color = (255, 165, 0)
    draw.polygon([(45, 45), (40, 48), (45, 51)], fill=beak_color)
    
    # Eye
    draw.ellipse([55, 40, 63, 48], fill=(255, 255, 255))
    draw.ellipse([57, 42, 61, 46], fill=(0, 0, 0))
    
    # Wing (blue)
    wing_color = (0, 0, 255)
    draw.ellipse([70, 55, 95, 80], fill=wing_color)
    
    # Party hat
    hat_color = (255, 0, 255)  # Magenta
    draw.polygon([(65, 20), (55, 35), (75, 35)], fill=hat_color)
    draw.ellipse([63, 18, 67, 22], fill=(255, 255, 0))  # Pom pom
    
    return img

def create_this_is_fine_emoji():
    """Create this is fine emoji - dog in burning room"""
    size = 128
    img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # Dog face (brown)
    dog_color = (139, 69, 19)
    draw.ellipse([40, 45, 88, 93], fill=dog_color)
    
    # Dog ears
    draw.ellipse([35, 40, 50, 60], fill=dog_color)
    draw.ellipse([78, 40, 93, 60], fill=dog_color)
    
    # Eyes (forced smile)
    eye_color = (0, 0, 0)
    draw.arc([48, 55, 58, 65], start=0, end=180, fill=eye_color, width=2)
    draw.arc([70, 55, 80, 65], start=0, end=180, fill=eye_color, width=2)
    
    # Forced smile
    draw.arc([52, 70, 76, 85], start=0, end=180, fill=eye_color, width=2)
    
    # Fire around
    fire_color = (255, 69, 0)  # Red-orange
    # Left fire
    draw.polygon([(20, 90), (25, 70), (30, 85), (25, 95)], fill=fire_color)
    draw.polygon([(15, 85), (18, 65), (22, 80), (18, 90)], fill=(255, 140, 0))
    
    # Right fire
    draw.polygon([(98, 90), (103, 70), (108, 85), (103, 95)], fill=fire_color)
    draw.polygon([(93, 85), (96, 65), (100, 80), (96, 90)], fill=(255, 140, 0))
    
    # Top fire
    draw.polygon([(55, 25), (58, 15), (61, 23), (58, 30)], fill=fire_color)
    draw.polygon([(67, 25), (70, 15), (73, 23), (70, 30)], fill=(255, 140, 0))
    
    return img

def create_thumbsup_emoji():
    """Create thumbsup emoji"""
    size = 128
    img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # Hand/fist (skin tone)
    hand_color = (255, 220, 177)
    draw.ellipse([45, 50, 85, 90], fill=hand_color)
    
    # Thumb up
    draw.rectangle([58, 30, 72, 55], fill=hand_color)
    draw.ellipse([58, 25, 72, 40], fill=hand_color)
    
    # Knuckle lines
    knuckle_color = (230, 190, 150)
    draw.line([50, 65, 55, 65], fill=knuckle_color, width=2)
    draw.line([60, 65, 65, 65], fill=knuckle_color, width=2)
    draw.line([70, 65, 75, 65], fill=knuckle_color, width=2)
    
    return img

def create_thumbsdown_emoji():
    """Create thumbsdown emoji"""
    size = 128
    img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # Hand/fist (skin tone)
    hand_color = (255, 220, 177)
    draw.ellipse([45, 40, 85, 80], fill=hand_color)
    
    # Thumb down
    draw.rectangle([58, 75, 72, 100], fill=hand_color)
    draw.ellipse([58, 90, 72, 105], fill=hand_color)
    
    # Knuckle lines
    knuckle_color = (230, 190, 150)
    draw.line([50, 65, 55, 65], fill=knuckle_color, width=2)
    draw.line([60, 65, 65, 65], fill=knuckle_color, width=2)
    draw.line([70, 65, 75, 65], fill=knuckle_color, width=2)
    
    return img

def create_clapping_emoji():
    """Create clapping hands emoji"""
    size = 128
    img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # Left hand
    hand_color = (255, 220, 177)
    draw.ellipse([25, 45, 60, 85], fill=hand_color)
    # Fingers
    for i in range(4):
        y = 40 + i * 8
        draw.rectangle([20 + i*3, y, 28 + i*3, y+20], fill=hand_color)
        draw.ellipse([20 + i*3, y-5, 28 + i*3, y+5], fill=hand_color)
    
    # Right hand
    draw.ellipse([68, 45, 103, 85], fill=hand_color)
    # Fingers
    for i in range(4):
        y = 40 + i * 8
        draw.rectangle([100 - i*3, y, 108 - i*3, y+20], fill=hand_color)
        draw.ellipse([100 - i*3, y-5, 108 - i*3, y+5], fill=hand_color)
    
    # Clap effect lines
    effect_color = (255, 215, 0, 150)  # Semi-transparent gold
    draw.line([60, 50, 68, 50], fill=effect_color, width=3)
    draw.line([60, 65, 68, 65], fill=effect_color, width=3)
    draw.line([60, 80, 68, 80], fill=effect_color, width=3)
    
    return img

def create_eyes_emoji():
    """Create eyes emoji - looking eyes"""
    size = 128
    img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # Left eye
    # White
    draw.ellipse([25, 50, 55, 80], fill=(255, 255, 255))
    # Iris
    draw.ellipse([33, 55, 48, 70], fill=(135, 206, 235))  # Sky blue
    # Pupil
    draw.ellipse([37, 59, 44, 66], fill=(0, 0, 0))
    # Shine
    draw.ellipse([39, 60, 42, 63], fill=(255, 255, 255))
    
    # Right eye
    # White
    draw.ellipse([73, 50, 103, 80], fill=(255, 255, 255))
    # Iris
    draw.ellipse([80, 55, 95, 70], fill=(135, 206, 235))  # Sky blue
    # Pupil
    draw.ellipse([84, 59, 91, 66], fill=(0, 0, 0))
    # Shine
    draw.ellipse([86, 60, 89, 63], fill=(255, 255, 255))
    
    return img

def create_thinking_emoji():
    """Create thinking emoji - hand on chin"""
    size = 128
    img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # Face (yellow)
    face_color = (255, 223, 0)
    draw.ellipse([30, 25, 98, 93], fill=face_color)
    
    # Raised eyebrow
    brow_color = (100, 100, 100)
    draw.line([40, 38, 55, 35], fill=brow_color, width=3)
    draw.line([73, 40, 88, 40], fill=brow_color, width=3)
    
    # Eyes (one squinting)
    eye_color = (0, 0, 0)
    draw.line([43, 50, 52, 50], fill=eye_color, width=3)  # Squinting
    draw.ellipse([75, 48, 83, 56], fill=eye_color)  # Normal
    
    # Thinking mouth
    draw.line([55, 70, 75, 68], fill=eye_color, width=2)
    
    # Hand on chin (skin tone)
    hand_color = (255, 220, 177)
    draw.ellipse([70, 75, 95, 100], fill=hand_color)
    # Finger pointing up to chin
    draw.rectangle([75, 70, 83, 85], fill=hand_color)
    
    return img

def create_shrug_emoji():
    """Create shrug emoji - person shrugging"""
    size = 128
    img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # Head (skin tone)
    head_color = (255, 220, 177)
    draw.ellipse([54, 25, 74, 45], fill=head_color)
    
    # Body (blue shirt)
    body_color = (0, 123, 255)
    draw.rectangle([50, 45, 78, 75], fill=body_color)
    
    # Arms (raised in shrug)
    # Left arm
    draw.polygon([(50, 50), (30, 45), (25, 55), (45, 60)], fill=body_color)
    draw.ellipse([20, 45, 35, 60], fill=head_color)  # Hand
    
    # Right arm
    draw.polygon([(78, 50), (98, 45), (103, 55), (83, 60)], fill=body_color)
    draw.ellipse([93, 45, 108, 60], fill=head_color)  # Hand
    
    # Face
    eye_color = (0, 0, 0)
    draw.ellipse([58, 32, 62, 36], fill=eye_color)
    draw.ellipse([66, 32, 70, 36], fill=eye_color)
    
    # Confused mouth
    draw.line([60, 40, 68, 38], fill=eye_color, width=2)
    
    return img

# Continue with more emoji functions...

def create_sob_emoji():
    """Create sob emoji - crying heavily"""
    size = 128
    img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # Face (yellow)
    face_color = (255, 223, 0)
    draw.ellipse([30, 30, 98, 98], fill=face_color)
    
    # Crying eyes (closed)
    eye_color = (0, 0, 0)
    draw.arc([40, 45, 55, 60], start=200, end=340, fill=eye_color, width=3)
    draw.arc([73, 45, 88, 60], start=200, end=340, fill=eye_color, width=3)
    
    # Tears streaming
    tear_color = (135, 206, 235)
    # Left tears
    draw.ellipse([43, 62, 52, 75], fill=tear_color)
    draw.ellipse([45, 75, 50, 85], fill=tear_color)
    draw.ellipse([42, 85, 47, 95], fill=tear_color)
    
    # Right tears
    draw.ellipse([76, 62, 85, 75], fill=tear_color)
    draw.ellipse([78, 75, 83, 85], fill=tear_color)
    draw.ellipse([81, 85, 86, 95], fill=tear_color)
    
    # Sad mouth
    draw.arc([48, 72, 80, 88], start=180, end=0, fill=eye_color, width=3)
    
    return img

def create_joy_emoji():
    """Create joy emoji - laughing with tears"""
    size = 128
    img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # Face (yellow)
    face_color = (255, 223, 0)
    draw.ellipse([30, 30, 98, 98], fill=face_color)
    
    # Laughing eyes (crescents)
    eye_color = (0, 0, 0)
    draw.arc([40, 45, 55, 60], start=200, end=340, fill=eye_color, width=3)
    draw.arc([73, 45, 88, 60], start=200, end=340, fill=eye_color, width=3)
    
    # Tears of joy
    tear_color = (135, 206, 235)
    draw.ellipse([38, 58, 45, 68], fill=tear_color)
    draw.ellipse([83, 58, 90, 68], fill=tear_color)
    
    # Big smile
    draw.arc([40, 65, 88, 90], start=0, end=180, fill=eye_color, width=3)
    # Show teeth
    draw.rectangle([45, 75, 83, 80], fill=(255, 255, 255))
    
    return img

def create_heart_emoji():
    """Create heart emoji"""
    size = 128
    img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # Heart shape
    heart_color = (255, 0, 0)
    
    # Left curve
    draw.ellipse([35, 35, 65, 65], fill=heart_color)
    # Right curve
    draw.ellipse([63, 35, 93, 65], fill=heart_color)
    # Bottom triangle
    draw.polygon([(35, 52), (93, 52), (64, 90)], fill=heart_color)
    
    # Shine
    shine_color = (255, 150, 150)
    draw.ellipse([45, 45, 55, 55], fill=shine_color)
    
    return img

def create_fire_emoji():
    """Create fire emoji"""
    size = 128
    img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # Outer flame (red-orange)
    outer_color = (255, 69, 0)
    draw.polygon([(64, 20), (45, 50), (40, 80), (50, 95), 
                  (64, 85), (78, 95), (88, 80), (83, 50)], fill=outer_color)
    
    # Inner flame (yellow-orange)
    inner_color = (255, 165, 0)
    draw.polygon([(64, 35), (52, 55), (50, 75), (58, 85),
                  (64, 75), (70, 85), (78, 75), (76, 55)], fill=inner_color)
    
    # Core flame (yellow)
    core_color = (255, 255, 0)
    draw.polygon([(64, 50), (58, 65), (60, 75), (64, 70),
                  (68, 75), (70, 65)], fill=core_color)
    
    return img

def create_100_emoji():
    """Create 100 emoji"""
    size = 128
    img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # Red background
    bg_color = (220, 20, 60)
    draw.rounded_rectangle([20, 40, 108, 88], radius=10, fill=bg_color)
    
    # White text "100"
    text_color = (255, 255, 255)
    # Number 1
    draw.rectangle([30, 50, 40, 78], fill=text_color)
    # Number 0 (first)
    draw.ellipse([45, 50, 65, 78], fill=text_color)
    draw.ellipse([50, 55, 60, 73], fill=bg_color)
    # Number 0 (second)
    draw.ellipse([70, 50, 90, 78], fill=text_color)
    draw.ellipse([75, 55, 85, 73], fill=bg_color)
    
    # Underlines for emphasis
    draw.rectangle([30, 80, 90, 82], fill=text_color)
    draw.rectangle([35, 84, 85, 86], fill=text_color)
    
    return img

def create_wave_emoji():
    """Create wave emoji - waving hand"""
    size = 128
    img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # Hand (skin tone)
    hand_color = (255, 220, 177)
    
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
    
    # Wave lines
    wave_color = (100, 100, 100, 100)
    draw.arc([85, 40, 100, 60], start=120, end=240, fill=wave_color, width=2)
    draw.arc([90, 45, 105, 65], start=120, end=240, fill=wave_color, width=2)
    
    return img

def create_raised_hands_emoji():
    """Create raised hands emoji - both hands up in celebration"""
    size = 128
    img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    hand_color = (255, 220, 177)
    
    # Left hand raised
    # Palm
    draw.ellipse([25, 30, 55, 70], fill=hand_color)
    # Fingers
    for i in range(4):
        x = 28 + i * 7
        draw.rectangle([x, 20, x+6, 35], fill=hand_color)
        draw.ellipse([x, 15, x+6, 23], fill=hand_color)
    # Thumb
    draw.ellipse([50, 40, 60, 55], fill=hand_color)
    
    # Right hand raised
    # Palm
    draw.ellipse([73, 30, 103, 70], fill=hand_color)
    # Fingers
    for i in range(4):
        x = 76 + i * 7
        draw.rectangle([x, 20, x+6, 35], fill=hand_color)
        draw.ellipse([x, 15, x+6, 23], fill=hand_color)
    # Thumb
    draw.ellipse([68, 40, 78, 55], fill=hand_color)
    
    # Celebration sparkles
    sparkle_color = (255, 215, 0)
    draw.polygon([(40, 75), (42, 80), (44, 75), (42, 70)], fill=sparkle_color)
    draw.polygon([(88, 75), (90, 80), (92, 75), (90, 70)], fill=sparkle_color)
    
    return img

def create_pray_emoji():
    """Create pray emoji - praying hands"""
    size = 128
    img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    hand_color = (255, 220, 177)
    
    # Left hand
    draw.polygon([(45, 30), (50, 25), (55, 30), (55, 85), (45, 85)], fill=hand_color)
    # Left fingers
    for i in range(4):
        y = 30 + i * 3
        draw.ellipse([42, y, 48, y+15], fill=hand_color)
    
    # Right hand
    draw.polygon([(73, 30), (78, 25), (83, 30), (83, 85), (73, 85)], fill=hand_color)
    # Right fingers
    for i in range(4):
        y = 30 + i * 3
        draw.ellipse([80, y, 86, y+15], fill=hand_color)
    
    # Hands pressed together line
    draw.line([64, 30, 64, 85], fill=(230, 190, 150), width=2)
    
    # Prayer sparkle
    sparkle_color = (255, 255, 0, 150)
    draw.ellipse([59, 20, 69, 30], fill=sparkle_color)
    
    return img

def create_muscle_emoji():
    """Create muscle emoji - flexed bicep"""
    size = 128
    img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # Arm (skin tone)
    arm_color = (255, 220, 177)
    
    # Upper arm
    draw.ellipse([30, 45, 70, 85], fill=arm_color)
    
    # Forearm
    draw.polygon([(65, 65), (90, 50), (95, 60), (70, 75)], fill=arm_color)
    
    # Fist
    draw.ellipse([85, 45, 105, 65], fill=arm_color)
    
    # Muscle definition lines
    muscle_color = (230, 190, 150)
    draw.arc([35, 50, 65, 80], start=30, end=150, fill=muscle_color, width=3)
    draw.line([50, 55, 55, 65], fill=muscle_color, width=2)
    
    # Power effect
    power_color = (255, 0, 0, 100)
    draw.ellipse([25, 40, 35, 50], fill=power_color)
    draw.ellipse([70, 35, 80, 45], fill=power_color)
    
    return img

def create_sparkles_emoji():
    """Create sparkles emoji"""
    size = 128
    img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    sparkle_color = (255, 215, 0)  # Gold
    
    # Large center sparkle
    # Vertical line
    draw.rectangle([62, 45, 66, 85], fill=sparkle_color)
    # Horizontal line
    draw.rectangle([45, 62, 85, 66], fill=sparkle_color)
    # Diagonal lines
    draw.polygon([(54, 54), (58, 58), (70, 70), (74, 74),
                  (74, 70), (70, 74), (58, 62), (54, 58)], fill=sparkle_color)
    draw.polygon([(74, 54), (70, 58), (58, 70), (54, 74),
                  (54, 70), (58, 74), (70, 62), (74, 58)], fill=sparkle_color)
    
    # Small sparkles
    # Top left
    draw.polygon([(30, 30), (32, 35), (34, 30), (32, 25)], fill=sparkle_color)
    draw.polygon([(27, 32), (32, 32), (37, 32), (32, 32)], fill=sparkle_color)
    
    # Bottom right
    draw.polygon([(95, 95), (97, 100), (99, 95), (97, 90)], fill=sparkle_color)
    draw.polygon([(92, 97), (97, 97), (102, 97), (97, 97)], fill=sparkle_color)
    
    # Top right
    draw.polygon([(95, 35), (97, 40), (99, 35), (97, 30)], fill=sparkle_color)
    
    return img

def create_tada_emoji():
    """Create tada emoji - party popper"""
    size = 128
    img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # Popper cone (gold)
    cone_color = (255, 215, 0)
    draw.polygon([(50, 70), (30, 50), (35, 45), (55, 65)], fill=cone_color)
    
    # Popper opening
    opening_color = (255, 20, 147)  # Deep pink
    draw.ellipse([25, 42, 40, 57], fill=opening_color)
    
    # Confetti and streamers
    # Red streamer
    draw.polygon([(35, 45), (60, 30), (65, 35), (40, 50)], fill=(255, 0, 0))
    # Blue streamer
    draw.polygon([(35, 50), (70, 40), (73, 45), (38, 55)], fill=(0, 0, 255))
    # Green confetti
    draw.ellipse([75, 35, 85, 45], fill=(0, 255, 0))
    # Yellow confetti
    draw.ellipse([80, 50, 90, 60], fill=(255, 255, 0))
    # Purple confetti
    draw.ellipse([65, 55, 75, 65], fill=(128, 0, 128))
    
    return img

def create_confetti_emoji():
    """Create confetti emoji - confetti ball"""
    size = 128
    img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # Various confetti pieces scattered
    colors = [
        (255, 0, 0),      # Red
        (0, 0, 255),      # Blue
        (255, 255, 0),    # Yellow
        (0, 255, 0),      # Green
        (255, 0, 255),    # Magenta
        (255, 165, 0),    # Orange
        (128, 0, 128),    # Purple
    ]
    
    # Confetti pieces at various positions and rotations
    pieces = [
        (30, 30, 45, 40),
        (50, 25, 65, 35),
        (70, 35, 85, 45),
        (25, 50, 40, 60),
        (80, 55, 95, 65),
        (40, 70, 55, 80),
        (65, 75, 80, 85),
        (45, 45, 60, 55),
        (85, 80, 100, 90),
        (20, 80, 35, 90),
    ]
    
    for i, piece in enumerate(pieces):
        color = colors[i % len(colors)]
        if i % 2 == 0:
            draw.rectangle(piece, fill=color)
        else:
            draw.ellipse(piece, fill=color)
    
    return img

def create_trophy_emoji():
    """Create trophy emoji"""
    size = 128
    img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # Trophy cup (gold)
    gold_color = (255, 215, 0)
    
    # Cup body
    draw.ellipse([40, 35, 88, 75], fill=gold_color)
    draw.rectangle([40, 55, 88, 75], fill=gold_color)
    
    # Handles
    # Left handle
    draw.arc([25, 45, 50, 65], start=270, end=90, fill=gold_color, width=5)
    # Right handle
    draw.arc([78, 45, 103, 65], start=90, end=270, fill=gold_color, width=5)
    
    # Base
    base_color = (184, 134, 11)  # Dark gold
    draw.rectangle([50, 75, 78, 85], fill=base_color)
    draw.rectangle([45, 85, 83, 95], fill=base_color)
    
    # Number 1 on trophy
    draw.rectangle([60, 50, 68, 65], fill=(255, 255, 255))
    
    return img

def create_medal_emoji():
    """Create medal emoji"""
    size = 128
    img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # Ribbon
    ribbon_color = (220, 20, 60)  # Crimson
    draw.polygon([(54, 20), (54, 50), (64, 60), (74, 50), (74, 20)], fill=ribbon_color)
    
    # Medal (gold circle)
    medal_color = (255, 215, 0)
    draw.ellipse([44, 50, 84, 90], fill=medal_color)
    
    # Inner circle
    draw.ellipse([49, 55, 79, 85], fill=(255, 193, 37))
    
    # Star in center
    star_color = (255, 255, 255)
    star_points = [
        (64, 60),
        (67, 67),
        (74, 67),
        (68, 72),
        (70, 79),
        (64, 74),
        (58, 79),
        (60, 72),
        (54, 67),
        (61, 67),
    ]
    draw.polygon(star_points, fill=star_color)
    
    return img

def create_star_emoji():
    """Create star emoji"""
    size = 128
    img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # Yellow star
    star_color = (255, 215, 0)
    
    star_points = [
        (64, 20),
        (74, 45),
        (100, 45),
        (80, 62),
        (88, 88),
        (64, 72),
        (40, 88),
        (48, 62),
        (28, 45),
        (54, 45),
    ]
    draw.polygon(star_points, fill=star_color)
    
    # Inner shadow for depth
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
    
    return img

def create_zap_emoji():
    """Create zap/lightning emoji"""
    size = 128
    img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # Lightning bolt (yellow)
    lightning_color = (255, 215, 0)
    
    lightning_points = [
        (70, 20),
        (45, 55),
        (58, 55),
        (48, 95),
        (78, 50),
        (65, 50),
        (85, 20),
    ]
    draw.polygon(lightning_points, fill=lightning_color)
    
    # Inner highlight
    highlight_points = [
        (72, 30),
        (55, 53),
        (63, 53),
        (58, 75),
        (73, 52),
        (67, 52),
        (78, 30),
    ]
    draw.polygon(highlight_points, fill=(255, 255, 0))
    
    return img

def create_boom_emoji():
    """Create boom/explosion emoji"""
    size = 128
    img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # Explosion shape (red-orange gradient effect)
    # Outer explosion
    outer_color = (255, 69, 0)
    explosion_points = [
        (64, 20), (75, 30), (90, 25), (85, 40),
        (100, 45), (90, 55), (95, 70), (80, 65),
        (75, 85), (64, 75), (53, 85), (48, 65),
        (33, 70), (38, 55), (28, 45), (43, 40),
        (38, 25), (53, 30)
    ]
    draw.polygon(explosion_points, fill=outer_color)
    
    # Inner explosion
    inner_color = (255, 165, 0)
    inner_points = [
        (64, 35), (70, 40), (75, 38), (73, 45),
        (78, 48), (73, 52), (75, 58), (68, 55),
        (65, 62), (60, 55), (55, 58), (57, 52),
        (52, 48), (57, 45), (55, 38), (60, 40)
    ]
    draw.polygon(inner_points, fill=inner_color)
    
    # Core (yellow)
    draw.ellipse([58, 45, 70, 57], fill=(255, 255, 0))
    
    return img

def create_sweat_emoji():
    """Create nervous sweat emoji"""
    size = 128
    img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # Face (yellow)
    face_color = (255, 223, 0)
    draw.ellipse([30, 30, 98, 98], fill=face_color)
    
    # Nervous eyes
    eye_color = (0, 0, 0)
    draw.ellipse([45, 50, 55, 60], fill=eye_color)
    draw.ellipse([73, 50, 83, 60], fill=eye_color)
    
    # Nervous smile
    draw.arc([45, 65, 83, 85], start=0, end=180, fill=eye_color, width=2)
    
    # Sweat drop
    sweat_color = (135, 206, 235)
    draw.ellipse([85, 35, 95, 50], fill=sweat_color)
    draw.polygon([(90, 35), (88, 30), (92, 30)], fill=sweat_color)
    
    return img

def create_cold_sweat_emoji():
    """Create cold sweat/worried emoji"""
    size = 128
    img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # Face (pale blue-ish)
    face_color = (200, 220, 255)
    draw.ellipse([30, 30, 98, 98], fill=face_color)
    
    # Worried eyes
    eye_color = (0, 0, 0)
    # Worried eyebrows
    draw.line([45, 45, 55, 42], fill=eye_color, width=2)
    draw.line([73, 42, 83, 45], fill=eye_color, width=2)
    
    draw.ellipse([45, 50, 55, 60], fill=eye_color)
    draw.ellipse([73, 50, 83, 60], fill=eye_color)
    
    # Worried mouth
    draw.arc([50, 75, 78, 85], start=180, end=0, fill=eye_color, width=2)
    
    # Multiple sweat drops
    sweat_color = (135, 206, 235)
    # Left sweat
    draw.ellipse([25, 40, 33, 50], fill=sweat_color)
    draw.polygon([(29, 40), (27, 35), (31, 35)], fill=sweat_color)
    # Right sweat
    draw.ellipse([95, 40, 103, 50], fill=sweat_color)
    draw.polygon([(99, 40), (97, 35), (101, 35)], fill=sweat_color)
    # Forehead sweat
    draw.ellipse([60, 25, 68, 35], fill=sweat_color)
    
    return img

def create_sleepy_emoji():
    """Create sleepy emoji with Zzz"""
    size = 128
    img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # Face (yellow)
    face_color = (255, 223, 0)
    draw.ellipse([30, 40, 98, 108], fill=face_color)
    
    # Closed eyes (lines)
    eye_color = (0, 0, 0)
    draw.line([45, 65, 55, 65], fill=eye_color, width=3)
    draw.line([73, 65, 83, 65], fill=eye_color, width=3)
    
    # Sleepy mouth (small)
    draw.ellipse([60, 85, 68, 92], fill=eye_color)
    
    # Zzz above head
    z_color = (0, 0, 255)
    # Large Z
    draw.line([70, 20, 85, 20], fill=z_color, width=3)
    draw.line([85, 20, 70, 35], fill=z_color, width=3)
    draw.line([70, 35, 85, 35], fill=z_color, width=3)
    
    # Medium Z
    draw.line([88, 25, 98, 25], fill=z_color, width=2)
    draw.line([98, 25, 88, 35], fill=z_color, width=2)
    draw.line([88, 35, 98, 35], fill=z_color, width=2)
    
    # Small z
    draw.line([100, 30, 106, 30], fill=z_color, width=1)
    draw.line([106, 30, 100, 36], fill=z_color, width=1)
    draw.line([100, 36, 106, 36], fill=z_color, width=1)
    
    return img

# Main execution
if __name__ == "__main__":
    output_dir = "images/reactions"
    os.makedirs(output_dir, exist_ok=True)
    
    # Create all reaction emojis
    emojis = [
        ("mindblown", create_mindblown_emoji),
        ("facepalm", create_facepalm_emoji),
        ("party-parrot", create_party_parrot_emoji),
        ("this-is-fine", create_this_is_fine_emoji),
        ("thumbsup", create_thumbsup_emoji),
        ("thumbsdown", create_thumbsdown_emoji),
        ("clapping", create_clapping_emoji),
        ("eyes", create_eyes_emoji),
        ("thinking", create_thinking_emoji),
        ("shrug", create_shrug_emoji),
        ("sob", create_sob_emoji),
        ("joy", create_joy_emoji),
        ("heart", create_heart_emoji),
        ("fire", create_fire_emoji),
        ("100", create_100_emoji),
        ("wave", create_wave_emoji),
        ("raised-hands", create_raised_hands_emoji),
        ("pray", create_pray_emoji),
        ("muscle", create_muscle_emoji),
        ("sparkles", create_sparkles_emoji),
        ("tada", create_tada_emoji),
        ("confetti", create_confetti_emoji),
        ("trophy", create_trophy_emoji),
        ("medal", create_medal_emoji),
        ("star", create_star_emoji),
        ("zap", create_zap_emoji),
        ("boom", create_boom_emoji),
        ("sweat", create_sweat_emoji),
        ("cold-sweat", create_cold_sweat_emoji),
        ("sleepy", create_sleepy_emoji),
    ]
    
    for name, create_func in emojis:
        img = create_func()
        img.save(os.path.join(output_dir, f"{name}.png"))
        print(f"Created: {name}.png")
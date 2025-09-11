#!/usr/bin/env python3
"""
Create korean-office emoji pack
Emojis for Korean office culture: 야근, 회식, 칼퇴, etc.
"""

from PIL import Image, ImageDraw
import os
import math

# Create output directory
output_dir = "images/korean-office"
os.makedirs(output_dir, exist_ok=True)

def create_yagun():
    """야근 (Night work) - moon with computer"""
    size = 128
    img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # Night sky (dark background circle)
    night_color = (25, 25, 112, 100)
    draw.ellipse([10, 10, 118, 118], fill=night_color)
    
    # Moon
    moon_color = (255, 243, 224)
    draw.ellipse([20, 20, 50, 50], fill=moon_color)
    
    # Moon craters
    crater_color = (230, 230, 200)
    draw.ellipse([25, 25, 30, 30], fill=crater_color)
    draw.ellipse([35, 35, 42, 42], fill=crater_color)
    
    # Stars
    star_color = (255, 255, 255)
    stars = [(60, 25), (80, 30), (70, 45), (90, 20), (55, 40)]
    for x, y in stars:
        draw.polygon([
            (x, y-2), (x-1, y), (x, y+2), (x+1, y)
        ], fill=star_color)
    
    # Computer
    computer_color = (66, 66, 66)
    draw.rectangle([45, 65, 95, 95], fill=computer_color)
    
    # Glowing screen (person still working)
    screen_color = (135, 206, 250)
    draw.rectangle([50, 70, 90, 90], fill=screen_color)
    
    # Code lines on screen
    code_color = (0, 100, 0)
    for i in range(4):
        y = 73 + i * 4
        draw.line([(52, y), (88, y)], fill=code_color, width=1)
    
    # Coffee cup (essential for 야근)
    cup_color = (139, 69, 19)
    draw.ellipse([98, 85, 108, 95], fill=cup_color)
    
    # Steam from coffee
    for i in range(3):
        x = 101 + i * 2
        y = 82 - i * 3
        draw.ellipse([x-1, y-1, x+1, y+1], fill=(200, 200, 200, 100))
    
    return img

def create_hoesik():
    """회식 (Company dinner) - soju glasses clinking"""
    size = 128
    img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # Soju bottle
    bottle_color = (46, 125, 50)
    draw.rectangle([20, 40, 40, 90], fill=bottle_color)
    draw.ellipse([20, 35, 40, 45], fill=bottle_color)
    draw.rectangle([25, 30, 35, 40], fill=(158, 158, 158))  # Cap
    
    # Label on bottle
    label_color = (255, 255, 255)
    draw.rectangle([23, 55, 37, 75], fill=label_color)
    draw.text((26, 60), "소주", fill=(0, 100, 0), font=None)
    
    # Two soju glasses clinking
    glass_color = (255, 255, 255, 200)
    
    # Glass 1 (tilted left)
    glass1_points = [(50, 70), (45, 50), (55, 50), (60, 70)]
    draw.polygon(glass1_points, fill=glass_color, outline=(200, 200, 200))
    
    # Glass 2 (tilted right)
    glass2_points = [(68, 70), (73, 50), (83, 50), (78, 70)]
    draw.polygon(glass2_points, fill=glass_color, outline=(200, 200, 200))
    
    # Soju in glasses (green tint)
    soju_color = (200, 255, 200, 180)
    draw.polygon([(48, 65), (46, 55), (54, 55), (58, 65)], fill=soju_color)
    draw.polygon([(70, 65), (74, 55), (82, 55), (76, 65)], fill=soju_color)
    
    # Cheers effect lines
    cheer_color = (255, 215, 0)
    for angle in range(0, 360, 45):
        x = 64 + 20 * math.cos(math.radians(angle))
        y = 50 + 20 * math.sin(math.radians(angle))
        draw.line([(64, 50), (x, y)], fill=cheer_color, width=2)
    
    # Korean BBQ meat (삼겹살)
    meat_color = (205, 92, 92)
    draw.rectangle([85, 75, 110, 85], fill=meat_color)
    
    # Grill marks
    grill_color = (139, 69, 19)
    for i in range(3):
        x = 88 + i * 7
        draw.line([(x, 75), (x, 85)], fill=grill_color, width=1)
    
    return img

def create_kaltwae():
    """칼퇴 (Sharp leave) - knife cutting clock at 6"""
    size = 128
    img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # Clock face
    clock_color = (255, 255, 255)
    draw.ellipse([30, 30, 98, 98], fill=clock_color)
    draw.ellipse([30, 30, 98, 98], outline=(0, 0, 0), width=3)
    
    # Clock numbers (12, 3, 6, 9)
    number_color = (0, 0, 0)
    draw.text((60, 35), "12", fill=number_color, font=None)
    draw.text((88, 60), "3", fill=number_color, font=None)
    draw.text((62, 85), "6", fill=number_color, font=None)
    draw.text((35, 60), "9", fill=number_color, font=None)
    
    # Clock hands pointing to 6:00 (칼퇴 time!)
    center = (64, 64)
    # Hour hand (pointing to 6)
    draw.line([center, (64, 80)], fill=(0, 0, 0), width=4)
    # Minute hand (pointing to 12)
    draw.line([center, (64, 40)], fill=(0, 0, 0), width=3)
    
    # Knife cutting through clock
    knife_color = (192, 192, 192)
    blade_color = (220, 220, 220)
    
    # Knife blade
    draw.polygon([
        (85, 20), (95, 25),  # Tip
        (70, 85), (60, 80)   # Base
    ], fill=blade_color)
    
    # Knife edge (darker)
    draw.line([(85, 20), (60, 80)], fill=knife_color, width=2)
    
    # Knife handle
    handle_color = (139, 69, 19)
    draw.polygon([
        (60, 80), (70, 85),
        (55, 105), (45, 100)
    ], fill=handle_color)
    
    # Speed lines (showing swift exit)
    speed_color = (255, 215, 0)
    for i in range(3):
        y = 90 + i * 5
        draw.line([(100, y), (115, y)], fill=speed_color, width=2)
    
    return img

def create_salary_day():
    """월급날 (Salary day) - money with calendar"""
    size = 128
    img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # Calendar
    cal_color = (255, 255, 255)
    draw.rectangle([20, 20, 60, 60], fill=cal_color)
    draw.rectangle([20, 20, 60, 30], fill=(244, 67, 54))  # Header
    
    # Calendar number (25 - typical salary day)
    draw.text((32, 35), "25", fill=(0, 0, 0), font=None)
    
    # Circle around 25
    draw.ellipse([28, 33, 48, 53], outline=(76, 175, 80), width=3)
    
    # Money bills floating
    bill_color = (76, 175, 80)
    bills = [
        (70, 30, 95, 40),
        (75, 45, 100, 55),
        (68, 60, 93, 70),
        (73, 75, 98, 85)
    ]
    
    for x1, y1, x2, y2 in bills:
        draw.rectangle([x1, y1, x2, y2], fill=bill_color)
        # Won symbol
        draw.text((x1+5, y1+1), "₩", fill=(255, 255, 255), font=None)
    
    # Coins
    coin_color = (255, 215, 0)
    coins = [(55, 70), (65, 80), (50, 85)]
    for x, y in coins:
        draw.ellipse([x-5, y-5, x+5, y+5], fill=coin_color)
        draw.text((x-3, y-4), "₩", fill=(139, 69, 19), font=None)
    
    # Happy sparkles
    sparkle_color = (255, 235, 59)
    sparkles = [(85, 20), (105, 40), (90, 90), (30, 70)]
    for x, y in sparkles:
        draw.polygon([
            (x, y-3), (x-2, y), (x, y+3), (x+2, y)
        ], fill=sparkle_color)
    
    return img

def create_sangsa():
    """상사 (Boss) - suit with authoritative aura"""
    size = 128
    img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # Head
    head_color = (255, 224, 178)
    draw.ellipse([48, 20, 80, 52], fill=head_color)
    
    # Hair (typical Korean boss style)
    hair_color = (33, 33, 33)
    draw.ellipse([48, 20, 80, 35], fill=hair_color)
    
    # Stern face
    # Eyes (serious look)
    draw.line([(55, 32), (60, 32)], fill=(0, 0, 0), width=2)
    draw.line([(68, 32), (73, 32)], fill=(0, 0, 0), width=2)
    
    # Frown
    draw.arc([58, 38, 70, 45], start=20, end=160, fill=(0, 0, 0), width=2)
    
    # Suit
    suit_color = (33, 33, 33)
    draw.polygon([
        (45, 52), (83, 52),  # Shoulders
        (85, 95), (43, 95)   # Bottom
    ], fill=suit_color)
    
    # Tie
    tie_color = (139, 0, 0)
    draw.polygon([
        (64, 52), (60, 52),
        (62, 85), (64, 90),
        (66, 85), (68, 52)
    ], fill=tie_color)
    
    # White shirt collar
    collar_color = (255, 255, 255)
    draw.polygon([
        (55, 52), (64, 60), (73, 52)
    ], fill=collar_color)
    
    # Authority aura (red lines)
    aura_color = (255, 0, 0, 100)
    for angle in [30, 45, 60, 120, 135, 150]:
        x = 64 + 35 * math.cos(math.radians(angle))
        y = 50 + 35 * math.sin(math.radians(angle))
        draw.line([(64, 50), (x, y)], fill=aura_color, width=3)
    
    # Name tag
    tag_color = (255, 255, 255)
    draw.rectangle([50, 65, 70, 72], fill=tag_color)
    draw.text((53, 66), "부장", fill=(0, 0, 0), font=None)
    
    return img

def create_maknae():
    """막내 (Youngest) - baby chick with work"""
    size = 128
    img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # Baby chick body
    chick_color = (255, 235, 59)
    draw.ellipse([40, 45, 88, 85], fill=chick_color)
    
    # Chick head
    draw.ellipse([48, 25, 80, 57], fill=chick_color)
    
    # Cute eyes
    eye_color = (0, 0, 0)
    draw.ellipse([55, 35, 61, 41], fill=eye_color)
    draw.ellipse([67, 35, 73, 41], fill=eye_color)
    
    # Eye sparkles (innocent look)
    draw.ellipse([57, 36, 59, 38], fill=(255, 255, 255))
    draw.ellipse([69, 36, 71, 38], fill=(255, 255, 255))
    
    # Beak
    beak_color = (255, 152, 0)
    draw.polygon([(64, 42), (61, 45), (67, 45)], fill=beak_color)
    
    # Wings (small)
    draw.ellipse([35, 55, 45, 70], fill=chick_color)
    draw.ellipse([83, 55, 93, 70], fill=chick_color)
    
    # Stack of papers (lots of work)
    paper_color = (255, 255, 255)
    for i in range(5):
        y = 85 - i * 3
        draw.rectangle([90, y, 110, y+15], fill=paper_color, outline=(200, 200, 200))
    
    # Coffee errands (multiple cups)
    coffee_color = (139, 69, 19)
    cups_x = [15, 25, 20]
    for i, x in enumerate(cups_x):
        y = 70 + i * 8
        draw.ellipse([x, y, x+8, y+8], fill=coffee_color)
    
    # Sweat drops (stressed)
    sweat_color = (135, 206, 250)
    draw.ellipse([82, 30, 86, 36], fill=sweat_color)
    draw.ellipse([45, 28, 49, 34], fill=sweat_color)
    
    return img

def create_annual_leave():
    """연차 (Annual leave) - airplane with calendar"""
    size = 128
    img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # Calendar with X marks
    cal_color = (255, 255, 255)
    draw.rectangle([15, 20, 55, 60], fill=cal_color)
    draw.rectangle([15, 20, 55, 30], fill=(33, 150, 243))  # Header
    
    # X marks on calendar (taking days off)
    x_color = (244, 67, 54)
    dates = [(25, 35), (35, 35), (45, 35), (25, 45), (35, 45)]
    for x, y in dates:
        draw.line([(x-3, y-3), (x+3, y+3)], fill=x_color, width=2)
        draw.line([(x-3, y+3), (x+3, y-3)], fill=x_color, width=2)
    
    # Airplane
    plane_color = (33, 150, 243)
    # Fuselage
    draw.ellipse([60, 55, 110, 70], fill=plane_color)
    
    # Wings
    draw.polygon([
        (80, 62), (70, 45), (75, 45), (85, 62)
    ], fill=plane_color)
    draw.polygon([
        (80, 63), (70, 80), (75, 80), (85, 63)
    ], fill=plane_color)
    
    # Tail
    draw.polygon([
        (105, 62), (115, 55), (115, 60), (107, 63)
    ], fill=plane_color)
    
    # Windows
    window_color = (135, 206, 250)
    for i in range(4):
        x = 68 + i * 8
        draw.ellipse([x, 60, x+4, 64], fill=window_color)
    
    # Flight path (dotted line)
    path_color = (76, 175, 80)
    for i in range(6):
        x = 20 + i * 15
        y = 80 - i * 5
        draw.ellipse([x-2, y-2, x+2, y+2], fill=path_color)
    
    # Sun (vacation destination)
    sun_color = (255, 235, 59)
    draw.ellipse([95, 25, 115, 45], fill=sun_color)
    
    # Sun rays
    for angle in range(0, 360, 45):
        x = 105 + 15 * math.cos(math.radians(angle))
        y = 35 + 15 * math.sin(math.radians(angle))
        draw.line([(105, 35), (x, y)], fill=sun_color, width=2)
    
    return img

def create_team_building():
    """팀빌딩 (Team building) - hands together"""
    size = 128
    img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # Multiple hands coming together in circle
    hand_colors = [
        (255, 224, 178),  # Light skin
        (241, 194, 125),  # Medium skin
        (255, 224, 178),  # Light skin
        (224, 172, 105),  # Tan skin
    ]
    
    # Center point where hands meet
    center = (64, 64)
    
    # Draw hands from different angles
    angles = [0, 90, 180, 270]
    for i, (angle, color) in enumerate(zip(angles, hand_colors)):
        # Calculate hand position
        rad = math.radians(angle)
        
        # Hand base position
        x_base = center[0] + 30 * math.cos(rad)
        y_base = center[1] + 30 * math.sin(rad)
        
        # Arm
        x_arm = center[0] + 50 * math.cos(rad)
        y_arm = center[1] + 50 * math.sin(rad)
        
        # Draw arm
        draw.line([(x_arm, y_arm), (x_base, y_base)], fill=color, width=15)
        
        # Draw hand (circle)
        draw.ellipse([x_base-10, y_base-10, x_base+10, y_base+10], fill=color)
    
    # Center circle (unity)
    unity_color = (255, 215, 0)
    draw.ellipse([54, 54, 74, 74], fill=unity_color)
    
    # Text in center
    draw.text((56, 58), "TEAM", fill=(255, 255, 255), font=None)
    
    # Sparkles around
    sparkle_color = (255, 235, 59)
    sparkles = [(30, 30), (98, 30), (30, 98), (98, 98)]
    for x, y in sparkles:
        draw.polygon([
            (x, y-4), (x-2, y), (x, y+4), (x+2, y)
        ], fill=sparkle_color)
    
    return img

# Generate all emojis
if __name__ == "__main__":
    emojis = [
        ("yagun", create_yagun),
        ("hoesik", create_hoesik),
        ("kaltwae", create_kaltwae),
        ("salary_day", create_salary_day),
        ("sangsa", create_sangsa),
        ("maknae", create_maknae),
        ("annual_leave", create_annual_leave),
        ("team_building", create_team_building)
    ]
    
    for name, create_func in emojis:
        img = create_func()
        img.save(f"{output_dir}/{name}.png")
        print(f"Created {name}.png")
    
    print(f"\nAll korean-office emojis created in {output_dir}/")
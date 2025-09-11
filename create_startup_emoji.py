#!/usr/bin/env python3
"""
Create startup-hustle emoji pack
Emojis for startup life: burn rate, pivot, runway, unicorn, etc.
"""

from PIL import Image, ImageDraw, ImageFont
import os
import math

# Create output directory
output_dir = "images/startup-hustle"
os.makedirs(output_dir, exist_ok=True)

def create_burn_rate():
    """Money on fire - burning cash"""
    size = 128
    img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # Dollar bill (green)
    bill_color = (46, 125, 50)
    draw.rectangle([30, 60, 98, 90], fill=bill_color)
    
    # $ symbol on bill
    draw.text((60, 68), "$", fill=(255, 255, 255), font=None)
    
    # Fire flames (orange to red gradient)
    flame_orange = (255, 152, 0)
    flame_red = (244, 67, 54)
    
    # Multiple flame shapes
    flames = [
        [(64, 50), (50, 35), (45, 20), (54, 25), (58, 35)],  # Left flame
        [(64, 50), (78, 35), (83, 20), (74, 25), (70, 35)],  # Right flame
        [(64, 45), (60, 30), (64, 15), (68, 30)]  # Center flame
    ]
    
    for flame in flames:
        draw.polygon(flame, fill=flame_orange)
    
    # Inner flames (lighter)
    inner_flame = (255, 235, 59)
    draw.polygon([(64, 45), (61, 35), (64, 25), (67, 35)], fill=inner_flame)
    
    return img

def create_pivot():
    """Pivot arrow - changing direction"""
    size = 128
    img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # Main arrow color
    arrow_color = (63, 81, 181)
    
    # Curved arrow showing pivot
    # Start point (going right)
    draw.rectangle([20, 58, 60, 70], fill=arrow_color)
    
    # Arrow head pointing right
    draw.polygon([(60, 50), (60, 78), (75, 64)], fill=arrow_color)
    
    # Curved part
    for i in range(20):
        angle = i * 4.5  # 90 degrees total
        x = 60 + 20 * math.cos(math.radians(angle))
        y = 64 - 20 * math.sin(math.radians(angle))
        draw.ellipse([x-3, y-3, x+3, y+3], fill=arrow_color)
    
    # New direction arrow (going up)
    draw.rectangle([75, 20, 87, 44], fill=(76, 175, 80))
    draw.polygon([(69, 20), (93, 20), (81, 8)], fill=(76, 175, 80))
    
    return img

def create_runway():
    """Runway with calendar - time until money runs out"""
    size = 128
    img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # Runway (perspective view)
    runway_color = (66, 66, 66)
    draw.polygon([
        (40, 100), (88, 100),  # Bottom
        (70, 30), (58, 30)     # Top (perspective)
    ], fill=runway_color)
    
    # Runway stripes
    stripe_color = (255, 255, 255)
    for i in range(4):
        y = 90 - i * 20
        width = 8 - i * 2
        x_center = 64
        draw.rectangle([x_center-width, y-2, x_center+width, y+2], fill=stripe_color)
    
    # Calendar overlay (top right)
    cal_color = (255, 87, 34)
    draw.rectangle([75, 20, 105, 45], fill=cal_color)
    draw.rectangle([75, 20, 105, 28], fill=(198, 40, 40))  # Header
    
    # Calendar grid dots
    for i in range(3):
        for j in range(3):
            x = 80 + j * 8
            y = 32 + i * 4
            draw.ellipse([x-1, y-1, x+1, y+1], fill=(255, 255, 255))
    
    return img

def create_unicorn():
    """Unicorn - billion dollar company"""
    size = 128
    img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # Body (white/light purple)
    body_color = (237, 231, 246)
    draw.ellipse([35, 55, 85, 95], fill=body_color)
    
    # Head
    draw.ellipse([55, 35, 85, 65], fill=body_color)
    
    # Horn (golden)
    horn_color = (255, 193, 7)
    draw.polygon([(70, 35), (65, 15), (75, 15)], fill=horn_color)
    
    # Spiral on horn
    for i in range(3):
        y = 20 + i * 5
        draw.line([(67, y), (73, y+2)], fill=(255, 152, 0), width=1)
    
    # Mane (rainbow colors)
    rainbow = [(244, 67, 54), (255, 152, 0), (255, 235, 59), (76, 175, 80), (33, 150, 243), (156, 39, 176)]
    for i, color in enumerate(rainbow):
        x = 50 + i * 3
        y = 40 + i * 2
        draw.ellipse([x-2, y-2, x+2, y+2], fill=color)
    
    # Eye
    draw.ellipse([72, 45, 76, 49], fill=(0, 0, 0))
    
    # Legs (simplified)
    for x in [45, 55, 65, 75]:
        draw.rectangle([x-2, 85, x+2, 105], fill=body_color)
    
    # Dollar signs floating around
    dollar_color = (76, 175, 80)
    positions = [(90, 30), (30, 40), (95, 70)]
    for x, y in positions:
        draw.text((x, y), "$", fill=dollar_color, font=None)
    
    return img

def create_series_a():
    """Series A funding - A with money bag"""
    size = 128
    img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # Large "A" 
    a_color = (25, 118, 210)
    # Left leg
    draw.polygon([(35, 80), (45, 80), (55, 40), (50, 40)], fill=a_color)
    # Right leg
    draw.polygon([(65, 40), (60, 40), (70, 80), (80, 80)], fill=a_color)
    # Horizontal bar
    draw.rectangle([45, 60, 70, 68], fill=a_color)
    
    # Money bag
    bag_color = (255, 193, 7)
    # Bag body
    draw.ellipse([70, 65, 100, 95], fill=bag_color)
    # Bag top/tie
    draw.polygon([(80, 65), (85, 55), (90, 65)], fill=bag_color)
    
    # Dollar sign on bag
    draw.text((81, 73), "$", fill=(76, 175, 80), font=None)
    
    # Sparkles around
    sparkle_color = (255, 235, 59)
    sparkles = [(30, 30), (95, 40), (40, 90), (105, 85)]
    for x, y in sparkles:
        draw.polygon([
            (x, y-3), (x-1, y), (x, y+3), (x+1, y),
            (x, y-3)
        ], fill=sparkle_color)
    
    return img

def create_mvp():
    """MVP - Minimum Viable Product (simple box)"""
    size = 128
    img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # Simple cardboard box (MVP is basic)
    box_color = (161, 136, 127)
    
    # Box front
    draw.rectangle([35, 50, 75, 90], fill=box_color)
    
    # Box top (perspective)
    top_color = (141, 110, 99)
    draw.polygon([
        (35, 50), (75, 50),
        (85, 40), (45, 40)
    ], fill=top_color)
    
    # Box side
    side_color = (121, 85, 72)
    draw.polygon([
        (75, 50), (85, 40),
        (85, 80), (75, 90)
    ], fill=side_color)
    
    # "MVP" text on box
    text_color = (33, 33, 33)
    draw.text((45, 65), "MVP", fill=text_color, font=None)
    
    # Tape on box (it's rough)
    tape_color = (224, 224, 224)
    draw.rectangle([30, 55, 80, 60], fill=tape_color)
    
    # Check mark (it works!)
    check_color = (76, 175, 80)
    draw.line([(88, 85), (95, 92)], fill=check_color, width=3)
    draw.line([(95, 92), (105, 75)], fill=check_color, width=3)
    
    return img

def create_growth_hacking():
    """Growth hacking - rocket chart going up"""
    size = 128
    img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # Chart axes
    axes_color = (158, 158, 158)
    draw.line([(25, 95), (95, 95)], fill=axes_color, width=2)  # X axis
    draw.line([(25, 95), (25, 25)], fill=axes_color, width=2)  # Y axis
    
    # Growth line (exponential)
    line_color = (76, 175, 80)
    points = []
    for i in range(60):
        x = 30 + i
        # Exponential growth
        y = 90 - int((i/60) ** 2 * 50)
        points.append((x, y))
    
    # Draw the line
    for i in range(len(points)-1):
        draw.line([points[i], points[i+1]], fill=line_color, width=3)
    
    # Rocket at the end of line
    rocket_pos = points[-1]
    rocket_color = (244, 67, 54)
    
    # Rocket body
    draw.polygon([
        (rocket_pos[0]-5, rocket_pos[1]+10),
        (rocket_pos[0]+5, rocket_pos[1]+10),
        (rocket_pos[0], rocket_pos[1]-5)
    ], fill=rocket_color)
    
    # Rocket flames
    flame_color = (255, 152, 0)
    draw.polygon([
        (rocket_pos[0]-3, rocket_pos[1]+10),
        (rocket_pos[0], rocket_pos[1]+15),
        (rocket_pos[0]+3, rocket_pos[1]+10)
    ], fill=flame_color)
    
    # Money symbols floating
    for x, y in [(40, 70), (60, 50), (80, 30)]:
        draw.text((x, y), "$", fill=(76, 175, 80), font=None)
    
    return img

def create_bootstrapping():
    """Bootstrapping - boot with straps"""
    size = 128
    img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # Boot
    boot_color = (78, 52, 46)
    
    # Boot foot part
    draw.ellipse([35, 70, 85, 95], fill=boot_color)
    
    # Boot leg part
    draw.rectangle([50, 35, 75, 75], fill=boot_color)
    
    # Boot sole
    sole_color = (33, 33, 33)
    draw.ellipse([35, 88, 85, 98], fill=sole_color)
    
    # Straps (pulling itself up)
    strap_color = (121, 85, 72)
    # Strap 1
    draw.rectangle([48, 25, 52, 40], fill=strap_color)
    draw.ellipse([47, 22, 53, 28], fill=strap_color)
    
    # Strap 2
    draw.rectangle([73, 25, 77, 40], fill=strap_color)
    draw.ellipse([72, 22, 78, 28], fill=strap_color)
    
    # Upward arrows showing "pulling up"
    arrow_color = (76, 175, 80)
    for x in [40, 62, 84]:
        draw.polygon([
            (x, 20), (x-4, 25), (x+4, 25)
        ], fill=arrow_color)
        draw.rectangle([x-1, 25, x+1, 30], fill=arrow_color)
    
    # Laces
    lace_color = (224, 224, 224)
    for i in range(3):
        y = 45 + i * 10
        draw.line([(52, y), (73, y)], fill=lace_color, width=1)
    
    return img

def create_ipo():
    """IPO - Bell ringing / stock chart"""
    size = 128
    img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # Bell (NYSE style)
    bell_color = (255, 193, 7)
    
    # Bell body
    draw.polygon([
        (64, 30),  # Top
        (50, 60),  # Left
        (50, 65),
        (78, 65),  # Bottom
        (78, 60)   # Right
    ], fill=bell_color)
    
    # Bell handle
    draw.ellipse([60, 25, 68, 33], fill=bell_color)
    
    # Clapper
    draw.ellipse([61, 62, 67, 68], fill=(66, 66, 66))
    
    # Sound waves
    wave_color = (255, 152, 0)
    for i in range(3):
        radius = 75 + i * 8
        draw.arc([64-radius//2, 50-radius//2, 64+radius//2, 50+radius//2], 
                 start=30, end=150, fill=wave_color, width=2)
    
    # Stock chart in background
    chart_color = (76, 175, 80, 100)  # Semi-transparent
    points = [(30, 85), (45, 80), (60, 70), (75, 65), (90, 55), (105, 45)]
    for i in range(len(points)-1):
        draw.line([points[i], points[i+1]], fill=chart_color, width=2)
    
    # IPO text
    draw.text((55, 80), "IPO", fill=(33, 150, 243), font=None)
    
    return img

def create_exit_strategy():
    """Exit strategy - exit door with money"""
    size = 128
    img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # Door frame
    frame_color = (121, 85, 72)
    draw.rectangle([35, 25, 85, 95], fill=frame_color)
    
    # Door (slightly open)
    door_color = (161, 136, 127)
    draw.polygon([
        (40, 30), (75, 33),
        (75, 90), (40, 90)
    ], fill=door_color)
    
    # Door handle
    handle_color = (255, 193, 7)
    draw.ellipse([67, 58, 73, 64], fill=handle_color)
    
    # EXIT sign above door
    sign_color = (244, 67, 54)
    draw.rectangle([45, 15, 75, 25], fill=sign_color)
    draw.text((52, 16), "EXIT", fill=(255, 255, 255), font=None)
    
    # Money flying out
    money_color = (76, 175, 80)
    bills = [(80, 40), (90, 55), (85, 70), (95, 45)]
    for x, y in bills:
        draw.rectangle([x, y, x+12, y+6], fill=money_color)
        draw.text((x+2, y), "$", fill=(255, 255, 255), font=None)
    
    # Arrow pointing out
    arrow_color = (33, 150, 243)
    draw.polygon([
        (90, 85), (100, 85), (100, 80),
        (105, 87), (100, 94), (100, 89), (90, 89)
    ], fill=arrow_color)
    
    return img

# Generate all emojis
if __name__ == "__main__":
    emojis = [
        ("burn_rate", create_burn_rate),
        ("pivot", create_pivot),
        ("runway", create_runway),
        ("unicorn", create_unicorn),
        ("series_a", create_series_a),
        ("mvp", create_mvp),
        ("growth_hacking", create_growth_hacking),
        ("bootstrapping", create_bootstrapping),
        ("ipo", create_ipo),
        ("exit_strategy", create_exit_strategy)
    ]
    
    for name, create_func in emojis:
        img = create_func()
        img.save(f"{output_dir}/{name}.png")
        print(f"Created {name}.png")
    
    print(f"\nAll startup-hustle emojis created in {output_dir}/")
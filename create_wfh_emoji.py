#!/usr/bin/env python3
"""
Create work-from-home emoji pack
Emojis for remote work life: pajamas, zoom fatigue, mute, pets, etc.
"""

from PIL import Image, ImageDraw
import os

# Create output directory
output_dir = "images/work-from-home"
os.makedirs(output_dir, exist_ok=True)

def create_pajamas():
    """Pajamas - working in PJs"""
    size = 128
    img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # Pajama top (striped)
    base_color = (156, 39, 176)
    stripe_color = (186, 104, 200)
    
    # Body of pajama
    draw.rectangle([35, 40, 93, 85], fill=base_color)
    
    # Stripes
    for i in range(5):
        y = 45 + i * 10
        draw.rectangle([35, y, 93, y+5], fill=stripe_color)
    
    # Collar
    draw.polygon([(55, 40), (64, 30), (73, 40)], fill=base_color)
    
    # Sleeves
    draw.rectangle([20, 50, 35, 70], fill=base_color)  # Left sleeve
    draw.rectangle([93, 50, 108, 70], fill=base_color)  # Right sleeve
    
    # Buttons
    button_color = (255, 255, 255)
    for i in range(3):
        y = 48 + i * 12
        draw.ellipse([61, y, 67, y+6], fill=button_color)
    
    # Pocket
    draw.rectangle([75, 55, 85, 65], outline=stripe_color, width=2)
    
    return img

def create_zoom_fatigue():
    """Zoom fatigue - tired face with laptop"""
    size = 128
    img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # Laptop screen
    screen_color = (66, 66, 66)
    draw.rectangle([25, 45, 103, 85], fill=screen_color)
    
    # Screen content (video grid)
    grid_color = (33, 150, 243)
    for i in range(3):
        for j in range(3):
            x = 30 + j * 24
            y = 50 + i * 10
            draw.rectangle([x, y, x+20, y+8], fill=grid_color)
    
    # Tired face above laptop
    face_color = (255, 224, 178)
    draw.ellipse([50, 15, 78, 43], fill=face_color)
    
    # Tired eyes (half closed)
    eye_color = (0, 0, 0)
    draw.arc([55, 25, 61, 31], start=0, end=180, fill=eye_color, width=2)
    draw.arc([67, 25, 73, 31], start=0, end=180, fill=eye_color, width=2)
    
    # Eye bags
    bag_color = (156, 39, 176, 50)
    draw.ellipse([55, 31, 61, 34], fill=bag_color)
    draw.ellipse([67, 31, 73, 34], fill=bag_color)
    
    # Frown
    draw.arc([58, 33, 70, 40], start=20, end=160, fill=eye_color, width=2)
    
    # ZZZ to show sleepiness
    sleep_color = (100, 100, 100)
    draw.text((80, 20), "Z", fill=sleep_color, font=None)
    draw.text((85, 15), "Z", fill=sleep_color, font=None)
    draw.text((90, 10), "Z", fill=sleep_color, font=None)
    
    # Laptop base
    draw.polygon([(25, 85), (103, 85), (108, 95), (20, 95)], fill=(158, 158, 158))
    
    return img

def create_mute_yourself():
    """Mute yourself - microphone with X"""
    size = 128
    img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # Microphone body
    mic_color = (66, 66, 66)
    draw.ellipse([54, 25, 74, 65], fill=mic_color)
    
    # Mic grille pattern
    grille_color = (97, 97, 97)
    for i in range(3):
        for j in range(5):
            x = 58 + i * 6
            y = 30 + j * 7
            draw.ellipse([x, y, x+3, y+3], fill=grille_color)
    
    # Mic stand
    stand_color = (33, 33, 33)
    draw.rectangle([62, 65, 66, 85], fill=stand_color)
    
    # Mic base
    draw.ellipse([54, 83, 74, 93], fill=stand_color)
    
    # Red X over microphone
    x_color = (244, 67, 54)
    draw.line([(40, 30), (88, 78)], fill=x_color, width=6)
    draw.line([(88, 30), (40, 78)], fill=x_color, width=6)
    
    # Mute indicator
    draw.text((35, 95), "MUTED", fill=x_color, font=None)
    
    return img

def create_camera_off():
    """Camera off - webcam with slash"""
    size = 128
    img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # Webcam body
    cam_color = (66, 66, 66)
    draw.ellipse([35, 35, 93, 93], fill=cam_color)
    
    # Lens outer ring
    lens_ring = (97, 97, 97)
    draw.ellipse([45, 45, 83, 83], fill=lens_ring)
    
    # Lens
    lens_color = (33, 33, 33)
    draw.ellipse([50, 50, 78, 78], fill=lens_color)
    
    # Lens reflection (when off it's dark)
    reflection_color = (50, 50, 50)
    draw.ellipse([55, 55, 65, 65], fill=reflection_color)
    
    # Webcam mount
    mount_color = (66, 66, 66)
    draw.rectangle([60, 93, 68, 105], fill=mount_color)
    
    # Diagonal line (camera off)
    off_color = (244, 67, 54)
    draw.line([(30, 30), (98, 98)], fill=off_color, width=5)
    
    # OFF text
    draw.text((50, 105), "OFF", fill=off_color, font=None)
    
    return img

def create_pet_cameo():
    """Pet cameo - cat walking on keyboard"""
    size = 128
    img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # Keyboard
    kb_color = (189, 189, 189)
    draw.rectangle([20, 75, 108, 95], fill=kb_color)
    
    # Keys
    key_color = (158, 158, 158)
    for i in range(8):
        for j in range(2):
            x = 25 + i * 10
            y = 78 + j * 8
            draw.rectangle([x, y, x+8, y+6], fill=key_color)
    
    # Cat body
    cat_color = (255, 152, 0)
    draw.ellipse([40, 45, 88, 75], fill=cat_color)
    
    # Cat head
    draw.ellipse([75, 35, 100, 60], fill=cat_color)
    
    # Cat ears
    draw.polygon([(78, 40), (75, 25), (83, 35)], fill=cat_color)
    draw.polygon([(92, 35), (100, 25), (97, 40)], fill=cat_color)
    
    # Cat face
    # Eyes
    eye_color = (76, 175, 80)
    draw.ellipse([82, 42, 86, 46], fill=eye_color)
    draw.ellipse([90, 42, 94, 46], fill=eye_color)
    
    # Pupils
    draw.ellipse([83, 43, 85, 45], fill=(0, 0, 0))
    draw.ellipse([91, 43, 93, 45], fill=(0, 0, 0))
    
    # Nose
    draw.polygon([(88, 48), (86, 50), (90, 50)], fill=(255, 182, 193))
    
    # Tail
    draw.ellipse([30, 50, 45, 55], fill=cat_color)
    
    # Paws on keyboard
    paw_color = (255, 182, 193)
    draw.ellipse([55, 72, 63, 78], fill=paw_color)
    draw.ellipse([70, 72, 78, 78], fill=paw_color)
    
    return img

def create_home_office():
    """Home office - house with laptop"""
    size = 128
    img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # House base
    house_color = (121, 85, 72)
    draw.rectangle([30, 50, 98, 95], fill=house_color)
    
    # Roof
    roof_color = (198, 40, 40)
    draw.polygon([(20, 50), (64, 20), (108, 50)], fill=roof_color)
    
    # Door
    door_color = (78, 52, 46)
    draw.rectangle([55, 65, 73, 95], fill=door_color)
    
    # Windows
    window_color = (135, 206, 235)
    draw.rectangle([35, 60, 48, 73], fill=window_color)
    draw.rectangle([80, 60, 93, 73], fill=window_color)
    
    # Window cross
    cross_color = (255, 255, 255)
    draw.line([(41, 60), (41, 73)], fill=cross_color, width=1)
    draw.line([(35, 66), (48, 66)], fill=cross_color, width=1)
    draw.line([(86, 60), (86, 73)], fill=cross_color, width=1)
    draw.line([(80, 66), (93, 66)], fill=cross_color, width=1)
    
    # Laptop on desk (visible through window)
    laptop_color = (66, 66, 66)
    draw.rectangle([38, 68, 45, 72], fill=laptop_color)
    
    # WiFi symbol on roof
    wifi_color = (33, 150, 243)
    for i in range(3):
        radius = 8 + i * 5
        draw.arc([64-radius, 15-radius, 64+radius, 15+radius], 
                start=225, end=315, fill=wifi_color, width=2)
    
    return img

def create_coffee_break():
    """Coffee break at home - mug with steam on couch"""
    size = 128
    img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # Couch
    couch_color = (63, 81, 181)
    # Couch back
    draw.rectangle([20, 50, 108, 70], fill=couch_color)
    # Couch seat
    draw.rectangle([20, 70, 108, 90], fill=(83, 101, 201))
    # Couch arms
    draw.rectangle([20, 50, 30, 85], fill=couch_color)
    draw.rectangle([98, 50, 108, 85], fill=couch_color)
    
    # Coffee mug
    mug_color = (255, 87, 34)
    draw.ellipse([52, 35, 76, 55], fill=mug_color)
    
    # Mug handle
    draw.arc([72, 38, 82, 48], start=270, end=90, fill=mug_color, width=3)
    
    # Coffee inside
    coffee_color = (78, 52, 46)
    draw.ellipse([55, 38, 73, 50], fill=coffee_color)
    
    # Steam
    steam_color = (189, 189, 189, 150)
    for i in range(3):
        x = 58 + i * 5
        for j in range(4):
            y = 30 - j * 5
            opacity = 150 - j * 30
            draw.ellipse([x-2, y-2, x+2, y+2], fill=(189, 189, 189, opacity))
    
    # Cushion
    cushion_color = (255, 193, 7)
    draw.ellipse([40, 72, 55, 85], fill=cushion_color)
    
    return img

def create_background_noise():
    """Background noise - sound waves with house stuff"""
    size = 128
    img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # Speaker/noise source
    speaker_color = (66, 66, 66)
    draw.rectangle([20, 45, 40, 75], fill=speaker_color)
    draw.ellipse([23, 48, 37, 62], fill=(97, 97, 97))
    draw.ellipse([23, 63, 37, 72], fill=(97, 97, 97))
    
    # Sound waves
    wave_colors = [(244, 67, 54), (255, 152, 0), (255, 235, 59)]
    for i, color in enumerate(wave_colors):
        for j in range(3):
            x = 45 + i * 15 + j * 5
            # Wavy line
            points = []
            for k in range(20):
                y_offset = k * 2
                x_pos = x + k * 2
                y_pos = 60 + 10 * ((k % 2) * 2 - 1)
                points.append((x_pos, y_pos))
            
            for p in range(len(points)-1):
                draw.line([points[p], points[p+1]], fill=color, width=2)
    
    # Dog barking
    dog_color = (139, 69, 19)
    draw.ellipse([85, 65, 105, 80], fill=dog_color)  # Body
    draw.ellipse([100, 60, 115, 75], fill=dog_color)  # Head
    draw.polygon([(103, 63), (102, 55), (107, 60)], fill=dog_color)  # Ear
    
    # Bark lines
    bark_color = (244, 67, 54)
    draw.text((110, 55), "WOOF!", fill=bark_color, font=None)
    
    return img

def create_snack_time():
    """Snack time - chips and snacks"""
    size = 128
    img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # Chip bag
    bag_color = (255, 193, 7)
    draw.polygon([
        (35, 30), (55, 30),  # Top
        (60, 80), (30, 80)   # Bottom
    ], fill=bag_color)
    
    # Bag label
    label_color = (244, 67, 54)
    draw.ellipse([37, 50, 53, 66], fill=label_color)
    draw.text((39, 54), "CHIPS", fill=(255, 255, 255), font=None)
    
    # Chips spilling out
    chip_color = (255, 235, 59)
    chips = [
        (38, 25), (48, 22), (43, 18),
        (55, 28), (52, 20)
    ]
    for x, y in chips:
        draw.ellipse([x-4, y-3, x+4, y+3], fill=chip_color)
    
    # Cookie
    cookie_color = (139, 69, 19)
    draw.ellipse([70, 55, 95, 80], fill=cookie_color)
    
    # Chocolate chips
    choc_color = (78, 52, 46)
    choc_chips = [(75, 60), (85, 63), (78, 70), (88, 72)]
    for x, y in choc_chips:
        draw.ellipse([x-2, y-2, x+2, y+2], fill=choc_color)
    
    # Soda can
    can_color = (244, 67, 54)
    draw.rectangle([75, 30, 95, 50], fill=can_color)
    draw.ellipse([75, 28, 95, 32], fill=(200, 40, 40))
    draw.ellipse([75, 48, 95, 52], fill=(200, 40, 40))
    
    return img

def create_no_commute():
    """No commute - bed to desk (short path)"""
    size = 128
    img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # Bed
    bed_color = (121, 85, 72)
    draw.rectangle([15, 60, 45, 85], fill=bed_color)
    
    # Pillow
    pillow_color = (255, 255, 255)
    draw.ellipse([18, 55, 35, 65], fill=pillow_color)
    
    # Blanket
    blanket_color = (156, 39, 176)
    draw.rectangle([20, 65, 40, 80], fill=blanket_color)
    
    # Dotted line path (very short)
    path_color = (76, 175, 80)
    for i in range(5):
        x = 48 + i * 8
        draw.ellipse([x-2, 70-2, x+2, 70+2], fill=path_color)
    
    # Desk
    desk_color = (139, 69, 19)
    draw.rectangle([83, 65, 113, 85], fill=desk_color)
    
    # Computer on desk
    computer_color = (66, 66, 66)
    draw.rectangle([88, 50, 108, 65], fill=computer_color)
    draw.rectangle([93, 65, 103, 68], fill=computer_color)  # Stand
    
    # Screen content
    screen_color = (33, 150, 243)
    draw.rectangle([91, 53, 105, 62], fill=screen_color)
    
    # Chair
    chair_color = (97, 97, 97)
    draw.rectangle([90, 75, 106, 90], fill=chair_color)
    draw.rectangle([85, 85, 111, 92], fill=chair_color)
    
    # Distance indicator
    draw.text((55, 90), "5 steps", fill=path_color, font=None)
    
    return img

# Generate all emojis
if __name__ == "__main__":
    emojis = [
        ("pajamas", create_pajamas),
        ("zoom_fatigue", create_zoom_fatigue),
        ("mute_yourself", create_mute_yourself),
        ("camera_off", create_camera_off),
        ("pet_cameo", create_pet_cameo),
        ("home_office", create_home_office),
        ("coffee_break", create_coffee_break),
        ("background_noise", create_background_noise),
        ("snack_time", create_snack_time),
        ("no_commute", create_no_commute)
    ]
    
    for name, create_func in emojis:
        img = create_func()
        img.save(f"{output_dir}/{name}.png")
        print(f"Created {name}.png")
    
    print(f"\nAll work-from-home emojis created in {output_dir}/")
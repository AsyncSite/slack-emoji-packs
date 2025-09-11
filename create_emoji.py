#!/usr/bin/env python3
"""
Create real emoji images for Slack emoji packs
"""

from PIL import Image, ImageDraw, ImageFont
import os

def create_bug_emoji():
    """Create a bug emoji - red bug icon"""
    size = 128
    img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # Bug body (red oval)
    body_color = (220, 53, 69)  # Bootstrap danger red
    draw.ellipse([30, 40, 98, 88], fill=body_color)
    
    # Bug head (darker red circle)
    head_color = (180, 33, 49)
    draw.ellipse([48, 25, 80, 57], fill=head_color)
    
    # Eyes (white dots)
    draw.ellipse([55, 35, 63, 43], fill='white')
    draw.ellipse([65, 35, 73, 43], fill='white')
    
    # Eye pupils (black dots)
    draw.ellipse([57, 37, 61, 41], fill='black')
    draw.ellipse([67, 37, 71, 41], fill='black')
    
    # Antennae (black lines)
    draw.line([55, 30, 50, 20], fill='black', width=2)
    draw.line([73, 30, 78, 20], fill='black', width=2)
    
    # Spots on body (darker red)
    spot_color = (150, 23, 39)
    draw.ellipse([40, 50, 50, 60], fill=spot_color)
    draw.ellipse([78, 55, 88, 65], fill=spot_color)
    draw.ellipse([60, 70, 70, 80], fill=spot_color)
    
    # Legs (black lines)
    # Left legs
    draw.line([35, 50, 20, 45], fill='black', width=2)
    draw.line([35, 60, 20, 60], fill='black', width=2)
    draw.line([35, 70, 20, 75], fill='black', width=2)
    
    # Right legs
    draw.line([93, 50, 108, 45], fill='black', width=2)
    draw.line([93, 60, 108, 60], fill='black', width=2)
    draw.line([93, 70, 108, 75], fill='black', width=2)
    
    return img

def create_coffee_emoji():
    """Create a coffee emoji - steaming coffee cup"""
    size = 128
    img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # Cup (brown)
    cup_color = (139, 69, 19)  # Saddle brown
    draw.rounded_rectangle([30, 50, 85, 100], radius=5, fill=cup_color)
    
    # Handle
    draw.arc([78, 60, 95, 80], start=270, end=90, fill=cup_color, width=4)
    
    # Coffee inside (darker brown)
    coffee_color = (83, 53, 10)
    draw.ellipse([35, 55, 80, 70], fill=coffee_color)
    
    # Steam (gray wavy lines)
    steam_color = (200, 200, 200, 180)
    # Steam line 1
    draw.line([45, 45, 47, 35], fill=steam_color, width=2)
    draw.line([47, 35, 45, 25], fill=steam_color, width=2)
    
    # Steam line 2
    draw.line([57, 45, 59, 35], fill=steam_color, width=2)
    draw.line([59, 35, 57, 25], fill=steam_color, width=2)
    
    # Steam line 3
    draw.line([69, 45, 71, 35], fill=steam_color, width=2)
    draw.line([71, 35, 69, 25], fill=steam_color, width=2)
    
    # Saucer (light brown)
    saucer_color = (205, 133, 63)
    draw.ellipse([20, 95, 95, 110], fill=saucer_color)
    
    return img

def create_fire_emoji():
    """Create a fire emoji - flame icon"""
    size = 128
    img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # Outer flame (red-orange)
    flame_points = [
        (64, 20),   # Top
        (75, 35),   # Right upper
        (85, 55),   # Right middle
        (82, 75),   # Right lower
        (75, 90),   # Right bottom
        (64, 95),   # Bottom center
        (53, 90),   # Left bottom
        (46, 75),   # Left lower
        (43, 55),   # Left middle
        (53, 35),   # Left upper
    ]
    draw.polygon(flame_points, fill=(255, 69, 0))  # Orange-red
    
    # Inner flame (yellow)
    inner_points = [
        (64, 35),   # Top
        (70, 45),   # Right upper
        (72, 60),   # Right middle
        (70, 75),   # Right lower
        (64, 80),   # Bottom center
        (58, 75),   # Left lower
        (56, 60),   # Left middle
        (58, 45),   # Left upper
    ]
    draw.polygon(inner_points, fill=(255, 215, 0))  # Gold
    
    # Core flame (white-yellow)
    core_points = [
        (64, 50),   # Top
        (67, 58),   # Right
        (66, 68),   # Right lower
        (64, 70),   # Bottom
        (62, 68),   # Left lower
        (61, 58),   # Left
    ]
    draw.polygon(core_points, fill=(255, 255, 200))  # Light yellow
    
    return img

def create_rocket_emoji():
    """Create a rocket emoji - launching rocket"""
    size = 128
    img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # Rocket body (silver/gray)
    body_color = (192, 192, 192)
    body_points = [
        (64, 20),   # Tip
        (75, 45),   # Right upper
        (75, 75),   # Right lower
        (64, 80),   # Bottom
        (53, 75),   # Left lower
        (53, 45),   # Left upper
    ]
    draw.polygon(body_points, fill=body_color)
    
    # Nose cone (red)
    nose_points = [
        (64, 20),   # Tip
        (71, 35),   # Right
        (57, 35),   # Left
    ]
    draw.polygon(nose_points, fill=(220, 53, 69))
    
    # Window (blue circle)
    draw.ellipse([58, 45, 70, 57], fill=(0, 123, 255))
    
    # Wings (darker gray)
    wing_color = (105, 105, 105)
    # Left wing
    left_wing = [(53, 60), (40, 75), (40, 80), (53, 75)]
    draw.polygon(left_wing, fill=wing_color)
    # Right wing
    right_wing = [(75, 60), (88, 75), (88, 80), (75, 75)]
    draw.polygon(right_wing, fill=wing_color)
    
    # Flames (orange and yellow)
    # Center flame
    draw.polygon([(64, 80), (60, 95), (68, 95)], fill=(255, 69, 0))
    draw.polygon([(64, 80), (62, 90), (66, 90)], fill=(255, 215, 0))
    
    # Left flame
    draw.polygon([(56, 78), (52, 88), (58, 88)], fill=(255, 140, 0))
    
    # Right flame
    draw.polygon([(72, 78), (70, 88), (76, 88)], fill=(255, 140, 0))
    
    return img

def create_failed_emoji():
    """Create a failed emoji - red X mark"""
    size = 128
    img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # Red circle background
    circle_color = (220, 53, 69)  # Bootstrap danger red
    draw.ellipse([20, 20, 108, 108], fill=circle_color)
    
    # White X mark (thick lines)
    x_color = 'white'
    line_width = 12
    
    # First diagonal (top-left to bottom-right)
    draw.line([40, 40, 88, 88], fill=x_color, width=line_width)
    
    # Second diagonal (top-right to bottom-left)
    draw.line([88, 40, 40, 88], fill=x_color, width=line_width)
    
    return img

def create_loading_emoji():
    """Create a loading emoji - circular loading spinner"""
    size = 128
    img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # Draw loading spinner segments
    center_x, center_y = 64, 64
    radius = 35
    thickness = 8
    
    # Define colors for each segment (gradient from dark to light blue)
    colors = [
        (0, 123, 255),      # Bright blue
        (50, 150, 255),     # Lighter blue
        (100, 180, 255),    # Even lighter
        (150, 200, 255),    # Light blue
        (200, 220, 255),    # Very light blue
        (220, 230, 255),    # Almost white blue
        (240, 245, 255),    # Very faint blue
        (250, 250, 255),    # Nearly invisible
    ]
    
    # Draw 8 segments of the spinner
    for i in range(8):
        start_angle = i * 45
        end_angle = start_angle + 30
        
        # Draw arc segment
        bbox = [center_x - radius, center_y - radius, 
                center_x + radius, center_y + radius]
        draw.arc(bbox, start=start_angle, end=end_angle, 
                fill=colors[i], width=thickness)
    
    return img

def create_idea_emoji():
    """Create an idea emoji - light bulb"""
    size = 128
    img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # Light bulb glass (yellow for lit state)
    bulb_color = (255, 223, 0)  # Golden yellow
    draw.ellipse([35, 20, 93, 78], fill=bulb_color)
    
    # Light rays (lines radiating from bulb)
    ray_color = (255, 215, 0)  # Gold
    # Top rays
    draw.line([64, 15, 64, 5], fill=ray_color, width=3)
    # Top-right
    draw.line([80, 25, 90, 15], fill=ray_color, width=3)
    # Right
    draw.line([95, 49, 105, 49], fill=ray_color, width=3)
    # Bottom-right
    draw.line([80, 73, 90, 83], fill=ray_color, width=3)
    # Top-left
    draw.line([48, 25, 38, 15], fill=ray_color, width=3)
    # Left
    draw.line([33, 49, 23, 49], fill=ray_color, width=3)
    # Bottom-left
    draw.line([48, 73, 38, 83], fill=ray_color, width=3)
    
    # Filament inside bulb (orange wavy line)
    filament_color = (255, 140, 0)  # Dark orange
    # Draw zigzag filament
    draw.line([54, 40, 58, 45], fill=filament_color, width=2)
    draw.line([58, 45, 62, 40], fill=filament_color, width=2)
    draw.line([62, 40, 66, 45], fill=filament_color, width=2)
    draw.line([66, 45, 70, 40], fill=filament_color, width=2)
    draw.line([70, 40, 74, 45], fill=filament_color, width=2)
    
    # Base of bulb (dark gray)
    base_color = (105, 105, 105)
    draw.rectangle([50, 75, 78, 85], fill=base_color)
    
    # Screw threads on base (darker gray lines)
    thread_color = (70, 70, 70)
    draw.line([50, 78, 78, 78], fill=thread_color, width=1)
    draw.line([50, 81, 78, 81], fill=thread_color, width=1)
    draw.line([50, 84, 78, 84], fill=thread_color, width=1)
    
    # Bottom contact point (darker gray)
    draw.ellipse([58, 85, 70, 90], fill=thread_color)
    
    return img

def create_terminal_emoji():
    """Create a terminal emoji - command line window"""
    size = 128
    img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # Terminal window frame (dark gray)
    frame_color = (64, 64, 64)
    draw.rounded_rectangle([20, 25, 108, 103], radius=5, fill=frame_color)
    
    # Title bar (lighter gray)
    titlebar_color = (128, 128, 128)
    draw.rounded_rectangle([20, 25, 108, 40], radius=5, fill=titlebar_color)
    # Fix bottom corners of title bar to be square
    draw.rectangle([20, 35, 108, 40], fill=titlebar_color)
    
    # Window control buttons (red, yellow, green)
    # Red close button
    draw.ellipse([27, 30, 35, 38], fill=(255, 95, 86))
    # Yellow minimize button
    draw.ellipse([39, 30, 47, 38], fill=(255, 189, 46))
    # Green maximize button
    draw.ellipse([51, 30, 59, 38], fill=(40, 205, 65))
    
    # Terminal screen (black)
    screen_color = (0, 0, 0)
    draw.rectangle([25, 40, 103, 98], fill=screen_color)
    
    # Terminal text (green, like classic terminals)
    text_color = (0, 255, 0)  # Bright green
    
    # Prompt symbol >
    draw.text((30, 45), ">", fill=text_color)
    
    # Command text (simulated with rectangles for cursor effect)
    # Simulate "npm run dev"
    draw.rectangle([40, 48, 85, 50], fill=text_color)  # Command line
    
    # Output lines (dimmer green)
    output_color = (0, 200, 0)
    draw.rectangle([30, 60, 95, 62], fill=output_color)  # Line 1
    draw.rectangle([30, 68, 80, 70], fill=output_color)  # Line 2
    draw.rectangle([30, 76, 88, 78], fill=output_color)  # Line 3
    
    # Blinking cursor (bright green rectangle)
    cursor_color = (0, 255, 0)
    draw.rectangle([87, 48, 92, 50], fill=cursor_color)
    
    return img

# Main execution
if __name__ == "__main__":
    output_dir = "images/dev-essentials"
    
    # Create terminal emoji
    terminal_img = create_terminal_emoji()
    terminal_img.save(os.path.join(output_dir, "terminal.png"))
    print("Created: terminal.png")
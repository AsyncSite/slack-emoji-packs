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

def create_warning_emoji():
    """Create a warning emoji - yellow triangle with exclamation mark"""
    size = 128
    img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # Warning triangle (yellow/amber)
    triangle_color = (255, 193, 7)  # Bootstrap warning yellow
    triangle_points = [
        (64, 20),   # Top
        (95, 85),   # Bottom right
        (33, 85),   # Bottom left
    ]
    draw.polygon(triangle_points, fill=triangle_color)
    
    # Black border for triangle
    border_color = (0, 0, 0)
    draw.polygon(triangle_points, outline=border_color, width=3)
    
    # Exclamation mark (black)
    exclamation_color = (0, 0, 0)
    
    # Exclamation line (vertical rectangle)
    draw.rectangle([60, 40, 68, 65], fill=exclamation_color)
    
    # Exclamation dot
    draw.ellipse([59, 70, 69, 80], fill=exclamation_color)
    
    return img

def create_python_emoji():
    """Create a Python emoji - Python logo style snake"""
    size = 128
    img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # Python blue
    blue_color = (55, 118, 171)
    # Python yellow
    yellow_color = (255, 212, 59)
    
    # Left side (blue snake)
    # Head
    draw.ellipse([30, 25, 60, 55], fill=blue_color)
    # Body curve
    draw.arc([25, 45, 75, 95], start=90, end=270, fill=blue_color, width=15)
    # Tail
    draw.ellipse([30, 75, 60, 105], fill=blue_color)
    
    # Right side (yellow snake)
    # Head
    draw.ellipse([68, 25, 98, 55], fill=yellow_color)
    # Body curve
    draw.arc([53, 45, 103, 95], start=270, end=90, fill=yellow_color, width=15)
    # Tail
    draw.ellipse([68, 75, 98, 105], fill=yellow_color)
    
    # Eyes (white dots)
    draw.ellipse([40, 35, 46, 41], fill='white')
    draw.ellipse([82, 35, 88, 41], fill='white')
    
    # Eye pupils (black dots)
    draw.ellipse([41, 36, 45, 40], fill='black')
    draw.ellipse([83, 36, 87, 40], fill='black')
    
    return img

def create_javascript_emoji():
    """Create a JavaScript emoji - JS logo"""
    size = 128
    img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # JavaScript yellow background
    js_yellow = (247, 223, 30)
    draw.rounded_rectangle([25, 25, 103, 103], radius=8, fill=js_yellow)
    
    # JS letters (black)
    text_color = (0, 0, 0)
    
    # J letter (simplified as rectangles)
    draw.rectangle([45, 45, 55, 75], fill=text_color)  # Vertical line
    draw.rectangle([35, 70, 55, 80], fill=text_color)  # Bottom curve
    draw.ellipse([33, 68, 45, 80], fill=text_color)    # Curve
    
    # S letter (simplified as curves)
    # Top curve
    draw.arc([65, 45, 85, 60], start=180, end=0, fill=text_color, width=5)
    # Middle
    draw.rectangle([68, 57, 82, 63], fill=text_color)
    # Bottom curve
    draw.arc([65, 60, 85, 75], start=0, end=180, fill=text_color, width=5)
    
    return img

def create_react_emoji():
    """Create a React emoji - React logo atom"""
    size = 128
    img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # React blue
    react_blue = (97, 218, 251)
    
    # Center nucleus
    draw.ellipse([58, 58, 70, 70], fill=react_blue)
    
    # Electron orbits (3 ellipses at different angles)
    # Horizontal orbit
    draw.ellipse([25, 55, 103, 73], outline=react_blue, width=3)
    
    # Diagonal orbit 1 (top-left to bottom-right)
    # Draw as multiple arcs to simulate rotation
    draw.arc([35, 35, 93, 93], start=30, end=120, fill=react_blue, width=3)
    draw.arc([35, 35, 93, 93], start=210, end=300, fill=react_blue, width=3)
    
    # Diagonal orbit 2 (top-right to bottom-left)
    draw.arc([35, 35, 93, 93], start=120, end=210, fill=react_blue, width=3)
    draw.arc([35, 35, 93, 93], start=300, end=30, fill=react_blue, width=3)
    
    return img

def create_git_emoji():
    """Create a Git emoji - Git logo branch"""
    size = 128
    img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # Git orange-red
    git_color = (240, 80, 50)
    
    # Main branch line (vertical)
    draw.rectangle([60, 30, 68, 98], fill=git_color)
    
    # Branch nodes (circles)
    # Top node
    draw.ellipse([56, 25, 72, 41], fill=git_color)
    
    # Middle node (branch point)
    draw.ellipse([56, 55, 72, 71], fill=git_color)
    
    # Bottom node
    draw.ellipse([56, 90, 72, 106], fill=git_color)
    
    # Side branch
    draw.line([68, 63, 85, 45], fill=git_color, width=8)
    
    # Side branch node
    draw.ellipse([80, 38, 96, 54], fill=git_color)
    
    return img

def create_docker_emoji():
    """Create a Docker emoji - Docker whale"""
    size = 128
    img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # Docker blue
    docker_blue = (0, 157, 224)
    
    # Whale body (simplified)
    body_points = [
        (30, 65),   # Left
        (35, 55),   # Top-left
        (85, 55),   # Top-right
        (95, 65),   # Right
        (90, 80),   # Bottom-right
        (35, 80),   # Bottom-left
    ]
    draw.polygon(body_points, fill=docker_blue)
    
    # Containers on whale's back (rectangles)
    container_color = (0, 130, 200)
    # Container 1
    draw.rectangle([40, 45, 50, 55], fill=container_color)
    # Container 2
    draw.rectangle([55, 40, 65, 55], fill=container_color)
    # Container 3
    draw.rectangle([70, 45, 80, 55], fill=container_color)
    
    # Whale tail
    tail_points = [
        (25, 70),   # Connection
        (20, 65),   # Top
        (15, 75),   # Bottom
    ]
    draw.polygon(tail_points, fill=docker_blue)
    
    # Eye (white dot)
    draw.ellipse([85, 62, 89, 66], fill='white')
    
    return img

def create_api_emoji():
    """Create an API emoji - network/API connection"""
    size = 128
    img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # Purple color for API
    api_color = (147, 51, 234)  # Purple
    
    # Central server/API box
    draw.rounded_rectangle([48, 48, 80, 80], radius=5, fill=api_color)
    
    # Connection nodes around the center
    node_color = (168, 85, 247)  # Lighter purple
    line_color = (200, 150, 255)  # Even lighter purple
    
    # Top node
    draw.ellipse([58, 20, 70, 32], fill=node_color)
    draw.line([64, 32, 64, 48], fill=line_color, width=3)
    
    # Right node
    draw.ellipse([96, 58, 108, 70], fill=node_color)
    draw.line([80, 64, 96, 64], fill=line_color, width=3)
    
    # Bottom node
    draw.ellipse([58, 96, 70, 108], fill=node_color)
    draw.line([64, 80, 64, 96], fill=line_color, width=3)
    
    # Left node
    draw.ellipse([20, 58, 32, 70], fill=node_color)
    draw.line([32, 64, 48, 64], fill=line_color, width=3)
    
    # API text (simplified as dots in center)
    draw.ellipse([56, 56, 60, 60], fill='white')
    draw.ellipse([62, 56, 66, 60], fill='white')
    draw.ellipse([68, 56, 72, 60], fill='white')
    
    draw.ellipse([56, 68, 60, 72], fill='white')
    draw.ellipse([62, 68, 66, 72], fill='white')
    draw.ellipse([68, 68, 72, 72], fill='white')
    
    return img

def create_database_emoji():
    """Create a database emoji - cylinder stack"""
    size = 128
    img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # Database blue-gray
    db_color = (52, 73, 94)
    db_light = (69, 90, 111)
    
    # Draw three cylinder segments for database
    cylinder_height = 25
    
    # Top cylinder
    # Top ellipse
    draw.ellipse([35, 25, 93, 40], fill=db_light)
    # Body
    draw.rectangle([35, 32, 93, 50], fill=db_color)
    # Bottom ellipse (partial, hidden)
    draw.arc([35, 42, 93, 58], start=0, end=180, fill=db_color, width=2)
    
    # Middle cylinder
    # Body
    draw.rectangle([35, 50, 93, 68], fill=db_color)
    # Bottom ellipse (partial, hidden)
    draw.arc([35, 60, 93, 76], start=0, end=180, fill=db_color, width=2)
    
    # Bottom cylinder
    # Body
    draw.rectangle([35, 68, 93, 86], fill=db_color)
    # Bottom ellipse
    draw.ellipse([35, 78, 93, 94], fill=db_color)
    
    # Data lines (to show it's a database)
    line_color = (150, 170, 190)
    draw.line([45, 38, 83, 38], fill=line_color, width=2)
    draw.line([45, 56, 83, 56], fill=line_color, width=2)
    draw.line([45, 74, 83, 74], fill=line_color, width=2)
    
    return img

def create_merged_emoji():
    """Create a merged emoji - git merge symbol"""
    size = 128
    img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # Green for successful merge
    merge_color = (40, 167, 69)  # Bootstrap success green
    
    # Main branch (vertical line on left)
    draw.rectangle([35, 30, 43, 98], fill=merge_color)
    
    # Branch that merges (diagonal from top right to center)
    draw.line([85, 30, 43, 64], fill=merge_color, width=8)
    
    # Commit nodes
    # Top left (main branch)
    draw.ellipse([31, 26, 47, 42], fill=merge_color)
    
    # Top right (feature branch)
    draw.ellipse([81, 26, 97, 42], fill=merge_color)
    
    # Merge point
    draw.ellipse([35, 56, 51, 72], fill=merge_color)
    
    # Bottom (after merge)
    draw.ellipse([31, 90, 47, 106], fill=merge_color)
    
    # Check mark in merge point to show success
    check_color = 'white'
    draw.line([38, 64, 41, 67], fill=check_color, width=2)
    draw.line([41, 67, 47, 61], fill=check_color, width=2)
    
    return img

def create_party_emoji():
    """Create a party emoji - party popper"""
    size = 128
    img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # Party popper cone (gold)
    cone_color = (255, 193, 7)  # Gold
    cone_points = [
        (30, 80),   # Bottom left
        (50, 85),   # Bottom right
        (75, 35),   # Top
    ]
    draw.polygon(cone_points, fill=cone_color)
    
    # Confetti pieces (various colors)
    confetti_colors = [
        (255, 0, 127),    # Pink
        (0, 191, 255),    # Deep sky blue
        (50, 205, 50),    # Lime green
        (255, 215, 0),    # Gold
        (147, 112, 219),  # Medium purple
        (255, 69, 0),     # Orange red
    ]
    
    # Draw confetti pieces
    draw.rectangle([75, 25, 82, 32], fill=confetti_colors[0])
    draw.rectangle([85, 30, 92, 37], fill=confetti_colors[1])
    draw.rectangle([70, 40, 77, 47], fill=confetti_colors[2])
    draw.rectangle([80, 45, 87, 52], fill=confetti_colors[3])
    draw.rectangle([90, 40, 97, 47], fill=confetti_colors[4])
    draw.rectangle([65, 30, 72, 37], fill=confetti_colors[5])
    
    # Streamers (curved lines)
    draw.arc([75, 35, 95, 55], start=180, end=270, fill=confetti_colors[0], width=3)
    draw.arc([65, 25, 85, 45], start=270, end=0, fill=confetti_colors[1], width=3)
    
    # Stars
    star_color = (255, 223, 0)  # Golden yellow
    # Small star at top
    draw.polygon([(95, 25), (97, 30), (102, 30), (98, 33), (100, 38), 
                  (95, 35), (90, 38), (92, 33), (88, 30), (93, 30)], fill=star_color)
    
    return img

def create_laptop_emoji():
    """Create a laptop emoji - laptop computer"""
    size = 128
    img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # Laptop screen (dark gray frame)
    screen_frame = (64, 64, 64)
    draw.rounded_rectangle([25, 25, 103, 75], radius=3, fill=screen_frame)
    
    # Screen display (blue)
    screen_color = (0, 123, 255)  # Blue screen
    draw.rectangle([30, 30, 98, 70], fill=screen_color)
    
    # Code on screen (simplified as lines)
    code_color = (255, 255, 255)  # White text
    draw.rectangle([35, 35, 65, 37], fill=code_color)
    draw.rectangle([35, 40, 80, 42], fill=code_color)
    draw.rectangle([35, 45, 70, 47], fill=code_color)
    draw.rectangle([35, 50, 85, 52], fill=code_color)
    draw.rectangle([35, 55, 75, 57], fill=code_color)
    draw.rectangle([35, 60, 90, 62], fill=code_color)
    
    # Laptop base/keyboard (silver)
    base_color = (192, 192, 192)
    # Base trapezoid
    base_points = [
        (20, 75),    # Top left
        (108, 75),   # Top right
        (113, 90),   # Bottom right
        (15, 90),    # Bottom left
    ]
    draw.polygon(base_points, fill=base_color)
    
    # Trackpad (darker gray)
    trackpad_color = (128, 128, 128)
    draw.rectangle([54, 80, 74, 86], fill=trackpad_color)
    
    return img

def create_infinity_emoji():
    """Create an infinity emoji - infinity symbol"""
    size = 128
    img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # Infinity color (gradient blue to purple effect using single color)
    infinity_color = (138, 43, 226)  # Blue violet
    
    # Draw infinity symbol as two circles connected
    thickness = 8
    
    # Left loop
    draw.arc([25, 45, 65, 85], start=30, end=330, fill=infinity_color, width=thickness)
    
    # Right loop
    draw.arc([63, 45, 103, 85], start=210, end=150, fill=infinity_color, width=thickness)
    
    # Connect the loops with diagonal lines
    draw.line([48, 52, 80, 78], fill=infinity_color, width=thickness)
    draw.line([48, 78, 80, 52], fill=infinity_color, width=thickness)
    
    return img

def create_working_from_home_emoji():
    """Create a working from home emoji - house with laptop"""
    size = 128
    img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # House outline (brown)
    house_color = (139, 69, 19)  # Saddle brown
    
    # Roof (triangle)
    roof_points = [
        (64, 20),   # Top
        (95, 50),   # Right
        (33, 50),   # Left
    ]
    draw.polygon(roof_points, fill=house_color)
    
    # House walls (beige)
    wall_color = (245, 222, 179)  # Wheat
    draw.rectangle([38, 50, 90, 95], fill=wall_color)
    
    # Door (darker brown)
    door_color = (101, 67, 33)  # Dark brown
    draw.rectangle([56, 70, 72, 95], fill=door_color)
    
    # Window with laptop inside (showing WFH)
    window_color = (135, 206, 235)  # Sky blue
    draw.rectangle([42, 55, 58, 70], fill=window_color)
    
    # Laptop in window (small, simplified)
    laptop_color = (64, 64, 64)  # Dark gray
    draw.rectangle([45, 62, 55, 68], fill=laptop_color)
    # Screen glow
    draw.rectangle([46, 63, 54, 67], fill=(255, 255, 255))
    
    # Window 2 (right side)
    draw.rectangle([70, 55, 86, 70], fill=window_color)
    
    # WiFi symbol above house (to show connectivity)
    wifi_color = (0, 123, 255)  # Blue
    # WiFi waves
    draw.arc([54, 5, 74, 25], start=200, end=340, fill=wifi_color, width=2)
    draw.arc([58, 8, 70, 20], start=200, end=340, fill=wifi_color, width=2)
    draw.ellipse([62, 12, 66, 16], fill=wifi_color)
    
    return img

# Main execution
if __name__ == "__main__":
    output_dir = "images/dev-essentials"
    
    # Create all remaining emojis
    emojis = [
        ("api", create_api_emoji),
        ("database", create_database_emoji),
        ("merged", create_merged_emoji),
        ("party", create_party_emoji),
        ("laptop", create_laptop_emoji),
        ("infinity", create_infinity_emoji),
        ("working-from-home", create_working_from_home_emoji),
    ]
    
    for name, create_func in emojis:
        img = create_func()
        img.save(os.path.join(output_dir, f"{name}.png"))
        print(f"Created: {name}.png")
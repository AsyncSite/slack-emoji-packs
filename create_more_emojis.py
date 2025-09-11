#!/usr/bin/env python3
"""
Create more emoji images for dev-essentials pack
"""

from PIL import Image, ImageDraw
import os

def create_done_emoji():
    """Create a done/checkmark emoji - green checkmark in circle"""
    size = 128
    img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # Green circle background
    circle_color = (40, 167, 69)  # Bootstrap success green
    draw.ellipse([20, 20, 108, 108], fill=circle_color)
    
    # White checkmark
    check_color = 'white'
    # Draw thick checkmark
    points = [
        (35, 64),   # Start point
        (52, 81),   # Bottom point
        (85, 48)    # End point
    ]
    
    # Draw checkmark with thickness
    for offset in range(-3, 4):
        draw.line([(35+offset, 64), (52+offset, 81)], fill=check_color, width=4)
        draw.line([(52+offset, 81), (85, 48+offset)], fill=check_color, width=4)
    
    return img

def create_failed_emoji():
    """Create a failed/error emoji - red X mark"""
    size = 128
    img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # Red circle background
    circle_color = (220, 53, 69)  # Bootstrap danger red
    draw.ellipse([20, 20, 108, 108], fill=circle_color)
    
    # White X mark
    x_color = 'white'
    # Draw thick X
    for offset in range(-3, 4):
        draw.line([(40+offset, 40), (88+offset, 88)], fill=x_color, width=5)
        draw.line([(88-offset, 40), (40-offset, 88)], fill=x_color, width=5)
    
    return img

def create_shipit_emoji():
    """Create a ship it emoji - squirrel with ship wheel (simplified)"""
    size = 128
    img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # Ship wheel (brown)
    wheel_color = (139, 69, 19)
    # Outer circle
    draw.ellipse([25, 25, 103, 103], outline=wheel_color, width=4)
    # Inner circle
    draw.ellipse([45, 45, 83, 83], outline=wheel_color, width=3)
    # Spokes
    draw.line([64, 25, 64, 103], fill=wheel_color, width=3)
    draw.line([25, 64, 103, 64], fill=wheel_color, width=3)
    draw.line([40, 40, 88, 88], fill=wheel_color, width=3)
    draw.line([88, 40, 40, 88], fill=wheel_color, width=3)
    
    # Center hub
    draw.ellipse([58, 58, 70, 70], fill=wheel_color)
    
    # Add "SHIP IT!" text effect with smaller box
    text_bg = (255, 193, 7)  # Bootstrap warning yellow
    draw.rectangle([35, 50, 93, 78], fill=text_bg)
    
    # Simple text representation (using rectangles as letters)
    text_color = 'black'
    # S
    draw.rectangle([40, 55, 44, 60], fill=text_color)
    draw.rectangle([40, 60, 44, 62], fill=text_color)
    draw.rectangle([40, 63, 44, 65], fill=text_color)
    draw.rectangle([40, 66, 44, 68], fill=text_color)
    draw.rectangle([40, 69, 44, 73], fill=text_color)
    
    # H
    draw.rectangle([47, 55, 51, 73], fill=text_color)
    draw.rectangle([52, 62, 54, 64], fill=text_color)
    draw.rectangle([55, 55, 59, 73], fill=text_color)
    
    # I
    draw.rectangle([62, 55, 66, 73], fill=text_color)
    
    # P
    draw.rectangle([69, 55, 73, 73], fill=text_color)
    draw.rectangle([74, 55, 78, 60], fill=text_color)
    draw.rectangle([74, 62, 78, 64], fill=text_color)
    
    # !
    draw.rectangle([84, 55, 88, 68], fill=text_color)
    draw.ellipse([84, 70, 88, 73], fill=text_color)
    
    return img

def create_code_review_emoji():
    """Create a code review emoji - magnifying glass over code"""
    size = 128
    img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # Code background (dark gray)
    code_bg = (52, 58, 64)
    draw.rounded_rectangle([15, 20, 85, 90], radius=5, fill=code_bg)
    
    # Code lines (different colors for syntax highlighting)
    # Line 1 - blue (function)
    draw.rectangle([20, 25, 50, 28], fill=(0, 123, 255))
    # Line 2 - green (comment)
    draw.rectangle([25, 33, 70, 36], fill=(40, 167, 69))
    # Line 3 - white (code)
    draw.rectangle([25, 41, 60, 44], fill='white')
    # Line 4 - orange (string)
    draw.rectangle([25, 49, 65, 52], fill=(255, 193, 7))
    # Line 5 - white (code)
    draw.rectangle([20, 57, 55, 60], fill='white')
    
    # Magnifying glass
    glass_color = (108, 117, 125)  # Gray
    # Glass circle
    draw.ellipse([55, 50, 95, 90], outline=glass_color, width=4)
    # Glass interior (light blue tint)
    draw.ellipse([59, 54, 91, 86], fill=(173, 216, 230, 128))
    # Handle
    draw.line([90, 85, 105, 100], fill=glass_color, width=6)
    
    # Reflection on glass
    draw.arc([62, 57, 75, 70], start=180, end=270, fill='white', width=2)
    
    return img

def create_debugging_emoji():
    """Create a debugging emoji - bug with magnifying glass"""
    size = 128
    img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # Console/terminal background
    terminal_bg = (33, 37, 41)  # Dark gray
    draw.rounded_rectangle([15, 15, 95, 85], radius=5, fill=terminal_bg)
    
    # Terminal header bar
    header_color = (52, 58, 64)
    draw.rectangle([15, 15, 95, 28], fill=header_color)
    
    # Terminal buttons (red, yellow, green)
    draw.ellipse([20, 19, 26, 25], fill=(255, 95, 86))   # Red
    draw.ellipse([30, 19, 36, 25], fill=(255, 189, 46))  # Yellow
    draw.ellipse([40, 19, 46, 25], fill=(39, 201, 63))   # Green
    
    # Debug output lines
    # Error line (red)
    draw.rectangle([20, 35, 25, 37], fill=(255, 95, 86))
    draw.rectangle([28, 35, 55, 37], fill=(255, 95, 86))
    
    # Warning line (yellow)
    draw.rectangle([20, 42, 25, 44], fill=(255, 189, 46))
    draw.rectangle([28, 42, 60, 44], fill=(255, 189, 46))
    
    # Info line (cyan)
    draw.rectangle([20, 49, 25, 51], fill=(0, 255, 255))
    draw.rectangle([28, 49, 50, 51], fill=(0, 255, 255))
    
    # Stack trace (gray)
    draw.rectangle([25, 56, 70, 58], fill=(108, 117, 125))
    draw.rectangle([30, 61, 65, 63], fill=(108, 117, 125))
    draw.rectangle([30, 66, 60, 68], fill=(108, 117, 125))
    
    # Cursor (blinking effect)
    draw.rectangle([72, 73, 76, 78], fill='white')
    
    # Small bug icon in corner
    bug_color = (220, 53, 69)
    draw.ellipse([75, 60, 90, 72], fill=bug_color)
    draw.ellipse([78, 57, 87, 64], fill=(180, 33, 49))
    
    return img

# Main execution
if __name__ == "__main__":
    output_dir = "images/dev-essentials"
    
    # Create done emoji
    done_img = create_done_emoji()
    done_img.save(os.path.join(output_dir, "done.png"))
    print("Created: done.png")
    
    # Create failed emoji
    failed_img = create_failed_emoji()
    failed_img.save(os.path.join(output_dir, "failed.png"))
    print("Created: failed.png")
    
    # Create shipit emoji
    shipit_img = create_shipit_emoji()
    shipit_img.save(os.path.join(output_dir, "shipit.png"))
    print("Created: shipit.png")
    
    # Create code-review emoji
    code_review_img = create_code_review_emoji()
    code_review_img.save(os.path.join(output_dir, "code-review.png"))
    print("Created: code-review.png")
    
    # Create debugging emoji
    debugging_img = create_debugging_emoji()
    debugging_img.save(os.path.join(output_dir, "debugging.png"))
    print("Created: debugging.png")
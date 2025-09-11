#!/usr/bin/env python3

from PIL import Image, ImageDraw, ImageFont
import os

# Food/Drink emojis
FOOD_EMOJIS = [
    # Food expressions
    ("delicious", "맛있다", "#FF6B6B", "맛있다"),
    ("jmt", "JMT", "#FF1744", "존맛탱 (매우 맛있음)"),
    ("jmt_full", "존맛탱", "#E91E63", "존나 맛있는 탱탱"),
    ("eating_alone", "혼밥", "#795548", "혼자 밥먹기"),
    ("drinking_alone", "혼술", "#7B1FA2", "혼자 술마시기"),
    ("chicken_beer", "치맥", "#FFC107", "치킨+맥주"),
    ("soju_beer", "소맥", "#4CAF50", "소주+맥주"),
    ("food_coma", "식곤증", "#9E9E9E", "식사 후 졸림"),
    ("hungry", "배고파", "#FF9800", "배고픔"),
    ("full", "배불러", "#8BC34A", "배부름"),
    ("lets_eat", "먹자", "#2196F3", "먹으러 가자"),
    ("cheers", "건배", "#FF5722", "건배!"),
    
    # Korean food
    ("kimchi", "김치", "#F44336", "김치"),
    ("ramen", "라면", "#FF9800", "라면"),
    ("kbbq", "삼겹살", "#8D6E63", "삼겹살"),
    ("tteokbokki", "떡볶이", "#FF5252", "떡볶이"),
    ("bibimbap", "비빔밥", "#FFC107", "비빔밥"),
    ("soju", "소주", "#4CAF50", "소주"),
    ("makgeolli", "막걸리", "#EEEEEE", "막걸리"),
    ("bulgogi", "불고기", "#6D4C41", "불고기"),
    ("japchae", "잡채", "#9E9E9E", "잡채"),
    ("gimbap", "김밥", "#424242", "김밥"),
    
    # Cafe culture
    ("coffee", "커피", "#6D4C41", "커피"),
    ("iced_americano", "아아", "#795548", "아이스 아메리카노"),
    ("latte", "라떼", "#8D6E63", "라떼"),
    ("bubble_tea", "버블티", "#E91E63", "버블티"),
    ("dessert", "디저트", "#FF80AB", "디저트"),
    ("cake", "케이크", "#FFCDD2", "케이크"),
    ("bread", "빵", "#FFE0B2", "빵"),
    ("snack", "간식", "#FFF9C4", "간식"),
    
    # Delivery/Ordering
    ("delivery", "배달", "#2196F3", "배달 주문"),
    ("takeout", "포장", "#00BCD4", "포장 주문"),
    ("reservation", "예약", "#9C27B0", "예약"),
    ("menu", "메뉴", "#3F51B5", "메뉴판"),
    ("order", "주문", "#00ACC1", "주문하기"),
    ("bill", "계산", "#4CAF50", "계산서"),
    ("split", "더치페이", "#FF9800", "더치페이"),
    ("my_treat", "내가쏨", "#F44336", "내가 낼게"),
    
    # Food moods
    ("craving", "땡긴다", "#FF6F00", "먹고 싶다"),
    ("no_appetite", "입맛없", "#757575", "입맛 없음"),
    ("spicy", "매워", "#F44336", "매운 맛"),
    ("sweet", "달아", "#E91E63", "단 맛"),
    ("salty", "짜", "#03A9F4", "짠 맛"),
    ("bland", "싱거워", "#BDBDBD", "싱거운 맛"),
    ("savory", "고소해", "#8D6E63", "고소한 맛"),
    ("fresh", "신선해", "#4CAF50", "신선함"),
]

def create_simple_text_emoji(text, color, name, output_dir, bg_type="transparent"):
    """Create a simple text emoji with specified background"""
    scale = 4
    size = 128 * scale
    
    # Create image with specified background
    if bg_type == "white":
        img = Image.new('RGBA', (size, size), (255, 255, 255, 255))
    else:  # transparent
        img = Image.new('RGBA', (size, size), (255, 255, 255, 0))
    
    draw = ImageDraw.Draw(img)
    
    # Try to use a good Korean font
    font_paths = [
        "/System/Library/Fonts/AppleSDGothicNeo.ttc",
        "/Library/Fonts/NanumGothic.ttf",
        "/usr/share/fonts/truetype/nanum/NanumGothic.ttf",
    ]
    
    font = None
    # Adjust font size based on text length
    if len(text) <= 2:
        base_size = 48 * scale
    elif len(text) <= 3:
        base_size = 36 * scale
    elif len(text) <= 4:
        base_size = 28 * scale
    elif len(text) <= 5:
        base_size = 24 * scale
    else:
        base_size = 20 * scale
    
    for font_path in font_paths:
        if os.path.exists(font_path):
            try:
                font = ImageFont.truetype(font_path, base_size)
                break
            except:
                continue
    
    if not font:
        font = ImageFont.load_default()
    
    # Get text dimensions
    bbox = draw.textbbox((0, 0), text, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]
    
    # Center the text
    x = (size - text_width) // 2
    y = (size - text_height) // 2 - bbox[1]
    
    # Draw shadow for better visibility (only on transparent bg)
    if bg_type == "transparent":
        shadow_offset = 3 * scale
        draw.text((x + shadow_offset, y + shadow_offset), text, 
                 fill=(0, 0, 0, 100), font=font)
    
    # Draw main text
    draw.text((x, y), text, fill=color, font=font)
    
    # Downscale for anti-aliasing
    img = img.resize((128, 128), Image.Resampling.LANCZOS)
    
    # Save with appropriate suffix
    suffix = "_white" if bg_type == "white" else ""
    filename = f"{name}{suffix}.png"
    filepath = os.path.join(output_dir, filename)
    img.save(filepath, 'PNG')
    print(f"Created: {filename}")
    return filename

def main():
    output_dir = "/Users/rene/asyncsite/slack-emoji-packs/images/korean-words"
    
    print("Creating food/drink emojis...")
    created_files = []
    
    for name, text, color, description in FOOD_EMOJIS:
        # Create transparent background version
        created_files.append(create_simple_text_emoji(text, color, name, output_dir, "transparent"))
        # Create white background version  
        created_files.append(create_simple_text_emoji(text, color, name + "_bg", output_dir, "white"))
    
    print(f"\n✅ Created {len(created_files)} food/drink emojis")
    print("\nCreated files:")
    for f in created_files[:10]:  # Show first 10 as sample
        print(f"  - {f}")
    print(f"  ... and {len(created_files) - 10} more")
    
    return created_files

if __name__ == "__main__":
    main()
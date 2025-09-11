#!/usr/bin/env python3

import os
import json

def update_pack_metadata():
    # Directory containing the emojis
    emoji_dir = "/Users/rene/asyncsite/slack-emoji-packs/images/korean-words"
    pack_json_path = os.path.join(emoji_dir, "pack.json")
    
    # Get all emoji files
    emoji_files = []
    for file in sorted(os.listdir(emoji_dir)):
        if file.endswith(('.png', '.gif')) and not file.startswith('.'):
            emoji_files.append(file)
    
    print(f"Found {len(emoji_files)} emoji files")
    
    # Create pack.json content
    pack_data = {
        "name": "korean-words",
        "title": "한국어 단어 모음 (Korean Words Collection)",
        "description": "한국어 표현, 인터넷 용어, 게임 용어, 사무실 생활, 감정, 음식, SNS 밈, 액션/상태 등 포함한 포괄적인 한국어 이모지 팩 (759개)",
        "emojis": emoji_files,
        "featured": True,
        "preview": [
            "daebak.gif",
            "fighting.gif",
            "ok.png",
            "good.png",
            "gg.png",
            "jmt.png",
            "sparkle_yes.gif",
            "rainbow_fighting.gif"
        ],
        "tags": [
            "korean",
            "한국어",
            "게임",
            "사무실",
            "감정",
            "음식",
            "SNS",
            "밈",
            "인터넷",
            "MZ"
        ],
        "categories": {
            "game_culture": "게임/인터넷 문화",
            "office": "사무실 생활",
            "emotions": "감정 표현",
            "food_drink": "음식/음료",
            "sns_meme": "SNS/밈",
            "action_state": "액션/상태",
            "special_effects": "특수 효과"
        },
        "emoji_count": len(emoji_files)
    }
    
    # Write pack.json
    with open(pack_json_path, 'w', encoding='utf-8') as f:
        json.dump(pack_data, f, ensure_ascii=False, indent=2)
    
    print(f"✅ Updated pack.json with {len(emoji_files)} emojis")
    print(f"📁 Location: {pack_json_path}")
    
    # Show some statistics
    png_count = len([f for f in emoji_files if f.endswith('.png')])
    gif_count = len([f for f in emoji_files if f.endswith('.gif')])
    
    print(f"\n📊 Statistics:")
    print(f"  - PNG files: {png_count}")
    print(f"  - GIF files: {gif_count}")
    print(f"  - Total: {len(emoji_files)}")
    
    # Show sample of new emojis
    print(f"\n🎯 Sample of emojis:")
    samples = ["gg.png", "jmt.png", "developing.png", "sparkle_yes.gif", 
               "rainbow_fighting.gif", "pulse_urgent.gif", "approval_request.png", 
               "honey_jam.png", "tmi.png", "gaza.png"]
    for sample in samples[:10]:
        if sample in emoji_files:
            print(f"  ✓ {sample}")

if __name__ == "__main__":
    update_pack_metadata()
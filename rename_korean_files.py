#!/usr/bin/env python3
"""
Rename Korean filenames to English (romanized)
"""

import os
import shutil
import json

# Mapping of Korean to English filenames
filename_mapping = {
    "굿.png": "good.png",
    "네.png": "ne.png",
    "네_.png": "ne_alt.png",
    "넵.png": "nep.png",
    "넹.png": "neng.png",
    "님아.png": "nimah.png",
    "대빵_동건.png": "daebang_donggeon.png",
    "도큐멘토.png": "documento.png",
    "돈.png": "don.png",
    "ㅇㅎ.png": "oh.png",
    "아니.png": "ani.png",
    "아니_.png": "ani_alt.png",
    "아하.png": "aha.png",
    "어허.png": "eoheo.png",
    "예.png": "ye.png",
    "완료.png": "wanryo.png",
    "일해.png": "ilhae.png",
    "제발요.png": "jebalyo.png",
    "진짜.png": "jinjja.png",
    "최고.png": "choego.png",
    "ㅋㅋㅋ_ㅋㅋㅋ.png": "kkk.png",
    "헐.png": "heol.png",
    "화이팅.png": "hwaiting.png",
    "확인.png": "hwagin.png",
    "확인중.png": "hwagin_jung.png",
    "흠.png": "heum.png",
    "고민중.png": "thinking_hard.png",
    "금지.png": "forbidden.png",
    "나는_감자예요.png": "im_a_potato.png",
    "느좋.png": "feels_good.png",
    "레츠고.png": "lets_go.png",
    "말.png": "speech.png",
    "멋져.png": "cool.png",
    "몰라.png": "dont_know.png",
    "믿습니다.png": "i_believe.png",
    "보는중.png": "watching.png",
    "부탁.png": "request.png",
    "소통해요.png": "lets_talk.png",
    "싫어.png": "dislike.png",
    "안돼.png": "no_way.png",
    "엥.png": "eng.png",
    "오호.png": "oho.png",
    "이건_좀.png": "this_is_a_bit.png",
    "저기요.png": "excuse_me.png",
    "저기요2.png": "excuse_me2.png",
    "좋은데.png": "its_good.png",
    "지금.png": "now.png",
    "ㅋ.png": "k.png",
    "클멘.png": "clmen.png",
    "파이팅.png": "paiting.png",
    "해야하는데.png": "should_do.png",
    "NO.png": "no_en.png",
    "OK.png": "ok_en.png",
}

# Rename files
directory = "images/korean-words"
print("Renaming Korean filenames to English...")

for old_name, new_name in filename_mapping.items():
    old_path = os.path.join(directory, old_name)
    new_path = os.path.join(directory, new_name)
    
    if os.path.exists(old_path):
        shutil.move(old_path, new_path)
        print(f"  {old_name} → {new_name}")

# Update pack.json with new filenames
pack_json_path = os.path.join(directory, "pack.json")
with open(pack_json_path, 'r', encoding='utf-8') as f:
    pack_data = json.load(f)

# Update emojis array
new_emojis = []
for emoji in pack_data.get('emojis', []):
    if emoji in filename_mapping:
        new_emojis.append(filename_mapping[emoji])
    else:
        new_emojis.append(emoji)  # Keep GIF files as is

pack_data['emojis'] = sorted(new_emojis)

# Update preview array
new_preview = []
preview_mapping = {
    "네.png": "ne.png",
    "화이팅.png": "hwaiting.png",
    "완료.png": "wanryo.png"
}
for preview in pack_data.get('preview', []):
    if preview in preview_mapping:
        new_preview.append(preview_mapping[preview])
    else:
        new_preview.append(preview)

pack_data['preview'] = new_preview

# Write updated pack.json
with open(pack_json_path, 'w', encoding='utf-8') as f:
    json.dump(pack_data, f, indent=2, ensure_ascii=False)

print(f"\n✅ Renamed {len(filename_mapping)} files to English filenames")
print("✅ Updated pack.json with new filenames")
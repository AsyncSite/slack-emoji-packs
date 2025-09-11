# 🎯 Slack Emoji Pack 기여 가이드

## ⚠️ **중요: 이 가이드를 반드시 읽고 따라주세요**
가이드를 따르지 않으면 PR이 자동으로 거절됩니다.

---

## 📁 **필수 디렉토리 구조**

```
slack-emoji-packs/
├── images/                    # ✅ 모든 이모지 팩은 여기에
│   └── your-pack-name/       # ✅ 팩 이름 (영문, 소문자, 하이픈만)
│       ├── pack.json         # ✅ 필수 메타데이터 파일
│       ├── emoji1.png        # ✅ 이모지 이미지들
│       ├── emoji2.gif        # ✅ GIF 애니메이션 가능
│       └── ...
├── packs.json                # ❌ 직접 수정 금지 (자동 생성됨)
└── packs/                    # ❌ 사용하지 마세요! (잘못된 위치)
```

### ❌ **자주 하는 실수**
- ~~`/packs/` 디렉토리 사용~~ → `/images/` 사용하세요
- ~~한글 파일명~~ → 영문만 사용하세요
- ~~pack.json 없이 제출~~ → 반드시 포함하세요

---

## 📝 **pack.json 형식 (필수)**

```json
{
  "id": "your-pack-name",
  "name": "Your Pack Display Name",
  "description": "간단한 설명 - 50자 이내",
  "category": "general|developer|culture|workplace|business",
  "author": "Your Name",
  "tags": ["tag1", "tag2", "tag3"],
  "featured": false,
  "preview": [
    "best-emoji1.gif",
    "best-emoji2.png",
    "best-emoji3.png",
    "best-emoji4.gif"
  ],
  "createdAt": "2025-09-11",
  "updatedAt": "2025-09-11"
}
```

### 📌 **필드 설명**
- `id`: 디렉토리명과 동일해야 함 (영문, 소문자, 하이픈만)
- `category`: 위 5개 중 하나만 선택
- `preview`: **정확히 4개**, GIF를 앞에 배치하면 더 좋음
- `featured`: 기본값 false (관리자가 결정)

### ⚠️ **주의사항**
- `emojis` 배열은 자동 생성되므로 직접 추가하지 마세요
- `emojiCount`도 자동 계산되므로 추가하지 마세요

---

## 🖼️ **이미지 파일 규칙**

### ✅ **허용되는 것**
- 형식: PNG, GIF만
- 크기: 128x128px 권장 (최대 256x256px)
- 파일명: 영문, 숫자, 하이픈, 언더스코어만
  - 좋은 예: `thumbs-up.png`, `coding_time.gif`, `happy_cat_2.png`
  - 나쁜 예: `좋아요.png`, `こんにちは.gif`, `hello world.png` (공백)

### ❌ **금지사항**
- 한글/일본어/중국어 등 비ASCII 문자
- 공백 (언더스코어 사용)
- 특수문자 (!@#$%^&* 등)
- 4MB 이상 파일

---

## 🚀 **제출 단계별 가이드**

### 1단계: 팩 디렉토리 생성
```bash
# ✅ 올바른 위치에 생성
mkdir -p images/my-awesome-pack

# ❌ 잘못된 위치
# mkdir packs/my-awesome-pack  # 이렇게 하지 마세요!
```

### 2단계: 이모지 파일 추가
```bash
# 이모지 파일들을 복사
cp my-emojis/*.png images/my-awesome-pack/
cp my-emojis/*.gif images/my-awesome-pack/

# 파일명 확인 (영문만 있는지)
ls images/my-awesome-pack/
```

### 3단계: pack.json 생성
```bash
# pack.json 생성 및 편집
nano images/my-awesome-pack/pack.json
```

### 4단계: preview 이미지 선택
- 가장 대표적인 이모지 4개 선택
- GIF가 있으면 1-2개 포함 (움직임이 눈에 띔)
- 파일명을 정확히 입력 (확장자 포함)

### 5단계: 검증
```bash
# 파일 구조 확인
tree images/my-awesome-pack/

# pack.json 문법 검증
python3 -m json.tool images/my-awesome-pack/pack.json
```

### 6단계: PR 제출
```bash
git add images/my-awesome-pack/
git commit -m "feat: Add my-awesome-pack emoji pack"
git push origin my-branch
```

---

## 🔍 **체크리스트 (PR 제출 전)**

제출 전 이 모든 항목을 확인하세요:

- [ ] `/images/` 디렉토리 아래에 팩을 만들었습니다
- [ ] 팩 이름은 영문 소문자와 하이픈만 사용했습니다
- [ ] 모든 이미지 파일명이 영문입니다
- [ ] pack.json을 올바르게 작성했습니다
- [ ] preview 배열에 정확히 4개 파일을 지정했습니다
- [ ] preview에 지정한 파일이 실제로 존재합니다
- [ ] 이미지 크기가 적절합니다 (128x128 권장)
- [ ] GIF 파일 크기가 4MB 미만입니다

---

## ❓ **자주 묻는 질문**

**Q: packs.json을 직접 수정해야 하나요?**
A: 아니요! 자동으로 생성됩니다. 절대 수정하지 마세요.

**Q: emojis 배열을 pack.json에 추가해야 하나요?**
A: 아니요! 자동으로 생성됩니다.

**Q: 한글 파일명을 꼭 영문으로 바꿔야 하나요?**
A: 네! Slack API와 호환성 문제가 있습니다. 반드시 영문을 사용하세요.

**Q: 왜 /packs/ 대신 /images/를 사용하나요?**
A: 프론트엔드가 /images/ 경로를 사용합니다. /packs/는 사용하지 않습니다.

**Q: featured를 true로 설정해도 되나요?**
A: 기본값은 false입니다. 관리자가 검토 후 결정합니다.

---

## 🚨 **문제 해결**

### "pack.json not found" 에러
→ `/images/your-pack/pack.json` 경로가 맞는지 확인

### "Invalid filename" 에러  
→ 파일명에 한글이나 특수문자가 있는지 확인

### "Preview image not found" 에러
→ preview 배열의 파일명이 실제 파일과 일치하는지 확인 (대소문자 포함)

### 이미지가 깨져 보임
→ 이미지 크기를 128x128로 조정해보세요

---

## 💡 **팁**

1. **GIF 우선 배치**: preview 배열에서 GIF를 앞에 놓으면 더 눈에 띕니다
2. **일관된 스타일**: 한 팩 내의 이모지들은 비슷한 스타일로 통일하세요
3. **명확한 네이밍**: `thumbs_up.png`이 `tu.png`보다 이해하기 쉽습니다
4. **적절한 크기**: 128x128이 Slack에서 가장 잘 보입니다

---

## 📞 **도움이 필요하면**

이슈를 생성하세요: [GitHub Issues](https://github.com/AsyncSite/slack-emoji-packs/issues)

**이슈 생성 시 포함할 정보:**
- 어떤 단계에서 문제가 발생했는지
- 에러 메시지 전체
- 디렉토리 구조 스크린샷

---

감사합니다! 여러분의 기여로 Slack이 더 재미있어집니다 🎉
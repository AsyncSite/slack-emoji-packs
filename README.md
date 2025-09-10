# Slack Emoji Packs 🎯

A curated collection of emoji packs for SlackDori - One-click Slack emoji installation service.

## 📁 Repository Structure

```
/
├── packs.json          # Main index of all emoji packs
├── packs/              # Individual pack data
│   ├── dev-essentials/ # Developer essentials pack
│   ├── korean-culture/ # Korean culture pack
│   └── ...
└── images/             # Emoji image files
    ├── dev-essentials/
    ├── korean-culture/
    └── ...
```

## 📊 Data Format

### packs.json
```json
{
  "packs": [
    {
      "id": "dev-essentials",
      "name": "Developer Essentials",
      "description": "Must-have emojis for developers",
      "category": "developer",
      "emojiCount": 30,
      "author": "AsyncSite",
      "tags": ["coding", "programming", "tech"],
      "preview": ["shipit", "bug", "fire", "rocket"]
    }
  ]
}
```

### Individual Pack Format (packs/[id]/pack.json)
```json
{
  "id": "dev-essentials",
  "name": "Developer Essentials",
  "emojis": [
    {
      "name": "shipit",
      "aliases": ["deploy", "ship"],
      "imageUrl": "/images/dev-essentials/shipit.png"
    }
  ]
}
```

## 🤝 Contributing

### Adding a New Emoji Pack

1. Create a new directory in `packs/` with your pack ID
2. Add `pack.json` with emoji definitions
3. Add images to `images/[pack-id]/`
4. Update `packs.json` with pack metadata
5. Submit a Pull Request

### Image Guidelines

- Format: PNG (transparent background preferred)
- Size: 128x128px recommended
- File size: < 100KB per image
- Naming: lowercase, no spaces (use hyphens)

## 📜 License

All emojis in this repository are either:
- Created by AsyncSite team
- Open source with proper attribution
- Public domain

## 🔗 Links

- [SlackDori Frontend](https://github.com/AsyncSite/slackdori-frontend)
- [SlackDori Website](https://slackdori.asyncsite.com)

---

*For commercial use or custom emoji packs, please contact team@asyncsite.com*
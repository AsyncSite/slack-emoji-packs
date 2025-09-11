# Contributing to Slack Emoji Packs

Thank you for your interest in contributing to our Slack emoji pack collection! We welcome contributions from the community.

## 🎯 Quick Start

1. Fork this repository
2. Add your emoji files to `images/[pack-name]/`
3. Run validation: `python scripts/validate_pack.py`
4. Submit a Pull Request

## 📋 Contribution Guidelines

### Emoji Standards

All emojis must meet these requirements:

| Requirement | Specification |
|------------|--------------|
| **Format** | PNG or GIF only |
| **Size** | 128x128 pixels (recommended) |
| **Max file size** | 100KB |
| **Filename** | Lowercase, numbers, hyphens, underscores only |
| **Transparency** | PNG with RGBA recommended |

### Adding a New Emoji Pack

1. **Create a new directory** under `images/`:
   ```bash
   mkdir images/your-pack-name
   ```

2. **Add your emoji files** following the standards above

3. **Create a `pack.json`** file in your pack directory:
   ```json
   {
     "name": "Your Pack Name",
     "description": "Description of your emoji pack",
     "category": "general|developer|culture|business|workplace",
     "author": "Your Name",
     "tags": ["tag1", "tag2", "tag3"]
   }
   ```

4. **Validate your pack locally**:
   ```bash
   pip install Pillow
   python scripts/validate_pack.py
   ```

### Adding Emojis to Existing Pack

1. Add your emoji files to the appropriate pack directory
2. Follow the naming and format standards
3. Run validation before submitting

## 🔄 Pull Request Process

1. **Fork & Clone**
   ```bash
   git clone https://github.com/YOUR-USERNAME/slack-emoji-packs.git
   cd slack-emoji-packs
   ```

2. **Create a feature branch**
   ```bash
   git checkout -b add-awesome-emojis
   ```

3. **Add your emojis and commit**
   ```bash
   git add images/
   git commit -m "Add [pack-name] emoji pack with X emojis"
   ```

4. **Push and create PR**
   ```bash
   git push origin add-awesome-emojis
   ```

5. **Wait for automated validation**
   - Our GitHub Actions will automatically validate your emojis
   - Check the PR comments for validation results
   - Fix any issues reported

## ✅ Validation Checks

Our automated system checks for:

- ✅ Valid file formats (PNG/GIF)
- ✅ Appropriate file sizes (<100KB)
- ✅ Correct image dimensions
- ✅ Proper filename formatting
- ✅ Pack metadata completeness

## 🏷️ Categories

Choose the most appropriate category for your pack:

- **general** - General purpose emojis
- **developer** - Programming and tech related
- **culture** - Cultural and regional emojis
- **business** - Business and workplace
- **workplace** - Office and remote work

## 📝 Pack Metadata Schema

Each pack can have a `pack.json` file with this structure:

```json
{
  "name": "Pack Display Name",
  "description": "What this pack contains",
  "category": "category-name",
  "author": "Author Name",
  "tags": ["array", "of", "tags"],
  "featured": false,
  "url": "https://optional-link.com"
}
```

## 🤝 Code of Conduct

- Be respectful and inclusive
- No offensive or inappropriate content
- Respect copyright - only submit emojis you have rights to share
- Keep emojis family-friendly

## 📜 License

By contributing, you agree that your contributions will be licensed under the same license as this project (MIT).

## 💡 Tips for Great Emojis

1. **Keep it simple** - Emojis are small, so simple designs work best
2. **Use transparency** - PNG with transparent backgrounds are versatile
3. **Consider animations** - Animated GIFs add fun, but keep file size small
4. **Test at small sizes** - Make sure your emoji is recognizable at 32x32
5. **Be creative** - Unique emojis that express specific emotions or situations are most valuable

## 🐛 Reporting Issues

Found a problem? Please [open an issue](https://github.com/AsyncSite/slack-emoji-packs/issues) with:
- Description of the problem
- Steps to reproduce
- Expected vs actual behavior

## 📮 Questions?

If you have questions about contributing, feel free to:
- Open a [discussion](https://github.com/AsyncSite/slack-emoji-packs/discussions)
- Check existing issues and PRs

---

Thank you for helping make our emoji collection awesome! 🎉
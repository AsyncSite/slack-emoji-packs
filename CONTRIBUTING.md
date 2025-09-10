# Contributing to Slack Emoji Packs

Thank you for your interest in contributing to our Slack emoji pack collection!

## How to Contribute

### Adding a New Emoji to an Existing Pack

1. Fork this repository
2. Add your emoji image to `images/[pack-id]/`
3. Update the pack's `pack.json` file with emoji metadata
4. Submit a Pull Request

### Creating a New Emoji Pack

1. Fork this repository
2. Create a new directory in `packs/` with your pack ID
3. Add `pack.json` with emoji definitions:
   ```json
   {
     "id": "your-pack-id",
     "name": "Your Pack Name",
     "description": "Pack description",
     "version": "1.0.0",
     "emojis": [
       {
         "name": "emoji-name",
         "aliases": ["alt1", "alt2"],
         "imageUrl": "/images/your-pack-id/emoji-name.png",
         "unicode": "😀"
       }
     ]
   }
   ```
4. Add emoji images to `images/[your-pack-id]/`
5. Update `packs.json` with your pack metadata
6. Submit a Pull Request

## Image Guidelines

- **Format**: PNG with transparent background
- **Size**: 128x128px recommended
- **File size**: < 100KB per image
- **Naming**: lowercase, use hyphens (no spaces)

## Quality Standards

- Emojis should be clear and recognizable at small sizes
- No offensive or inappropriate content
- Respect copyright and licensing
- Original work or properly licensed content only

## Testing Your Changes

1. Ensure all JSON files are valid
2. Verify image paths are correct
3. Test that images display properly
4. Check file sizes are within limits

## Pull Request Process

1. Describe what you're adding/changing
2. Include screenshots of new emojis
3. Mention any licensing information
4. Wait for review and feedback

## Code of Conduct

- Be respectful and inclusive
- Welcome feedback and suggestions
- Help others when you can
- Keep discussions professional

## Questions?

Open an issue if you have questions or need help!

## License

By contributing, you agree that your contributions will be licensed under the same license as this project (MIT).
#!/usr/bin/env python3
"""
Validate emoji pack files for quality and standards.
"""

import sys
import os
import re
import json
from pathlib import Path
from PIL import Image
from typing import List, Dict, Tuple

# Validation rules
MAX_FILE_SIZE_KB = 100
RECOMMENDED_SIZE = (128, 128)
MAX_SIZE = (256, 256)
ALLOWED_FORMATS = {'.png', '.gif'}
FILENAME_PATTERN = re.compile(r'^[a-z0-9_-]+$')

class EmojiValidator:
    def __init__(self):
        self.errors = []
        self.warnings = []
        self.info = []
        
    def validate_files(self, file_paths: List[str]) -> bool:
        """Validate a list of emoji files."""
        for file_path in file_paths:
            if not os.path.exists(file_path):
                continue
            
            path = Path(file_path)
            
            # Skip non-image files
            if path.suffix.lower() not in ALLOWED_FORMATS:
                if path.name not in ['pack.json', '.gitkeep']:
                    self.errors.append(f"❌ {file_path}: Invalid file format (only PNG and GIF allowed)")
                continue
            
            self.validate_single_file(path)
        
        return len(self.errors) == 0
    
    def validate_single_file(self, path: Path):
        """Validate a single emoji file."""
        file_path = str(path)
        
        # Check filename
        name_without_ext = path.stem
        if not FILENAME_PATTERN.match(name_without_ext):
            self.errors.append(
                f"❌ {path.name}: Invalid filename. Use only lowercase letters, numbers, hyphens and underscores"
            )
        
        # Check file size
        file_size_kb = path.stat().st_size / 1024
        if file_size_kb > MAX_FILE_SIZE_KB:
            self.errors.append(
                f"❌ {path.name}: File too large ({file_size_kb:.1f}KB > {MAX_FILE_SIZE_KB}KB)"
            )
        elif file_size_kb > MAX_FILE_SIZE_KB * 0.8:
            self.warnings.append(
                f"⚠️ {path.name}: File size is large ({file_size_kb:.1f}KB)"
            )
        
        # Check image dimensions
        try:
            with Image.open(path) as img:
                width, height = img.size
                
                # Check if square
                if width != height:
                    self.warnings.append(
                        f"⚠️ {path.name}: Image is not square ({width}x{height})"
                    )
                
                # Check size
                if width > MAX_SIZE[0] or height > MAX_SIZE[1]:
                    self.errors.append(
                        f"❌ {path.name}: Image too large ({width}x{height} > {MAX_SIZE[0]}x{MAX_SIZE[1]})"
                    )
                elif (width, height) != RECOMMENDED_SIZE:
                    self.warnings.append(
                        f"⚠️ {path.name}: Non-standard size ({width}x{height}, recommended {RECOMMENDED_SIZE[0]}x{RECOMMENDED_SIZE[1]})"
                    )
                
                # Check format details
                if path.suffix.lower() == '.png':
                    if img.mode not in ['RGBA', 'RGB']:
                        self.warnings.append(
                            f"⚠️ {path.name}: PNG mode is {img.mode} (RGBA recommended for transparency)"
                        )
                
                # For GIFs, check if animated
                if path.suffix.lower() == '.gif':
                    try:
                        img.seek(1)
                        self.info.append(f"ℹ️ {path.name}: Animated GIF detected")
                    except EOFError:
                        self.info.append(f"ℹ️ {path.name}: Static GIF (consider converting to PNG)")
                        
        except Exception as e:
            self.errors.append(f"❌ {path.name}: Failed to open image ({str(e)})")
    
    def check_pack_structure(self, file_paths: List[str]):
        """Check if pack structure is valid."""
        packs = set()
        for file_path in file_paths:
            if 'images/' in file_path:
                parts = file_path.split('/')
                if len(parts) >= 3:
                    pack_name = parts[parts.index('images') + 1]
                    packs.add(pack_name)
        
        for pack in packs:
            pack_dir = Path('images') / pack
            
            # Check for pack.json
            pack_json_path = pack_dir / 'pack.json'
            if pack_json_path.exists():
                try:
                    with open(pack_json_path, 'r') as f:
                        pack_data = json.load(f)
                    
                    # Validate pack.json structure
                    required_fields = ['name', 'description', 'category']
                    for field in required_fields:
                        if field not in pack_data:
                            self.warnings.append(
                                f"⚠️ {pack}/pack.json: Missing required field '{field}'"
                            )
                except json.JSONDecodeError:
                    self.errors.append(f"❌ {pack}/pack.json: Invalid JSON format")
            else:
                self.info.append(
                    f"ℹ️ {pack}: No pack.json found (will use defaults from packs.json)"
                )
    
    def generate_report(self) -> str:
        """Generate a markdown report of validation results."""
        report = []
        
        if not self.errors and not self.warnings:
            report.append("✅ **All validations passed!**\n")
            report.append("Your emoji pack meets all quality standards. Great job! 🎉")
        else:
            if self.errors:
                report.append("### ❌ Errors (must fix)\n")
                for error in self.errors:
                    report.append(f"- {error}")
                report.append("")
            
            if self.warnings:
                report.append("### ⚠️ Warnings (recommended fixes)\n")
                for warning in self.warnings:
                    report.append(f"- {warning}")
                report.append("")
        
        if self.info:
            report.append("### ℹ️ Information\n")
            for info in self.info:
                report.append(f"- {info}")
        
        # Add guidelines
        report.append("\n---")
        report.append("📚 **Emoji Guidelines:**")
        report.append(f"- File format: PNG or GIF")
        report.append(f"- Recommended size: {RECOMMENDED_SIZE[0]}x{RECOMMENDED_SIZE[1]} pixels")
        report.append(f"- Max file size: {MAX_FILE_SIZE_KB}KB")
        report.append(f"- Filename: lowercase, numbers, hyphens and underscores only")
        
        return "\n".join(report)

def main():
    # Get file paths from command line arguments
    file_paths = sys.argv[1:] if len(sys.argv) > 1 else []
    
    if not file_paths:
        # If no files specified, validate all
        file_paths = []
        for pack_dir in Path('images').iterdir():
            if pack_dir.is_dir():
                for file in pack_dir.iterdir():
                    if file.suffix.lower() in ALLOWED_FORMATS:
                        file_paths.append(str(file))
    
    validator = EmojiValidator()
    
    # Validate files
    is_valid = validator.validate_files(file_paths)
    
    # Check pack structure
    validator.check_pack_structure(file_paths)
    
    # Generate report
    report = validator.generate_report()
    
    # Write report to file for GitHub Actions
    with open('validation_report.md', 'w') as f:
        f.write(report)
    
    # Print report to console
    print(report)
    
    # Exit with appropriate code
    sys.exit(0 if is_valid else 1)

if __name__ == "__main__":
    main()
#!/usr/bin/env python3
"""
Insert kit catalog section into README.md

This script replaces the Kit Catalog section in README.md with the content
from kit_catalog_section.md, preserving the rest of the file.

Usage:
    python scripts/insert_catalog_into_readme.py
"""

from pathlib import Path
import re


def insert_catalog_section(readme_path: Path, catalog_section_path: Path) -> bool:
    """
    Replace the Kit Catalog section in README.md with content from catalog_section_path.
    
    Args:
        readme_path: Path to README.md
        catalog_section_path: Path to kit_catalog_section.md
        
    Returns:
        True if successful, False otherwise
    """
    # Read the catalog section
    with open(catalog_section_path, 'r', encoding='utf-8') as f:
        catalog_content = f.read().strip()
    
    # Read the README
    with open(readme_path, 'r', encoding='utf-8') as f:
        readme_content = f.read()
    
    # Define the pattern to match the Kit Catalog section
    # Match from "## Kit Catalog" to the next "---" or "##" (whichever comes first)
    pattern = r'(---\s*\n\s*)## Kit Catalog.*?(?=\n---|\n## |\Z)'
    
    # Create the replacement (preserve the leading ---)
    replacement = r'\1' + catalog_content + '\n\n'
    
    # Perform the replacement
    new_content, count = re.subn(pattern, replacement, readme_content, flags=re.DOTALL)
    
    if count == 0:
        print("Warning: Kit Catalog section not found in README.md")
        return False
    
    # Write back to README
    with open(readme_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print(f"✓ Successfully updated Kit Catalog section in {readme_path}")
    return True


def main():
    """Main execution function."""
    script_dir = Path(__file__).parent
    repo_root = script_dir.parent
    
    readme_path = repo_root / 'README.md'
    catalog_section_path = repo_root / 'kits' / 'kit_catalog_section.md'
    
    # Verify files exist
    if not readme_path.exists():
        print(f"Error: {readme_path} not found")
        return 1
    
    if not catalog_section_path.exists():
        print(f"Error: {catalog_section_path} not found")
        print("Run generate_kit_catalog.py first to create the catalog section")
        return 1
    
    # Insert the catalog section
    success = insert_catalog_section(readme_path, catalog_section_path)
    
    return 0 if success else 1


if __name__ == '__main__':
    exit(main())

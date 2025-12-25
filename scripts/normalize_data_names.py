#!/usr/bin/env python3
"""
Normalize data filenames and folder names from Hebrew to English.

This script:
1. Finds the Hebrew-named folders under data/
2. Renames all files in 'תשובות טובות' to good_001, good_002, etc.
3. Renames all files in 'תשובות פחות טובות' to bad_001, bad_002, etc.
4. Renames folders to 'good_answers' and 'bad_answers'

Usage:
    python scripts/normalize_data_names.py
"""

import os
from pathlib import Path


def normalize_filenames():
    """Rename all files in Hebrew-named folders to consistent English names."""
    
    # Define the data root
    data_root = Path("data")
    
    if not data_root.exists():
        print("❌ Error: data/ folder not found.")
        print("   Create it and add your training data first.")
        return
    
    # Hebrew folder names, their English prefixes, and new folder names
    folder_mapping = {
        "תשובות טובות": {"prefix": "good", "new_name": "good_answers"},
        "תשובות פחות טובות": {"prefix": "bad", "new_name": "bad_answers"},
    }
    
    total_renamed = 0
    folders_renamed = []
    
    for hebrew_name, config in folder_mapping.items():
        prefix = config["prefix"]
        new_folder_name = config["new_name"]
        folder_path = data_root / hebrew_name
        
        if not folder_path.exists():
            print(f"⚠️  Skipping '{hebrew_name}' (folder not found)")
            continue
        
        # Get all files in the folder (sorted for consistency)
        files = sorted([f for f in folder_path.iterdir() if f.is_file()])
        
        if not files:
            print(f"⚠️  No files found in '{hebrew_name}'")
            continue
        
        print(f"\n📁 Processing '{hebrew_name}' ({len(files)} files)...")
        
        for idx, file_path in enumerate(files, start=1):
            # Keep the original extension
            extension = file_path.suffix
            
            # Create new name: good_001.txt, bad_042.wav, etc.
            new_name = f"{prefix}_{idx:03d}{extension}"
            new_path = folder_path / new_name
            
            # Skip if already correctly named
            if file_path.name == new_name:
                continue
            
            # Rename the file
            file_path.rename(new_path)
            total_renamed += 1
            print(f"   ✓ {file_path.name} → {new_name}")
        
        # Rename the folder itself
        new_folder_path = data_root / new_folder_name
        if folder_path != new_folder_path:
            folder_path.rename(new_folder_path)
            folders_renamed.append(f"{hebrew_name} → {new_folder_name}")
            print(f"   📂 Folder renamed to: {new_folder_name}")
    
    print(f"\n✅ Done! Renamed {total_renamed} files and {len(folders_renamed)} folders.")
    if folders_renamed:
        print("\nFolder changes:")
        for change in folders_renamed:
            print(f"  • {change}")


if __name__ == "__main__":
    normalize_filenames()

# Data Setup Guide

How to add and organize your training data.

## Directory Structure

Create a `data/` folder in the repo root with this structure:

```
data/
├── תשובות טובות/          (your good answer audio files)
└── תשובות פחות טובות/     (your bad answer audio files)
```

## Steps

### 1. Create Data Folder

### 2. Add Your Audio Files

Place your audio files (`.m4a`, `.mp3`, `.wav`, etc.) in the two folders:

- `data/תשובות טובות/` → Good answer recordings
- `data/תשובות פחות טובות/` → Bad answer recordings

### 3. Normalize Filenames

Run the normalization script to rename all files consistently to English:

```powershell
python scripts/normalize_data_names.py
```

This will:

- Rename all files in the folders to: `good_001.m4a`, `good_002.m4a`, etc. and `bad_001.m4a`, `bad_002.m4a`, etc.
- Rename the folders to `good_answers` and `bad_answers`
- Preserve original file extensions

After running, your structure will be:

```
data/
├── good_answers/
│   ├── good_001.m4a
│   ├── good_002.m4a
│   └── ...
└── bad_answers/
    ├── bad_001.m4a
    ├── bad_002.m4a
    └── ...
```

### 4. Generate Transcripts

In the `data_processing.ipynb` notebook, run the Whisper transcription cells to automatically generate transcripts:

```
data/
├── good_answers/          (original audio files)
├── good_answer_transcripts/   (generated text files)
├── bad_answers/           (original audio files)
└── bad_answer_transcripts/    (generated text files)
```

## Notes

- The `data/` folder is git-ignored to avoid committing large audio files
- All file paths are relative, so the notebook can find data from any machine
- Collaborators run the same normalization script to maintain consistent naming

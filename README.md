# customer-support-llm

Fine-tune language models for customer support using Whisper transcription and Hugging Face models.

This project processes audio recordings (good and bad customer support answers), transcribes them using OpenAI's Whisper, and prepares the data for model training.

## Quick Links

- **New to this project?** Start with [Quick Start Guide](docs/QUICKSTART.md)
- **Adding training data?** See [Data Setup Guide](docs/DATA_SETUP.md)
- **Having issues?** Read [Troubleshooting Guide](docs/TROUBLESHOOTING.md)

## What's Inside

```
notebooks/
  └── data_processing.ipynb    # Whisper transcription pipeline
scripts/
  └── normalize_data_names.py  # Rename audio files to consistent format
data/
  ├── good_answers/            # Good customer support recordings
  ├── good_answer_transcripts/ # Generated transcripts
  ├── bad_answers/             # Poor customer support recordings
  └── bad_answer_transcripts/  # Generated transcripts
```

## Key Features

✅ **Automated transcription** - Whisper handles speech-to-text in Hebrew  
✅ **Consistent naming** - Script ensures all collaborators use the same file format  
✅ **Jupyter notebooks** - Interactive data exploration and processing  
✅ **Reproducible setup** - Virtual environment for clean dependency management

## Prerequisites

- Python 3.10+ (3.11 recommended)
- ffmpeg (for audio processing)
- Git

## Get Started

See [Quick Start Guide](docs/QUICKSTART.md) for step-by-step setup instructions.

## Collaboration

This setup is designed for team collaboration:

1. Each collaborator gets their own virtual environment (`.venv` is local, not committed)
2. Run `python scripts/normalize_data_names.py` to ensure consistent file naming across team
3. The `data/` folder is git-ignored; store it locally and pull audio files as needed
4. All code and configuration is version-controlled for reproducibility

## License & Credits

Whisper by OpenAI - [GitHub](https://github.com/openai/whisper)  
Transformers by Hugging Face - [huggingface.co](https://huggingface.co)

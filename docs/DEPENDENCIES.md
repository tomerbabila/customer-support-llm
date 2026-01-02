# Dependencies Guide

Overview of all libraries and their purposes.

## Python & Core

- **Python 3.10+** (3.11 recommended)
  - Language runtime
  - Use 3.11 to avoid compatibility issues with transformers

## Audio Processing

- **openai-whisper** (20231117+)

  - Speech-to-text model by OpenAI
  - Downloads base model (~140MB) on first use
  - Supports 99 languages including Hebrew
  - Models available: tiny, base, small, medium, large

- **soundfile** (0.12.1+)

  - Reads/writes audio files
  - Supports `.wav`, `.flac`, and other formats

- **ffmpeg** (system requirement, not pip)
  - Audio codec library required by Whisper
  - Install with: `winget install "FFmpeg (Essentials Build)"`
  - Must be on system PATH

## Data Processing

- **pandas** (2.1.0+)

  - Data manipulation and analysis
  - Used for creating DataFrames from transcripts

- **numpy** (1.26.0+)
  - Numerical computing
  - Array operations for data processing

## Deep Learning & NLP

- **torch** (2.1.0+)

  - PyTorch deep learning framework
  - Required by Whisper and Transformers
  - CPU version included; GPU version optional

- **transformers** (4.36.0+)

  - Hugging Face library for NLP models
  - Provides AlephBERT (Hebrew BERT) and other models
  - Model downloading and fine-tuning

- **datasets** (2.16.0+)

  - Hugging Face datasets library
  - Loading, processing, and batching data

- **accelerate** (0.27.0+)

  - Distributed training and inference
  - Enables GPU/multi-GPU support
  - Handles mixed precision training

- **scikit-learn**
  - Included for metrics (accuracy, F1, precision, recall)
  - Used in model evaluation

## Jupyter & Notebooks

- **jupyter** (1.0.0+)

  - Interactive notebook environment
  - Web-based interface for running code

- **ipykernel** (6.27.0+)

  - Jupyter kernel for Python
  - Bridges Jupyter and your Python environment
  - Allows `python -m ipykernel install`

- **jupyter_nbextensions_configurator** (0.6.0+)
  - Notebook extensions manager
  - Optional, for advanced notebook features

## System Requirements

### Disk Space

- Python packages: ~2GB
- Whisper base model cache: ~140MB
- Fine-tuned model: ~600MB
- Transcripts: ~10-20% of audio file size
- **Total: 4-5GB recommended**

### Memory

- RAM: 4GB minimum, 8GB recommended
- GPU: Not required; CPU works fine for this dataset size

### Internet

- Required for downloading models on first use
- Whisper model: ~140MB
- AlephBERT model: ~500MB
- Total: ~700MB to download

## Optional: GPU Support

If you have an NVIDIA GPU, Torch will automatically detect and use it.

**To enable CUDA:**

```powershell
# Remove CPU PyTorch
pip uninstall torch

# Install CUDA version
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121
```

Then verify:

```python
import torch
print(torch.cuda.is_available())  # Should print True
```

## Hugging Face Authentication

If using private models, set your Hugging Face token:

```powershell
# In PowerShell
$env:HF_TOKEN = "your_huggingface_token"

# Or create .env file (git-ignored):
# HF_TOKEN=your_huggingface_token
```

Get a token at [huggingface.co/settings/tokens](https://huggingface.co/settings/tokens)

## Version Notes

- **Python 3.9:** Not recommended (typing issues with transformers)
- **transformers 4.36+:** Fixes compatibility issues
- **torch 2.1+:** Better performance and stability
- **Whisper 20231117+:** Latest version with improvements

## Complete Requirements.txt

See [requirements.txt](../requirements.txt) for pinned versions.

## Updating Dependencies

To update all packages:

```powershell
pip install --upgrade -r requirements.txt
```

To update specific package:

```powershell
pip install --upgrade transformers
```

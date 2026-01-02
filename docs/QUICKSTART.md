# Quick Start Guide

Get the environment up and running in few minutes.

## Prerequisites

- **Python 3.11** (3.10+ works, but 3.11 is recommended)
- ffmpeg (see [Troubleshooting](troubleshooting.md) for installation)
- Git
- ~4GB disk space for models

### Verify Python Version

```powershell
python --version
```

Must show `3.10.x` or higher. If you have 3.9 or lower, install Python 3.11 first.

## Setup Steps

### 1. Create Virtual Environment (One-time)

```powershell
python -m venv .venv
```

### 2. Activate Virtual Environment

```powershell
.\.venv\Scripts\Activate
```

Verify: `python --version` should show 3.10+

### 3. Install Dependencies (One-time)

```powershell
python -m pip install --upgrade pip
pip install -r requirements.txt
```

This installs:

- Whisper (speech-to-text)
- Transformers & Datasets (for model fine-tuning)
- PyTorch (deep learning)
- Jupyter (interactive notebooks)

### 4. Register Jupyter Kernel (One-time)

```powershell
python -m ipykernel install --user --name customer-support-llm
```

This allows Jupyter to use your venv automatically.

### 5. Launch Jupyter Notebook

```powershell
jupyter notebook
```

Browser will open to Jupyter. Navigate to the `notebooks/` folder.

## Next Steps

### To Transcribe Audio

1. Add your audio files to `data/good_answers/` and `data/bad_answers/`
2. Run [notebooks/data_processing.ipynb](../notebooks/data_processing.ipynb)
3. See [Data Setup](DATA_SETUP.md) for details

### To Fine-tune a Model

1. Run the transcription notebook first (see above)
2. Run [notebooks/model_finetuning.ipynb](../notebooks/model_finetuning.ipynb)
3. Model will save to `models/customer-support-classifier-final/`

## Kernel Selection

When you open a notebook, select the `customer-support-llm` kernel:

- Click **Kernel** menu → **Change kernel** → **customer-support-llm**

Or when creating a new notebook, it will prompt you to select a kernel.

## Verify Setup

Create a quick test cell:

```python
import whisper
import torch
from transformers import AutoTokenizer

print(f"Python: {torch.__version__}")
print(f"Whisper: {whisper.__version__}")
print(f"CUDA available: {torch.cuda.is_available()}")
print("✅ All imports successful!")
```

If this runs without errors, your setup is complete.

## Troubleshooting

- **FFmpeg not found?** See [Troubleshooting - FFmpeg](troubleshooting.md#ffmpeg-not-found)
- **Kernel not available?** See [Troubleshooting - Jupyter Kernel](troubleshooting.md#jupyter-kernel-not-found)
- **Python version issues?** See [Troubleshooting - Python Version](troubleshooting.md#python-version-compatibility)
- **Import errors?** See [Troubleshooting - Dependencies](troubleshooting.md#import-errors)

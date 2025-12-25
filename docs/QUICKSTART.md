# Quick Start Guide

Get the environment up and running in 5 minutes.

## Prerequisites

- Python 3.10+ (3.11 recommended)
- ffmpeg available on PATH (see [Troubleshooting](TROUBLESHOOTING.md) if you have issues)
- Git

## Setup Steps

### 1. Create Virtual Environment (One-time)

```powershell
python -m venv .venv
```

### 2. Activate Virtual Environment

```powershell
.\.venv\Scripts\Activate
```

### 3. Install Dependencies (One-time)

```powershell
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### 4. Register Kernel with Jupyter (One-time)

This allows Jupyter to use your virtual environment:

```powershell
python -m ipykernel install --user --name customer-support-llm
```

### 5. Launch Jupyter Notebook

```powershell
jupyter notebook
```

The notebook interface will open in your browser. Navigate to `notebooks/data_processing.ipynb` to start working.

## Next Steps

- See [Data Setup](DATA_SETUP.md) to add your training data
- See [Troubleshooting](TROUBLESHOOTING.md) if you run into issues

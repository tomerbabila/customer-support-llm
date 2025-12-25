# Troubleshooting Guide

Common issues and solutions.

## FFmpeg Not Found

### Symptom

```
❌ Error processing bad_005.m4a: [WinError 2] The system cannot find the file specified
```

This happens when Whisper can't find ffmpeg, even though it's installed.

### Solution

1. **Close VS Code completely** (not just the terminal)
2. **Reopen VS Code**
3. **Open a new integrated terminal** (Terminal → New Terminal)
4. Try the ffmpeg check in the notebook again

### Why This Works

Windows doesn't update the PATH environment variable for running applications until you restart them. Restarting VS Code forces it to reload the system PATH.

### If Still Not Found

Verify ffmpeg is installed:

```powershell
where ffmpeg
```

If this returns nothing, install it:

```powershell
winget install "FFmpeg (Essentials Build)"
```

Then close and reopen VS Code.

### Alternative: Restart Your Computer

If closing VS Code doesn't work, restart your computer to refresh all environment variables system-wide.

## Jupyter Kernel Not Found

### Symptom

Notebook shows "kernel not found" when you try to select the `customer-support-llm` kernel.

### Solution

Register the kernel again:

```powershell
# Make sure your .venv is activated
.\.venv\Scripts\Activate

# Register the kernel
python -m ipykernel install --user --name customer-support-llm
```

Then restart the Jupyter server or refresh your browser tab.

## Audio File Errors

### Symptom

```
❌ Error processing good_001.m4a: [Errno -5] Input/output error
```

### Causes & Solutions

1. **Corrupted audio file** - Try re-exporting from your source
2. **Unsupported codec** - Whisper supports most formats but some edge cases fail
3. **Very large files** - Whisper may struggle with files >1GB; consider splitting them
4. **Permissions issue** - Make sure you have read access to the file

## Model Download Hangs

### Symptom

The notebook seems to hang when loading the Whisper model.

### Solution

1. Check your internet connection
2. The first download can take several minutes (base model is ~140MB)
3. Once downloaded, subsequent runs use the cached version
4. Models are stored in: `~/.cache/huggingface/`

## Out of Memory Error

### Symptom

```
RuntimeError: CUDA out of memory
```

### Solution

Use a smaller Whisper model. In the notebook, change:

```python
model = whisper.load_model("base")  # or "tiny", "small"
```

Try "tiny" or "small" models for lower memory usage.

## Still Having Issues?

1. Check that your venv is activated: `python -m site`
2. Verify all dependencies installed: `pip list | grep whisper`
3. Check Python version: `python --version` (should be 3.10+)
4. Review the full error message for clues

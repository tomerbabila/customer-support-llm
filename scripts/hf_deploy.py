import os
from pathlib import Path
from huggingface_hub import HfApi

# ---- EDIT THESE 2 LINES ----
REPO_ID = "tomerbabila/customer-support-model"  # your HF username / repo name
MODEL_FOLDER = Path(r"models/customer-support-classifier-final")  # <- your trained folder
# ----------------------------

def main():
    if not MODEL_FOLDER.exists():
        raise FileNotFoundError(f"MODEL_FOLDER not found: {MODEL_FOLDER.resolve()}")

    # Optional: set token via env var to avoid interactive login:
    #   setx HF_TOKEN "hf_..."
    # Then restart terminal.
    token = os.getenv("HF_TOKEN") or os.getenv("HUGGINGFACE_TOKEN")

    api = HfApi(token=token)

    # Create repo if missing
    api.create_repo(repo_id=REPO_ID, repo_type="model", exist_ok=True)

    # Upload folder (skip common junk)
    api.upload_folder(
        folder_path=str(MODEL_FOLDER),
        repo_id=REPO_ID,
        repo_type="model",
        ignore_patterns=[
            "**/.git/**",
            "**/.venv/**",
            "**/venv/**",
            "**/__pycache__/**",
            "**/*.ipynb",
            "**/.DS_Store",
        ],
    )

    print(f"✅ Upload complete: https://huggingface.co/{REPO_ID}")

if __name__ == "__main__":
    main()

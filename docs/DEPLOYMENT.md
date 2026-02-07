# Model Deployment Guide

Deploy your fine-tuned model to Hugging Face Hub to share it publicly.

## 1. Install & Setup

Install the Hugging Face hub library:

```bash
pip install huggingface-hub
```

Authenticate with your account:

```bash
huggingface-cli login
```

## 2. Configure the Deployment Script

Edit `scripts/hf_deploy.py` and set your repository:

```python
REPO_ID = "your-username/your-repo-name"
MODEL_FOLDER = Path(r"models/customer-support-classifier-final")
```

## 3. Patch labels (required)

Ensure the model config has the correct `id2label` and `label2id` mapping:

```bash
python scripts/patch_labels.py
```

This updates [models/customer-support-classifier-final/config.json](models/customer-support-classifier-final/config.json).

## 4. Deploy

Run the deployment script:

```bash
python scripts/hf_deploy.py
```

This uploads your model to Hugging Face Hub automatically.

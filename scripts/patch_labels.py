from transformers import AutoConfig

MODEL_PATH = "models/customer-support-classifier-final"

config = AutoConfig.from_pretrained(MODEL_PATH)

config.id2label = {
    0: "bad",
    1: "good",
}

config.label2id = {
    "bad": 0,
    "good": 1,
}

config.save_pretrained(MODEL_PATH)
print("✅ Labels saved to config.json")

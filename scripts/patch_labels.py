from transformers import AutoConfig

MODEL_PATH = "models/customer-support-classifier-final"

config = AutoConfig.from_pretrained(MODEL_PATH)

config.id2label = {
    0: "bad_response",
    1: "good_response",
}

config.label2id = {
    "bad_response": 0,
    "good_response": 1,
}

config.save_pretrained(MODEL_PATH)
print("✅ Labels saved to config.json")

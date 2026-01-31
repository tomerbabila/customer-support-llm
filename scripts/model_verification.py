from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

PATH = r"models/customer-support-classifier-final"

tokenizer = AutoTokenizer.from_pretrained(PATH)
model = AutoModelForSequenceClassification.from_pretrained(PATH)

text = "The agent was helpful and solved my issue quickly."
inputs = tokenizer(text, return_tensors="pt", truncation=True)

with torch.no_grad():
    logits = model(**inputs).logits
pred = logits.argmax(dim=-1).item()

print("pred class id:", pred)
print("logits:", logits)

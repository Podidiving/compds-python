import requests
import torch
from PIL import Image
from transformers import AutoImageProcessor, ResNetForImageClassification

# dataset = load_dataset("huggingface/cats-image")
# image = dataset["test"]["image"][0]
url = "https://images.rawpixel.com/image_800/cHJpdmF0ZS9sci9pbWFnZXMvd2Vic2l0ZS8yMDIzLTA4L3Jhd3BpeGVsX29mZmljZV8yNF9pbGx1c3RyYXRpb25fb2ZfYV9sYWJyYWRvcl9mdWxsX2JvZHlfc2l0dGluZ19kN2E1NjhkMS01MTBjLTRjMjktYTRmNS04YzExYTNlYmJkOTZfMS5qcGc.jpg"
image = Image.open(requests.get(url, stream=True).raw)

print("LOADING MODEL")
processor = AutoImageProcessor.from_pretrained("microsoft/resnet-50")
model = ResNetForImageClassification.from_pretrained("microsoft/resnet-50")
print("MODEL LOADED")

print("INFERENCE")
inputs = processor(image, return_tensors="pt")

with torch.no_grad():
    logits = model(**inputs).logits

# model predicts one of the 1000 ImageNet classes
predicted_label = logits.argmax(-1).item()
print(model.config.id2label[predicted_label])

import os
from io import BytesIO

import telebot
import torch
from dotenv import load_dotenv
from PIL import Image
from transformers import (
    AutoImageProcessor,
    ResNetForImageClassification,
    pipeline,
)

load_dotenv()

API_TOKEN = os.environ.get("API_TOKEN")
if API_TOKEN is None:
    raise ValueError("API_TOKEN is not set")
bot = telebot.TeleBot(API_TOKEN)


def initialize_model():
    torch_device = torch.device("cpu")
    if torch.cuda.is_available():
        torch_device = torch.device("cuda")
    if torch.backends.mps.is_available():
        torch_device = torch.device("mps")
    classifier = pipeline(
        task="text-classification",
        model="SamLowe/roberta-base-go_emotions",
        top_k=None,
        device=torch_device,
    )
    return classifier


classifier = initialize_model()


def initialize_image_classifier():
    processor = AutoImageProcessor.from_pretrained("microsoft/resnet-50")
    model = ResNetForImageClassification.from_pretrained(
        "microsoft/resnet-50"
    )
    return processor, model


image_processor, image_model = initialize_image_classifier()


# Handle '/start' and '/help'
@bot.message_handler(commands=["help", "start"])
def send_welcome(message):
    bot.reply_to(message, "Hi there, I am SentimentAnalysisBot.")


# Handle all other messages with content_type 'text' (content_types defaults to ['text'])
@bot.message_handler(func=lambda message: True)
def echo_message(message):
    output = classifier([message.text])
    bot.reply_to(
        message,
        f"sentiment is {output[0][0]['label']} with score {output[0][0]['score']}",
    )


@bot.message_handler(content_types=["photo"])
def photo(message):
    fileID = message.photo[-1].file_id
    file_info = bot.get_file(fileID)
    downloaded_file = bot.download_file(file_info.file_path)

    with BytesIO() as new_file:
        new_file.write(downloaded_file)
        new_file.seek(0)
        inputs = image_processor(Image.open(new_file), return_tensors="pt")

    with torch.no_grad():
        logits = image_model(**inputs).logits
    predicted_label = logits.argmax(-1).item()
    bot.reply_to(
        message,
        image_model.config.id2label[predicted_label],
    )


bot.infinity_polling()

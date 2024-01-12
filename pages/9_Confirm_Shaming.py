import streamlit as st
# import easyocr
import openai
import requests

openai.api_key = "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"


def detect_confirm_shaming(text):
    prompt = f"Analyze the following text for confirm shaming patterns:\n\n{text}\n\nIs there confirm shaming present? If yes, list the phrases that indicate confirm shaming."

    response = openai.Completion.create(
        model="gpt-3.5-turbo-instruct",
        prompt=f"{prompt}",
        max_tokens=150
    )
    return response.choices[0].text.strip()


# def get_text(image_path):
#     reader = easyocr.Reader(['en'])
#     result = reader.readtext(image_path)
#     text = " ".join([item[1] for item in result])
#     return text


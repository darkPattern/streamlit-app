import streamlit as st
import os
from DarkPatterns.utils.helper_functions import get_text_bboxes, get_pred_img, get_text_bboxes
from DarkPatterns.utils.another_helper import get_only_text_bboxes
from ultralytics import YOLO
from DarkPatterns.basket_sneaking import give_text_highest_price
from config import ANYSCALE_API
import openai
import cv2
import pytesseract

SAVE_DIR = "predictions"

st.set_page_config(page_title="Dark Pattern Detector", page_icon=":eyes:", layout="wide")

st.title("This is the bounding box detector page")
st.subheader("Upload an image to detect bounding boxes in it")

input_image = st.file_uploader("Upload Image", type=['jpg', 'png', 'jpeg'])

client = openai.OpenAI(
    base_url="https://api.endpoints.anyscale.com/v1",
    api_key=ANYSCALE_API
)


def save_uploadedfile(uploadedfile, file_name):
    with open(os.path.join("tempDir", file_name), "wb") as f:
        f.write(uploadedfile.getbuffer())
    return st.success("Image saved!")


def get_image_output(image_path):
    model = YOLO("DarkPatterns/runs/detect/train/weights/best.pt")
    get_pred_img(model, image_path, SAVE_DIR)


def crop_image(image, coords):
    x1, y1, x2, y2 = coords
    cropped_image = image[int(y1):int(y2), int(x1):int(x2)]
    return cropped_image


def get_text_list(bboxes, image):
    bb = []
    for i in bboxes:
        bb.append(i.tolist()[0])

    sorted_bb = sorted(bb, key=lambda bbox: (bbox[2] - bbox[0]) * (bbox[3] - bbox[1]))[::-1]

    img = cv2.imread(image)
    im_list = []

    for i in sorted_bb:
        im_list.append(crop_image(img, i))

    text_list = []
    for image in im_list:
        text = pytesseract.image_to_string(image)
        text_list.append(text)
    text_list = [p for p in text_list if any(char.isdigit() for char in p)]

    return text_list


def llm_response(prompt):
    chat_completion = client.chat.completions.create(
        model="meta-llama/Llama-2-70b-chat-hf",
        messages=[{"role": "system", "content": "You are a helpful assistant."},
                  {"role": "user", "content": prompt}],
        temperature=0.7
    )
    return chat_completion.choices[0].message.content


model = YOLO("DarkPatterns/runs/detect/train/weights/best.pt")
if input_image:
    if st.button("Upload!", key="image"):
        st.write("Image uploaded")
        st.write("Detecting bounding boxes...")
        save_uploadedfile(input_image, file_name="temp.jpg")
        get_image_output("tempDir/temp.jpg")
        # b_boxes = get_text_bboxes(model, "tempDir/temp.jpg")
        # text_list = get_text_list(b_boxes, "tempDir/temp.jpg")
        # st.write(text_list)
        col1, col2 = st.columns(2)
        with col1:
            st.subheader("Original Image")
            st.image(input_image, use_column_width=True)
        with col2:
            st.subheader("Image with Bounding Boxes")
            st.image("predictions/results.jpg")

prompt_input = st.text_input("Enter your prompt here")
if st.button("Send"):
    st.write(llm_response(prompt_input))

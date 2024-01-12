import streamlit as st
from scraper import fetch_html_with_selenium
from DarkPatterns.utils.helper_functions import get_pred_img
from ultralytics import YOLO


st.set_page_config(page_title="Dark Pattern Detector", page_icon="🕵️")

from api import get_collection

st.title("🕵️ Dark Pattern Detector")
st.subheader("By Team PerryThePlatypus")


def dark_pattern_detector():
    st.write(
        "Dark patterns are user interfaces designed to trick people into doing things they might not otherwise do, like buying insurance with their purchase or signing up for recurring bills.")
    st.write("This tool is designed to help you identify and report dark patterns in e-Commerce Website.")
    st.write("You can also learn more about dark patterns by visiting the [Information Section](/Information_Section).")


def get_image_output(image_path):
    model = YOLO("DarkPatterns/runs/detect/train/weights/best.pt")
    get_pred_img(model, image_path, "predictions")


def url_input():
    st.subheader("URL Input")
    st.write("Enter the URL of the website you want to check for dark patterns.")
    input_url = st.text_input("Enter URL")
    st.write("You have entered: ", input_url)
    st.write("Click on the button below to check for dark patterns.")
    if st.button("Check"):
        message_placeholder = st.empty()
        message_placeholder.text("Checking for dark patterns...")
        html_content = fetch_html_with_selenium(input_url, headless=False)
        get_image_output("tempDir/temp.png")
        message_placeholder.empty()
        st.image("predictions/results.jpg")


def main():
    dark_pattern_detector()
    url_input()
    hide_streamlit_style = """
                        <style>
                        # MainMenu{
                            visibility: hidden;
                        }
                        footer {
                            visibility: hidden;
                        }
                        footer:after {
                            content:'Developed by PerryThePlatypus Team'; 
                            visibility: visible;
                            display: block;
                            position: relative;
                            # background-color: red;
                            padding: 15px;
                            top: 2px;
        	            }
        	            img{
                            border-radius: 10px !important;
                        }
                        </style>
                        """
    st.markdown(hide_streamlit_style, unsafe_allow_html=True)


main()

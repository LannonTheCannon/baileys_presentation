import streamlit as st
import base64

def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
    f"""
    <style>
    .stApp {{
        display: flex;
        justify-content: center;
        align-items: center;
        background-image: url(data:image/{"png"};base64,{encoded_string.decode()});
        background-size: cover;
        background-repeat: no-repeat
        background-position: center;
        height: auto;
        
    }}
    </style>
    """,
    unsafe_allow_html=True
    )

add_bg_from_local('./images/pink_thing.jpg')

# text is for the folder path
# use folder called images for the image

import streamlit as st
import base64

def add_image_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
    f"""
    <style>
    .stApp {{
        display: flex;
        justify-content: center;
        align-items: center;
        /* background-image: url(data:image/{"png"};base64,{encoded_string.decode()});
        background-size: cover;
        background-repeat: no-repeat
        background-position: center;*/
        height: auto;
        background-color: #ABC4AB;
        
    }}

    [data-testid="stSidebar"] {{
    background-color: #A39171;

    }}
    </style>
    """,
    unsafe_allow_html=True
    )


def change_bg(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
    f"""
    <style>
    .stApp {{
        display: flex;
        justify-content: center;
        align-items: center;
        /* background-image: url(data:image/{"png"};base64,{encoded_string.decode()});
        background-size: cover;
        background-repeat: no-repeat
        background-position: center;*/
        height: auto;
        background-color: #5D536B;
        
    }}

    [data-testid="stSidebar"] {{
    background-color: #272838;

    }}

    .st-emotion-cache-qdbtli {{
    background-color: #5D536B;
    }}

    .st-emotion-cache-h4xjwg {{
    background-color: #5D536B;
    }}

    .st-emotion-cache-135xp1h {{
    background-color: #272838;
    }}

    .st-emotion-cache-xlis0j {{
    background-color: #272838;
    }}

    .st-emotion-cache-1247n7e {{
    background-color: #272838;
    }}

    .st-emotion-cache-1it2hzq {{
    background-color: #272838;
    }}

    .st-emotion-cache-isr5fz {{
    background-color: #272838;
    }}

    .st-emotion-cache-1apb2ab {{
    background-color: #272838;
    }}

    .st-emotion-cache-46p3ro {{
    background-color: #272838;
    }}

    .st-emotion-cache-15hul6a {{
    background-color: #272838;
    }}

    .st-emotion-cache-3cfd58 {{
    background-color: #272838;
    }}

    .st-emotion-cache-1yahvp0 {{
    background-color: #272838;
    }}
    </style>
    """,
    unsafe_allow_html=True
    )

# text is for the folder path
# use folder called images for the image

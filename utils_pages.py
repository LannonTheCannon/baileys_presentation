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

    .st-emotion-cache-h4xjwg {{
    background-color: #5D536B;
    }}

    
    </style>
    """,
    unsafe_allow_html=True
    )


def change_bg():
    st.markdown(
    f"""
    <style>
    .stApp {{
    background-color: #5D536B;        
    }}

    [data-testid="stSidebar"] {{
    background-color: #272838;
    }}

    .st-emotion-cache-h4xjwg {{
    background-color: #5D536B;
    }}

    /*Home_Page*/
    
    .st-emotion-cache-1yahvp0 {{
    background-color: #272838;
    }}

    /*My_Projects*/

    /*Chatbot*/
    
    .st-emotion-cache-1j20h4v {{
    background-color: #272838;
    }}

    .st-emotion-cache-qdbtli {{
    background-color: #5D536B;
    }}

    .st-cp {{
    background-color: #272838;
    }}

    .st-emotion-cache-janbn0 {{
    background-color: #272838;
    }}

    .st-emotion-cache-4oy321 {{
    background-color: #272838;
    }}

    .st-emotion-cache-4zpzjl {{
    background-color: #DFD9E2;
    }}

    .st-emotion-cache-jmw8un {{
    background-color: #53A2BE;
    }}

    /*Chatbot_Explained*/

    .st-emotion-cache-15hul6a {{
    background-color: #5D536B;
    }}

    .st-emotion-cache-yk7at5{{
    background-color: #272838;
    }}

    .st-emotion-cache-135xp1h {{
    background-color: #272838;
    }}

    .st-emotion-cache-xlis0j {{
    background-color: #272838;
    }}

    .st-emotion-cache-isr5fz {{
    background-color: #272838;
    }}

    .st-emotion-cache-1247n7e {{
    background-color: #272838;
    }}

    /*Material Game*/
    
    .st-emotion-cache-1it2hzq {{
    background-color: #272838;
    }}

    .st-emotion-cache-15hul6a {{
    background-color: #272838;
    }}

    /*Contacts*/

    /*Project Showcase*/
    .st-emotion-cache-1apb2ab {{
    background-color: #272838
    }}

    </style>
    """,
    unsafe_allow_html=True
    )

# text is for the folder path
# use folder called images for the image

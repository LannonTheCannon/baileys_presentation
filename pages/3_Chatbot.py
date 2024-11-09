# chatbot_v3_standalone
import streamlit as st
import openai
import time
import os
from utils_pages import change_bg
from Home import get_assistant_response, display_chatbot

st.set_page_config(page_title="Chatbot", page_icon = ":three", layout="wide")

ASSISTANT_ID = "asst_I5jUjKMGObw1PnasEbEn2AQ5"
THREAD_ID = "thread_XDnikh1ZmG683T20PlfSSsWs"

# Openai Client
api_key = st.secrets.get("OPENAI_API_KEY") or os.environ.get("OPENAI_API_KEY")
if not api_key:
    st.error('OpenAi API Key was not found. Please set it in Streamlit secrets or as an enviromental varible')
    st.stop()
client = openai.OpenAI(api_key=api_key)

# Creating Chat
if "messages" not in st.session_state:
    st.session_state.messages = []

with st.sidebar:
    st.write("")
    page_back, page_forward = st.columns(2)
    with page_back:
        if st.button("Back"):
            st.switch_page("pages/2_My_Projects.py")
    with page_forward:
        if st.button("Next"):
             st.switch_page("pages/4_Chatbot_Explained.py")


def main():
    display_chatbot()
    
    

if __name__ == "__main__":
    main()

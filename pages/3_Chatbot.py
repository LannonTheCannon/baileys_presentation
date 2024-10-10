# chatbot_v3_standalone
import streamlit as st
import openai
import time
import os
from utils import add_image_from_local, change_bg
from chatbot_v3 import get_assistant_response, display_chatbot

ASSISTANT_ID = "asst_I5jUjKMGObw1PnasEbEn2AQ5"
THREAD_ID = "thread_9vkU15hrjp4L4lQYOLKpabrP"

# Openai Client
api_key = st.secrets.get("OPENAI_API_KEY") or os.environ.get("OPENAI_API_KEY")
if not api_key:
    st.error('OpenAi API Key was not found. Please set it in Streamlit secrets or as an enviromental varible')
    st.stop()
client = openai.OpenAI(api_key=api_key)

# Creating Chat
if "messages" not in st.session_state:
    st.session_state.messages = []

def main():
    display_chatbot()
    

if __name__ == "__main__":
    main()

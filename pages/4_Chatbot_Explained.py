# Chatbot_Explained.py
import streamlit as st
from src.chatbot_expanded import display_chatbot_expanded

st.set_page_config(page_title="Chatbot Explained", page_icon = ":four:", layout="wide")

with st.sidebar:
    st.write("")
    page_back, page_forward = st.columns(2)
    with page_back:
        if st.button("Back"):
            st.switch_page("pages/3_Chatbot.py")
    with page_forward:
        if st.button("Next"):
             st.switch_page("pages/5_Contacts.py")

def main():
    display_chatbot_expanded()

if __name__ == "__main__":
    main()

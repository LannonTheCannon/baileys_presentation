# 5_Contacts.py
import streamlit as st
from src.contacts import display_contacts

st.set_page_config(page_title="Contacts", page_icon = ":five:", layout="wide")

with st.sidebar:
    st.write("")
    page_back, page_forward = st.columns(2)
    with page_back:
        if st.button("Back"):
            st.switch_page("pages/4_Chatbot_Explained.py")
    with page_forward:
        if st.button("Next"):
             st.switch_page("pages/6_Project_ShowCase.py")

def main():
    display_contacts()

if __name__ == "__main__":
    main()

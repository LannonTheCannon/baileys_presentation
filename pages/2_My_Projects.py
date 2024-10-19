# My_Projects.py
import streamlit as st
from src.my_project_page import display_my_projects
from streamlit_card import card

st.set_page_config(page_title="My Projects", page_icon = ":two:", layout="wide")

with st.sidebar:
    st.write("")
    page_back, page_forward = st.columns(2)
    with page_back:
        if st.button("Back"):
            st.switch_page("Home.py")
    with page_forward:
        if st.button("Next"):
             st.switch_page("pages/3_Chatbot.py")


def main():
    display_my_projects()

if __name__ == "__main__":
    main()
    

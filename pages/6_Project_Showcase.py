# 6_Project_Showcase.py
import streamlit as st
from src.showcase import display_showcase


st.set_page_config(page_title="Showcase", page_icon = ":six:", layout="wide")
with st.sidebar:
    st.write("")
    page_back, page_forward = st.columns(2)
    with page_back:
        if st.button("Back"):
            st.switch_page("pages/5_Contacts.py")

def main():
    display_showcase()

if __name__ == "__main__":
    main()

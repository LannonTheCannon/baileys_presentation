# contacts.py
import streamlit as st
from utils_pages import change_bg

def display_contacts():
    change_bg()
    st.title(":violet-background[Contacts]")
    st.subheader("Here are a few ways to contact me or see what I've done!")

    st.write("")

    gmail_col, git_col,ygo_col = st.columns(3,vertical_alignment="center")

    with gmail_col:
        with st.container(height=450):
            st.image("./images/Contacts_gmail.png",width=230)
            st.title("Gmail")
            st.caption("epicred1000@gmail.com")
    with git_col:
        with st.container(height=450):
            st.image("./images/Contacts_github.png",width=200)
            st.title("Github")
            st.caption("https://github.com/EpicRed1000")
    with ygo_col:
        with st.container(height=450):
            st.image("./images/Contacts_ygo.png",width=230)
            st.title("Ygoprodeck.com")
            st.caption("https://ygoprodeck.com/author/marune-184564")

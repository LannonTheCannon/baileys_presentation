# my_projects.py

import streamlit as st

def display_my_projects():
    st.title(":blue-background[My projects]")
    # 380 with image
    with st.container(height = 135):
        st.header("Material Selection AI")
        st.caption("Helpful Ai that searches for the best material for engineers based on given criteria")
    with st.container(height = 135):
        st.header("Locked Up")
        st.caption("A fun text based adventure game etc")

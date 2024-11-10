# my_projects.py
import streamlit as st
from streamlit_card import card
from utils_pages import change_bg


def display_my_projects():
    change_bg()
    st.title(":blue-background[My projects]")
    material_ai, locked_up = st.columns(2)
    with material_ai:
        with st.container(height=450):
            st.image("./images/Material_image.png",width=200)
            st.title("Material Selection AI")
            st.caption("Helpful Ai that searches for the best material for engineers based on given criteria")

    with locked_up:
        with st.container(height= 450):
            st.image("./images/Lock_image.png",width=205)
            st.title("Locked Up")
            st.caption("A Text Adventure")

    

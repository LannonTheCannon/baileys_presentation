# homepage_pages.py
import streamlit as st
from streamlit_timeline import st_timeline
from src.homepage import display_home
from utils_pages import change_bg
def main():
    display_home()

if __name__ == "__main__":
    main()

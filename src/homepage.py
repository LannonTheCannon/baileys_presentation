# homepage.py
import streamlit as st
from streamlit_timeline import st_timeline
from utils_pages import change_bg

def display_home():
    change_bg()
    st.title(":green-background[Welcome to Bailey Tang's Profile]")
    st.caption("Just have fun with it")
    st.write("")
    # about me
    st.title("About me")
    general, current, future = st.columns(3, vertical_alignment="center")

    with general:
        st.image("./images/Homepage_me.jpg", width=250)
        st.write("My name is Bailey Tang and I am 14 years old, I like card games, and band/music (0.5% of Hamilton Listeners October 2024)")
    with current:
        st.image("./images/Homepage_marching.jpg",width=275)
        st.write("I'm in school studying computer science and practicing for marching band (I play clarinet)")
    with future:
        st.image("./images/Homepage_grad.jpg",width=270)
        st.write("I am going to go to MIT for computer science, study hard, rent out houses while im in college, and get a job in the tech industry (Cyber security, software designer etc.)")
    st.write("")
    # Timeline
    st.title("Timeline")
    items = [
        {"content":"Born","start":"2010-5-7"},
        {"content":"Started Scratch","start":"2019-9-26"},
        {"content":"Started Python Coding","start":"2023-10-11"},
        {"content":"SMS Jazz Band Solo","start":"2024-5-21"},
        {"content":"WHS Marching Competition","start":"2024-11-16"},
        {"content":"Graduate","start":"2028"},
        {"content":"Join MIT","start":"2028-8-15"}

    ]
    timeline = st_timeline(items,groups=[],options={},height="300px")
    st.write(timeline)

    # Skills
    st.write("")
    st.title("Skills")
    # Languages
    st.header("Languages")
    with st.container(height = 130):
        st.header("Python")
        st.caption("2 Years")
    with st.container(height = 130):
        st.header("Scratch")
        st.caption("5 Years")
    with st.container(height = 130):
        st.header("Unity")
        st.caption("1 month")

    st.write("")

    st.header("Frameworks and Libaries")
    with st.container(height = 130):
        st.header("Streamlit")
        st.caption("Created Chatbots, Websites, and more")
    with st.container(height = 130):
        st.header("Tkinter")
        st.caption("Designed GUI for multiple projects")
    with st.container(height = 130):
        st.header("PyGame")
        st.caption("Utilized for simple games")

    st.write("")

    st.write("")

    # Featured Projects
    st.title("Featured Projects")

    locked_up, material_ai, kaiba_ai = st.columns(3, vertical_alignment="center")

    with locked_up:
        st.image("./images/Lock_image.png",width=200)
        st.header("Locked Up")
        st.write("Locked up is a text based adventure game")

    with material_ai:
        st.image("./images/Material_image.png",width=200)
        st.header("Engineering Material Selection AI")
        st.write("An AI made to help Engineers select materials based on given criteria")

    with kaiba_ai:
        st.image("./images/Homepage_kaiba.png",width=200)
        st.header("Kaiba AI")
        st.write("A fun Ai made to test the ability of AI")

    st.write("")

    st.title("What I Can Do For You")
    with st.container(height = 130):
        st.header("Yu-Gi-Oh Deck Building")
        st.caption("Give me a budget and an hour")
    with st.container(height = 130):
        st.header("Coding")
        st.caption("I'll try my best :sob:")
##    with st.container(height = 130):
##        st.header("Something")
##        st.caption("Something")

    

        
    



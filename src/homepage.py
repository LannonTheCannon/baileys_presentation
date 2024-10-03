# homepage.py
import streamlit as st
from streamlit_timeline import st_timeline

def display_home():
    st.title(":green-background[Welcome to Bailey Tang's Profile]")
    st.caption("Just have fun with it")
    st.write("")
    # about me
    st.title("About me")
    general, current, future = st.columns(3)

    with general:
        st.image("https://cdn.discordapp.com/attachments/960728516104699935/1290470263275786311/bumkiltan-ezgif.com-added-text.jpg?ex=66fc9396&is=66fb4216&hm=9bcfe2dd9c0f81d61bcccd4f4c9eb406f243a4559764ff9f235faa76bfac2f20&")
        st.write("My name is Bailey Tang and I am 14 years old, I like card games, and band/music")
    with current:
        st.image("https://cdn.discordapp.com/attachments/960728516104699935/1290470167066972283/IMG_2179.jpg?ex=66fc937f&is=66fb41ff&hm=b81c74e30d68b8882dbc205f0433500d608cf79ade4a4481311b8e76e329d765&")
        st.write("I'm in school studying computer science and practicing for marching band (I play clarinet)")
    with future:
        st.image("https://cdn.discordapp.com/attachments/960728516104699935/1290470337942650921/cedf9254-7044-48f9-a568-7f07f3ec2980.jpg?ex=66fc93a8&is=66fb4228&hm=e3712114f5dad0b8cd9dae84f269d7fe13be77252b7766db6f05a991fa15f7cb&")
        st.write("I am going to go to MIT for computer science, study hard, rent out houses while im in college, and get a job in the tech industry (Cyber security, software designer etc.)")
    st.write("")
    # Timeline
    st.title("Timeline")
    items = [
        {"content":"Born","start":"2010-5-7"},
        {"content":"Started Scratch","start":"2019-9-26"},
        {"content":"Started Python Coding","start":"2023-10-11"},
        {"content":"SMS Jazz Band Solo","start":"2024-5-21"},
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

    locked_up, material_ai, kaiba_ai = st.columns(3)

    with locked_up:
        st.image("https://cdn.discordapp.com/attachments/960728516104699935/1290471140753670266/9k.png?ex=66fc9467&is=66fb42e7&hm=a090c1c919fe0aa1a813789475e5ec7ca18e8ba0b595000bc5106c987958c88c&")
        st.header("Locked Up")
        st.write("Locked up is a text based adventure game")

    with material_ai:
        st.image("https://cdn.discordapp.com/attachments/960728516104699935/1290471402847080579/2Q.png?ex=66fc94a6&is=66fb4326&hm=11fe1fe41e628a2ffc851878b37eae0c52bfa729876126b395d887a89f0c6684&")
        st.header("Engineering Material Selection AI")
        st.write("An AI made to help Engineers select materials based on given criteria")

    with kaiba_ai:
        st.image("https://cdn.discordapp.com/attachments/960728516104699935/1290471653285036205/Z.png?ex=66fc94e1&is=66fb4361&hm=3d53a142765db4bcfc26b919c2795000ff34a72ae8e8b3b78ea522497a2b8660&")
        st.header("Kaiba AI")
        st.write("A fun Ai made to test the ability of AI")

    st.write("")

    #st.title("What I Can Do For You")
    

    

    

        
    



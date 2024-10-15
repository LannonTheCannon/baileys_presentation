# contacts.py
import streamlit as st
from streamlit_card import card
from utils_pages import change_bg

def display_contacts():
    change_bg()
    st.title(":violet-background[Contacts]")
    st.subheader("Here are a few ways to contact me!")

    st.write("")

    gmail_col, git_col = st.columns(2)

    with gmail_col:
        gmail = card(
            image ="https://cdn.discordapp.com/attachments/960728516104699935/1290466735509471314/8La7Qmwt7iflleveiiMzMzMzMzMz52l4DsCqnoc4aHnchZYHg2h5hIqWh81oeSyPngcY6XnUk5aHYml5fJieB63peSSdNiri8D5N7iB1zKGeB0LqeXSmew1O2TUmSbHsf4FmcCYeLX7yQAAAAASUVORK5CYII.png?ex=66fc904d&is=66fb3ecd&hm=19838d3bf7f743c574983bcebdb2af355b8a4a32de9eaaa84e4e474d5f2338eb&",
            title ="Gmail:",
            text = "epicred1000@gmail.com",
            url = "https://github.com/EpicRed1000",
            styles={
                "card":{
                    "width": "300px",
                    "Height": "300px",
                    "border-radius": "40px",
                    }
                }
        )
    with git_col:
        git = card(
            image = "https://cdn.discordapp.com/attachments/960728516104699935/1290466120473509899/4B0HNeEbhWByQAAAAASUVORK5CYII.png?ex=66fc8fba&is=66fb3e3a&hm=5cd52b9be54cfc34f442d6d4ad00d7f573d0f55e43d826c93a03d55118eb8351&",
            title ="Github: ",
            text = "https://github.com/EpicRed1000",
            styles={
                "card":{
                    "width": "300px",
                    "Height": "300px",
                    "border-radius": "40px"
                    }
                }
            )

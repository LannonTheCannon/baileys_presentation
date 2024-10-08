# my_projects.py
import streamlit as st
from streamlit_card import card


def display_my_projects():
    st.title(":blue-background[My projects]")
    material_ai, locked_up = st.columns(2)
    with material_ai:
        MSA = card(
            title="Material Selection AI",
            text= "Helpful Ai that searches for the best material for engineers based on given criteria",
            image= "https://cdn.discordapp.com/attachments/960728516104699935/1290471402847080579/2Q.png?ex=66fc94a6&is=66fb4326&hm=11fe1fe41e628a2ffc851878b37eae0c52bfa729876126b395d887a89f0c6684&",
            styles={
                "card":{
                    "width": "500px",
                    "Height": "500px",
                    "border-radius": "120px"
                    #"box-shadow": "0 0 10px rgba(0,0,0,0.5)"
                    }
                }
        )
    if MSA:
        st.switch_page(".\pages\chatbot_v3_standalone.py")
    
    with locked_up:
        LU = card(
            title="Locked Up",
            text= "A fun text based adventure game ",
            image= "https://cdn.discordapp.com/attachments/960728516104699935/1290471140753670266/9k.png?ex=66fc9467&is=66fb42e7&hm=a090c1c919fe0aa1a813789475e5ec7ca18e8ba0b595000bc5106c987958c88c&",
            url ="https://docs.google.com/presentation/d/1wdwPSt2--QWsECZDnHycqSL4-7iVV3m_D9J2SMWXmZE/edit?usp=sharing",
            styles={
                "card":{
                    "width": "500px",
                    "Height": "500px",
                    "border-radius": "120px"
                    #"box-shadow": "0 0 10px rgba(0,0,0,0.5)"
                    }
                }
        )
    

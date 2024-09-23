# chatbot_expanded.py
import streamlit as st
from streamlit_extras.stoggle import stoggle
from src.material_game import material_game



def display_chatbot_expanded():
    st.title(":green-background[What can this chatbot do for you]")
    st.subheader("Image it's 6 pm. You just finished designing plans for your next big project. You're ready to fall asleep on your nice comfortable bed... but suddently your boss marches him and forces you figure out the necessary materials for the project. Tired and defeated you groan as you work for the next couple hours reaserching and comparing diffrent materials, never getting to go home, never getting to your bed...")
    st.write("")
##    if st.button("But...",key = game_start):
##        st.subheader("This Ai allows you to compare and contrast diffrent materials in minutes.")
##        st.subheader("The Ai gives out information about a wide range of materials using the given critera and prompt.")
##        st.subheader("For example...")
##        material_game()
    stoggle("But...",
        '''This Ai allows you to compare and contrast diffrent materials in minutes.
        The Ai gives out information about a wide range of materials using the given critera and prompt.'''
            )
        
        # companies used materials
        # vn esque
        # have emebeded chat
    #if st.button("Really?"):
        #st.subheader("")
        
    # stories (I wanted to know if [HOOK]. Use code as CD explain with CM, )
    # pictures


    # st.title("company")
    # yamah clarients use grenadilla wood save for next one
    

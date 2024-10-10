# chatbot_expanded.py
import streamlit as st
from streamlit_extras.stateful_button import button
from src.material_game import material_game
from utils_pages import change_bg



def display_chatbot_expanded():
    change_bg()
    st.title(":green-background[What can this chatbot do for you]")
    with st.container(height = 220):
        st.subheader(''':rainbow[Imagine...] :red[it's 6 pm.] You just :green[finished designing plans for your next big project]. You're ready to fall asleep on your :green[nice comfortable bed...] :red[but suddenly] your boss :red[marches in and forces you figure out the necessary materials for the project.] :blue[Tired] and :violet[defeated] you groan as you work for the next :red[couple hours reaserching and comparing diffrent materials], never getting to go :red[home], never getting to your :red[bed...]''')
    st.write("")
##    if st.button("But...",key = game_start):
##        st.subheader("This Ai allows you to compare and contrast diffrent materials in minutes.")
##        st.subheader("The Ai gives out information about a wide range of materials using the given critera and prompt.")
##        st.subheader("For example...")
##        material_game()


    if button(":green[But...]", key="button1"):
        with st.container(height = 230):
            st.subheader("Using this :blue[AI] we can :green[fix all of that]")
            st.subheader("This :blue[Ai] allows you to :green[compare] and :green[contrast] diffrent materials in :green[seconds]")
            st.subheader("The :blue[Ai] gives out :green[information] about a wide range of :green[materials] using the given critera and prompt.")
        if button(":green[For Example...]", key="button2"):
            material_game()
            if button(":green[What is the Purpose of these Materials?]", key="button3"):
                with st.container(height = 250):
                    st.subheader("Why do :green[doctors] use :orange[stainless steel]")
                    st.subheader("Does :orange[polystyrene foam] have :green[thermal insulation properties?]")
                    st.subheader("Isn't :orange[aluminum] flimsy? How can it be used for :green[Aircraft?]")
                    st.subheader("Lets ask the :blue[AI] for answers")
                if button(":green[Conclusion]", key="button4"):
                    with st.container(height = 180):
                        st.subheader("This :blue[AI] has been designed to help solve any questions and problems about materials")
                        st.subheader("From rubber to titanium this :blue[AI] will help you find the best material for you")

        
        # companies used materials
        # vn esque
        # have emebeded chat
    #if st.button("Really?"):
        #st.subheader("")
        
    # stories (I wanted to know if [HOOK]. Use code as CD explain with CM, )
    # pictures


    # st.title("company")
    # yamah clarients use grenadilla wood save for next one
    

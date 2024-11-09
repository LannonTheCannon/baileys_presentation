# Zombie_game2.py

import random
import streamlit as st
#from utils_pages import change_bg

if "current_room" not in st.session_state:
    st.session_state.current_room = 'woods'

if "feeling_brave" not in st.session_state:
    st.session_state.feeling_brave = True

if "move" not in st.session_state:
    st.session_state.move = ""
if 'inventory' not in st.session_state:
    st.session_state.inventory =[]
if "time" not in st.session_state:
    st.session_state.time = 12

if "events_done" not in st.session_state:
    st.session_state.events_done = []

if "traffic_event" not in st.session_state:
    st.session_state.traffic_event = False

if "event_guesses" not in st.session_state:
    st.session_state.hoard_guesses = 0

rooms = {
    'woods':{
        'right':'mall'},
    'mall':{
        'left':'woods',
        'right':'parking lot',
        'down':'construction site'},
    'parking lot':{
        'left':'mall',
        'down':'traffic'},
    'construction site':{
        'up':'mall',
        'right':'traffic'},
    'traffic':{
        'up':'parking lot',
        'down':'resturants',
        'left':'construction site',
        'right':'graveyard',
        'event':'hoard'},
    'resturants':{
        'up':'traffic',
        'right':'houses'},
    'graveyard':{
        'left':'traffic',
        'down':'houses'},
    'houses':{
        'up':'graveyard',
        'left':'resturants',
        'right':'car'},
    }
# finish car later

def show_intro():
    st.write('''

You were camping out in the woods when an emergency alert popped up on your phone.
*EMERGENCY ALERT* PEOPLE ARE BEING INFECTED BY A BRAIN CONTROLING PARASITE
EVACUATIONS HAVE STARTED

You look on your phone to check your map:
''')
    #st.image()
    st.write('''
According to the schedule you only have a few hours to get their. You snuff out your fire and pack up your gear.
After loading up your car you attempt to start it up...
Unfortunately you had left the lights on inside the car killing the battery.
You now have to walk to the evacuation point

commands:
go[left,right,up,down]
''')

def show_status():
    st.write("----------------------------------------------------------------------------------------")
    st.write(f'You are currently in the {st.session_state.current_room}')
    if  'item' in rooms[st.session_state.current_room]:
        st.write(f"You see a {rooms[st.session_state.current_room]}")
    st.write(f'You have :blue-background[{st.session_state.time}] hours left')
    st.write("----------------------------------------------------------------------------------------")
    if st.session_state.current_room == 'car':
        st.write("You drive away...")

# Events
def hoard_event():
    if st.session_state.current_room == "traffic":
        st.write("You walk in to see a hoard of zombies rampaging across a busy road filled with empty cars")
    st.write("You have to stay silent to sneak pass the huge hoard")
    if "secret_number" not in st.session_state:
        st.session_state.secret_number = randint(1,40)
    st.session_state.event_guesses = 8
    st.write('Pick a number between 1 and 40 to stay silent')

    if st.session_state.feeling_brave:
        st.session_state.move = st.session_state.move.lower().split()
        if st.session_state.move[0] > st.session_state.secret_number:
            st.write(f"The number is too high! {st.session_state.event_guesses} steps before they hear you!")
        elif st.session_state.move[0] < st.session_state.secret_number:
            st.write(f"The number is too low! {st.session_state.event_guesses} steps before they hear you!")
        elif st.session_state.move[0] == st.session_state.secret_number:
            st.write("You sneaked pass the hoard of zombies! Lucky you!")
            st.session_state.traffic_event = True
        else:
            st.write('Please Enter a number')
        


def main():
    show_intro()
    if st.session_state.feeling_brave:
        st.session_state.move = st.text_input('Enter An Action',key='txt_inpt')
        st.session_state.move = st.session_state.move.lower().split()
        try:
            if st.session_state.move[0] == 'go':
                if st.session_state.move[1] in rooms[st.session_state.current_room]:
                    st.session_state.current_room = rooms[st.session_state.current_room][st.session_state.move[1]]
                else:
                    st.write("Don't get side tracked! Stay on the path!")
            show_status()
            st.write(f'{st.session_state.current_room}')
        except:
            pass

        if st.session_state.current_room == "traffic" and st.session_state.traffic_event == False:
            hoard_event()

if __name__ == "__main__":
    main()
    

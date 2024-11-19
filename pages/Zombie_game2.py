# Zombie_game2.py
#PAGES
import random
import streamlit as st
#from utils_pages import change_bg

if "current_room" not in st.session_state:
    st.session_state.current_room = 'Camp Goodman'

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
    'Camp Goodman':{
        'right':'Drytron Mall'},
    'Drytron Mall':{
        'left':'Camp Goodman',
        'right':'parking lot',
        'down':'construction site'},
    'parking lot':{
        'left':'Drytron Mall',
        'down':'traffic'},
    'construction site':{
        'up':'Drytron Mall',
        'right':'traffic'},
    'traffic':{
        'up':'parking lot',
        'down':'resturants',
        'left':'construction site',
        'right':'hospital',
        'event':'hoard'},
    'resturants':{
        'up':'traffic',
        'right':'houses'},
    'hospital':{
        'left':'traffic',
        'down':'houses'},
    'houses':{
        'up':'hospital',
        'left':'resturants',
        'right':'car'},
    }
# finish car later

def show_intro():
    st.write('''

You were camping out in the Camp Goodman when an emergency alert popped up on your phone.
*EMERGENCY ALERT* PEOPLE ARE BEING INFECTED BY A BRAIN CONTROLING PARASITE
EVACUATIONS HAVE STARTED

You look on your phone to check your map:
''')
    st.image("./images/Zombie_Game_map.png")
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
    if "zombie_game_state" not in st.session_state:
        st.session_state.zombie_game_state = {
                "secret_number":random.randint(1,40),
                "guesses_remaining": 8,
                "game_active": True,
                "message": None,
                "show_transition": False
            }
        
    game_state = st.session_state.zombie_game_state

    # WIn
    if game_state["show_transition"]:
        st.write("Good job ") # Fill out later
        if st.button("continue on"):
            st.session_state.traffic_event = True
            # Restart Zombie game state (to play again)
##            del st.session_state.zombie_game_state
##            st.rerun()
        return False
    
    st.write("You walk in to see a hoard of zombies rampaging across a busy road filled with empty cars")    
    st.write("You have to stay silent to sneak pass the huge hoard")
    st.write('Pick a number between 1 and 40 to stay silent')
    st.write(f'You currently have {game_state["guesses_remaining"]}')

    if game_state["message"]:
        if "success" in game_state["message"]:
            st.success(game_state["message"])
        elif "warning" in game_state["message"]:
            st.warning(game_state["message"])
        elif "error" in game_state["message"]:
            st.error(game_state["message"])

    if game_state["game_active"]:
        col1, col2 = st.columns([3,1])
        
        with col1:
            guess = st.number_input("Enter a number",min_value=1,max_value=40, key=f'zombie_guess')
            
        with col2:
            if st.button("Make Your Move",key="zombie_submit"):
                if guess == game_state["secret_number"]:
                    game_state["message"] = "success"
                    game_state["game_active"] = False
                    game_state["show_transition"] = True
                else:
                    game_state["guesses_remaining"] -= 1
                    if game_state["guesses_remaining"] <= 0:
                        game_state["message"] = "loss"
                        game_state["game_active"] = False
                    else:
                        hint = "too high" if guess > game_state["secret_number"] else "too low"
                        game_state["message"] = f'warning {hint} {game_state["guesses_remaining"]} Guesses left'
                game_state["last_guess"] = guess
                st.session_state.zombie_game_state = game_state
                st.rerun()
                show_status()
    return not game_state["game_active"] and not game_state["show_transition"]

def main():
    if "game_initialized" not in st.session_state:
        st.session_state.game_initialized = True
    show_intro()
    
    if st.session_state.feeling_brave:
        if st.session_state.current_room == "traffic" and not st.session_state.traffic_event:
            can_move = hoard_event()
            if not can_move:
                return
            
        st.session_state.move = st.text_input("Enter an Action", key="txt_input")
        st.session_state.move = st.session_state.move.lower().split()            
        try:
            if st.session_state.move[0] == 'go':
                if st.session_state.move[1] in rooms[st.session_state.current_room]:
                    st.session_state.current_room = rooms[st.session_state.current_room][st.session_state.move[1]]
                    st.session_state.time -= 1
                    
                else:
                    st.write("Don't get side tracked! Stay on the path!")
                    
            show_status()
            st.write(f'{st.session_state.current_room}')
        except:
            pass
        if st.session_state.current_room == "traffic" and not st.session_state.traffic_event:
            can_move = hoard_event()
            if not can_move:
                return

if __name__ == "__main__":
    main()
    

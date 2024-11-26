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
    
if "time" not in st.session_state:
    st.session_state.time = 12

if "traffic_event" not in st.session_state:
    st.session_state.traffic_event = False

rooms = {
    'Camp Goodman':{
        'right':'Drytron Mall',
        'description':"yada yada",
        'image':"./images/Contacts_github.png"},
    'Drytron Mall':{
        'left':'Camp Goodman',
        'right':'parking lot',
        'down':'Amazement Land',
        'description':"yada yada",
        'image':"./images/Contacts_github.png"},
    'parking lot':{
        'left':'Drytron Mall',
        'down':'The Suburbs',
        'description':"yada yada",
        'image':"./images/Contacts_github.png"},
    'Amazement Land':{
        'up':'Drytron Mall',
        'right':'The Suburbs',
        'description':"yada yada",
        'image':"./images/Contacts_github.png"},
    'The Suburbs':{
        'up':'parking lot',
        'down':'Schuyler\'s Seaside Saloon',
        'left':'Amazement Land',
        'right':'Vigil Hospital',
        'description':"yada yada",
        'image':"./images/Contacts_github.png"},
    'Schuyler\'s Seaside Saloon':{
        'up':'The Suburbs',
        'right':'Easy Apartment',
        'description':"yada yada",
        'image':"./images/Contacts_github.png"},
    'Vigil Hospital':{
        'left':'The Suburbs',
        'down':'Easy Apartment',
        'description':"yada yada",
        'image':"./images/Contacts_github.png"},
    'Easy Apartment':{
        'up':'Vigil Hospital',
        'left':'Schuyler\'s Seaside Saloon',
        'right':'BKT Airport',
        'description':"yada yada",
        'image':"./images/Contacts_github.png"},
    'BKT Airport':{
        'left':'Easy Apartment',
        'description':"yada yada",
        'image':"./images/Contacts_github.png"}
    }
# finish car later

def show_status():
    st.write("----------------------------------------------------------------------------------------")
    st.write(f'You are currently in the {st.session_state.current_room}')
    st.image(f'{rooms[st.session_state.current_room]["image"]}')
    st.write(f'{rooms[st.session_state.current_room]["description"]}')
    st.write(f'You have :blue-background[{st.session_state.time}] hours left')
    st.write("----------------------------------------------------------------------------------------")
    if st.session_state.current_room == 'BKT Airport':
        st.write("You drive away...")


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
    #show_status()



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
    st.write(f'You currently have {game_state["guesses_remaining"]} guesses remaing and :blue-background[{st.session_state.time}]')

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
                    st.session_state.time -= 1
                    if st.session_state.time == 0 and not st.session_state.current_room == "BKT Airport":
                        lose()
                        game_state["message"] = "loss"
                        game_state["game_active"] = False
                        return 
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

def survivor_event():
    if "survivor_game_state" not in st.session_state:
        st.session_state.survivor_game_state = {
                "save_cost":random.randint(1,3),
                "game_active": True,
                "survivor_name": random.randint(0,5), # make a dictionary with names of people RANDOM CHOICE
                "show_transition": False
            }
    game_state = st.session_state.survivor_game_state

    # list of names

    #survior_names{}
    



def lose():
    st.write("You lose")
    st.session_state.feeling_brave = False
    return 


def main():
    if "game_initialized" not in st.session_state:
        st.session_state.game_initialized = True
    show_intro()
    
    if st.session_state.feeling_brave:
        if st.session_state.current_room == "The Suburbs" and not st.session_state.traffic_event:
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
                    if st.session_state.time == 0 and not st.session_state.current_room == "BKT Airport":
                        lose()
                        return 
                else:
                    st.write("Don't get side tracked! Stay on the path!")
                    
            show_status()
            st.write(f'{st.session_state.current_room}')
        except:
            pass
        if st.session_state.current_room == "The Suburbs" and not st.session_state.traffic_event:
            can_move = hoard_event()
            if not can_move:
                return

if __name__ == "__main__":
    main()
    

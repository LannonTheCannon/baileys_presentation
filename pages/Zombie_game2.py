# Zombie_game2.py

# What increases in value the less you have?
# FRIENDS! 

# one night a ninja and a samurai are on a boat
# the ninja and the samurai get on a life raft
# who dies

#PAGES
import random
import streamlit as st
#from utils_pages import change_bg

# Hello: Lannon was here :)

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

if "survivor_event" not in st.session_state:
    st.session_state.survivor_event = False

rooms = {
    'Camp Goodman':{
        'right':'Drytron Mall',
        'description':"yada yada",
        'image':"./images/Contacts_github.png"},
    'Drytron Mall':{
        'left':'Camp Goodman',
        'right':'parking lot',
        'down':'Amazement Land',
        'survivor': 'Drew',
        'survivor_event': True,
        'description':"You walk past the empty stalls of the once popular mall.",
        'image':"./images/Drytronmall1.jpg"},
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
        'right':'Virgil Hospital',
        'description':"yada yada",
        'image':"./images/Contacts_github.png"},
    'Schuyler\'s Seaside Saloon':{
        'up':'The Suburbs',
        'right':'Easy Apartment',
        'description':"yada yada",
        'image':"./images/Contacts_github.png"},
    'Virgil Hospital':{
        'left':'The Suburbs',
        'down':'Easy Apartment',
        'survivor': 'Name2',
        'survivor_event': True ,
        'description':"yada yada",
        'image':"./images/Contacts_github.png"},
    'Easy Apartment':{
        'up':'Virgil Hospital',
        'left':'Schuyler\'s Seaside Saloon',
        'right':'BKT Airport',
        'survivor': 'Name3',
        'survivor_event': True ,
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

# survivor event

def survivor_event():
##    if "survivor_name_list" not in st.session_state:
##        st.session_state.survivor_name_list = ["name1","name2","name3","name4","name5"]
    if "survivor_game_state" not in st.session_state:
        st.session_state.survivor_game_state = {
                "save_cost":random.randint(1,3), # the amount it takes to save them
                "game_active": True,
                "survivor_name": rooms[st.session_state.current_room]["survivor"],
                "show_transition": False
            }
    game_state = st.session_state.survivor_game_state

    if game_state["show_transition"]:
        st.write("Good job saving the survivor")
        if st.button("continue on"):
            rooms[st.session_state.current_room]["survivor_event"]
            st.session_state.survivor_event = True
        return False

    st.write("You see a survivor wandering")
    st.write(f'You encounter {game_state["survivor_name"]}')
    
        
##    st.write(f'{game_state["survivor_event"]}')
##    st.write("You see a survivor on the street")
##    st.write(f'{game_state["survivor_name"]}')
##    game_state["survivor_event"] = False
##    st.write(f'{game_state["survivor_event"]}')
    #st.write(f'{rooms[st.session_state.current_room]["survivor_event"]}')
    
##    st.session_state.survivor_name_list.remove(game_state["survivor_name"])

##    if game_state["survivor_name"] == "name1":
##        st.write("backstory")
##
##    elif game_state["survivor_name"] == "name2":
##        st.write("backstory")
##        
##    elif game_state["survivor_name"] == "name3":
##        st.write("backstory")
##
##    elif game_state["survivor_name"] == "name4":
##        st.write("backstory")
##
##    elif game_state["survivor_name"] == "name5":
##        st.write("backstory")
##    else:
##        st.error("error")
##        return

    if game_state["game_active"]:
        col1, col2 = st.columns(2)

        with col1:
            if st.button("Save the survivor", key = "save"):
                st.write("You saved them")
                st.session_state.time -= game_state["save_cost"]
                game_state["game_active"] = False
                game_state["show_transition"] = True

        with col2:
            if st.button("Leave the survivor", key = "leave"):
                st.write("You left them")
                game_state["game_active"] = False
                game_state["show_transition"] = True

            st.session_state.suvivor_game_state = game_state
            st.rerun()
            show_status()
    return not game_state["game_active"] and not game_state["show_transition"]

##    st.session_state.zombie_game_state = game_state
##    st.rerun()
##    show_status()
##    return not game_state["game_active"] and not game_state["show_transition"]



def lose():
    st.write("You lose")
    st.session_state.feeling_brave = False
    return 


def main():
    if "game_initialized" not in st.session_state:
        st.session_state.game_initialized = True
    show_intro()
    
    if st.session_state.feeling_brave:
##        if st.session_state.current_room == "The Suburbs" and not st.session_state.traffic_event:
##            can_move = hoard_event()
##            if not can_move:
##                return

##        if (st.session_state.current_room == "Drytron Mall" or st.session_state.current_room == "Virgil Hospital" or st.session_state.current_room == "Easy Apartment") and not st.session_state.survivor_event:
##            can_move = survivor_event()
##            if not can_move:
##                return

##        if st.session_state.current_room in "Drytron Mall": #and not st.session_state.survivor_event:
##            st.write(f'{rooms["Drytron Mall"]["survivor"]}')
##            st.write(f'{rooms["Drytron Mall"]["survivor_event"]}')
##
##            # if the user beats the survivor event
####            rooms["Drytron Mall"]["survivor_event"] = False
##            # if the user does not beat the survivor event
##
####            st.write("You hear someone yelling for help somewhere in the mall.")
####            st.write("\"I-is someone there? H-hello?\"")
####            st.write("You turn the corner to see a man trapped underneath of a shelf.")
####            st.write("\"Oh thank god! Someone that isn\'t a zombie. Can you help me out?\"")
##            #survivor_event()
##            

            
            
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
##            st.write(f'{st.session_state.current_room}')
        except:
            pass
        
        if st.session_state.current_room == "The Suburbs" and not st.session_state.traffic_event:
            can_move = hoard_event()
            if not can_move:
                return

        if st.session_state.current_room == "Drytron Mall" and not st.session_state.survivor_event:
            can_move = survivor_event()
            if not can_move:
                return
            
##        if st.session_state.current_room in rooms and "survivor_event" in rooms[st.session_state.current_room] and rooms[st.session_state.current_room]["survivor_event"]:
##            can_move = survivor_event()
##            if not can_move:
##                return


       #if st.session_state.current_room in "Drytron Mall" and not st.session_state.survivor_event:
            #st.write(f'{rooms["Drytron Mall"]["survivor"]}')
            #st.write(f'{rooms["Drytron Mall"]["survivor_event"]}')

            # if the user beats the survivor event
           # rooms["Drytron Mall"]["survivor_event"] = False
            # if the user does not beat the survivor event

##            st.write("You hear someone yelling for help somewhere in the mall.")
##            st.write("\"I-is someone there? H-hello?\"")
##            st.write("You turn the corner to see a man trapped underneath of a shelf.")
##            st.write("\"Oh thank god! Someone that isn\'t a zombie. Can you help me out?\"")
            #survivor_event()
            
            
##        if (st.session_state.current_room == "Drytron Mall" or st.session_state.current_room == "Virgil Hospital" or st.session_state.current_room == "Easy Apartment") and not st.session_state.survivor_event:
##            can_move = survivor_event()
##            if not can_move:
##                return
##            if st.session_state.current_room == "Drytron Mall": #and not st.session_state.survivor_event:
##                st.write(f'{st.session_state.current_room["Drytron Mall"]["survivor"]}')
##                st.write(f'{st.session_state.current_room["Drytron Mall"]["survivor_event"]}')
##                st.session_state.current_room["Drytron Mall"]["survivor_event"] = False

if __name__ == "__main__":
    main()
    

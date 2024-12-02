<<<<<<< Updated upstream
# Zombie_game2.py

# What increases in value the less you have?
# FRIENDS! 

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
=======
import streamlit as st
import random
>>>>>>> Stashed changes


class MiniGame:
    """Base class for mini-games"""

    def __init__(self):
        self.is_complete = False
        self.was_successful = False

    def initialize_state(self):
        pass

    def render(self):
        pass

    def update(self):
        pass


class ZombieHordeGame(MiniGame):
    """Mini-game for sneaking past zombie horde"""

    def __init__(self):
        super().__init__()
        self.state_key = "horde_game_state"

    def initialize_state(self):
        if self.state_key not in st.session_state:
            st.session_state[self.state_key] = {
                "secret_number": random.randint(1, 40),
                "guesses_remaining": 8,
                "last_guess": None,
                "message": None
            }

    def render(self):
        state = st.session_state[self.state_key]

        st.write("A massive horde of zombies blocks the street ahead.")
        st.write("You need to move very carefully to sneak past them...")
        st.write(f"You have {state['guesses_remaining']} chances to move quietly.")

        if state["message"]:
            if "success" in state["message"]:
                st.success(state["message"])
            elif "warning" in state["message"]:
                st.warning(state["message"])
            elif "error" in state["message"]:
                st.error(state["message"])

        col1, col2 = st.columns([3, 1])
        with col1:
            guess = st.number_input("Pick a number between 1 and 40 to determine how quietly you move:",
                                    min_value=1,
                                    max_value=40,
                                    key="horde_guess")
        with col2:
            return st.button("Move", key="horde_submit"), guess

    def update(self, player_input):
        submitted, guess = player_input
        if not submitted:
            return

<<<<<<< Updated upstream
def survivor_event():
    if "survivor_name_list" not in st.session_state:
        st.session_state.surivor_name_list = ["name1","name2","name3","name4","name5"]
    if "survivor_game_state" not in st.session_state:
        st.session_state.survivor_game_state = {
                "save_cost":random.randint(1,3),
                "game_active": True,
                "survivor_name": random.choice(st.session_state.survivor_name_list),
                "show_transition": False
            }
    game_state = st.session_state.survivor_game_state

    if game_state["show_transition"]:
        st.write("Good job ") # Fill out later
        if st.button("continue on"):
            st.session_state.survivor_event = True
        return False
    st.write("You see a survivor on the street")
    del st.session_state.survivor_name_list[game_state["survivor_name"]]

    if game_state["survivor_name"] == "name1":
        st.write("backstory")

    elif game_state["survivor_name"] == "name2":
        st.write("backstory")
        
    elif game_state["survivor_name"] == "name3":
        st.write("backstory")

    elif game_state["survivor_name"] == "name4":
        st.write("backstory")

    elif game_state["survivor_name"] == "name5":
        st.write("backstory")
    else:
        st.error("error")
        return

    col1, col2 = st.columns(2)

    with col1:
        if st.button("Save the survivor", key = "save"):
            st.write("You saved them")
            st.session_state.time -= game_state["save_cost"]
            game_state["game_active"] = False
            game_state["show_transition"] = True

=======
        state = st.session_state[self.state_key]
        if guess == state["secret_number"]:
            state["message"] = "success: You successfully sneak past the horde!"
            self.is_complete = True
            self.was_successful = True
        else:
            state["guesses_remaining"] -= 1
            if state["guesses_remaining"] <= 0:
                state["message"] = "error: The zombies spotted you!"
                self.is_complete = True
                self.was_successful = False
            else:
                hint = "higher" if guess < state["secret_number"] else "lower"
                state["message"] = f"warning: Try moving {hint}. {state['guesses_remaining']} attempts remaining."

        state["last_guess"] = guess
        st.session_state[self.state_key] = state


class SurvivorEvent:
    """Class to handle survivor encounters"""

    def __init__(self, survivor_name, time_cost=None):
        self.survivor_name = survivor_name
        self.time_cost = time_cost or random.randint(1, 3)
        self.is_complete = False
        self.was_successful = False

    def render(self):
        st.write(f"You encounter {self.survivor_name} who needs help!")
        st.write(f"It will take {self.time_cost} hours to help them.")

        col1, col2 = st.columns(2)
        with col1:
            if st.button("Save the survivor", key=f"save_{self.survivor_name}"):
                self.was_successful = True
                self.is_complete = True
                return True
>>>>>>> Stashed changes
        with col2:
            if st.button("Leave them behind", key=f"leave_{self.survivor_name}"):
                self.was_successful = False
                self.is_complete = True
                return True
        return False

<<<<<<< Updated upstream
    st.session_state.zombie_game_state = game_state
    st.rerun()
    show_status()
    return not game_state["game_active"] and not game_state["show_transition"]



def lose():
    st.write("You lose")
    st.session_state.feeling_brave = False
    return 
=======

class ZombieGame:
    def __init__(self):
        self.initialize_game_state()
        self.initialize_rooms()
        self.current_minigame = None
        self.current_survivor_event = None

    def initialize_game_state(self):
        if "game_state" not in st.session_state:
            st.session_state.game_state = {
                "current_room": "Camp Goodman",
                "time_remaining": 12,
                "events_completed": set(),
                "survivors_saved": set(),
                "is_game_over": False
            }

    def initialize_rooms(self):
        self.rooms = {
            'Camp Goodman': {
                'exits': {'right': 'Drytron Mall'},
                'description': "A once peaceful campground, now eerily quiet.",
                'image': "./images/Contacts_github.png"
            },
            'Drytron Mall': {
                'exits': {
                    'left': 'Camp Goodman',
                    'right': 'parking lot',
                    'down': 'The Suburbs'
                },
                'description': "You walk past the empty stalls of the once popular mall.",
                'image': "./images/Drytronmall1.jpg",
                'event': {
                    'type': 'survivor',
                    'survivor': SurvivorEvent("Drew"),
                    'description': "You hear someone calling for help from inside the mall."
                }
            },
            'The Suburbs': {
                'exits': {
                    'up': 'Drytron Mall',
                    # 'down': "Schuyler's Seaside Saloon",
                    # 'left': 'Amazement Land',
                    # 'right': 'Virgil Hospital'
                },
                'description': "Abandoned houses line the streets. A horde of zombies blocks your path.",
                'image': "./images/Contacts_github.png",
                'event': {
                    'type': 'minigame',
                    'game': ZombieHordeGame(),
                    'failure_message': "The zombies spot you. Game Over!",
                    'success_message': "You successfully sneak past the horde!"
                }
            }
            # ... other rooms ...
        }

    def handle_movement(self, direction):
        current = st.session_state.game_state["current_room"]
        if direction in self.rooms[current]['exits']:
            st.session_state.game_state["current_room"] = self.rooms[current]['exits'][direction]
            st.session_state.game_state["time_remaining"] -= 1
            return True
        return False

    def handle_survivor_event(self, room_name):
        """Handle survivor encounters"""
        room = self.rooms[room_name]
        if 'event' not in room or room['event']['type'] != 'survivor':
            return None

        if room_name not in st.session_state.game_state["events_completed"]:
            survivor = room['event']['survivor']
            if not survivor.is_complete:
                st.write(room['event']['description'])
                if survivor.render():  # If the event is complete
                    if survivor.was_successful:
                        st.session_state.game_state["time_remaining"] -= survivor.time_cost
                        st.session_state.game_state["survivors_saved"].add(survivor.survivor_name)
                        st.success(f"You saved {survivor.survivor_name}!")
                    else:
                        st.warning(f"You left {survivor.survivor_name} behind...")
                    st.session_state.game_state["events_completed"].add(room_name)
                    return True
            return False
        return None

    def handle_minigame(self, room_name):
        """Handle mini-game events"""
        room = self.rooms[room_name]
        if 'event' not in room or room['event']['type'] != 'minigame':
            return None

        if room_name not in st.session_state.game_state["events_completed"]:
            if self.current_minigame is None:
                self.current_minigame = room['event']['game']
                self.current_minigame.initialize_state()

            player_input = self.current_minigame.render()
            self.current_minigame.update(player_input)

            if self.current_minigame.is_complete:
                if self.current_minigame.was_successful:
                    st.success(room['event']['success_message'])
                    st.session_state.game_state["events_completed"].add(room_name)
                else:
                    st.error(room['event']['failure_message'])
                    st.session_state.game_state["is_game_over"] = True
                self.current_minigame = None
                return True
            return False
        return None

    def show_status(self):
        st.write("-" * 80)
        current_room = st.session_state.game_state["current_room"]
        st.write(f"Location: {current_room}")
        st.image(self.rooms[current_room]['image'])
        st.write(self.rooms[current_room]['description'])
        st.write(f"Time remaining: {st.session_state.game_state['time_remaining']} hours")
        if st.session_state.game_state["survivors_saved"]:
            st.write(f"Survivors saved: {', '.join(st.session_state.game_state['survivors_saved'])}")
        st.write("-" * 80)

    def run(self):
        if st.session_state.game_state["is_game_over"]:
            st.error("Game Over!")
            if st.button("Restart Game"):
                del st.session_state.game_state
                st.rerun()
            return

        self.show_status()
        current_room = st.session_state.game_state["current_room"]

        # Handle any events in the current room
        if self.handle_survivor_event(current_room) is not None:
            return
        if self.handle_minigame(current_room) is not None:
            return

        # Handle movement
        move = st.text_input("Enter your move (e.g., 'go left', 'go right')", key="move_input")
        if move:
            parts = move.lower().split()
            if len(parts) == 2 and parts[0] == "go":
                if self.handle_movement(parts[1]):
                    st.rerun()
                else:
                    st.error("You can't go that way!")

        # Check win/lose conditions
        if current_room == "BKT Airport":
            st.success("You made it to safety!")
            if st.button("Play Again"):
                del st.session_state.game_state
                st.rerun()
        elif st.session_state.game_state["time_remaining"] <= 0:
            st.session_state.game_state["is_game_over"] = True
            st.rerun()
>>>>>>> Stashed changes


def main():
    st.title("Zombie Escape")

    if "game_initialized" not in st.session_state:
        st.write("""
        You were camping at Camp Goodman when an emergency alert appeared on your phone:
        *EMERGENCY ALERT* PEOPLE ARE BEING INFECTED BY A BRAIN CONTROLLING PARASITE
        EVACUATIONS HAVE STARTED

        Your car won't start - you'll have to make it to the evacuation point on foot!
        """)
        st.image("./images/Zombie_Game_map.png")
        st.session_state.game_initialized = True
<<<<<<< Updated upstream
    show_intro()
    
    if st.session_state.feeling_brave:
        if st.session_state.current_room == "The Suburbs" and not st.session_state.traffic_event:
            can_move = hoard_event()
            if not can_move:
                return

        if (st.session_state.current_room == "Drytron Mall" or st.session_state.current_room == "Vigil Hospital" or st.session_state.current_room == "Easy Apartment") and not st.session_state.survivor_event:
            can_move = survivor_event()
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
            
        if (st.session_state.current_room == "Drytron Mall" or st.session_state.current_room == "Vigil Hospital" or st.session_state.current_room == "Easy Apartment") and not st.session_state.survivor_event:
            can_move = survivor_event()
            if not can_move:
                return
=======

    game = ZombieGame()
    game.run()
>>>>>>> Stashed changes

if __name__ == "__main__":
    main()
import streamlit as st
import random


# ending event
# cutscene about the people you saved
# losing event
#
# if you run out of time there should be something that plays a cutscene about that
# adds on text from the characters you saved
# if you saved drew you would get drew's text
# if you didnt save alexander you wouldnt get his text
#
# Lose time if you fail a question in horde event
# time - questions wrong / 2 (or floor divide)
#
# Skipping places
# After completing survivor event
# maybe after the hoard event


# MiniGame Class
# Base/Blueprint of all minigames

class MiniGame:

    def __init__(self):
        self.is_complete = False
        self.was_successful = False

    def initialize_state(self):
        pass

    def render(self):
        pass

    def update(self):
        pass

# ZombieHordeGame Class (Child of MiniGame class)
# Minigame for sneaking past zombie horde
# intialize_state
# render
# update


class ZombieHordeGame(MiniGame):

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

# SurvivorEvent Class
# Class to handle survivor encounters
# No children?
# Render

class SurvivorEvent:

    def __init__(self, survivor_name,time_cost = None):
        self.state_key = f'survivor_{survivor_name}_state'
        self.survivor_name = survivor_name
##        self.time_cost = random.randint(1, 3)
        self.is_complete = False
        self.was_successful = False
        self.init_state(time_cost)

    def init_state(self,time_cost):
        if self.state_key not in st.session_state:
            st.session_state[self.state_key] = {
                'time_cost': time_cost if time_cost is not None else random.randint(1,3)
            }
        self.time_cost = st.session_state[self.state_key]["time_cost"]

    def render(self):
        st.write(f"You encounter {self.survivor_name} who needs help!")
        st.write(f"It will take {self.time_cost} hours to help them.")

        col1, col2 = st.columns(2)
        with col1:
            if st.button("Save the survivor", key=f"save_{self.survivor_name}"):
                self.was_successful = True
                self.is_complete = True
                return True
        with col2:
            if st.button("Leave them behind", key=f"leave_{self.survivor_name}"):
                self.was_successful = False
                self.is_complete = True
                return True
        return False

# ZombieGame Class
# Main class runs everything
# No children
# initalize_game_state
# initialize_rooms
# handle_movement
# handle_survivor_event
# handle_minigame
# show_status
# run

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
                    'right': 'Fletcher\'s Car Center',
                    'down': 'Amazement Land'
                },
                'description': "You walk past the empty stalls of the once popular mall.",
                'image': "./images/Drytronmall1.jpg",
                'event': {
                    'type': 'survivor',
                    'survivor': SurvivorEvent("Drew"),
                    'description': "You hear someone calling for help from inside the mall."
                }
            },
            'Fletcher\'s Car Center': {
                'exits': {
                    'left': 'Drytron Mall',
                    'down':'The Suburbs'          
                },
                'description': "A once peaceful campground, now eerily quiet.",
                'image': "./images/Contacts_gmail.png"
            },
            'Amazement Land': {
                'exits': {
                    'right':'The Suburbs',
                    'up':'Drytron Mall'
                    },
                'description': "A once peaceful campground, now eerily quiet.",
                'image': "./images/Contacts_github.png"
            },
            'The Suburbs': {
                'exits': {
                    'up': 'Drytron Mall',
                     'down': 'Schuyler\'s Seaside Saloon',
                     'left': 'Amazement Land',
                     'right': 'Virgil Hospital'
                },
                'description': "Abandoned houses line the streets. A horde of zombies blocks your path.",
                'image': "./images/Contacts_github.png",
                'event': {
                    'type': 'minigame',
                    'game': ZombieHordeGame(),
                    'failure_message': "The zombies spot you. Game Over!",
                    'success_message': "You successfully sneak past the horde!"
                }
            },
            'Virgil Hospital': {
                'exits': {
                    'left':'The Suburbs',
                    'down':'Easy Apartment'
                    },
                'description': "A once peaceful campground, now eerily quiet.",
                'image': "./images/Contacts_github.png",
                'event': {
                    'type': 'survivor',
                    'survivor': SurvivorEvent("Alexander"),
                    'description': "You hear labored breathing in a nearby room in the hospital ward."
                }
        },
            'Schuyler\'s Seaside Saloon': {
                'exits': {
                    'up': 'The Suburbs',
                    'right':'Easy Apartment'          
                },
                'description': "A once peaceful campground, now eerily quiet.",
                'image': "./images/Contacts_github.png"
            },
            'Easy Apartment': {
                'exits': {
                    'up':'Virgil Hospital',
                    'left':'Schuyler\'s Seaside Saloon',
                    'right':'BKT Airport'
                    },
                'description': "A once peaceful campground, now eerily quiet.",
                'image': "./images/Contacts_github.png",
                'event': {
                    'type': 'survivor',
                    'survivor': SurvivorEvent("David"),
                    'description': "You hear a baby crying in a nearby room"
                }
        },
            'BKT Airport': {
                'exits': {},
                'description': "A once peaceful campground, now eerily quiet.",
                'image': "./images/Contacts_github.png"
                # event to handle the end of the game
                # You interact with the people you saved
##                'event': {
##                    'type': 'survivor',
##                    'survivor': SurvivorEvent("Drew"),
##                    'description': "You hear someone calling for help from inside the mall."
##                }
            }
    } # the end
            
            

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
                        st.write(f'{type(survivor)}')
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
        st.image("./images/Zombie_Game_map.png")
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
                del st.session_state.state_key
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

# Main
# Starts the game

def main():
    st.title("Zombie Escape")

    if "game_initialized" not in st.session_state:
        st.write("""
        You were camping at Camp Goodman when an emergency alert appeared on your phone:
        *EMERGENCY ALERT* PEOPLE ARE BEING INFECTED BY A BRAIN CONTROLLING PARASITE
        EVACUATIONS HAVE STARTED

        Your car won't start - you'll have to make it to the evacuation point on foot!
        """)
        st.session_state.game_initialized = True

    game = ZombieGame()
    game.run()


if __name__ == "__main__":
    main()

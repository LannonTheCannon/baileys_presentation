import streamlit as st
import random

class MiniGame:
    def __init__(self):
        self.is_complete = False
        self.was_successful = False
        

    def initialize_state(self):
        pass

    def render(self):
        pass

    def update(self, player_input):
        pass


class ZombieHordeGame(MiniGame):
    def __init__(self,state_key = "horde_game_state"):
        super().__init__()
        self.state_key = state_key

    def initialize_state(self):
        if self.state_key not in st.session_state:
            st.session_state[self.state_key] = {
                "secret_number": random.randint(1, 40),
                "guesses_remaining": 8,
                "wrong_guesses": 0,
                "last_guess": None,
                "message": None
            }

    def render(self):
        state = st.session_state[self.state_key]

        st.write("A massive horde of zombies blocks the street ahead.")
        st.write("You need to move **very** carefully to sneak past them...")
        st.write(f"You have **{state['guesses_remaining']}** chances to move quietly.")
##        st.write("Pick a number between 1 and 40 to sneak past the horde")

        if state["message"]:
            if "success" in state["message"]:
                st.success(state["message"])
            elif "warning" in state["message"]:
                st.warning(state["message"])
            elif "error" in state["message"]:
                st.error(state["message"])

        col1, col2 = st.columns([3, 1])
        with col1:
            guess = st.number_input(
                "Pick a number between 1 and 40 to continue:",
                min_value=1, max_value=40,
                key="horde_guess"
            )
        with col2:
            submitted = st.button("Move", key="horde_submit")

        return submitted, guess

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
            state["wrong_guesses"] += 1
            if state["guesses_remaining"] <= 0:
                state["message"] = "error: The zombies spotted you!"
                self.is_complete = True
                self.was_successful = False
            else:
                hint = "higher" if guess < state["secret_number"] else "lower"
                st.write(f'The secret number is {state["secret_number"]}')
                state["message"] = f"warning: Try moving {hint}. {state['guesses_remaining']} attempts remaining."

        state["last_guess"] = guess
        st.session_state[self.state_key] = state


class SurvivorEvent:
    def __init__(self, survivor_name, time_cost=None, cutscene_text=None):
        self.state_key = f'survivor_{survivor_name}_state'
        self.survivor_name = survivor_name
        self.is_complete = False
        self.was_successful = False
        self.cutscene_text = cutscene_text or f"{survivor_name} thanks you profusely for saving them."
        self.init_state(time_cost)

    def init_state(self, time_cost):
        if self.state_key not in st.session_state:
            st.session_state[self.state_key] = {
                'time_cost': time_cost if time_cost is not None else random.randint(1, 3)
            }
        self.time_cost = st.session_state[self.state_key]["time_cost"]

    def render(self):
        st.write(f"You encounter **{self.survivor_name}** who needs help!")
        st.write(f"It will take **{self.time_cost}** hours to help them.")

        col1, col2 = st.columns(2)
        with col1:
            if st.button(f"Save {self.survivor_name}", key=f"save_{self.survivor_name}"):
                self.was_successful = True
                self.is_complete = True
                return True
        with col2:
            if st.button(f"Leave {self.survivor_name} behind", key=f"leave_{self.survivor_name}"):
                self.was_successful = False
                self.is_complete = True
                return True
        return False


class ZombieGame:
    def __init__(self):
        self.initialize_game_state()
        self.initialize_rooms()
        self.current_minigame = None  # Will hold the minigame object (e.g., ZombieHordeGame)

    def initialize_game_state(self):
        if "game_state" not in st.session_state:
            st.session_state.game_state = {
                "current_room": "Camp Goodman",
                "time_remaining": 12,
                "events_completed": set(),
                "survivors_saved": set(),
                "is_game_over": False,
                "game_ending": None,
                "can_skip": False
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
                    'right': "Fletcher's Car Center",
                    'down': 'Amazement Land'
                },
                'description': "You walk past the empty stalls of the once-popular mall.",
                'image': "./images/Drytronmall1.jpg",
                'event': {
                    'type': 'survivor',
                    'survivor': SurvivorEvent(
                        "Drew",
                        cutscene_text="Drew: Thank you for saving me! I'm a former military medic, I can help treat injuries."
                    ),
                    'description': "You hear someone calling for help from inside the mall."
                }
            },
            "Fletcher's Car Center": {
                'exits': {
                    'left': 'Drytron Mall',
                    'down': 'The Suburbs'
                },
                'description': "An auto repair shop littered with wrenches. Undead lurk near the lifts.",
                'image': "./images/Contacts_github.png",
                'event': {
                    'type': 'minigame',
                    'game': ZombieHordeGame(state_key = "zombie_horde_car_center"),
                    'success_message': "You quietly fix the car's ignition and slip away!",
                    'failure_message': "Your clumsy repairs make too much noise... the horde arrives!",
                    'description': "Try to guess how quietly you can fix the car while zombies lurk outside."
                }
            },
            'Amazement Land': {
                'exits': {
                    'up':'Drytron Mall',
                    'right': 'The Suburbs'
                },
                'description': "A work in progress theme park stands infront of you.",
                'image': "./images/Contacts_gmail.png"
            },
            "The Suburbs": {
                'exits': {
                    'up': "Fletcher's Car Center",
                    'down': "Schuyler's Seaside Saloon",
                    'left': 'Amazement Land',
                    'right': 'Virgil Hospital'
                },
                'description': "You see a street filled with empty cars and open home doors",
                'image': "./images/Contacts_gmail.png",
                'event': {
                    'type': 'minigame',
                    'game': ZombieHordeGame(state_key = "zombie_horde_suburbs"),
                    'success_message': "You quietly sneak past the horde of zombie",
                    'failure_message': "You unsuccessfully attempted to sneak past the horde", # reword later
                    'description': "Sneak past the horde of zombies." # reword later
                }
            },
            "Schuyler's Seaside Saloon": {
                'exits': {
                    'up': 'The Suburbs',
                    'right': 'Easy Apartment'
                },
                'description': "One of the most popular spots by the beach is now empty",
                'image': "./images/Contacts_github.png"
            },
            'Virgil Hospital': {
                'exits': {
                    'left': 'The Suburbs',
                    'down': 'Easy Apartment'
                },
                'description': "Something something hospital.",
                'image': "./images/Drytronmall1.jpg",
                'event': {
                    'type': 'survivor',
                    'survivor': SurvivorEvent(
                        "Alex",
                        cutscene_text="Alex: Thank you for saving me! I'm a former military medic, I can help treat injuries."
                    ),
                    'description': "You hear someone calling for help from inside the hospital."
                }
            },
            'Easy Apartment': {
                'exits': {
                    'up':'Virgil Hospital',
                    'left': "Schuyler's Seaside Saloon",
                    'right': 'The Suburbs'
                }, # Add a new event???
                'description': "You heard about this place from an ad.",
                'image': "./images/Contacts_gmail.png"
            },
            'BKT Airport': {
                'exits': {},
                'description': "You've reached the evacuation point.",
                'image': "./images/Contacts_github.png",
                'event': {
                    'type': 'ending',
                    'description': "You've made it to the airport!"
                }
            }
        }

    def show_status(self):
        """
        Always show room description, image, and general status (time, survivors).
        """
        st.image("./images/Zombie_Game_map.png")
        st.write("-" * 80)

        current_room = st.session_state.game_state["current_room"]
        st.write(f"**Location:** {current_room}")
        st.image(self.rooms[current_room]['image'])
        st.write(self.rooms[current_room]['description'])
        st.write(f"**Time remaining:** {st.session_state.game_state['time_remaining']} hour(s)")
        if st.session_state.game_state["survivors_saved"]:
            st.write(f"**Survivors saved:** {', '.join(st.session_state.game_state['survivors_saved'])}")
        st.write("-" * 80)

    def handle_survivor_event(self, room_name):
        """
        Shows the survivor event if it hasn't been completed yet.
        Always returns None if there's no event or it's already completed.
        """
        room = self.rooms[room_name]
        if 'event' not in room or room['event']['type'] != 'survivor':
            return None

        # If this event was already completed before, skip re-playing it
        if room_name in st.session_state.game_state["events_completed"]:
            return None

        # Otherwise, it's a new or unfinished event:
        survivor = room['event']['survivor']
        st.write(room['event']['description'])
        if survivor.render():
            # The user made a choice
            if survivor.was_successful:
                st.session_state.game_state["time_remaining"] -= survivor.time_cost
                st.session_state.game_state["survivors_saved"].add(survivor.survivor_name)
                st.success(f"You saved {survivor.survivor_name}!")
                # Optionally enable skipping after saving a survivor
                st.session_state.game_state["can_skip"] = True
            else:
                st.warning(f"You left {survivor.survivor_name} behind...")
            st.session_state.game_state["events_completed"].add(room_name)
            return True
        return False

    def handle_minigame(self, room_name):
        """
        Shows the minigame event if it hasn't been completed yet.
        """
        room = self.rooms[room_name]
        if 'event' not in room or room['event']['type'] != 'minigame':
            return None

        # If this event was already completed, do nothing
        if room_name in st.session_state.game_state["events_completed"]:
            return None

        # If we don't have an active minigame yet, set it up
        if self.current_minigame is None:
            self.current_minigame = room['event']['game']
            self.current_minigame.initialize_state()

        # Show the minigame description once
        st.write(f"**Minigame Event:** {room['event']['description']}")
        player_input = self.current_minigame.render()
        self.current_minigame.update(player_input)

        if self.current_minigame.is_complete:
            if self.current_minigame.was_successful:
                st.success(room['event']['success_message'])
                # Time penalty for wrong guesses
                wrong_guesses = st.session_state[self.current_minigame.state_key]["wrong_guesses"]
                time_penalty = wrong_guesses // 2
                st.session_state.game_state["time_remaining"] -= time_penalty
                if time_penalty > 0:
                    st.warning(f"You lost {time_penalty} hour(s) making noise!")
                st.session_state.game_state["events_completed"].add(room_name)
            else:
                st.error(room['event']['failure_message'])
                st.session_state.game_state["is_game_over"] = True
                st.session_state.game_state["game_ending"] = "caught"

            # Clear the minigame from memory
            self.current_minigame = None
            return True
        return False

    def handle_movement(self, direction):
        current = st.session_state.game_state["current_room"]
        # If the direction is valid, move the player and subtract one hour
        if direction in self.rooms[current]['exits']:
            st.session_state.game_state["current_room"] = self.rooms[current]['exits'][direction]
            st.session_state.game_state["time_remaining"] -= 1
            return True
        return False

    def show_ending_cutscene(self):
        ending_type = st.session_state.game_state["game_ending"]
        if ending_type == "success":
            st.success("You've made it to the airport!")
            saved_survivors = st.session_state.game_state["survivors_saved"]
            if not saved_survivors:
                st.write("You made it out alone, wondering about those you left behind...")
            else:
                st.write("The survivors you helped gather around to share their gratitude:")
                for survivor_name in saved_survivors:
                    st.write(f"* {survivor_name} thanks you personally.")
        elif ending_type == "caught":
            st.error("The zombies caught you! Your journey ends here...")
        elif ending_type == "timeout":
            st.error("You ran out of time! The evacuation proceeded without you...")

    def run(self):
        if st.session_state.game_state["is_game_over"]:
            self.show_ending_cutscene()
            if st.button("Restart Game"):
                for key in list(st.session_state.keys()):
                    del st.session_state[key]
                st.rerun()
            return

        # Always show the current room's status, description, etc.
        self.show_status()
        current_room = st.session_state.game_state["current_room"]

        # Now handle events in the current room (minigame/survivor)
        # The handle functions won't do anything if the event is already completed.
        event_handled = self.handle_survivor_event(current_room)
        if event_handled is not None:
            return  # If the user just finished the event, wait for next rerun

        event_handled = self.handle_minigame(current_room)
        if event_handled is not None:
            return

        # OPTIONAL: skip feature if enabled
        if st.session_state.game_state["can_skip"] and current_room != "BKT Airport":
            if st.button("Skip to next location"):
                possible_exits = list(self.rooms[current_room]['exits'].values())
                if possible_exits:
                    st.session_state.game_state["current_room"] = possible_exits[0]
                    st.session_state.game_state["time_remaining"] -= 1
                    st.rerun()

        # Text input movement
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
            st.session_state.game_state["is_game_over"] = True
            st.session_state.game_state["game_ending"] = "success"
            st.rerun()
        elif st.session_state.game_state["time_remaining"] <= 0:
            st.session_state.game_state["is_game_over"] = True
            st.session_state.game_state["game_ending"] = "timeout"
            st.rerun()


def main():
    st.title("Zombie Escape")

    if "game_initialized" not in st.session_state:
        st.write("""
            You were camping at Camp Goodman when an emergency alert appeared on your phone:
            *EMERGENCY ALERT* PEOPLE ARE BEING INFECTED BY A BRAIN CONTROLLING PARASITE
            EVACUATIONS HAVE STARTED

            Your car won't start - you'll have to make it to the evacuation point on foot!
            Try to save as many survivors as you can, but be careful - you only have 12 hours 
            before the last evacuation flight leaves!
        """)
        st.session_state.game_initialized = True

    game = ZombieGame()
    game.run()

if __name__ == "__main__":
    main()

# Zombie_game2.py

import random
import streamlit as st
#from utils_pages import change_bg

if "current_room" not in st.session_state:
    current_room = 'woods'

if "feeling_brave" not in st.session_state:
    feeling_brave = True

inventory = []
health = 100
tasks = []
points = 0
guessgame_count = 0

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
        'left':'construction lot',
        'right':'graveyard',
        'task':'guessing_game'},
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

def show_intro():
    st.write('''

You are a survior of a zombie apocalypse. There is a strong zombie chasing you.
You can kill it or escape to your car. Which will you do? test

commands:
go[up,down,left,right]
get[item]

''')

def show_status():
    st.write("++++++++++++++++++++++++++++++++++++++++++++++++")
    st.write(f'You are currently in {current_room}')
    st.write(f'The zombie is in {monster_room}')
    if  'item' in rooms[current_room]:
        st.write(f"You see a {rooms[current_room]['item']}")
    st.write(f' Points: {points}')
    st.write(f'Inventory: {inventory}')
    st.write("++++++++++++++++++++++++++++++++++++++++++++++++")
    if current_room == 'car':
        st.write("You drive away...")


def main():
    show_intro()
    st.write(st.session_state.feeling_brave)
    while st.session_state.feeling_brave == True:
        show_status()
        move = st.text_input('Enter An Action','>  ') 
        move = move.lower().split()
##        if move[0] == 'go' :
##            if move[1] in rooms[current_room]:
##                current_room = rooms[current_room][move[1]]
##            else:
##                print("you ran into a wall")
##        if monster_health > 0:
##            random.shuffle(monster_moves)
##            for move in monster_moves:
##                if  move  in rooms[monster_room]:
##                    monster_move = move
##                    break
##            monster_room = rooms[monster_room][monster_move]

if __name__ == "__main__":
    main()
    

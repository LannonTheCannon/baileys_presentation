#  Escape  Escape Room Simulator

import random
import streamlit as st
#from utils_pages import change_bg



# create a def that stores intro

def show_intro():
    st.write('''

You are a survior of a zombie apocalypse. There is a strong zombie chasing you.
You can kill it or escape to your car. Which will you do?

commands:
go[up,down,left,right]
get[item]

''')

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
    

                                            

def check_guess(response, answer):
    pass
##    global score
##    global health
##    global monster_health
##    global count
##    if reasponse == answer:
##        st.write("you shot at the zombie")
##        score += 15
##        
##    else:
##        print("The zombie hit you")
##        health -= 15
##        response = input("The zombie is re-charging")
def guessing_game():
    global health
    global points
    global puzzle1_complete
    global guessgame_count
    print('There is a rock in your way...')
    time.sleep(2)
    print('Please pick a number between 1 and 50 to try to lift the rocks')
    time.sleep(2)
    secret_number = random.randint(1,20)
    for x in range(7):
    
        user_num = int(input('Please enter a number: '))

        if user_num < secret_number:
            print('Please try higher')

        elif user_num > secret_number:
            print('Please try lower')
        else:
            print("You moved the rocks")
            break
    if user_num == secret_number:
        points += 15
        guessgame_count += 1
        if guessgame_count == 2:
            puzzle1a_complete = True
        else:
            puzzle1_complete = True
            tasks.append(rooms[current_room]['task'])
            del rooms[current_room]['task']

    else:
        health -= 15




def RPS():


    global health
    global points
    moves = ['rock', 'paper', 'scissor']
    score = 0
    global puzzle2_complete
    for x in range(3):

        player_move = input("Please enter your first move (rock/paper/scissor: ").lower()

        computer_move = random.choice(moves)

        if player_move == computer_move:
            print("There is a tie!")

        elif player_move == "rock":
            if computer_move == "paper":
                print("Player loses")
                score -= 1
            else:
                print("Player wins")
                score += 1

        elif player_move == "paper":
            if computer_move == "scissor":
                print("Player loses")
                score -= 1
            else:
                print("Player wins")
                score += 1
        elif player_move == "scissor":
            if computer_move == "rock":
                print("Player loses")
                score -= 1
            else:
                print("Player wins")
                score += 1

    print(f'You scored {score}')

    if score > 0:
        points = score * 15
        puzzle2_complete = True
        task.append(rooms[current_room]['tasks'])
        del (rooms[current_room]['task'])
        print("You knocked out the flood form")
    else:
        health = health + (score * 15)
        print('the flood won')


def check_monster():
    global monster_health
    global health
    monster_num = random.randint(1,25)
    print("The zombie runs towards you")
    time.sleep(2)
    for x in range(5):
    
        user_num = int(input('Please enter a number to attack the zombie 1-25 : '))

        if user_num < monster_num:
            print('Please try higher')

        elif user_num > monster_num:
            print('Please try lower')
        else:
            print("You knocked the zombie out")
            break
    if user_num == monster_num:
        monster_health += -35
        
        
    else:
        health -= 35
        print("The zombie punched you")

def show_status():
    st.write("++++++++++++++++++++++++++++++++++++++++++++++++")
    st.write(f'You are currently in {current_room}')
    st.write(f'The zombie is in {monster_room}')
##    st.write(f'HP: {health} ')
##    print(f'zombie HP: {monster_health}')
    if  'item' in rooms[current_room]:
        st.write(f"You see a {rooms[current_room]['item']}")
    st.write(f' Points: {points}')
    st.write(f'Inventory: {inventory}')

    st.write("++++++++++++++++++++++++++++++++++++++++++++++++")
    if current_room == 'car':
        st.write("You drive away...")


if "current_room" not in st.session_state:
    current_room = 'woods'
##monster_room = 'rubble'
##monster_moves = ['up','right','down','left']
##monster_health = 100
inventory = []
health = 100
tasks = []
points = 0
guessgame_count = 0

show_intro()

if "feeling_brave" not in st.session_state:
    feeling_brave = True

puzzle1_complete = False
puzzle1a_complete = False
puzzle2_complete = False
puzzle3_complete = False
while st.session_state.feeling_brave == True:
    show_status()
    move = st.text_input('Enter An Action','>  ') 
    move = move.lower().split()
    if move[0] == 'go' :
        if move[1] in rooms[current_room]:
            current_room = rooms[current_room][move[1]]
        else:
            print("you ran into a wall")
    if monster_health > 0:
        random.shuffle(monster_moves)
        for move in monster_moves:
            if  move  in rooms[monster_room]:
                monster_move = move
                break
        monster_room = rooms[monster_room][monster_move]

        
    if move[0] == 'get':
        print(f'{current_room}')
        if 'item' in rooms[current_room] and move[1] == rooms[current_room]['item']:
            print(f'you got the {move[1]}!')
            inventory.append(move[1])
            
            del rooms[current_room]['item']
        else:
            print('sorry you cannot get that item. ')
        


    if current_room == 'building' and puzzle1_complete == False:

        guessing_game()

    if current_room == 'rubble' and puzzle1a_complete == False:

        guessing_game()
        
    if current_room == monster_room:
        check_monster()

### 1 -- method for this game by me using if condition 


# player_name1 = input("Please enter your name, player1?.. ").capitalize()
# player_name2 = input("Please enter your name, player2?.. ").capitalize()
# print(f'Welcome to our \'rock_paper_scissors\' game. Good luck {player_name1} and {player_name2}!!')


# while True:
#     gamer1 = input(f"\tWhat's your choice, {player_name1} ?  'p' Paper,  's' Scissors  and  'r' Rock\n>>>> ")
#     gamer2 = input(f"\tWhat's your choice, {player_name2} ?  'p' Paper,  's' Scissors  and  'r' Rock\n>>>> ")
#     if gamer1 == 'r' and gamer2 == 's':
#         print(f'Congratulations. {player_name1} won!')
#         break
#     elif gamer1 == 's' and gamer2 == 'p':
#         print(f'Congratulations. {player_name1} won!')
#         break
#     elif gamer1 == 'p' and gamer2 == 'r':
#         print(f'Congratulations. {player_name1} won!')
#         break
#     elif gamer2 == 'r' and gamer1 == 's':
#         print(f'Congratulations. {player_name2} won!')
#         break
#     elif gamer2 == 's' and gamer1 == 'p':
#         print(f'Congratulations. {player_name2} won!')
#         break
#     elif gamer2 == 'p' and gamer1 == 'r':
#         print(f'Congratulations. {player_name2} won!')
#         break
#     else:
#         print("You have the same result. Please try again!")



### 2 -- method !!

import random 

def play():
    user = input("\tWhat's your choice ?  'r' Rock,  's' Scissors  and  'p' Paper\n>>> ")
    computer = random.choice(['r', 'p', 's'])
    print(computer)

    if user == computer:
        return "It's the same result"
        
    if is_win(user, computer):
        return 'Congrats. You won! :)'

    return 'You lost game!'

def is_win(player, opponent):
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') \
         or (player == 'p' and opponent == 'r'):
         return True

 
print(play())

import random 
from words import words

def hangman(words):
    mystery_word = random.choice(words).upper()
    while '-' in mystery_word or ' ' in mystery_word:
        mystery_word = random.choice(words)

    print(mystery_word)


# def hangman(words):
#     print('\n', mystery_word)
#     print("\t\t******  Welcome to HANGMAN game!  ******\n")
#     x = input('Enter your name: ').capitalize()
#     x_y = input(f"{x}, do you want to play this game ?  'y' YES  or  'n' NO >> ").lower()
#     gamer_list = []

#     if x_y == 'y':
#         while True:
#             gamer_cho = input("Please enter choice letter: >> ").upper()
#             if gamer_cho in mystery_word:
#                 gamer_list.append(gamer_cho)
#                 print("You choose these letters ", ''.join(gamer_list))


#     else:
        # breakpoint


# def is_win(gamer_choice):

    



hangman(words)




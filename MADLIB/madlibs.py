# name = input("Please enter your name: ")

# print("Subscribe to " + name)
# print("Subscribe to {}".format(name))
# print(f"Subscribe to {name}")

# adj1 = input("Enter adj: ")
# adj2 = input("Enter 2nd adj: ")
# verb1 = input("Enter verb: ")
# famous_person = input("Enter Profession: ")


# matlib = f"I really love programming because it is {adj1} and makes me \
# so {adj2}. I just {verb1} to be {famous_person}!"

# print(matlib)

# import random

# def guess(x):
#     comp_guess = random.randint(1, x)
#     gamer = 0

#     while gamer != comp_guess:
#         gamer = int(input(f"Please enter number between 1 and {x}: "))
#         if gamer > comp_guess:
#             print("Too big")
#         elif gamer < comp_guess:
#             print("Too small")          
      
#     print(f"Congrats! You won and found {comp_guess} :)")

# guess(int(input("Enter range: ")))

# import random

# def comp(x):
#     counter = 0
#     fed = ''
#     while fed != 'c':
#         counter += 1
#         guess = random.randint(1, x)
#         fed = input("Is " + f"{guess} too high (H), too low (L) or correct (C) ?? ".lower())
#         if fed == 'h':
#             high = guess - 1
#         elif fed == 'l':
#             low = guess + 1

#     print(f"The computer have won! The guess number was {guess}. :)")

#     if counter < 4:
#         print("Well done! Thanksgiving :)")
#     else:
#         print("Try again! :(")

# comp(int(input("Please enter your range: ")))

import random

def guess(x):
    counter = 0
    f = ""
    while f != "c":
        counter += 1
        comp_guess = random.randint(1, x)
        f = input("Is " + f"{comp_guess} is too high (H), too low (L) or correct (C) ?..".lower())
        if f == "h":
            h = comp_guess - 1
        elif f == "l":
            l = comp_guess + 1
    
    print("Yay Congrats, the computer have found {comp_guess} successfully!! ")

    if counter >= 5:
        print("Try again :(")
    else:
        print("Well done. Thanksgiving :)")

guess(int(input("Please enter your range: ")))







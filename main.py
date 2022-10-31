# importing modules
from random import randint
from random import choice

# creating batting and bowling functions
def batting(target):
    my_score = 0
    runs = 1
    runs_one = 0
    while runs != runs_one and target >= my_score:
        runs = int(input("How many runs do you choose?"))
        runs_one = randint(1,6)
        if runs != runs_one:
            my_score = my_score + runs
            scoreboard(target, my_score)
        else:
            print("Your innings ends.")
            scoreboard(target, my_score)
    return my_score

def bowling(target):
    comp_score = 0
    runs = 1
    runs_one = 0
    while runs != runs_one and target >= comp_score:
        runs = int(input("How many runs do you choose to bowl?"))
        runs_one = randint(1,6)
        if runs != runs_one:
            comp_score = comp_score + runs_one
            scoreboard(comp_score, target)
        else:
            print("Opponent's innings ends.")
            scoreboard(comp_score, target)
    return comp_score

def scoreboard(comp_score, my_score):
    if comp_score == 100000:
        comp_score = "Yet to play"
    if my_score == 100000:
        my_score = "Yet to play"
    print("----------------------------------")
    print("Opponent's score is:", comp_score)
    print("Your score is:", my_score)
    print("----------------------------------")

print("------------------")
print("Welcome to the hand cricket game.")
print("Created by Raeyaan.")
print("------------------")
# Setting up toss and scores

coin = ("heads" , "tails")
ask = input("Do you call heads or tails?")
decision = ["bat" , "bowl"]
comp_choice = choice(decision)
toss = choice(coin)

# Conducting toss

if ask == toss:
    my_choice = input("You won the toss. Do you want to bat or bowl first.")
    if my_choice == "bat":
        print("You are batting first.")
        my_score = batting(100000)
        print("Now, you are bowling.")
        comp_score = bowling(my_score)
        if comp_score > my_score:
            print("The total was chased down.")
        
    else:
        print(" You are bowling first.")
        comp_score = bowling(100000)
        print("Now, you are batting.")
        my_score = batting(comp_score)
        if my_score > comp_score:
            print("You chased the total down.")
else:
    if comp_choice == "bat":
        print("Opponent won the toss and selected to bat first. You are bowling first.")
        comp_score = bowling(100000)
        print("Now, you are batting.")
        my_score = batting(comp_score)
        if my_score > comp_score:
            print("You chased the total down.")
    else:
        print("Opponent won the toss and selected to bowl first. You are batting first.")
        my_score = batting(100000)
        print("Now, you are bowling.")
        comp_score = bowling(my_score)
        if comp_score > my_score:
            print("The total was chased down.")

# Seeing who wins
if my_score > comp_score:
    margin = int(my_score) - int(comp_score)
    print("You won the game by", margin , "runs.")
elif comp_score > my_score:
    margin = int(comp_score) - int(my_score)
    print("You lost the game by", margin , "runs.")
else:
    print("It was a tie.")

print("Thank you for playing this game.")

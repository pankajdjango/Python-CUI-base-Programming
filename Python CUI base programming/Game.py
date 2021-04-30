import random
options = ['Rock', 'Papers', 'Scissors']

def computers_turn():
    choice = random.choice(options)
    return choice

def users_turn():
    user_choice = input("Choose one: Rock, Papers, Scissors : ")
    if user_choice in options:
        return user_choice
    else:
        print("Oops! Wrong input. ")

def play(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "user"       # user won
    else:
        return "computer"   # computer won

def print_who_won(who_won):
    if who_won == "computer":
        print("Oops! You lost. Computer's choice was : " + computer_choice)
    else:
        print("Yayyy ! You one. You guess it right.")


user_choice = users_turn()                      # get choice from user
computer_choice = computers_turn()              # get choice from computer

who_won = play(user_choice, computer_choice)    # play the game
print_who_won(who_won)  # print who won

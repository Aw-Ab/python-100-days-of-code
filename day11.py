#BlackJack game

import random

cards = [1 , 2, 3 , 4 , 5 , 6 , 7 , 8 , 9 , 10 , 10 , 10 , 10]
err = "Unknown answer !\n Try again "

def playing():     # a loop to keep the game running as long as the player wants |
    wanna_play = input("Do you want to play a game of BlackJack ? 'y'/'n' ").lower()
    if wanna_play == "y" :
        return True
    elif wanna_play == "n" :
         print("See you next time :) ")
         return False
    else :
        print(err)
        playing()

def scores(hand): # a loop to calculate the sum of integers in a list  |
    score = 0
    for card in hand :
        score += card
    return score

def hit(): 
    another = input("Type 'y' to get another card , or 'p' to pass ").lower()
    if another == "y":
        user.append(random.choice(cards))
        print(f"Your cards : {user}") 
        hit()	
    elif another != "p":
        print(err)
        hit()
    while scores(computer) < 17 :
        computer.append(random.choice(cards))



switch = playing()

print("BLACKJACK logo")

while switch :
    computer = [random.choice(cards)]
    user = [random.choice(cards) , random.choice(cards)]

    print(f"Your cards : {user}")
    print(f"computer's first card : {computer[0]}")

    hit()

    computer_score = scores(computer)
    user_score = scores(user)

    print(f"Your final hand {user} | Score : {user_score}")
    print(f"Computer's final hand {computer} | score : {computer_score}")
        
    if computer_score < user_score < 22 or computer_score > 21:
        print(" You WIN !! ")
    elif user_score < computer_score < 22 or user_score > 21 :
        print("The computer WINS !!")
    else :
        print(" DROW !! ")
    # A function to clear the console
    switch = playing()

from game_data import data
from ascii import logo,vs
import random 
6

score = 0
winning = True
temp = random.choice(data)



while winning:

    print(logo)
    if score != 0 :
        print(f"You are correct :) \n Your score --> {score}")

    first = temp
    second = random.choice(data)

    if first['follower_count'] > second['follower_count']:
        correct = "A"
        temp = first
    else:
        correct = "B"
        temp = second

    print(f"Compare A:{first["name"]}, a {first["description"]} , from {first["country"]}")
    print(vs)
    print(f"Against B:{second["name"]}, a {second["description"]} , from {second["country"]}")

    answer = input("Who has more followers? Type 'A' or 'B' :").upper()
    if answer[0] != correct:
        print("Wrong answer ! \n Final score : " + str(score))
        winning = False
    else :
        score += 1
# supposed to be a function that clear the console




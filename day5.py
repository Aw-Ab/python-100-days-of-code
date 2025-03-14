import random

choices =[ "rock" , "paper" , "scissors" ]

user = int(input("Choice : 0 for Rock - 1 for Paper - 2 for Scissors  "))

#the user choice
if user == 0 :
    print("user --> Rock")
elif user == 1:
    print("user --> Paper")    
elif user == 2 :
    print("user --> Scissors")   
else : 
    print("Unknown answer")
    
#choice a random number which represents the computer choice
num = random.randint(0,2)
computer = choices[num]
 
#the computer choice  
if num == 0 :
    print("computer --> Rock")
elif num == 1:
    print("computer --> Paper")    
elif num == 2 :
    print("computer --> Scissors")   


#compare the computer choice to the user choice and see the winner
if user == num :
    print("Draw !")
    exit("No one wins")
elif user == num-1 or  user == num-2:
    print("the computer wins !!")
    exit
elif num == user-1 or num == user-2:
    print("You win !!!")
    exit
#Hangman game 
import random 
from replit import clear
words = ["football" ,"camel", "shotgun","crown"] #just a list of random words 


def letters(string): #a function to generate the blanks for the word
    blanks = []
    for n in range(0,len(string)):
        blanks.append("_")
    return blanks
    
    
    
print("Welcome to Hangman game !")

word = random.choice(words)     # choice a random word from the words list
print(word)

empty = letters(word)      # generate as many blanks as the letters in the "word" [ as a list]
print(empty) 



falts = 0      # a counter for the wrong gusses

while "_" in empty:
    
    empty_word = ""  # A string version of the "empty -word"
    for n in range(0,len(empty)):
        empty_word += empty[n]
    print(empty_word)

    guess = input("Guess a letter :").lower()

    if guess[0] not in word:
        print("wrong")
        falts += 1
        clear()
    if falts == 5 :
        exit("You Lost !!")     
            
    else :
        print("right")
        places = [i for i ,char in enumerate(word) if char == guess[0]]   
        print(places)
        for place in places:
            empty[place] = word[place]
        print(empty)
        clear()
print(empty_word)       
exit("You Win !!")        
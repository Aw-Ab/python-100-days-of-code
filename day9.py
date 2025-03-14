# silent acctuain program 

countune_acctuain = True # Are you sure u need a while loop ?
bidders ={} 

def highest_bid(the_bidders):  #A function to find and ptint out the higher bidder and his bid
    winner = "" # A string to hold the winner name
    highest = 0 # A counter to for the highest bid 
    for bidder in the_bidders:
        amount = the_bidders[bidder]
        if amount > highest:
            highest = amount
            winner = bidder
    print(f"The winner is {winner} for ${highest}")
    
print("👨‍⚖️🔨")

while countune_acctuain :
    name = input("What is your name ? ")
    bid = int(input("What is your bid ? $"))
    bidders[name] = bid
    
    again = input("is there is another bidder ? [yes/no] \n").lower()

    if again == "yes" :
        print("#This function supposed to clear the terminal :)")
        
    elif again == "no" : # At last announce the winner and his pid
        countune_acctuain = False
        highest_bid(bidders)
    
        
         
    
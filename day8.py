#ceaser cipher


def cipher(input ,number):     #here is where is all the MAGIC  
    output = ""
    for letter in input :
        letter =  chr(ord(letter)+number)
        output += letter
    return output    
    
def switch(boolean):  # A switch to control the while loop 
    req = input("Do you want to run the code again ? [Y/N] ").lower()
    if req[0] == "y" :
        boolean = True
    elif req[0] == "n" :
        boolean = False
    else :
        exit("Unknown Request !")
    return boolean     

print("    _____ ______  _____         _____     _____ _____ _____  _    _ ______  _____")   
print("   / ____|  ____|/ ____|  /\   |  __ \   / ____|_   _|  __ \| |  | |  ____|  __ \  ")
print("  | |    | |__  | (___   /  \  | |__) | | |      | | | |__) | |__| | |__  | |__) | ")
print("  | |    |  __|  \___ \ / /\ \ |  _  /  | |      | | |  ___/|  __  |  __| |  _  /  ")
print("  | |____| |____ ____) / ____ \| | \ \  | |____ _| |_| |    | |  | | |____| | \ \  ")
print("   \_____|______|_____/_/    \_\_|  \_\  \_____|_____|_|    |_|  |_|______|_|  \_\ ")

On =True   # A boolean variable to keep the while loop running 

while On:
    request = input("Enter \"encode\" to encode a text , otherwise enter \"decode\" \n  ").lower()
    text = input("Enter your text \n  ")
    key = int(input("Enter the cipher key \n  "))
 
    if request == 'encode':
        display = cipher(text,key)
    elif request == 'decode':
        key -= (key*2) # change the key to be negative 
        display = cipher(text,key)
    else :
        print("Unknown Request !!\n Try again")   
        
    print("\n" + display + "\n")
    
    switch(On)   
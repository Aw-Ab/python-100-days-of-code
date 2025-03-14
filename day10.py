# A calculator
print("🧮")
operations = ["+" , "-" , "*" , "/" , "^" ]
def calculate(number1 ,number2 , symbol):
    if symbol == operations[0]: 
        return number1 + number2 
    elif  symbol == operations[1]: 
        return number1 - number2 
    elif symbol == operations[2]: 
        return number1 * number2 
    elif symbol == operations[3]: 
        return number1 / number2 
    elif     symbol == operations[4]: 
        return pow(number1,number2)
a = float(input("Enter the first number : "))
while True :
    operation = input(f"Enter the operation :  {operations}\n")
    while operation not in operations :
        print("Invalid operation !")
        operation = input(f"Enter the operation :  {operations}\n")
    b = float(input("Enter the second number : "))
    c = calculate(a , b , operation)
    print(f" {a} {operation} {b} = {c}")
    again = input(f"Enter Y to use {c} at next calculate .\nEnter E to exit the calculator,otherwise you will start clear \n ").lower()
    #here is supposed to be a function to clear the console
    if again[0] == "y" :
        a = c 
        print(f"The first number : {a} ")
    elif  again[0] == "e" : 
        exit()
    else :
        a = float(input("Enter the first number : "))
        
    

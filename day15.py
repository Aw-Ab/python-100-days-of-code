#coffee machine

supplies={ # the machine resources and it's wallet
    "water" : 300 ,
    "milk" : 200 ,
    "coffee" : 100 ,
    "money" : 0.00
}

drinks =( #the drinks in the machine and it's details
    {"name" : "espresso" ,
     "water" : 50 ,
     "milk" : 00 ,
     "coffee" : 18 ,
     "cost" : 1.50},
    {"name" : "latte" ,
     "water" : 200 ,
     "milk" : 150 ,
     "coffee" : 150 ,
     "cost" : 2.50},
    {"name" : "cappuccino" ,
     "water" : 250 ,
     "milk" : 100 ,
     "coffee" : 24 ,
     "cost" : 3.00}
)
def cashup(): # A function to calculate the money inserted
    print("|| Insert your coins ||")
    quarters = int(input(" Quarters : "))
    dimes = int(input(" Dimes : "))
    nickles = int(input(" Nickles : "))
    pennies = int(input(" Pennies : "))
    overall = (quarters*0.25)+(nickles*0.05)+(dimes*0.10)+(pennies*0.01)
    return overall


def resources(menu, cup): # A function to check and offer the order based on the resources
   global supplies
   for request in menu: # A loop to check the name of the order from the menu , once the requested drink is found ->
       #-> the machine would check the resources and the inserted money .
         if cup == request["name"] :
           if supplies['water'] >= request["water"] :
               if supplies['milk'] >= request["milk"] :
                   if supplies['coffee'] >= request["coffee"] :
                       print(f"{request['name']} will cost you ${request['cost']}")
                       cash = cashup()
                       if cash >= request["cost"]:
                              supplies['water'] -= request["water"]
                              supplies['milk'] -= request["milk"]
                              supplies['coffee'] -= request["coffee"]
                              print(f"Here is your {request['name']}, Enjoy !")
                              if cash >= (request["cost"] + 0.50):
                                   supplies['money'] += (request["cost"] + 0.50)
                                   cash -= (request["cost"] + 0.50)
                                   print(f"Here is your change ${round(cash , 2)}")
                              else :
                                  supplies['money'] += cash
                       else:
                           print("Sorry that's not enough money.\n Money refunded")
                   else :
                       print("Sorry there is no enough coffee for", request["name"])
               else:
                   print("Sorry there is no enough milk for", request["name"])
           else:
              print("Sorry there is no enough water for", request["name"])



while True:

   order = input("What would you like ? (espresso/latte/cappuccino) : ").lower()
   if order == "report" :
       print(f"Water : {supplies['water']}ml")
       print(f"Milk : {supplies['milk']}ml")
       print(f"Coffee : {supplies['coffee']}g")
       print(f"Money : $ {round(supplies['money'], 2)}")
   elif order == "off" :
       exit()
   elif order not in ['espresso' , 'latte' , 'cappuccino']:
       print("Sorry , unknown order .")
   else :
       resources(drinks , order)
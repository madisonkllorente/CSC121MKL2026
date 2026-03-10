#7.5 Movie Tickets MKL

print("Welcome to Spruce Pines Theater Ticketing Sites")
show = input("Which show are you watching?")
ticketprice = 0

while True:
    age = input("How old is this ticket holder? Type ages of all your tickets numerically.")
    print("Type 'quit' when you're done")
    
    if age == "quit":
        break
    age = int(age)

    if age < 3:
        ticketprice += 0
    elif age <= 12:
     ticketprice += 10
    elif 12 <= age:
        ticketprice += 15
    else:
       print("Please type a numerical age or 'quit' to exit")
    
    
        

print("Your total for ", show, "is:", ticketprice)
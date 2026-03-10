#7.8 Deli MKL

print("Welcome to RICO's SUB n'PUB")
print("Menu: BLT, BEC,Hoagie, Gyro, Reuben, Burger, Grilled Cheese")

sworder = ['BLT','BEC','Hoagie','Gyro','Reuben','Burger','Grilled Cheese']
swmade =[]

while True:
    sw = input("What's ya sandwhich order? Say 'quit' when you're done!")
    
    if sw == "quit":
        break

    print("I made your", sw)
    swmade.append(sw)
    
print("Your sandwiches have been made!")
print(swmade)
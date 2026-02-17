#MKL CSC121 3.4 Guest List Copy for 4.10 Slices Assignment

guests = ['Emily Jones', 'Natalie Ward', 'Miggy Garcia']

for index, value in enumerate(guests):
    print (f"Join me for a delicious meal, {value}, you're seat #{index + 1}.")

print("\nWe have secured 3 additional seats for your plus ones. \n")
guests.insert(1,"Greyson Dembroski")
guests.insert(3, "Thomas Evans")
guests.append("Trinity Skinner")
guests.sort()

for index, value in enumerate(guests):
    print (f"Join me for a delicious meal, {value}, you're seat #{index + 1}.") 

print(f"The first three items in the list are: ") 
for guest in guests[0:3]:
    print(guest.title())

print(f"The middle three items in the list are: ") 
for guest in guests[2:5]:
    print(guest.title())

print(f"The last three items in the list are: ") 
for guest in guests[3:6]:
    print(guest.title())

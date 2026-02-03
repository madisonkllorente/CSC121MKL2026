#MKL CSC121 3.4 Guest List

guests = ['Emily Jones', 'Natalie Ward', 'Miggy Garcia']

for index, value in enumerate(guests):
    print (f"Please join me for a delicious 5 course meal, {value}, you're seat #{index + 1}.")

print("\nI am pleased to announce we have secured 3 additional seats for your plus ones. \n")
guests.insert(1,"Greyson Dembroski")
guests.insert(3, "Thomas Evans")
guests.append("Trinity Skinner")
guests.sort()

for index, value in enumerate(guests):
    print (f"Please join me for a delicious 5 course meal, {value}, you're seat #{index + 1}.") 
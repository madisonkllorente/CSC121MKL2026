#5.3 Aliens MKL
import random

alien_color=['green','yellow','red']

random.shuffle(alien_color)

for color in alien_color:
    if color == 'green':
        print("Player earned 5 points")
    elif color == 'yellow':
        print("Player earned 10 points")
    elif color == 'red':
        print("Player earned 15 points")
    else:
        print("No points earned")    
    break
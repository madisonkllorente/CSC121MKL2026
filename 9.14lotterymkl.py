#9.14 lottery mkl
import random

items = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'A', 'B', 'C', 'D', 'E']

numbers = items[:10]
letters = items[10:]

lottery_numbers = random.sample(numbers, 4)
lottery_letter = random.choice(letters)

lottery_result = lottery_numbers + [lottery_letter]

print("Winning lottery combination:", lottery_result)

user_input = input("Enter your lottery (4 numbers and 1 letter, separated by spaces): ")

user_list = user_input.split()

user_numbers = list(map(int, user_list[:4]))
user_letter = user_list[4].upper()

user_result = user_numbers + [user_letter]

if user_result == lottery_result:
    print("Congratulations! You are a winner!")
else:
    print("Sorry, you did not win. Try again!")
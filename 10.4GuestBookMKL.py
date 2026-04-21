#10.4 Guest Book MKL 
print("Welcome to the Adair Inn! Sign your name in our book to be a part of our history!")
print("Enter 'quit' once you're done!")

with open("guest_book.txt", "a") as file:
    while True:
        name = input("Enter your name: ")

        if name.lower() == 'quit':
            print("Goodbye!")
            break

        date = input("Enter the date of stay: ")

        print(f"Thank you, {name}, for staying with us on {date}.")
        file.write(f"{name} - {date}\n")
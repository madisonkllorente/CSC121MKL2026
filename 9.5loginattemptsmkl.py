#9.5 login attempts mkl
class User:
    def __init__(self, first_name, last_name, age, email):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email
        self.login_attempts = 0  

    def describe_user(self):
        print(f"User: {self.first_name} {self.last_name}")
        print(f"Age: {self.age}")
        print(f"Email: {self.email}")

    def greet_user(self):
        print(f"Hello, {self.first_name}! Welcome back.\n")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

user1 = User("Maddi", "LLorente", 20, "maddill@gmail.com")

user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()

print(f"Login attempts: {user1.login_attempts}")

user1.reset_login_attempts()

print(f"Login attempts after reset: {user1.login_attempts}")
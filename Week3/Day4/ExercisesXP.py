# 🌟 Exercise 1: Currencies
# Goal: Implement dunder methods for a Currency class to handle string representation, integer conversion, addition, and in-place addition.

# Instructions:

# class Currency:
#     def __init__(self, currency, amount):
#         self.currency = currency
#         self.amount = amount

# Using the code above, implement the relevant methods and dunder methods which will output the results below.

# Hint : When adding 2 currencies which don’t share the same label you should raise an error.

class Currency:
    def __init__(self, currency, amount):
        self.currency = currency
        self.amount = amount

    def __str__(self):
        return (f"{self.amount} {self.currency}s")
    
    def __int__(self):
        return int(self.amount)
    
    def __repr__(self):
        return self.__str__()
    
    def __add__(self, other):
        if isinstance(other, int):
            return int(self.amount + other)
        elif isinstance(other, Currency):
            if self.currency == other.currency:
                return self.amount + other.amount
            else:
                raise TypeError (f"Cannot add between Currency type <{self.currency}> and <{other.currency}>")
        else:
            raise TypeError
        
    def __iadd__(self, other):
        if isinstance(other, int):
            self.amount = self.amount + other
            return self
        elif isinstance(other, Currency):
            if self.currency == other.currency:
                self.amount = self.amount + other.amount
                return self
            else:
                raise TypeError
        else:
            raise TypeError
        
# 🌟 Exercise 3: String module
# Goal: Generate a random string of length 5 using the string module.

# Instructions:
# Use the string module to generate a random string of length 5, consisting of uppercase and lowercase letters only.

# Step 1: Import the string and random modules
# Import the string and random modules.

# Step 2: Create a string of all letters
# Read about the strings methods to find the best methods for this step

# Step 3: Generate a random string
# Use a loop to select 5 random characters from the combined string.
# Concatenate the characters to form the random string.

# Step 1: Import the string and random modules
import string
import random

# Step 2: Create a string of all letters
upper_letters = string.ascii_uppercase
lower_letters = string.ascii_lowercase
all_letters = upper_letters + lower_letters

# Step 3: Generate a random string
random_string = ""
for letter in range(5):
    char = random.choice(all_letters)
    random_string = random_string + char

print(random_string)

# 🌟 Exercise 4: Current Date
# Goal: Create a function that displays the current date.

# Instructions:
# Use the datetime module to create a function that displays the current date.

# Step 1: Import the datetime module
# Step 2: Get the current date
# Step 3: Display the date

# Step 1: Import the datetime module
from datetime import datetime

# Step 2: Get the current date
def show_date():
    current_date = datetime.now()
    print (current_date)

# Step 3: Display the date
show_date()

# 🌟 Exercise 5: Amount of time left until January 1st
# Goal: Create a function that displays the amount of time left until January 1st.

# Instructions:
# Use the datetime module to calculate and display the time left until January 1st.
# more info about this module HERE

# Step 1: Import the datetime module
# Step 2: Get the current date and time
# Step 3: Create a datetime object for January 1st of the next year
# Step 4: Calculate the time difference
# Step 5: Display the time difference

# Step 1: Import the datetime module
from datetime import datetime

def time_until_new_year():
    # Step 2: Get the current date and time
    current_time = datetime.now()
    # Step 3: Create a datetime object for January 1st of the next year
    next_new_year = datetime(current_time.year + 1, 1, 1, 0, 0, 0)
    # Step 4: Calculate the time difference
    time_difference = next_new_year - current_time
    print(time_difference)

# Step 5: Display the time difference
time_until_new_year()

# 🌟 Exercise 6: Birthday and minutes

# Instruccions:
# Create a function that accepts a birthdate as an argument (in the format of your choice), 
# then displays a message stating how many minutes the user lived in his life.

def total_lived_time(birthdate):
    birthdate_dt = datetime.strptime(birthdate, "%Y-%m-%d")
    current_time = datetime.now()
    lived_time = current_time - birthdate_dt
    final_time = lived_time.total_seconds()/60
    print(f"You lived approximately {final_time} minutes")
total_lived_time("1999-04-26")

# 🌟 Exercise 7: Faker Module
# Goal: Use the faker module to generate fake user data and store it in a list of dictionaries.

# Instructions:
# Install the faker module and use it to create a list of dictionaries, where each dictionary represents a user with fake data.

# Step 1: Install the faker module
# Step 2: Import the faker module
# Step 3: Create an empty list of users
# Step 4: Create a function to add users
# Create a function that takes the number of users to generate as an argument.
# Inside the function, use a loop to generate the specified number of users.
# For each user, create a dictionary with the keys name, address, and language_code.
# Use the faker instance to generate fake data for each key:
# name: faker.name()
# address: faker.address()
# language_code: faker.language_code()
# Append the user dictionary to the users list.
# Step 5: Call the function and print the users list

# Step 2: Import the faker module
from faker import Faker
fake = Faker()

# Step 3: Create an empty list of users
users_list = []

# Step 4: Create a function to add users
def add_users(n):
    for user in range(n):
        user_data = {
            "name" : fake.name(),
            "address" : fake.address(),
            "language_code" : fake.language_code()
        }
        users_list.append(user_data)

# Step 5: Call the function and print the users list
from pprint import pprint 

add_users(4)
pprint(users_list)




















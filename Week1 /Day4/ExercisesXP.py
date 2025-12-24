# 🌟 Exercise 1: Favorite Numbers

# Create a set called my_fav_numbers and populate it with your favorite numbers.
my_fav_numbers = {7, 203, 2604, 1010, 1605, 26}

# Add two new numbers to the set.
my_fav_numbers.update ({1968, 1969})

# Remove the last number you added to the set.
lastadd = 1969
my_fav_numbers.remove(lastadd)

# Create another set called friend_fav_numbers and populate it with your friend’s favorite numbers.
friend_fav_numbers = {12, 16, 22, 32, 97}

# Concatenate my_fav_numbers and friend_fav_numbers to create a new set called our_fav_numbers.
our_fav_numbers = my_fav_numbers.union(friend_fav_numbers)
print(our_fav_numbers)

# 🌟 Exercise 2: Tuple
# Given a tuple of integers, try to add more integers to the tuple.
# Hint: Tuples are immutable, meaning they cannot be changed after creation. 
# Think about why you can’t add more integers to a tuple.

# Tuplenum = (1, 2, 3, 4, 5, 6, 7)
# Tuplenum.add(8)
# print(Tuplenum)

# Traceback (most recent call last):
#   File "/Users/juanepstein/Documents/DI_Bootcamp/Week1 /Day4/ExercisesXP.py", line 26, in <module>
#     Tuplenum.add(8)
#     ^^^^^^^^^^^^
# Tuples are innmutable, which means that new elements cannot be added

# 🌟 Exercise 3: List Manipulation
# You have a list: basket = ["Banana", "Apples", "Oranges", "Blueberries"]
# Remove "Banana" from the list.
# Remove "Blueberries" from the list.
# Add "Kiwi" to the end of the list.
# Add "Apples" to the beginning of the list.
# Count how many times "Apples" appear in the list.
# Empty the list.
# Print the final state of the list.

basket = ["Banana", "Apples", "Oranges", "Blueberries"]
basket.remove("Banana")
basket.remove("Blueberries")
basket.append("Kiwi")
basket.insert(0, "Apples")

apples = basket.count("Apples")
print(basket, apples)

basket.clear()
print(basket)

# 🌟 Exercise 4: Floats
# Recap: What is a float? What’s the difference between a float and an integer?
# Create a list containing the following sequence of mixed types: floats and integers:
# 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5.
# Avoid hard-coding each number manually.
# Think: Can you generate this sequence using a loop or another method?

#Integers are whole numbers without decimals, while floats can have decimal values.
int_flo = []
for n in range  (0, 4):
    int_flo.append(n + 1.5)
    int_flo.append(n + 2)
print(int_flo)

# 🌟 Exercise 5: For Loop
# Write a for loop to print all numbers from 1 to 20, inclusive.
# Write another for loop that prints every number from 1 to 20 where the index is even.

for n in range(1, 21):
    print(n)

for i in range (1, 21):
    if i %2 == 0:
        print(i)

# 🌟 Exercise 6: While Loop
# Use an input to ask the user to enter their name.
# Using a while True loop, check if the user gave a proper name (not digits and at least 3 letters long)
# hint: check for the method isdigit()
# if the input is incorrect, keep asking for the correct input until it is correct
# if the input is correct print “thank you” and break the loop

while True:
    name = input("What's your name?: ")

    if not name.isalpha() or len(name) < 3:
        print("Give the correct name: ")
    else: 
        print("Thanks")
        break 

# At first I only checked if the input was digits, but that allowed mixed values like ‘er1k’. So I improved the validation using isalpha()

# 🌟 Exercise 7: Favorite Fruits
# Ask the user to input their favorite fruits (they can input several fruits, separated by spaces).
# Store these fruits in a list.
# Ask the user to input the name of any fruit.
# If the fruit is in their list of favorite fruits, print:
# "You chose one of your favorite fruits! Enjoy!"
# If not, print:
# "You chose a new fruit. I hope you enjoy it!"

userfruits = input("Tell me your favorite fruits: ")
fruit_list = userfruits.split()

fruitname = input("Tell me any fruit: ")

if fruitname in fruit_list:
    print("You chose one of your favorite fruits! Enjoy!")
else:
    print("You chose a new fruit. I hope you enjoy it!")

# 🌟 Exercise 8: Pizza Toppings
# Write a loop that asks the user to enter pizza toppings one by one.
# Stop the loop when the user types 'quit'.
# For each topping entered, print:
# "Adding [topping] to your pizza."
# After exiting the loop, print all the toppings and the total cost of the pizza.
# The base price is $10, and each topping adds $2.50.

usertoppings = []
base_price = (10)

while True:
    topping = input("Enter a topping (or 'quit' to finish your pizza): ")
    if topping == "quit":
        break

    usertoppings.append(topping)
    print(f"Adding {topping} to your pizza")

total_price = base_price + len(usertoppings) * 2.5 
print(f"Total: ${total_price}")

# 🌟 Exercise 9: Cinemax Tickets
# Ask for the age of each person in a family who wants to buy a movie ticket.
# Calculate the total cost based on the following rules:
# Free for people under 3.
# $10 for people aged 3 to 12.
# $15 for anyone over 12.
# Print the total ticket cost.

totalcost = 0

while True:
    user_age = input("How old are you: ")

    if user_age != "done":
        age = int(user_age)
    else:
        break
    if age <3:
        totalcost += 0
    elif 3 <= age <= 12:
        totalcost += 10
    else:
        totalcost += 15

print(f"The total tickets cost is ${totalcost}")

# Imagine a group of teenagers wants to see a restricted movie (only for ages 16–21).
# Write a program to:
# Ask for each person’s age.
# Remove anyone who isn’t allowed to watch.
# Print the final list of attendees.

attendees = []

while True:
    user_age = input("How old are you: ")

    if user_age == "done": 
        break

    age = int(user_age)

    if 16 <= age <= 21:
        attendees.append(age)

print(f"The final amount of attendees is {attendees}")





    




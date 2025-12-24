# Exercise 1: Hello World
# Print the following output using one line of code:
# Hello world
# Hello world
# Hello world
# Hello world

print("Hello world\nHello world\nHello world\nHello world")

# Exercise 2: Some Math
# Write code that calculates the result of:
# (99^3)*8 (meaning 99 to the power of 3, times 8).

print (99**3 *8)

# Exercise 3: What is the output?
# Predict the output of the following code snippets:
# Coment what is your guess, then run the code and compare

# >>> 5 < 3 False
# >>> 3 == 3 True
# >>> 3 == "3" False
# >>> "3" > 3 False 
# >>> "Hello" == "hello" False

# Output: Traceback (most recent call last):
#   File "/Users/juanepstein/Documents/DI_Bootcamp/Week1 /Day2/ExercisesXP.py", line 39, in <module>
#     "3" > 3
# TypeError: '>' not supported between instances of 'str' and 'int'

# 🌟 Exercise 4: Your computer brand
# Create a variable called computer_brand which value is the brand name of your computer.
# Using the computer_brand variable, print a sentence that states the following:
# "I have a <computer_brand> computer."

computer_brand = "Apple"
print (f"I have an {computer_brand} computer.")

# 🌟 Exercise 5: Your information
# Create a variable called name, and set it’s value to your name.
# Create a variable called age, and set it’s value to your age.
# Create a variable called shoe_size, and set it’s value to your shoe size.
# Create a variable called info and set it’s value to an interesting sentence about yourself. The sentence must contain all the variables created in parts 1, 2, and 3.
# Have your code print the info message.
# Run your code.

name = "Juan"
age = "26"
shoe_size = "42"
info = (f"My name is {name}, I'm {age} and if you want to gift me sneakers, my size is {shoe_size}")
print(info)

# 🌟 Exercise 6: A & B
# Create two variables, a and b.
# Each variable’s value should be a number.
# If a is bigger than b, have your code print "Hello World".

a = 7
b = 3
if a > b: 
    print ("Hello World")

# Exercise 7: Odd or Even
# Write code that asks the user for a number and determines whether this number is odd or even.

usernumber = int(input("Choose a number: "))
if usernumber % 2 == 0:
    print("The number is even")
else:
    print("The number is odd")

# 🌟 Exercise 8: What’s your name?
# Write code that asks the user for their name and determines whether or not you have the same name. Print out a funny message based on the outcome.

username = input ("Whats your name?: ")
myname = "Juan"
if username == myname:
    print ("You have a great name!")
else:
    print ("“Admit it… you’d love to have my name.”")

# 🌟 Exercise 9: Tall enough to ride a roller coaster
# Write code that will ask the user for their height in centimeters.
# If they are over 145 cm, print a message that states they are tall enough to ride.
# If they are not tall enough, print a message that says they need to grow some more to ride.

userheight = int(input("What is your height?(cm): "))
if userheight > 145: 
    print ("You are fine, take the ride and have fun")
else:
    print("I'm sorry you're not tall enough, comeback next year")
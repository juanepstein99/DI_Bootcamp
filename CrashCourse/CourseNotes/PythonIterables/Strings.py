# Write a Python program that:

# 1. Asks the user to input a sentence.

# 2. Checks if the sentence is made up of only alphabetic characters. If not, print how many non-alphabetic characters are in the sentence.

# 3. Determines if the sentence ends with an exclamation mark (!).

# 4. Finds out if the sentence contains any whitespace characters and prints a message accordingly. 

sentence = input ("Tell me a sentence: ")

if sentence.isalpha():
    print("The sentence contains only alphabetic characters.")
else:
    non_alpha_count = len([char for char in sentence if not char.isalpha()])
    print(f"The sentence contains {non_alpha_count} non-alphabetic characters.")

if sentence.endswith('!'):
    print("The sentence ends with an exclamation mark.")
else:
    print("The sentence does not end with an exclamation mark.")

if sentence.isspace():
    print("The sentence contains only whitespace characters.")
elif any(char.isspace() for char in sentence):
    print("The sentence contains some whitespace characters.")
else:
    print("The sentence contains no whitespace characters.")
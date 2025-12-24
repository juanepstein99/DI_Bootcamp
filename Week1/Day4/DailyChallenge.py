# Challenge 1: Multiples of a Number
# 1. Ask the user for two inputs:
# A number (integer).
# A length (integer).
# 2. Create a program that generates a list of multiples of the given number.
# 3. The list should stop when it reaches the length specified by the user.

number = int(input("Gimme a number: "))
length = int(input("How many multiples do u want: "))

multiples_list = []

for i in range(1, length + 1):
    multiples_list.append(number * i)

print(multiples_list)

# Challenge 2: Remove Consecutive Duplicate Letters
# 1. Ask the user for a string.
# 2. Write a program that processes the string to remove consecutive duplicate letters.
# The new string should only contain unique consecutive letters.
# For example, “ppoeemm” should become “poem” (removes consecutive duplicates like ‘pp’, ‘ee’, and ‘mm’).
# 3. The program should print the modified string.

user_word = input("Tell me a word: ")
final_word = ("")

for letter in user_word:
    if final_word == "":
        final_word += letter
    elif letter != final_word[-1]:
        final_word += letter

print(final_word)
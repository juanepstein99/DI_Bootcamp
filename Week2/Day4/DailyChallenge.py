# Challenge 1: Sorting

# Instructions:
# Write a Python program that takes a single string of words as input, where the words are separated by commas.
# The program should output these words sorted in alphabetical order, with the sorted words also separated by commas.

# Step 1: Get Input
# Use the input() function to get a string of words from the user.
# The words will be separated by commas.

# Step 2: Split the String

# Step 3: Sort the List

# Step 4: Join the Sorted List

# Step 5: Print the Result
# Print the resulting comma-separated string.

user_input = input("Gimme a few words: ")      # Step 1: Get Input
user_list = user_input.split(",")              # Step 2: Split the String
sorted_list = sorted(user_list)                # Step 3: Sort the List
result = ",".join(sorted_list)                 # Step 4: Join the Sorted List
print(result)                                  # Step 5: Print the Result

# Challenge 2: Longest Word

# Instructions:
# Write a function that takes a sentence as input and returns the longest word in the sentence. 
# If there are multiple longest words, return the first one encountered. 
# Characters like apostrophes, commas, and periods should be considered part of the word.

# Step 1: Define the Function
# Define a function that takes a string (the sentence) as a parameter.

# Step 2: Split the Sentence into Words

# Step 3: Initialize Variables

# Step 4: Iterate Through the Words

# Step 5: Compare Word Lengths

# Step 6: Return the Longest Word

def longest_word(sentence):                         # Step 1: Define the Function
    words = sentence.split(" ")                     # Step 2: Split the Sentence into Words
    longest = ""                                    # Step 3: Initialize Variables
    for word in words:                              # Step 4: Iterate Through the Words
        if len(word) > len(longest):                # Step 5: Compare Word Lengths
            longest = word                      
    return longest                                  # Step 6: Return the Longest Word

print(longest_word("Margaret's toy is a pretty doll."))
print(longest_word("A thing of beauty is a joy forever."))
print(longest_word("Forgetfulness is by all means powerless!"))



            


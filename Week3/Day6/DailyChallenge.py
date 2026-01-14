# Text Analysis

# Instructions:
# Create a Text class to analyze text data, either from a string or a file. Then, create a TextModification class to perform text cleaning.

# Part I: Analyzing a Simple String

# Step 1: Create the Text Class
# Create a class called Text.
# The __init__ method should take a string as an argument and store it in an attribute (e.g: self.text).

# Step 2: Implement word_frequency Method
# Create a method called word_frequency(word).
# Split the text attribute into a list of words.
# Count the occurrences of the given word in the list.
# Return the count.
# If the word is not found, return None or a meaningful message.

# Step 3: Implement most_common_word Method
# Create a method called most_common_word().
# Split the text into a list of words.
# Use a dictionary to store word frequencies.
# Find the word with the highest frequency.
# Return the most common word.

# Step 4: Implement unique_words Method
# Create a method called unique_words().
# Split the text into a list of words.
# Use a set to store unique words.
# Return the unique words as a list.

# Part II: Analyzing Text from a File

# Step 5: Implement from_file Class Method
# Create a class method called from_file(file_path).
# Open the file at file_path in read mode.
# Read the file content.
# Create and return a Text instance with the file content as the text.

# Bonus: Text Modification
# Step 6: Create the TextModification Class
# Create a class called TextModification that inherits from Text.

# Step 7: Implement remove_punctuation Method
# Create a method called remove_punctuation().
# Use the string module to get a string of punctuation characters.
# Use a string method or regular expressions to remove punctuation from the text attribute.
# Return the modified text.

# Step 8: Implement remove_stop_words Method
# Create a method called remove_stop_words().
# Search online for a list of English stop words (common words like “a”, “the”, “is”).
# Split the text into a list of words.
# Filter out stop words from the list.
# Join the remaining words back into a string.
# Return the modified text.

# Step 9: Implement remove_special_characters Method
# Create a method called remove_special_characters().
# Use regular expressions to remove special characters from the text attribute.
# Return the modified text.

import string
import re

# Part I: Analyzing a Simple String

# Step 1: Create the Text Class
class Text:
    def __init__(self, text):
        self.text = text

# Step 2: Implement word_frequency Method
    def word_frequency(self, word):
        words = self.text.split()
        counter = 0 
        for w in words:
            if w == word:
                counter += 1
        if counter == 0:
            return None
        else:
            return counter

# Step 3: Implement most_common_word Method
    def most_common_word(self):
        words = self.text.split()
        counts = {}
        for w in words:
            if w in counts:
                counts[w] = counts[w] + 1
            else:
                counts[w] = 1
        max_count = 0
        most_common = None
        for word, count in counts.items():
            if count > max_count:
                max_count = count
                most_common = word
        return most_common

# Step 4: Implement unique_words Method
    def unique_words(self):
        words = self.text.split()
        unique = set(words)
        return list(unique)
    
# Part II: Analyzing Text from a File

# Step 5: Implement from_file Class Method
    @classmethod
    def from_file(cls, file_path):
        with open(file_path, "r", encoding="utf-8") as f:
            text = f.read()
        return cls(text)
    
# Bonus: Text Modification
# Step 6: Create the TextModification Class

class TextModification(Text):

# Step 7: Implement remove_punctuation Method
    def remove_punctuation(self):
        punctuation = string.punctuation
        clean_text = ""
        for i in self.text:
            if i not in punctuation:
                clean_text = clean_text + i
        return clean_text

# Step 8: Implement remove_stop_words Method
    def remove_stop_words(self):
        stop_words = ("a", "the", "is")
        words = self.text.split()
        filtered_words = []
        for i in words:
            if i not in stop_words:
                filtered_words.append(i)
        return " ".join(filtered_words)
    
# Step 9: Implement remove_special_characters Method
    def remove_special_characters(self):
        cleaned = re.sub("[^a-zA-Z\s]", "", self.text)
        return cleaned




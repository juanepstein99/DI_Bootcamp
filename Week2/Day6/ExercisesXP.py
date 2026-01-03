# 🌟 Exercise 1: Cats

# Instructions:
# Use the provided Cat class to create three cat objects. 
# Then, create a function to find the oldest cat and print its details.

# Step 1: Create Cat Objects
# Use the Cat class to create three cat objects with different names and ages.

# Step 2: Create a Function to Find the Oldest Cat
# Create a function that takes the three cat objects as input.
# Inside the function, compare the ages of the cats to find the oldest one.
# Return the oldest cat object.

# Step 3: Print the Oldest Cat’s Details
# Call the function to get the oldest cat.
# Print a formatted string: “The oldest cat is <cat_name>, and is <cat_age> years old.”
# Replace <cat_name> and <cat_age> with the oldest cat’s name and age.

class Cat:
    def __init__(self, cat_name, cat_age):
        self.name = cat_name
        self.age = cat_age

# Step 1: Create Cat Objects
cat1 = Cat("Julian", 3)
cat2 = Cat("Maradona", 7)
cat3 = Cat("Messi", 10)

# Step 2: Create a Function to Find the Oldest Cat
def find_oldest_cat(cat1, cat2, cat3):
    oldest = cat1
    if cat2.age > oldest.age:
        oldest = cat2
    if cat3.age > oldest.age:
        oldest = cat3
    return oldest 

# Step 3: Print the Oldest Cat’s Details
oldest_cat = find_oldest_cat(cat1, cat2, cat3)
print(f"The oldest cat is {oldest_cat.name}, and is {oldest_cat.age} years old")



# 🌟 Exercise 2 : Dogs
# Goal: Create a Dog class, instantiate objects, call methods, and compare dog sizes.

# Instructions:
# Create a Dog class with methods for barking and jumping. 
# Instantiate dog objects, call their methods, and compare their sizes.

# Step 1: Create the Dog Class
# Create a class called Dog.
# In the __init__ method, take name and height as parameters and create corresponding attributes.
# Create a bark() method that prints “<dog_name> goes woof!”.
# Create a jump() method that prints “<dog_name> jumps <x> cm high!”, where x is height * 2.

# Step 2: Create Dog Objects
# Create davids_dog and sarahs_dog objects with their respective names and heights.

# Step 3: Print Dog Details and Call Methods
# Print the name and height of each dog.
# Call the bark() and jump() methods for each dog.

# Step 4: Compare Dog Sizes

# Step 1: Create the Dog Class
class Dog: 
    def __init__(self, name, height):
        self.name = name
        self.height = height 

    def bark (self):
        print(f"{self.name} goes woof!" )

    def jump (self):
        print (f"{self.name} jumps {self.height * 2} cm high!")

# Step 2: Create Dog Objects
davids_dog = Dog("Juanfer", 70)
sarahs_dog = Dog("Marcelo", 45) 

# Step 3: Print Dog Details and Call Methods
print(f"David's dog is {davids_dog.name} and it's height is {davids_dog.height}")

davids_dog.bark()
davids_dog.jump() 

print(f"Sarah's dog is {sarahs_dog.name} and it's height is {sarahs_dog.height}")

sarahs_dog.bark()
sarahs_dog.jump() 

# Step 4: Compare Dog Sizes
if davids_dog.height > sarahs_dog.height:
    print("David's dog is taller")
else:
    print("Sarah's dog is taller")

# 🌟 Exercise 3 : Who’s the song producer?
# Goal: Create a Song class to represent song lyrics and print them.

# Instructions:
# Create a Song class with a method to print song lyrics line by line.

# Step 1: Create the Song Class
# Create a class called Song.
# In the __init__ method, take lyrics (a list) as a parameter and create a corresponding attribute.
# Create a sing_me_a_song() method that prints each element of the lyrics list on a new line.

class Song:
    def __init__(self, lyrics):
        self.lyrics = lyrics 

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line) 
    
my_song = Song(["I'm walking down the street tonight", "Thinking about the things I lost", "But tomorrow I'll be alright"])

my_song.sing_me_a_song()


# 🌟 Exercise 4 : Afternoon at the Zoo
# Goal:
# Create a Zoo class to manage animals. 
# The class should allow adding animals, displaying them, selling them, and organizing them into alphabetical groups.

# Instructions
# Step 1: Define the Zoo Class

# 1. Create a class called Zoo.

# 2. Implement the __init__() method:
# It takes a string parameter zoo_name, representing the name of the zoo.
# Initialize an empty list called animals to keep track of animal names.

# 3. Add a method add_animal(new_animal):
# This method adds a new animal to the animals list.
# Do not add the animal if it is already in the list.

# 4. Add a method get_animals():
# This method prints all animals currently in the zoo.

# 5. Add a method sell_animal(animal_sold):
# This method checks if a specified animal exists on the animals list and if so, remove from it.

# 6. Add a method sort_animals():
# This method sorts the animals alphabetically.
# It also groups them by the first letter of their name.
# The result should be a dictionary where:
# Each key is a letter.
# Each value is a list of animals that start with that letter.

# 7. Add a method get_groups():
# This method prints the grouped animals as created by sort_animals().

# Step 2: Create a Zoo Object
# Create an instance of the Zoo class and pass a name for the zoo.

# Step 3: Call the Zoo Methods
# Use the methods of your Zoo object to test adding, selling, displaying, sorting, and grouping animals.

# Bonus: Modify the add_animal() method to get *args so you dont need to repeat the method each time for a new animal, 
# you can pass multiple animals names separated by a comma.

# 1. Create a class called Zoo.
class Zoo: 
# 2. Implement the __init__() method:
    def __init__(self, zoo_name):
        self.zoo_name = zoo_name
        self.animals = [] 
    
# 3. Add a method add_animal(new_animal):
    def add_animal(self, new_animal):
        if new_animal not in self.animals:
            self.animals.append(new_animal)

# 4. Add a method get_animals():
    def get_animals(self):
        print(self.animals)

# 5. Add a method sell_animal(animal_sold):
    def sell_animal(self, animal_sold):
        if animal_sold in self.animals:
            self.animals.remove(animal_sold)

# 6. Add a method sort_animals():
    def sort_animals(self):
        self.animals.sort()
        groups = {}
        for animal in self.animals: 
            letter = animal[0]
            if letter not in groups:
                groups[letter] = []
            groups[letter].append(animal)
        self.groups = groups 

# 7. Add a method get_groups():
    def get_groups(self):
        for letter, animals in self.groups.items():
            print(f"{letter} : {animals}")

# Bonus: Modify the add_animal() method to get *args so you dont need to repeat the method each time for a new animal, 
# you can pass multiple animals names separated by a comma.

    def add_animal(self, *new_animal):
        for animal in new_animal:
            if animal not in self.animals:
                self.animals.append(animal)

# Step 2: Create a Zoo Object
safari_rg = Zoo("safari_rg")

# Step 3: Call the Zoo Methods
safari_rg.add_animal("Elephant")
safari_rg.add_animal("Monkey")
safari_rg.add_animal("Lion")

safari_rg.get_animals()

safari_rg.sell_animal("Monkey")

safari_rg.get_animals()

safari_rg.sort_animals()

safari_rg.get_groups()

safari_rg.add_animal("Monkey", "Zebra", "Giraffe", "Bear", "Kangaroo")

safari_rg.get_animals()



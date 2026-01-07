# 🌟 Exercise 3: Dogs Domesticated
# Goal: Create a PetDog class that inherits from Dog and adds training and tricks.

# Instructions:
# Step 1: Import the Dog Class
# In a new Python file, import the Dog class from the previous exercise.

# Step 2: Create the PetDog Class
# Create a class called PetDog that inherits from the Dog class.
# Add a trained attribute to the __init__ method, with a default value of False.
# trained means that the dog is trained to do some tricks.
# Implement a train() method that prints the output of bark() and sets trained to True.
# Implement a play(*args) method that prints “<dog_names> all play together”.
# *args on this method is a list of dog instances.
# Implement a do_a_trick() method that prints a random trick if trained is True.
# Use this list for the ramdom tricks:
# tricks = ["does a barrel roll", "stands on his back legs", "shakes your hand", "plays dead"]
# Choose a random index from it each time the method is called.

# Step 3: Test PetDog Methods
# Create instances of the PetDog class and test the train(), play(*args), and do_a_trick() methods.

# Step 1: Import the Dog Class
from ExercisesXp import Dog 

import random

# Step 2: Create the PetDog Class
class PetDog(Dog):

# Add a trained attribute to the __init__ method, with a default value of False.
    def __init__(self, name, age, weight):
        super().__init__(name, age, weight)
        self.trained = False 

# Implement a train() method that prints the output of bark() and sets trained to True.
    def train(self):
        self.bark()
        self.trained = True

# Implement a play(*args) method that prints “<dog_names> all play together”.
    def play(self, *args):
        names = [self.name]
        for dog in args:
            names.append(dog.name)
        playing_dogs = ", ".join(names)
        print(f"{playing_dogs} all play together")

# Implement a do_a_trick() method that prints a random trick if trained is True.
    def do_a_trick(self):
        if self.trained: True
        tricks = ["does a barrel roll", "stands on his back legs", "shakes your hand", "plays dead"]
        random_trick = random.choice(tricks)
        print(f"{self.name} {random_trick}")

# Step 3: Test PetDog Methods
Momuno = PetDog("Momuno", 12, 15)
Tepele = PetDog("Tepele", 6, 23)
Cobias = PetDog("Cobias", 10, 7)

Momuno.train()
Momuno.play(Tepele, Cobias)
Momuno.do_a_trick()


    

    





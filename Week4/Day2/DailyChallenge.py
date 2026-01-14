# Exercise 1: Quizz
# Answer the following questions:

# What is a class?
# It is a blueprint or template used to create objects with attributes and methods.

# What is an instance?
# It is a concrete object created from a class.

# What is encapsulation?
# It is the practice of grouping data and methods together and controlling their access.

# What is abstraction?
# It means showing only the essential features and hiding the internal details.

# What is inheritance?
# It is when a child class inherits attributes and methods from a parent class.

# What is multiple inheritance?
# It is when a class inherits from more than one class.

# What is polymorphism?
# It is the ability to use the same method in different ways depending on the object.

# What is method resolution order or MRO?
# It is the order Python uses to look for methods in a class hierarchy.

# Exercise 2: Create a deck of cards class
# The Deck of cards class should NOT inherit from a Card class.

# The requirements are as follows:
# The Card class should have a suit (Hearts, Diamonds, Clubs, Spades) and a value (A,2,3,4,5,6,7,8,9,10,J,Q,K)
# The Deck class :
# should have a shuffle method which makes sure the deck of cards has all 52 cards and then rearranges them randomly.
# should have a method called deal which deals a single card from the deck. 
# After a card is dealt, it should be removed from the deck.

# Exercise 2: Create a deck of cards class
import random

class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __repr__(self):
        return f"{self.value} of {self.suit}"

class Deck:
    def __init__(self):
        self.cards = []

    def shuffle(self):
        suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
        values = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]

        self.cards = []

        for suit in suits:
            for value in values:
                self.cards.append(Card(suit, value))

        random.shuffle(self.cards)

    def deal(self):
        if len(self.cards) == 0:
            return "No more cards in the deck"
        return self.cards.pop()
    
deck = Deck()
deck.shuffle()

card1 = deck.deal()
card2 = deck.deal()

print(card1)
print(card2)
print(len(deck.cards))
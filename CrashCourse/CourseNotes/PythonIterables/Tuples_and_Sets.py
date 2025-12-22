#TUPLES
# Create a tuple that contains your three favorite fruits. Write code that:
# Accesses the first fruit in the tuple.
# Counts how many times a specific fruit appears in the tuple.
# Finds the index of a specific fruit in the tuple.

Fruits = ("Sandía", "Pera", "Frutilla", "Sandía", "Durazno")
print (Fruits[0])
print (Fruits.count("Sandía"))
print (Fruits[2])

#SETS
# Create a set of your five favorite numbers. Write code that:
# Adds a new number to the set.
# Removes all elements from the set.
# Finds the common elements between two sets (use a set of your five favorite numbers and a set of prime numbers).

Numbers = {203, 68, 7, 1010, 69}
print(Numbers)
Numbers.add(2604)
print(Numbers)
Numbers.clear()
Numbers = {1010, 68, 69, 7, 203, 2604}
Prime_Numbers = {2, 3, 5, 7, 13}
print(Numbers.intersection(Prime_Numbers))
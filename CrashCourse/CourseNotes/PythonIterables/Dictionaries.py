# 1. Print the author of "1984".
# 2. Change the author of "The Great Gatsby" to "Francis Scott Fitzgerald".
# 3. Add a new book: "Moby Dick" by Herman Melville.
# 4. Use the get() method to try to access the author of "To Kill a Mockingbird".
# 5. Remove the book "Brave New World" using the pop() method.

Books = {'1984': 'George Orwell', 'Brave New World': 'Aldous Huxley', 'The Great Gatsby': 'F. Scott Fitzgerald'}
print (Books["1984"])

Books["The Great Gatsby"] = "Francis Scott Fitzgerald"
print (Books)

Books ["Moby Dick"] = "Herman Melville"
print(Books)

print (Books.get("To Kill a Mockingbird"))
print(Books.pop("Brave New World"))
print(Books)
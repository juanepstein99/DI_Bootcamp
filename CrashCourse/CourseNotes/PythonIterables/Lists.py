# Given the list:

# fruits = ["apple", "banana", "cherry", "date", "elderberry"]
# 1. Print the first element from the list.

# 2. Print the third element from the list.

# 3. Try accessing an element at an index that doesn't exist (e.g., the 6th element) and note what happens.

# 4. Change the second fruit ("banana") to "blueberry".

fruits = ["apple", "banana", "cherry", "date", "elderberry"]
print(fruits[0])
print(fruits[2])

fruits[1] = "blueberry"
print (fruits)

# Using the same list from the previous exercise:

# 1. Add "fig" to the end of the fruits

# 2. Insert "grape" at the beginning of the list

# 3. Remove "cherry" from the list using using the specific method for it

# 4. Remove the last element from the list using the specific method for it

# 5. Create another list of berries and combine it with the fruits list into a list called "combined_list"

# 6. Sort the combined_list

# 7. Slice the last three elements of the combined list

fruits = ["apple", "banana", "cherry", "date", "elderberry"]

fruits.insert(5, "fig")
print (fruits)

fruits.insert(0, "grape")
print (fruits)

fruits.pop(3)
print(fruits)

fruits.pop()
print (fruits)

fruits = ['grape', 'apple', 'banana', 'date', 'elderberry']
fruits_berries = ["strawberrys", "blueberrys", "blackerrys"]
print (fruits_berries)
combined_list = (fruits + fruits_berries)
print(combined_list)

combined_list.sort()
print(combined_list)

# 7. Slice the last three elements of the combined list
print (combined_list[-3:])
# Instructions: Pagination System
# Goal:
# Create a Pagination class that simulates a basic pagination system.

# Step 1: Create the Pagination Class
# Define a class called Pagination to represent paginated content.
# It should optionally accept a list of items and a page size when initialized.

# Step 2: Implement the __init__ Method
# Accept two optional parameters:
# items (default None): a list of items
# page_size (default 10): number of items per page

# Step 3: Implement the get_visible_items() Method
# This method returns the list of items visible on the current page.
# Use slicing based on the current_idx and page_size.

# Step 4: Implement Navigation Methods
# These methods should help navigate through pages:

# go_to_page(page_num)
# → Goes to the specified page number (1-based indexing).
# → If page_num is out of range, raise a ValueError.

# first_page()
# → Navigates to the first page.

# last_page()
# → Navigates to the last page.

# next_page()
# → Moves one page forward (if not already on the last page).

# previous_page()
# → Moves one page backward (if not already on the first page).

# Bonus
# Step 5: Add a Custom __str__() Method
# This magic method should return a string displaying the items on the current page, each on a new line.

# Step 6: Test Your Code

import math 
# Step 1: Create the Pagination Class
class Pagination:

# Step 2: Implement the __init__ Method
    def __init__(self, items = None, page_size = 10):
        if items is None:
            items = []
        self.items = items
        self.page_size = page_size
        self.current_idx = 0
        self.total_pages = math.ceil(len(self.items) / self.page_size)

# Step 3: Implement the get_visible_items() Method
    def get_visible_items(self):
        start = self.current_idx * self.page_size
        end = start + self.page_size
        return self.items[start:end]
    
# Step 4: Implement Navigation Methods
# go_to_page(page_num)
    def go_to_page(self, page_num):
        if page_num < 1 or page_num > self.total_pages:
            raise ValueError
        self.current_idx = page_num - 1
        return self


# first_page()
    def first_page(self):
        self.current_idx = 0
        return self
    
# last_page()
    def last_page(self):
        if self.total_pages == 0:
            self.current_idx = 0
        else:
            self.current_idx = self.total_pages - 1
        return self

    
# next_page()
    def next_page(self):
        if self.current_idx < self.total_pages -1:
            self.current_idx += 1
        return self

# previous_page()
    def previous_page(self):
        if self.current_idx > 0:
            self.current_idx = self.current_idx -1
        return self  
    
# alphabet = list("abcdefghijklmnopqrstuvwxyz")
# p = Pagination(alphabet, 4)

# print(p.get_visible_items())
# p.next_page().next_page()
# print(p.get_visible_items())    

# Bonus
# Step 5: Add a Custom __str__() Method
    def __str__(self):
        items = self.get_visible_items()
        united_items = "\n".join(items)
        return united_items
    
alphabetList = list("abcdefghijklmnopqrstuvwxyz")
p = Pagination(alphabetList, 4)

print(p.get_visible_items())

p.next_page()
print(p.get_visible_items())

p.last_page()
print(p.get_visible_items())

p.go_to_page(10)
print(p.current_idx + 1)

p.go_to_page(0)
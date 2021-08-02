# li = [1, 2, 3, 4, 5]

# # Access List Item
# print(li[1]) # Output: 2
# print(li[-1]) # Output: 5 (-1 return the last item)
# print(li[1:3]) # Output: [2, 3]

# # Concatenate List
# li1, li2 = [1, 2, 3], [4, 5, 6]
# li_items = li1 + li2
# print(li_items) # Output: [1, 2, 3, 4, 5, 6]

# # Concatenated the 2nd List with 1st List
# li1.extend(li2)
# print(li1) # Output: [1, 2, 3, 4, 5, 6]

# # Unpacking List
# names = ['John', 'Doe', 'Foo', 'Bar']
# first_user, seccod_user, *other_users, last_user = names
# print(first_user, seccod_user, last_user) # Output: John Doe Bar
# print(other_users) # Output: ['Foo']

# # Check the Item Existence in List
# names = ['John', 'Doe', 'Foo', 'Bar']
# print('John' in names) # Output: True
# print('Hello' in names) # Output: False

# # Print Array Item using Loop
# nums = [23, 33, 52, 65, 76, 28, 32]
# for item in nums:
#     print(item)

# # List Comprehension
# even_nums = [num for num in nums if num % 2 == 0]
# print(even_nums) # Output: [52, 76, 28, 32]

# List Conversion
# li = [1, 2, 3, 4, 5]
# list_to_tpl = tuple(li)
# print(list_to_tpl) # Output: (1, 2, 3, 4, 5)

# list_to_set = set(li)
# print(list_to_set) # Output: {1, 2, 3, 4, 5}

# Insert List Item

# names = ['John', 'Doe', 'Foo', 'Bar']
## Add Data in the Last
# names.append('Hudson') 
# print(names) # Output: ['John', 'Doe', 'Foo', 'Bar', 'Hudson']

# # Add Data in the First
# names.insert(0, 'Michel') 
# print(names) # Output: ['Michel', 'John', 'Doe', 'Foo', 'Bar']

# # Add Data in the any position
# names.insert(2, 'Watson') 
# print(names) # Output: ['John', 'Doe', 'Watson', 'Foo', 'Bar']


# Remove Item from List
names = ['John', 'Doe', 'Foo', 'Bar']

## Remove the last Element
# names.pop()
# print(names) # Output: ['John', 'Doe', 'Foo']

## Remove any existing item passing index in pop(index)
# names.pop(0)
# print(names) # Output: ['Doe', 'Foo', 'Bar']

## Remove Multiple Items
# del names[1:3]
# print(names) # Output: ['John', 'Bar']

## Remove item passing Value
# names.remove('John')
# print(names) # Output: ['Doe', 'Foo', 'Bar']

# # Remove all items 
# names.clear()
# print(names) # Output: []


# index() return the index of list item
# li = [32, 54, 32, 43]
# print(li.index(32)) # Output: 0

# count() counts the similar list item
# print(li.count(32)) # Output: 2


# Other List Methods
nums = [23, 33, 52, 65, 76, 28, 32]
# nums.sort()
# print(nums) # Output: [23, 28, 32, 33, 52, 65, 76]

# Reverse the List Item
# nums.reverse()
# print(nums) # Output: [32, 28, 76, 65, 52, 33, 23]


# # The copy() method returns a copy of the specified list. 
# nums2 = nums.copy()
# nums2.append(100)
# print(nums) # Outptu: [23, 33, 52, 65, 76, 28, 32]
# print(nums2) # Output: [23, 33, 52, 65, 76, 28, 32, 100]

# # Shortcut Create List
# similar_nums = [4] * 10
# print(similar_nums) # Output: [4, 4, 4, 4, 4, 4, 4, 4, 4, 4]













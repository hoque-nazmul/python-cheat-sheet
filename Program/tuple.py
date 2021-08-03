# It's Iterable, we can only access the item of tuple using index or using loop. But can't assign, insert or delete any item of tuple.
tpl = (10, 20, 30, 40, 50, 60)

# Access the Item of Tuple
tpl = (10, 20, 30, 40, 50, 60)
print(tpl[1]) # Output: 20
print(tpl[-1]) # Output: 60
print(tpl[2:5]) # Output: (30, 40, 50)

# Unpack the Tuple
users = ("Joe", "John", "Root", "Justin", "Foo")
user_1, user_2, *other_users, last_user = users 
print(user_1) # Output: Joe
print(user_2) # Output: John
print(other_users) # Output: ['Root', 'Justin']
print(last_user) # Output: Foo

# Check the Existance of Tuple Item
users = ("Joe", "John", "Root", "Justin", "Foo")
print('Justin' in users) # Output: True
print('Doe' in users) # Output: False

# Built-in Method of Tuple
# Find the index of Tuple
users = ("Joe", "John", "Root", "Justin", "Foo")
print(users.index('John')) # Output: 1

# Count the similar item of Tuple
users = ("Joe", "John", "Root", "Justin", "Foo")
print(users.count('Justin')) # Output: 1

# Create a Generator using Tuple Comprehension
users = ("Joe", "John", "Root", "Justin", "Foo")
gen = (item for item in users)
print(type(gen)) # Output: <class 'generator'>

# Tuple Conversion
nums = (2, 5, 6, 3, 2, 2)
print(list(nums)) # Output: [2, 5, 6, 3, 2, 2]
print([*nums]) # Output: [2, 5, 6, 3, 2, 2]
print(set(nums)) # Output: {2, 3, 5, 6}



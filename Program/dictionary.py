# Access the Dictionary Item
person = { 'name': 'John Doe', 'country': 'usa', 'age': 30 }
print(person['name']) # Output: John Doe
print(person['country']) # Output: usa
print(person.get('name')) # Output: John Doe

# Add the property in Dictionary
person = { 'name': 'John Doe', 'country': 'usa', 'age': 30 }
person['city'] = 'New York'
print(person) 
# Output: {'name': 'John Doe', 'country': 'usa', 'age': 30, 'city': 'New York'}

# Remove the Item of Dictionary
person = { 'name': 'John Doe', 'country': 'usa', 'age': 30 }
person.pop('age')
print(person) # Output: {'name': 'John Doe', 'country': 'usa'}

# Clear the Dictionary
person = { 'name': 'John Doe', 'country': 'usa', 'age': 30 }
person.clear()
print(person) # Output: {}

# Dictionary Keys
person = { 'name': 'John Doe', 'country': 'usa', 'age': 30 }
print(person.keys()) # Output: dict_keys(['name', 'country', 'age'])

# Dictionary Values
person = { 'name': 'John Doe', 'country': 'usa', 'age': 30 }
print(person.values()) # Output: dict_values(['John Doe', 'usa', 30])

# Loop in Dictionary
# Print the Keys of Dictionary
person = { 'name': 'John Doe', 'country': 'usa', 'age': 30 }
for key in person:
    print (key) # Output: name country age
# Print the Values of Dictionary
for key in person:
    print (person[key]) # Output: John Doe usa 30


# Create the new Instance of a Dictionary
person = { 'name': 'John Doe', 'country': 'usa', 'age': 30 }
a_person = person.copy()
# Before Changing 
print(person) # Output: {'name': 'John Doe', 'country': 'usa', 'age': 30}
print(a_person) # Output: {'name': 'John Doe', 'country': 'usa', 'age': 30}
# After Changing 
a_person['gender'] = 'Male'
print(person) # Output: {'name': 'John Doe', 'country': 'usa', 'age': 30}
print(a_person) # Output: {'name': 'John Doe', 'country': 'usa', 'age': 30, 'gender': 'Male'}

# Print the Items of Dictionary
person = { 'name': 'John Doe', 'country': 'usa', 'age': 30 }
print(person.items()) # Output: dict_items([('name', 'John Doe'), ('country', 'usa'), ('age', 30)])




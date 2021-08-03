# Python Cheet Sheet

## Table of Contents

1. [Print Output](#print-output)
2. [Variable](#variable)
3. [Built-in Data Types](#built-in-data-types)
    - [Data Types](#data-types)
    - [Type Conversion](#type-conversion)
4. [Function](#function)
    - [Arguments](#arguments)
    - [lambda](#lambda)
5. [Control Flow](#control-flow)
    - [Short Hand](#short-hand)
6. [Loop](#loop)
    - [While Loop](#while-loop)
    - [For Loop](#for-loop)
7. [Python Built-in Data Structure](#python-built-in-data-structure)
    - [List](#list)
    - [Tuple](#tuple)
    - [Set](#set)
    - [Dictionary](#dictionary)
8. [File in Python](#file-in-python)

## Print Output
```python
# Print Somthing
print("Hello World")  # Output: Hello World

name = "John Doe"
age = 30
# Print Multiple Data
print(name, age)  # Output: John Doe 30

# Print Horizontally - Default end="\n"
for item in range(5):
    print(item, end=' ')  # Output: 0 1 2 3 4
```
**[⬆ back to top](#table-of-contents)**

## Variable
```python
txt = "Hello World"
num = 2021
is_login = True
string = str(1)

# Assaign Multiple Variable
name, age = 'John Doe', 30
```
**[⬆ back to top](#table-of-contents)**

# Built-in Data Types
## Data Types
```python
# Most Used Built-in Data Types in Python
1. str -> 'Hey'
2. int -> 100
3. float -> 10.1
4. bool -> True/False
5. list -> [1, 2, 3]
6. tuple -> (1, 2, 3)
7. set -> {1, 2, 3}
8. dict -> {'name': 'John Doe', 'age': 30}
9. range -> range(5)
10. complex -> 1j

# Type Checking Method
type([1, 2, 3]) # Output: <class 'list'>
```
**[⬆ back to top](#table-of-contents)**

## Type Conversion
```python
int('100') # String -> Integer
str(100) # Integer -> String
float(10) # Integer -> Float
list((1, 2, 3)) # Tuple -> List
list({1, 2, 3}) # Set -> List
tuple([1, 2, 3]) # List -> Tuple
tuple({1, 2, 3}) # Set -> Tuple
set([1, 2, 3]) # List -> Set
set((1, 2, 3)) # Tuple -> Set

# Also Change Data Type Using *
tpl = (1, 2, 3)
tpl_to_list = [*tpl]
print(tpl_to_list) # Output: [1, 2, 3]
```
**[⬆ back to top](#table-of-contents)**

# Function
```python
# Normal Function Defination
def add (num1, num2):
    return num1 + num2 
print(add(25, 10)) # Output: 35

# Set a Default Argument
def say_hello (name, greeting="Hello"):
    return f"{greeting}, {name}"
print(say_hello("John", 'Hey')) # Output: Hey, John
```
**[⬆ back to top](#table-of-contents)**

## Arguments
```python
# It'll be return a Tuple
def get_nums (*nums):
    return nums
print(get_nums(2, 3, 4, 5, 6)) # Output: (2, 3, 4, 5, 6)

# It'll be return a Dictionary
def get_data (**data):
    return data
print(get_data(name='John Doe', age=20)) # Output: {'name': 'John Doe', 'age': 20}
```
**[⬆ back to top](#table-of-contents)**

## lambda
```python
# lambda arguments : expression
func1 = lambda x, y: x + y
print(func1(1, 2)) #Output: 3

func2 = lambda x, y=2: x + y
print(func2(1)) #Output: 3

func3 = lambda *args: args
print(func3(1, 2)) #Output: (1, 2)

func4 = lambda **args: args
print(func4(name='John Doe', age=30)) #Output: {'name': 'John Doe', 'age': 30}

# lmbda IIFE
(lambda num1, num2: num1 * num2)(10, 5)
```
**[⬆ back to top](#table-of-contents)**

# Control Flow
```python
a, b, c = 100, 200, 300
if a > b and a > c:
    print(f"{a} is biggest number!")
elif b > a and b > c:
    print(f"{b} is biggest number!")
else: 
    print(f"{c} is a biggest number!")

# Output: 300 is a biggest number!
```
**[⬆ back to top](#table-of-contents)**

## Short Hand
```python
# value_if_true if condition else value_if_false
print(a) if a > b else print(b) if b > a else print(a, b) # Output: 200

a, b = 100, 200
print(f"{a} > {b} or {a} < {b}") if a > b or a < b else print(f"{a} = {b}")
# Output: 100 > 200 or 100 < 200
```
**[⬆ back to top](#table-of-contents)**

# Loop
## While Loop
```python
counter = 0
while (counter <= 10):
    counter += 1
    if counter == 3:
        continue
    if counter > 5:
        break
    print(counter)  # Output: 1 2 4 5
```
**[⬆ back to top](#table-of-contents)**

## For Loop
```python
for item in range(0, 11, 2):
    print(item, end=' ')  # Print Even: 0 2 4 6 8 10

# Create a List Using For
li = [item for item in range(1, 5)]
print(li) # Output: [1, 2, 3, 4]
```
**[⬆ back to top](#table-of-contents)**

# List
#### Access the List Item
```python
li = [1, 2, 3, 4, 5]
print(li[1]) # Output: 2
print(li[-1]) # Output: 5 (-1 return the last item)
print(li[1:3]) # Output: [2, 3]
```
#### Concatenate List
```python
li1, li2 = [1, 2, 3], [4, 5, 6]
li_items = li1 + li2
print(li_items) # Output: [1, 2, 3, 4, 5, 6]
```
```python
# Concatenated the 2nd List with 1st List
li1, li2 = [1, 2, 3], [4, 5, 6]
li1.extend(li2)
print(li1) # Output: [1, 2, 3, 4, 5, 6]
```

#### Unpacking List
```python
names = ['John', 'Doe', 'Foo', 'Bar']
first_user, seccod_user, *other_users, last_user = names
print(first_user, seccod_user, last_user) # Output: John Doe Bar
print(other_users) # Output: ['Foo']
```

#### Check the Existence of List Item
```python
names = ['John', 'Doe', 'Foo', 'Bar']
print('John' in names) # Output: True
print('Hello' in names) # Output: False
```

#### Print the List Item using For Loop
```python
nums = [23, 33, 52, 65, 76, 28, 32]
for item in nums:
    print(item)
```

#### List Comprehension
```python
nums = [23, 33, 52, 65, 76, 28, 32]

even_nums = [num for num in nums if num % 2 == 0]
print(even_nums) # Output: [52, 76, 28, 32]
```

#### List Conversion
```python
li = [1, 2, 3, 4, 5]
print(tuple(li)) # Output: (1, 2, 3, 4, 5)
print(set(li)) # Output: {1, 2, 3, 4, 5}
```

#### index() returns the Index of Item
```python
li = [32, 54, 32, 43]
print(li.index(32)) # Output: 0
```

#### count() counts the similar list item
```python
li = [32, 54, 32, 43]
print(li.count(32)) # Output: 2
```

### Insert the List Item
```python
# Add Item in the Last
names = ['John', 'Doe', 'Foo', 'Bar']
names.append('Hudson') 
print(names) # Output: ['John', 'Doe', 'Foo', 'Bar', 'Hudson']
```
```python
# Add Item in the First
names = ['John', 'Doe', 'Foo', 'Bar']
names.insert(0, 'Michel') 
print(names) # Output: ['Michel', 'John', 'Doe', 'Foo', 'Bar']
```
```python
# Add Item in the any position
names = ['John', 'Doe', 'Foo', 'Bar']
names.insert(2, 'Watson') 
print(names) # Output: ['John', 'Doe', 'Watson', 'Foo', 'Bar']
```

### Remove Item from List
```python 
# Remove the last Element
names = ['John', 'Doe', 'Foo', 'Bar']
names.pop()
print(names) # Output: ['John', 'Doe', 'Foo']
```
```python 
# Remove any existing item passing index in pop(index)
names = ['John', 'Doe', 'Foo', 'Bar']
names.pop(0)
print(names) # Output: ['Doe', 'Foo', 'Bar']
```
```python 
# Remove Multiple Items
names = ['John', 'Doe', 'Foo', 'Bar']
del names[1:3]
print(names) # Output: ['John', 'Bar']
```
```python 
# Remove item passing Value
names = ['John', 'Doe', 'Foo', 'Bar']
names.remove('John')
print(names) # Output: ['Doe', 'Foo', 'Bar']
```
```python 
# Remove all items 
names = ['John', 'Doe', 'Foo', 'Bar']
names.clear()
print(names) # Output: []
```

### Other Method of List
```python
# Sort the List Item
nums = [23, 33, 52, 65, 76, 28, 32]
nums.sort()
print(nums) # Output: [23, 28, 32, 33, 52, 65, 76]
```
```python
# Reverse the List Item
nums = [23, 33, 52, 65, 76, 28, 32]
nums.reverse()
print(nums) # Output: [32, 28, 76, 65, 52, 33, 23]
# or
print(nums[::-1]) # Output: [32, 28, 76, 65, 52, 33, 23]
```
```python
# copy() creates a new Instance of List. 
nums = [23, 33, 52, 65, 76, 28, 32]
nums2 = nums.copy()
nums2.append(100)
print(nums) # Outptu: [23, 33, 52, 65, 76, 28, 32]
print(nums2) # Output: [23, 33, 52, 65, 76, 28, 32, 100]
```
```python
# Shortcut Create List
similar_nums = [4] * 10
print(similar_nums) # Output: [4, 4, 4, 4, 4, 4, 4, 4, 4, 4]
```
```python
# print the index & value using enumerate()
nums = [23, 33, 52, 65, 76, 28, 32]
for index, value in enumerate(nums):
    print(index, value)
# Output: 
# 0 23
# 1 33
# 2 52
# 3 65
# 4 76
# 5 28
# 6 32
```
**[⬆ back to top](#table-of-contents)**


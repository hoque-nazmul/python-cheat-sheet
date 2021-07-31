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
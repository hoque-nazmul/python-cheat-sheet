# Normal Function Defination
def add (num1, num2):
    return num1 + num2 

print(add(25, 10)) # Output: 35

# Set a Default Argument
def say_hello (name, greeting="Hello"):
    return f"{greeting}, {name}"

print(say_hello("John", 'Hey')) # Output: Hey, John
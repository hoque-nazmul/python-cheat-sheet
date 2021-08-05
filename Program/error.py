# Define a Divided Function
def get_div (num1, num2):
    return num1 / num2

# Problem: 1
print(get_div(10, 0))
# Error Output: ZeroDivisionError: division by zero

# Handle the Problem: 1
try:
    print(get_div(10, 0))
except ZeroDivisionError:
    print("You can't divided by Zero!")
# Output: You can't divided by Zero!


# Problem: 2
print(get_div(1, '1'))
# Error Output: TypeError: unsupported operand type(s) for /: 'int' and 'str'

# Handle the Problem: 2
try:
    print(get_div(1, '1'))
except ZeroDivisionError:
    print("You can't divided by Zero!")
except TypeError:
    print("You can't divided by String")

# Output: You can't divided by String

# If don't have any exception, else block will work
def get_div(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("You can't divided by Zero!")
    except TypeError:
        print("You can't divided by String")
    else:
        return result

print(get_div(4, 2))
# Output: 2.0

# If we want to run after completing the try, else or even except block, 'finally' block is perfect for that.
# Defining Try, Catch block inside get_div function
def get_div(a, b):
    try: 
        result = a / b
    except ZeroDivisionError:
        print("You can't divided by Zero")
    except TypeError:
        print("You can't divided by String")
    else:
        return result
    finally:
        print('Operation is Completed!')

print(get_div(3, 5))
# Operation is Completed! 
# 0.6

print(get_div(3, 0))
# You can't divided by Zero
# Operation is Completed!
# None

print(get_div(3, '4'))
# You can't divided by String
# Operation is Completed!
# None
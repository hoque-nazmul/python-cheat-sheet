# It'll be return a Tuple
def get_nums (*nums):
    return nums

print(get_nums(2, 3, 4, 5, 6)) # Output: (2, 3, 4, 5, 6)

# It'll be return a Dictionary
def get_data (**data):
    return data

print(get_data(name='John Doe', age=20)) # Output: {'name': 'John Doe', 'age': 20}
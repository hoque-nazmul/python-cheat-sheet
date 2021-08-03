# # Math Relavant Built-in Function

# # sum()
# print(sum([2, 3, 5])) # Output: 10
# print(sum((2, 3, 5))) # Output: 10
# print(sum({2, 3, 5})) # Output: 10
# # We can define a start value as 2nd arg
# print(sum([2, 3], 10)) # Output: 15

# # divmod()
# # divmod() takes two int as arguments and returns a tuple of two numbers where the 1st number is the quotient and the 2nd is the remainder.
# print(divmod(10, 3)) # Output: (3, 1)

# # abs()
# print(abs(-1)) # Output: 1

# # round()
# print(round(12.20)) # Output: 12
# print(round(12.55)) # Output: 13

# # pow()
# print(pow(3,2)) # Output: 9
# print(pow(3,3)) # Output: 27
# print(pow(5,2)) # Output: 25

# # min()
# print(min(3, 2, 4, 7)) # Output: 2
# print(min([5, 2, 8, 1])) # Output: 1

# # max()
# print(max([5, 2, 8, 1])) # Output: 8
# print(max(10, 2, 8, 1)) # Output: 10

# # range()
# print([*range(5)]) # Output: [0, 1, 2, 3, 4]
# print([*range(0, 5, 2)]) # Output: [0, 2, 4]

# # format()
# print(format(10, '.2%')) # Output: 1000.00%
# print(format(100, 'b')) # Output: 1100100 (Binary of 100)
# print(format(100, 'o')) # Output: 144 (Octal of 100)
# print(format(1000, 'x')) # Output: 3e8 (hex of 1000)
# print(format(1000, 'X')) # Output: 3E8 (hex of 1000)
# print(format(10.0040, '.1f')) # Output: 10.0
# print(format(100000, ',')) # Output: 100,000
# print(format(100000, 'n')) # Output: 100000
# print(format(3.13592, '.2g')) # Output: 3.1

# # eval()
# print(eval('2 + 5')) # Output: 7

# # Function for Number System
# # int(), bin(), oct(), hex(), format(value, first chr of number system)
# print(int('10')) # Output: 10
# print(type(int('10'))) # Output: <class 'int'>
# print(int(0b1010)) # Output: 10
# print(bin(10)) # Output: 0b1010
# print(oct(70)) # Output: 0o106
# print(hex(1000)) # Output: 0x3e8
# print(format(1000, 'x')) # Output: 3e8 (hex of 1000)

# # Data type Functions
# str()
# int()
# float()
# list()
# tuple()
# set()
# dict()
# frozenset()

# # Fuctions for Traversing Iterable Object
# all()
# all() retuns False, if any the of iterable object item is Falsy, Otherwise it returns True 
# print(all([])) # Output: True
# print(all([1, 2, 3])) # Output: True
# print(all([1, 2, 0])) # Output: False

# # any()
# # any() returns False, if all of the iterable object item is Falsy or empty iterable like [], () etc. Otherwise it returns True
# print(any([])) # Output: False
# print(any([1, 2, 3])) # Output: True
# print(any([1, 2, 0])) # Output: True
# print(any([0, False, ''])) # Output: False

# # map()
# def get_double(item):
#     return item + item
# mapped = map(get_double, [2, 3, 4])
# print(mapped) # Output: <map object at 0x0000023AF5BCA1F0>
# # Readable map object
# print(list(mapped)) # Output: [4, 6, 8]

# # Implement Map with magic lambda function
# mapped_obj = map(lambda x: x + x, [2, 3, 4])
# mapped_list = list(mapped_obj)
# print(mapped_list) # Same Output: [4, 6, 8]
# # or Simply 
# print(list(map(lambda x: x + x, [2, 3, 4]))) # Output: [4, 6, 8]
# # We Can pass multiple iterable object as arg
# print(list(map(lambda first_li_item, seccond_li_item: first_li_item + seccond_li_item, [1, 2, 3], [100, 200, 300])))
# # Output: [101, 202, 303]

# # filter()
# def get_adult(age):
#     if age > 18:
#         return age
# filtered_age_obj = filter(get_adult, [22, 10, 12, 40, 32, 33, 15])
# print(filtered_age_obj) # Output: <filter object at 0x00000261B6F6A1F0>
# filtered_age_list = list(filtered_age_obj)
# print(filtered_age_list) # Output: [22, 40, 32, 33]
# # Implement filter() using lambda function
# filtered_obj = filter(lambda age: age > 18, [22, 10, 12, 40, 32, 33, 15])
# filtered_list = list(filtered_obj)
# print(filtered_list) # Output: [22, 40, 32, 33]
# # Or Simply print in one line
# print(list(filter(lambda age: age > 18, [22, 10, 12, 40, 32, 33, 15])))
# # Exactly Same Output: [22, 40, 32, 33]

# # sorted()
# # default sorted function -> sorted(iterable, key=None, reverse=False)
# # smaller -> bigger
# print(sorted([11, 2, 43, 10, 50, 5, 7])) #Output: [2, 5, 7, 10, 11, 43, 50]
# # bigger -> smaller
# print(sorted([11, 2, 43, 10, 50, 5, 7], key=None, reverse=True)) #Output: [50, 43, 11, 10, 7, 5, 2]

# # reversed()
# print(list(reversed([32,22,31]))) # Output: [31, 22, 32]
# print(tuple(reversed((32,22,31)))) # Output: (31, 22, 32)
# print(list(reversed((32,22,31)))) # Output: [31, 22, 32]
# # Reverse string
# print(''.join(reversed('Hello World'))) # Output: dlroW olleH

# # len()
# print(len([2,3,4])) # Output: 3
# print(len({'name': 'John', 'age': 30}))  # Output: 2
# print(len('Hello'))  # Output: 5

# enumerate()
# zip()
# slice()
# # min(), max()
# print(min([5, 2, 8, 1])) # Output: 1
# print(max([5, 2, 8, 1])) # Output: 8

# # Access the Object property 
# getattr()
# setattr()
# delattr()
# hasattr()

# # Int -> Unicode & Unicode -> Int
# # chr(), ord()
# print(ord('a')) # Output: 97
# print(chr(97))  # Output: a

# # Iterators
# # iter(), next()
# # iter() function is used to create iterable object & next() is used to access the item of Iterable Object.
# itr = iter([5,2,3])
# print(type(itr)) # Output: <class 'list_iterator'>
# print(next(itr)) # Output: 5

# # Input & Ouput
# # input(), print()
# name = input('Please type your name: ')
# print(name)

# # Referance Builtin Function
# dir()
# id()
# globals()
# locals()
# vars()

# # Builtin Function for Checking
# bool()
# type()
# isinstance()
# issubclass()
# callable()

# # Others Builtin Function
# open()
# __import__
# ascii()
# help()
# hash()
# breakpoint()
# exec()
# classmethod()
# # super()
# property()
# bytes()
# bytearray()
# object()
# memoryview()
# staticmethod()
# repr()
# compile()
# complex()
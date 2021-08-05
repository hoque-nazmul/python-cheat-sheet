# # Math Relavant Built-in Function

# sum()
print(sum([2, 3, 5])) # Output: 10
print(sum((2, 3, 5))) # Output: 10
print(sum({2, 3, 5})) # Output: 10
# We can define a start value as 2nd arg
print(sum([2, 3], 10)) # Output: 15

# divmod()
# divmod() takes two int as arguments and returns a tuple of two numbers where the 1st number is the quotient and the 2nd is the remainder.
print(divmod(10, 3)) # Output: (3, 1)

# abs()
print(abs(-1)) # Output: 1

# round()
print(round(12.20)) # Output: 12
print(round(12.55)) # Output: 13

# pow()
print(pow(3,2)) # Output: 9
print(pow(3,3)) # Output: 27
print(pow(5,2)) # Output: 25

# min()
print(min(3, 2, 4, 7)) # Output: 2
print(min([5, 2, 8, 1])) # Output: 1

# max()
print(max([5, 2, 8, 1])) # Output: 8
print(max(10, 2, 8, 1)) # Output: 10

# range()
print([*range(5)]) # Output: [0, 1, 2, 3, 4]
print([*range(0, 5, 2)]) # Output: [0, 2, 4]

# format()
print(format(10, '.2%')) # Output: 1000.00%
print(format(100, 'b')) # Output: 1100100 (Binary of 100)
print(format(100, 'o')) # Output: 144 (Octal of 100)
print(format(1000, 'x')) # Output: 3e8 (hex of 1000)
print(format(1000, 'X')) # Output: 3E8 (hex of 1000)
print(format(10.0040, '.1f')) # Output: 10.0
print(format(100000, ',')) # Output: 100,000
print(format(100000, 'n')) # Output: 100000
print(format(3.13592, '.2g')) # Output: 3.1

# eval()
print(eval('2 + 5')) # Output: 7

# Function for Number System
# int(), bin(), oct(), hex(), format(value, first chr of number system)
print(int('10')) # Output: 10
print(type(int('10'))) # Output: <class 'int'>
print(int(0b1010)) # Output: 10
print(bin(10)) # Output: 0b1010
print(oct(70)) # Output: 0o106
print(hex(1000)) # Output: 0x3e8
print(format(1000, 'x')) # Output: 3e8 (hex of 1000)

# Data type Functions
str()
int()
float()
list()
tuple()
set()
dict()
frozenset()

# Fuctions for Traversing Iterable Object
# all()
# all() retuns False, if any the of iterable object item is Falsy, Otherwise it returns True 
print(all([])) # Output: True
print(all([1, 2, 3])) # Output: True
print(all([1, 2, 0])) # Output: False

# any()
# any() returns False, if all of the iterable object item is Falsy or empty iterable like [], () etc. Otherwise it returns True
print(any([])) # Output: False
print(any([1, 2, 3])) # Output: True
print(any([1, 2, 0])) # Output: True
print(any([0, False, ''])) # Output: False

# map()
def get_double(item):
    return item + item
mapped = map(get_double, [2, 3, 4])
print(mapped) # Output: <map object at 0x0000023AF5BCA1F0>
# Readable map object
print(list(mapped)) # Output: [4, 6, 8]

# Implement Map with magic lambda function
mapped_obj = map(lambda x: x + x, [2, 3, 4])
mapped_list = list(mapped_obj)
print(mapped_list) # Same Output: [4, 6, 8]
# or Simply 
print(list(map(lambda x: x + x, [2, 3, 4]))) # Output: [4, 6, 8]
# We Can pass multiple iterable object as arg
print(list(map(lambda first_li_item, seccond_li_item: first_li_item + seccond_li_item, [1, 2, 3], [100, 200, 300])))
# Output: [101, 202, 303]

# filter()
def get_adult(age):
    if age > 18:
        return age
filtered_age_obj = filter(get_adult, [22, 10, 12, 40, 32, 33, 15])
print(filtered_age_obj) # Output: <filter object at 0x00000261B6F6A1F0>
filtered_age_list = list(filtered_age_obj)
print(filtered_age_list) # Output: [22, 40, 32, 33]

# Implement filter() using lambda function
filtered_obj = filter(lambda age: age > 18, [22, 10, 12, 40, 32, 33, 15])
filtered_list = list(filtered_obj)
print(filtered_list) # Output: [22, 40, 32, 33]

# Or Simply print in one line
print(list(filter(lambda age: age > 18, [22, 10, 12, 40, 32, 33, 15])))
# Exactly Same Output: [22, 40, 32, 33]

# sorted()
# default sorted function -> sorted(iterable, key=None, reverse=False)
# smaller -> bigger
print(sorted([11, 2, 43, 10, 50, 5, 7])) #Output: [2, 5, 7, 10, 11, 43, 50]
# bigger -> smaller
print(sorted([11, 2, 43, 10, 50, 5, 7], key=None, reverse=True)) #Output: [50, 43, 11, 10, 7, 5, 2]

# reversed()
print(list(reversed([32,22,31]))) # Output: [31, 22, 32]
print(tuple(reversed((32,22,31)))) # Output: (31, 22, 32)
print(list(reversed((32,22,31)))) # Output: [31, 22, 32]
# Reverse string
print(''.join(reversed('Hello World'))) # Output: dlroW olleH

# len()
print(len([2,3,4])) # Output: 3
print(len({'name': 'John', 'age': 30}))  # Output: 2
print(len('Hello'))  # Output: 5

enumerate()
bd_players = ['Tamim Iqbal', 'Moshfiqur Rahim', 'Sakib Al Hasan', 'Mashrafi Mortaza', 'Mahmudullah Riad']
# Start Default -> 0
print(list(enumerate(bd_players, start=1)))
# Output: [(0, 'Tamim Iqbal'), (1, 'Moshfiqur Rahim'), (2, 'Sakib Al Hasan'), (3, 'Mashrafi Mortaza'), (4, 'Mahmudullah Riad')]

# zip()
# Pack the multiple iterable object
bd_players = ['Tamim Iqbal', 'Moshfiqur Rahim', 'Sakib Al Hasan', 'Mashrafi Mortaza', 'Mahmudullah Riad']
runs = [23, 55, 75, 10, 34]
wickets = [0, 0, 4, 2, 3]
print(list(zip(bd_players, runs, wickets)))
# Output: [('Tamim Iqbal', 23, 0), ('Moshfiqur Rahim', 55, 0), ('Sakib Al Hasan', 75, 4), ('Mashrafi Mortaza', 10, 2), ('Mahmudullah Riad', 34, 3)]

# min(), max()
print(min([5, 2, 8, 1])) # Output: 1
print(max([5, 2, 8, 1])) # Output: 8

# Access the Object property 
# hasattr() setattr(), getattr(), delattr(), 
class Person:
    pass
ps = Person()
print(hasattr(ps, 'name')) # Output: False
setattr(ps, 'name', 'John Foo')
print(hasattr(ps, 'name')) # Output: True
print(getattr(ps, 'name')) # Output: John Foo
delattr(ps, 'name')
print(hasattr(ps, 'name')) # Output: False


# Int -> Unicode & Unicode -> Int
# chr(), ord()
print(ord('a')) # Output: 97
print(chr(97))  # Output: a

# Iterators
# iter(), next()
# iter() function is used to create iterable object & next() is used to access the item of Iterable Object.
itr = iter([5,2,3])
print(type(itr)) # Output: <class 'list_iterator'>
print(next(itr)) # Output: 5

# Input & Ouput
# input(), print()
name = input('Please type your name: ')
print(name)

# Referance Builtin Function
# dir()
# dir() function returns list of the attributes and methods of any object like functions , modules, strings, lists, dictionaries etc. If no argument passed, it returns the list of names in the current local scope.
print(dir()) 
# Output: ['__annotations__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__']
print(dir(list))
# Output: ['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
print(dir(tuple))
# Output: ['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'count', 'index']

# vars()
# vars() provides the built in function provided by python standard library.
# The vars() function returns the __dic__ attribute of an object.
# The __dict__ attribute is a dictionary containing the object's changeable attributes.
name = "Justin"
print(vars())
# Output: {'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <_frozen_importlib_external.SourceFileLoader object at 0x7f5182a994c0>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, '__file__': 'Program/builtin.py', '__cached__': None, 'name': 'Justin'}
print(vars(list))
# Output: {'__repr__': <slot wrapper '__repr__' of 'list' objects>, '__hash__': None, '__getattribute__': <slot wrapper '__getattribute__' of 'list' objects>, '__lt__': <slot wrapper '__lt__' of 'list' objects>, '__le__': <slot wrapper '__le__' of 'list' objects>, '__eq__': <slot wrapper '__eq__' of 'list' objects>, '__ne__': <slot wrapper '__ne__' of 'list' objects>, '__gt__': <slot wrapper '__gt__' of 'list' objects>, '__ge__': <slot wrapper '__ge__' of 'list' objects>, '__iter__': <slot wrapper '__iter__' of 'list' objects>, '__init__': <slot wrapper '__init__' of 'list' objects>, '__len__': <slot wrapper '__len__' of 'list' objects>, '__getitem__': <method '__getitem__' of 'list' objects>, '__setitem__': <slot wrapper '__setitem__' of 'list' objects>, '__delitem__': <slot wrapper '__delitem__' of 'list' objects>, '__add__': <slot wrapper '__add__' of 'list' objects>, '__mul__': <slot wrapper '__mul__' of 'list' objects>, '__rmul__': <slot wrapper '__rmul__' of 'list' objects>, '__contains__': <slot wrapper '__contains__' of 'list' objects>, '__iadd__': <slot wrapper '__iadd__' of 'list' objects>, '__imul__': <slot wrapper '__imul__' of 'list' objects>, '__new__': <built-in method __new__ of type object at 0x905e20>, '__reversed__': <method '__reversed__' of 'list' objects>, '__sizeof__': <method '__sizeof__' of 'list' objects>, 'clear': <method 'clear' of 'list' objects>, 'copy': <method 'copy' of 'list' objects>, 'append': <method 'append' of 'list' objects>, 'insert': <method 'insert' of 'list' objects>, 'extend': <method 'extend' of 'list' objects>, 'pop': <method 'pop' of 'list' objects>, 'remove': <method 'remove' of 'list' objects>, 'index': <method 'index' of 'list' objects>, 'count': <method 'count' of 'list' objects>, 'reverse': <method 'reverse' of 'list' objects>, 'sort': <method 'sort' of 'list' objects>, '__doc__': 'Built-in mutable sequence.\n\nIf no argument is given, the constructor creates a new empty list.\nThe argument must be an iterable if specified.'}

globals()
# It always returns the global scope data. either inside of funtion of outside of a function.
name = "Justin"
print(globals())
# Output: {'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <_frozen_importlib_external.SourceFileLoader object at 0x7f69628e04c0>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, '__file__': 'Program/builtin.py', '__cached__': None, 'name': 'Justin'}

# locals()
# It returns only function local scope data, if we use it inside a function
# if we use it in globle scope, it will react like globals() - I mean, return the global scope data.
name = "Justin"
print(locals())
print('hey')
def diff_locals_and_globals():
    age = 20
    print(globals())
    print(locals())

diff_locals_and_globals()
# globals() Output -> {'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <_frozen_importlib_external.SourceFileLoader object at 0x7fe5c69dc4c0>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, '__file__': 'Program/builtin.py', '__cached__': None, 'name': 'Justin', 'diff_locals_and_globals': <function diff_locals_and_globals at 0x7fe5c6885dc0>}
# locals() Output: {'age': 20}

# id()
# id() is a adresss of the object in memory. It returns the unique identity of an object.
print(id('John')) # 140434664974640
print(id(10)) # 9788896
print(id([21, 54, 65])) # 139834604658304
print(id({'name': 'Doe'})) # 140615104266112


# Builtin Function for Checking
# bool()
# bool() is used to check the Truthy & Falsy value
print(bool(0)) # False
print(bool(1)) # True
print(bool([]), bool([100, 200])) # False True

# type()
# type() is used to check the data type
print(type('he he')) # Output: <class 'str'>
print(type(['hey', 'hello'])) # Output: <class 'list'>
print(type(20)) # Output: <class 'int'>

# isinstance(), issubclass()
class Rectangle:
    def __init__(self, height, width):
        self.height = height
        self.width = width
    
    def get_area(self):
        return self.height * self.width

class Square(Rectangle):
    pass

rc = Rectangle(5, 4)
sq = Square(5, 5)
print(isinstance(rc, Rectangle)) # True
print(isinstance(sq, Rectangle)) # True
print(isinstance(sq, Square)) # True
print(isinstance(rc, Square)) # False

print(issubclass(Square, Rectangle)) # True
print(issubclass(Rectangle, Square)) # False


# Others Builtin Function
open()
__import__
ascii()
slice()
callable()
help()
hash()
breakpoint()
exec()
classmethod()
# super()
property()
bytes()
bytearray()
object()
memoryview()
staticmethod()
repr()
compile()
complex()
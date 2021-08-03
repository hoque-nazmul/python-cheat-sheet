# Write in a File
with open('hello.txt', 'w') as fp:
    fp.write('Hello World\n')
    fp.write('Another Text\n')
    fp.write('Python is Awesom\n')

# Read a File
with open('hello.txt', 'r') as fp:
    print(fp.read())
# Output:
# Hello World
# Another Text
# Python is Awesom

# Loop throw the line of file using readlines()
lines = []
with open('hello.txt', 'r') as fp:
    for line in fp.readlines():
        lines.append(line)
print(lines) 
# Output: ['Hello World\n', 'Another Text\n', 'Python is Awesom\n']

# Read the First Line using readline()
with open('hello.txt', 'r') as fp:
    print(fp.readline())
# Output: Hello World

# Add a new line in a Existing File using Append Mode
with open('hello.txt', 'a') as fp:
    fp.write('Another line added in append mode')

with open('hello.txt', 'r') as fp:
    print(fp.read())
# Output: 
# Hello World
# Another Text
# Python is Awesom
# Another line added in append mode

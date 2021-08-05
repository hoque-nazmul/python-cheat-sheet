# When the loop iteration is completed, then the 'StopIteration Exception' & 'else' execute.
for item in range(1,4):
    print(item)
else:
    print('Item Finished!')
# Output: 1 2 3
# Item Finished!

# If the loop iteration isn't completed, 'StopIteration Exception' & 'else' won't execute.
for i in range(1, 5):
    if i > 3:
        break
    print(i)
else:
    print('Iteration Complete!')
# Output: 1 2 3

# Implementing Loop Exception logic, We can create efficient program. Such as:
def check_prime(num):
    for i in range(2, num):
        if num % i == 0:
            print(False)
            break
    else:
        print(True)

# print(check_prime(17)) # True
# print(check_prime(13)) # True
# print(check_prime(10)) # False


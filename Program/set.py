# It's Iterable. Doesn't have any index to access. We can add, delete, clear & copy the item of Set. 
nums = {2, 3, 4, 5, 6}

# Remove the Duplicate item of List & Tuple
print(set((22, 23, 22, 23))) # Output: {22, 23}
print(set([54, 50, 50, 55])) # Output: {50, 54, 55}

# Mathmatical Operation Using Set
a_set = {1, 2, 3, 4}
b_set = {2, 4, 5, 6}

# Union 
a_set = {1, 2, 3, 4}
b_set = {2, 4, 5, 6}
print(a_set | b_set) # Output: {1, 2, 3, 4, 5, 6}
# or
print(a_set.union(b_set)) # Output: {1, 2, 3, 4, 5, 6}

# Intersection
a_set = {1, 2, 3, 4}
b_set = {2, 4, 5, 6}
print(a_set & b_set) # Output: {2, 4}
# or
print(a_set.intersection(b_set)) # Output: {2, 4}

# Difference
a_set = {1, 2, 3, 4}
b_set = {2, 4, 5, 6}
print(a_set - b_set) # Output: {1, 3}
# or
print(a_set.difference(b_set)) # Output: {1, 3}

# Symmetric Difference
a_set = {1, 2, 3, 4}
b_set = {2, 4, 5, 6}
print(a_set ^ b_set) # Output: {1, 3, 5, 6}
# or
print(a_set.symmetric_difference(b_set)) # Output: {1, 3, 5, 6}

# Set Conversion
nums = {2, 3, 4, 5, 6}
print(list(nums)) # Output: [2, 3, 4, 5, 6]
print([*nums]) # Output: [2, 3, 4, 5, 6]
print(tuple(nums)) # Output: (2, 3, 4, 5, 6)


# Add the Item in Last of Set
nums = {2, 3, 4, 5, 6}
nums.add(10)
print(nums) # Output: {2, 3, 4, 5, 6, 10}

# Remove the First Item of Set
nums = {2, 3, 4, 5, 6}
nums.pop()
print(nums) # Output: {3, 4, 5, 6}

# Remove the Specific Item of Set
nums = {2, 3, 4, 5, 6}
nums.remove(5)
print(nums) # Output: {2, 3, 4, 6}

# Clear the Whole Set
nums = {2, 3, 4, 5, 6}
nums.clear()
print(nums) # Output: set()

# Create a New Instance of Set using copy()
nums = {2, 3, 4, 5, 6}
nums_1 = nums.copy()
# Before Changing nums_1
print(nums) # Output: {2, 3, 4, 5, 6}
print(nums_1) # Output: {2, 3, 4, 5, 6}

nums_1.add(100)
# After Changing nums_1
print(nums) # Output: {2, 3, 4, 5, 6}
print(nums_1) # Output: {2, 3, 4, 5, 6, 100}




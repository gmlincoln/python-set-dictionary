"""my_set = {1, 2, 3, 4}

print(type(my_set))"""

# fruits = {"apple", "banana", "mango"}
# print(fruits)

# {} or set([])

# numbers = set([1, 2, 3, 4])
# print(numbers)

# empty_set1 = set()    # Correct
# empty_set2 = {}       # Wrong → This creates a dictionary

# print(type(empty_set1))
# print(type(empty_set2))

fruits = {"apple", "banana"}

fruits.add("mango")

# print(fruits)

fruits.update(["grape", "orange"])

print(fruits)

# {'apple', 'mango', 'grape', 'orange', 'banana'}

# fruits.remove("bandana")
# print(fruits)

# fruits.discard("bana")
# print(fruits)


# fruits.pop() 
# print(fruits)

# fruits.clear()

# print(fruits)

a = {1, 2, 3}
b = {3, 4, 5}

print(a.union(b)) # {1, 2, 3, 4, 5}
print(a.intersection(b)) # {3}

print(a.difference(b)) # {1, 2}

numbers = [1, 2, 2, 3, 4, 4, 5]
numbers_set = set(numbers)
print(numbers_set)
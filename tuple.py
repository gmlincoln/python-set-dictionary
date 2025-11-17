"""my_tuple = (10, 20, 30)
print(my_tuple)
print(type(my_tuple))"""

"""
student = ("Rahim", 21, 3.75, True)
print(id(student))
print(student)

"""

#Tuple Packing 
"""
fruits = "apple", "mango", "banana"

print(fruits)"""

#Single Item in Tuple

"""
single_tuple = (10,)       # Correct
print(single_tuple)
print(type(single_tuple))

# Wrong → This is an integer
not_tuple = (10) 
print(type(not_tuple))    
"""


"""numbers = (10, 20, 30, 40, 50, 40)
print(numbers[0])   # 10
print(numbers[2])   # 30

print(numbers[-1])  #40
print(numbers[-3])  #20
print(numbers[0:-3]) """



# name = "hello world!"


# print(name[6:11])
# print(name[-1])


"""colors = ("red", "green", "blue")

for c in colors:
    print(c)"""

"""
person = ("Rafi", 25, "Dhaka")

name, age, city = person

print(name)  # Rafi
print(age)   # 25
print(city)  # Dhaka
"""

"""

values = (10, 20, 30, 40, 50)

a, b, *others = values

print(a)     # 10
print(b)     # 20
print(others)  # [30, 40, 50]

"""

students = [
    ("Shuvo", 24),
    ("Fairoz", 23),
    ("Tamim", 22),
    ("Sayem", 25)
]

# print(type(students[2]))
# print(students[3][0])
# print(students[3][1])



#Modify the tuple value using index numbe

"""

num = (10, 20, 30, 40, 50)
# print(type(num))


numList = list(num)
# print(type(numList))

numList[3] = 60
print(numList)

num = tuple(numList)
print(num)

"""
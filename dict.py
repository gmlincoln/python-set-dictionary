# couple = {
#     "Abul" : "Abida",
#     "Babul" : "Bobita",
#     "Cabul" : "Chobita",
# }

# print(couple["Abul"])



student = {
    "name": "Karina", 
}


# print(student["name"])  # Karina
# print(student.get("dept"))       # CSE
print(student.get("CGPA", "N/A")) 
student2 = student.setdefault("dept", "EEE")
print(student2)

# student["cgpa"] = 3.92
# student["name"] = "Tamim"

#  print(student)


student = {
    "name": "Shuvo",
    "age": 22, 
    "city": "Dhaka",
    "isMarried": False,
}


# student.pop("age")  # removes age key

# print(student)

# student.popitem()
# print(student)

student = {
    "name": "Shuvo",
    "age": 22, 
    "city": "Dhaka",
    "isMarried": False,
}

# student["name"] -> Shuvo


# print("Keys: ")

# for key in student:
#     print(key)

# # print("Values: ")
# for value in student.values():
#     print(value)

# for key, value in student.items():
#     print(key, value)


# allKeys = student.keys()

# for key in allKeys:
#     print(student[key])

# student_two = student.copy()

# print(student_two)

# game_one = {
#     "batsman1":{
#         "name": "Tamim",
#         "run" : 42
#     },
#     "batsman2":{
#         "name": "Shuvo",
#         "run": 30
#     },
#     "batsman3":{
#         "name": "Saikot",
#         "run" : 13
#     },
#     "batsman4":{
#         "name": "Sultan",
#         "run" : 0
#     }
    
# }

# batsman3 = game_one["batsman3"]

# print(batsman3["name"])
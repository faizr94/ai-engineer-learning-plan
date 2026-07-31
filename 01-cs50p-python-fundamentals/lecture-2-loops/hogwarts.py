# students = ["Hermione", "Harry", "Ron"]

# for student in students:
#     print(student)
# for i in range(len(students)):
#     print(i+1, students[i])


# Using dictionary
# students = {
#     "Hermione": "Gryffindor",
#     "Harry": "Gryffindor",
#     "Ron": "Gryffindor",
#     "Draco": "Slytherin",
# }

#List of dictionaries
students = [
    {"name": "Hermione", "house": "Gryffindor", "patronus": "Otter"},
    {"name": "Harry", "house": "Gryffindor", "patronus": "Stag"},
    {"name": "Ron", "house": "Gryffindor", "patronus": "Jack Russell Terrier"},
    {"name": "Draco", "house": "Slytherin", "patronus": None},
]



# you can use words as indices for dictionaries
# for loops for dictionaries will return you the keys
for student in students:
    print(student["name"], student["house"], student["patronus"], sep=", ")
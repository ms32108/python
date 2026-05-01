students = {
    "Mani":"Chirra",
    "Sai":"Ch",
    "Raju":"C"
}

"""
print(students["Mani"])
print(students["Sai"])
print(students["Raju"])
"""

for student in students:
    print(student) # print only keys
    print(student,students[student]) # print keys with values too
    print(student,students[student],sep=",") # print keys with values too with seperator
    
    
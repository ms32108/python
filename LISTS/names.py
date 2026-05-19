#declare an empty list
students=[]


for i in range(3):
    name =input(f"Whats name {i+1} = ")
    students.append(name)
"""
for i in range(3):
    students.append(input("Whats ur name??"))

"""

for i,name in enumerate(sorted(students),start=1):
    print(f"{i}. hello, {name}")



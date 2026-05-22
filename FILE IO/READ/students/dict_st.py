students=[]



with open("students.csv") as file:
    for line in file:
        name,marks=line.rstrip().split(",")
        student={"name":name,"marks":marks}
        students.append(student)
print("Unsorted")
for i in students:
    print(f"{i['name']} got {i['marks']}")
    
print("Sorted")
for i in sorted(students):
    print(f"{i['name']} got {i['marks']}")



"""
with open("students.csv") as file:
    for line in file:
        name,marks=line.rstrip().split(",")
        student={}
        student["name"]=name
        student["marks"]=marks
        students.append(student)
"""
    

 
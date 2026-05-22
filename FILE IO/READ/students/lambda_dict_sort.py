students=[]
with open("students.csv") as file:
    for line in file:
        name,marks=line.rstrip().split(",")
        student={"name":name,"marks":int(marks)}
        students.append(student)


for student in sorted(students,key=lambda student :student["marks"] ):
    print(f"{student['name']} got {student['marks']}")
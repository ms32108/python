import csv

# no need to use strip , split etc ?? easy

students=[]
with open("students.csv") as file:
    reader =csv.reader(file)
    for name,marks in reader:
        student={"name":name,"marks":int(marks)}
        students.append(student)


for student in sorted(students,key=lambda student :student["marks"] ):
    print(f"{student['name']} got {student['marks']}")

"""

students=[]
with open("students.csv") as file:
    reader =csv.reader(file)
    for row in reader:
        student={"name":row[0],"marks":int(row[1]))}
        students.append(student)

"""
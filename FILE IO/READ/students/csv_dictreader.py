import csv
students=[]
with open("students_heads.csv") as file:
    reader =csv.DictReader(file)
    for row in reader:
        students.append({"name":row["name"],"marks":row["marks"]})
        #or simple students.append(row) as Dictreader return 1 dict at a time


for student in sorted(students,key=lambda student :student["marks"] ):
    print(f"{student['name']} got {student['marks']}")


#    reader =csv.DictReader(file) reades first 1 line as keys (headers)
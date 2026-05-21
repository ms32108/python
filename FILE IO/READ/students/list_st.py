students=[]

with open("students.csv") as file:
    for line in file:
        student,marks=line.rstrip().split(",")
        students.append(f"{student} got {marks}")

    for i in sorted(students):
        print(i)
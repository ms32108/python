students=[]
student={}


with open("students.csv") as file:
    for line in file:
        student,marks=line.rstrip().split(",")
        students["student"]=student
        students["marks"]=marks
        students.append(student)
    for i in students:
        print(f"{i['name']} got {i['score']}")

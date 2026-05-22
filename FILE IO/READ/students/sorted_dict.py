students=[]
with open("students.csv") as file:
    for line in file:
        name,marks=line.rstrip().split(",")
        student={"name":name,"marks":marks}
        students.append(student)
print("Unsorted :")
for i in students:
    print(f"{i['name']} got {i['marks']}")


#Now sorted

def get_marks(i):
    return i["marks"]
print("Sorted :")
for i in sorted(students,key=get_marks):
    print(f"{i['name']} got {i['marks']}")
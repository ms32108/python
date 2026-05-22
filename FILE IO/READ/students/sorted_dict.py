students=[]
with open("students.csv") as file:
    for line in file:
        name,marks=line.rstrip().split(",")
        student={"name":name,"marks":int(marks)}
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


"""
names = ["Mani","Sai","Chirra"]
print(sorted(names,key=len))

## internally
# 
#   for i  in names
    ....len(i)   

    hold 3,4,5 values then maps to the strings in the list then prints them 
    this how len vs len()this calls function()   

"""
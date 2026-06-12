def main():
    student=get_student()
    student1=get_student_dict()
    student2=get_student_dict1()
    print(f"{student[0]} from {student[1]}")
    print(f"{student1['name']} from {student1['house']}")
    print(f"{student2['name']} from {student2['house']}")


def get_student():
    name= input("Name: ")
    house= input("House: ")
    return (name,house) #returning 1 value which is a tuple (name,house)

def get_student_dict():
    student={}
    student["name"]= input("Name: ")
    student["house"]= input("House: ")
    return student

def get_student_dict1():
    name= input("Name: ")
    house= input("House: ")
    return {"name":name,"house":house}

if __name__ =="__main__":
    main()
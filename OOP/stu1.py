#Using Class
class Student:
    ... 

def main():
    student=get_student()
    print(f"{student.name} got {student.marks}")



def get_student():
    student=Student() # creating an obj from class
    student.name = input("Name:")
    student.marks = input("Marks:")
    return student



if __name__ =="__main__":
    main()
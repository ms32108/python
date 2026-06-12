#Using Class
class Student:
    def __init__(self,name,marks):  # contents of the method
        self.name=name
        self.marks=marks


def main():
    student=get_student()
    print(f"{student.name} got {student.marks}")



def get_student():
    name = input("Name:")
    marks = input("Marks:")
    student=Student(name,marks)
    return student
#or
#   return Student(name,marks) itself



if __name__ =="__main__":
    main()
with open("students.csv") as file:
    for line in file:
        student=line.rstrip().split(",")
        #student,marks=line.rstrip().split(",") can also be used
        if int(student[1]) < 35:
            print(f"{student[0]}=={student[1]}  [FAILED]")
        else:
             print(f"{student[0]}=={student[1]}  [PASSED]")     
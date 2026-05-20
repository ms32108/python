with open("students.csv") as file:
    for line in file:
        student=line.rstrip().split(",")
        if int(student[1]) < 35:
            print(f"{student[0]} got {student[1]} marks in the test and as FAILED the test")
        else:
             print(f"{student[0]} got {student[1]} marks in the test and as PASSED the test")
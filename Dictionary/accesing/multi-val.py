#Multi values
students = {"name": ["Mani","Sai","MS"], "age": 20}
students = {"name": {"Mani","Sai","MS"}, "age": 20}
#for i in student:
print(students.get(("name")[1]))
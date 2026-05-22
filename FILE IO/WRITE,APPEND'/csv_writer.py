import csv
name=input("name=")
marks=input("marks=")

with open("students.csv","a") as file:
    writer=csv.writer(file)
    writer.writerow([name,marks])
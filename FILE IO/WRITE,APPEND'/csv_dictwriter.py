import csv
name=input("name=")
marks=input("marks=")

with open("students.csv","a") as file:
    writer=csv.DictWriter(file,fieldnames=["name","marks"])
    writer.writerow({"name":name,"marks":marks})
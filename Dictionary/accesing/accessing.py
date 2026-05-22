#Creating a dictionary

student = {"name": "Mani", "age": 20}
# Direct access — raises KeyError if missing
print(student["name"])         # "Mani"
# .get() — returns None if missing (safe)
print(student.get("age"))      # 20
print(student.get("gpa"))      # None
print(student.get("gpa", 0))   # 0  ← default value
# Check if key exists
print("name" in student )      # True
print("gpa" in student)        # False




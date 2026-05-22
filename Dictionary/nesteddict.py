students = {
    "Mani":  {"age": 20, "score": 95},
    "Rahul": {"age": 21, "score": 88},
}

# Access nested value
print(students["Mani"]["score"])   # 95

# Add to nested dict
students["Mani"]["city"] = "Hyderabad"

# Loop over nested
for name, info in students.items():
    print(name, "→", info["score"])
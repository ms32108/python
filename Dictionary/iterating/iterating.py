d = {
    "name": "Mani", 
    "age": 20,
    "city": "Hyderabad"
    }

print(key)
# Loop over keys (default)
for key in d:
    print(key)

# Loop over values
for val in d.values():
    print(val)

# Loop over key-value pairs ← most common
for key, val in d.items():
    print(f"{key}: {val}")

# Output:
# name: Mani
# age: 20
# city: Hyderabad
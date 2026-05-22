d = {"name": "Mani", "age": 20}
print(f"Default-- {d}")


# Add or update a key
d["score"] = 95          # adds new key
d["age"] = 21            # updates existing key
print(f"added score and updated-- {d}")


# Update with another dict
d.update({"city": "Hyderabad", "age": 22})
print(f"updated wth .update() fun --{d}")


# Remove a key
del d["score"]           # raises KeyError if missing
print(f"Deleted with deld['key']-- {d}")


d.pop("city")            # returns the value, safer
d.pop("gpa", None)       # returns None if missing (safe)
print(f"used pop('key')to pop --{d}")


# Remove & return last inserted item
d.popitem()              # → ("age", 22)
print(f"poped last insert item --{d}")


# Clear everything
#d.clear()
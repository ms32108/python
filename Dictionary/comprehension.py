# Basic: {key_expr: val_expr for item in iterable}
squares = {x: x**2 for x in range(1, 6)}
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
print(squares)

# With condition
even_sq = {x: x**2 for x in range(10) if x % 2 == 0}
# {0: 0, 2: 4, 4: 16, 6: 36, 8: 64}
print(even_sq)

# Invert a dict (swap keys and values)
original = {"a": 1, "b": 2, "c": 3}
print(original.items())
inverted = {v: k for k, v in original.items()}
# {1: "a", 2: "b", 3: "c"}
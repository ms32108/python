#two way 1- {},2- using dict() constructor
student = {"name": "Mani", "age": 20, "score": 95}
student = dict(name="Mani", age=20, score=95)

# Empty dict
data = {}
data = dict()

# From list of tuples
pairs = [("a", 1), ("b", 2)]
d = dict(pairs)
print(d) # o/p-- {'a': 1, 'b': 2}
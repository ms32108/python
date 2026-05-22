Common patterns
# Count frequency of items
words = ["hi", "bye", "hi", "hello", "bye", "hi"]
freq = {}
for w in words:
    freq[w] = freq.get(w, 0) + 1
# {"hi": 3, "bye": 2, "hello": 1}

# Group items by a property
people = [("Alice", "Dev"), ("Bob", "HR"), ("Eve", "Dev")]
groups = {}
for name, dept in people:
    groups.setdefault(dept, []).append(name)
# {"Dev": ["Alice", "Eve"], "HR": ["Bob"]}

# Sorting a dict by value
sorted_d = dict(sorted(freq.items(), key=lambda x: x[1], reverse=True))
# {"hi": 3, "bye": 2, "hello": 1}
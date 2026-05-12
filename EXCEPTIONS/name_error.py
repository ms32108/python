try:
    x = int(input("What is x?? ")) # If this fails...
except ValueError:
    print("Error")
50
print(f"x is {x}") # ...x was never created when we type any string in it, causing a NameError.
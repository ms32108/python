try:
    x = int(input("What is x?? "))
except ValueError:
    print("Error enterr  an integer")
else:
    print(f"x is {x}") 
name = input("What's your name? ")

with open("n1.txt", "a") as file:
    file.write(f"{name}\n")

#Automates file.close()
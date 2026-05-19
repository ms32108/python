name = input("Enter name=")
file=open("names(a).txt","a")
#file.write(name)
file.write(f"{name}\n")

file.close()

with open("n1(r).txt", "r") as file:
#lines=file.readlines() #saves as a List is not needed
    for line in file:
        print("hello,",line.rstrip())

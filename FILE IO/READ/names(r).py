
with open("n1(r).txt", "r") as file:
    lines=file.readlines() #saves as a List

for line in lines:
    print("hello,",line.rstrip())


"""
for line in lines:
    print("hello, ",line)

O/P--
hello,  Sai

hello,  ManiSai

hello,  Mani"""
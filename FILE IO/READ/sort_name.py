#add .txt data into a List
#remove extra space/line
#print soredted names saying hell0

names=[]

with open("n1(r).txt") as file:
    for name in file:
        names.append(name.rstrip())


for j in sorted(names):
    print(j)

for j in sorted(names,reverse=True):
    print(j)






"""






names=[]




with open("n1(r).txt") as file:
    for line in file:
        names.append(line.strip())


for i in sorted(names):
    print(f"hello, {i}")"""
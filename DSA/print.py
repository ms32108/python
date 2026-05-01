''''
x=int(input("enter size========"))
print(x)

#x1= list (map(int,input().split()))

#print(x1)

arr = []
for i in range(1, x + 1):
    arr.append(i)
print(arr)

'''


x = int(input("How many numbers do you want to enter? "))
arr =[]
for i in range(x):
    ele=int(input(f"enter {i+1}th element"))
    arr.append(ele)
print(arr)
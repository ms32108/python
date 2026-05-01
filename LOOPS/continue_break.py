"""
while 1:
    n=int(input("n====="))
    if n < 0:
        continue
    else :
        break
for _ in range(n):
    print("meow")

        #or

while 1:
    n=int(input("n====="))
    if n > 0:
        break

for _ in range(n):
    print("meow")

"""
## now with function
def main():
    number = get_num()
    meow(number)

def get_num():
    while 1:
        x=int(input("n====="))
        if x > 0:
            break
    return x

def meow(n):
    for _ in range(n):
        print("meow")



main()
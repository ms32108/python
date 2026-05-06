def main():
    x=num()
    stars(x)

def num():
    n=int(input("Enter the size.......>>"))
    return n

def stars(size):
    for i in range(size):
        print("*" * (i+1),end="")
        print("\n",end="")
    

main()

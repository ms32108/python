def main():
    while 1:
        x=int (input("enter size->"))
        print_squares(x)
        z=int (input("enter width->"))
        row(z)

def print_squares(size):
    for i in range(size):
        #this prints 1 line 
        for j in range(size):
            print("#",end="")
        print() #new line

def row(w):
    # only rows
    print("#" * w)
    

main()
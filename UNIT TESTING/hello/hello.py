def main():
    name=input("What is ur name??")
    print(hello())
    print(hello(name))

def hello(to="World"):
    return f"hello, {to}"

if __name__=="__main__":
    main()
    
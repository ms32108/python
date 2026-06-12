#always take self as first parameter
#Functions inside a class are called methods
class Name:
    def __init__(self, name, age):
        self.name = name
        self.age  = age
    
    def greet(self):                        # method
        print(f"Hi I am {self.name}")
    
    def is_adult(self):                     # method
        if self.age >= 18:
            print("I am an adult")
        else:
            print("I am not an adult")


#Now you can call them on any object:

s1 = Name("John", 20)
s2 = Name("Ali", 15)

s1.greet()      # Hi I am John
s2.greet()      # Hi I am Ali

s1.is_adult()   # I am an adult
s2.is_adult()   # I am not an adult
## WHY use objects?
Imagine you have 3 students:
python# without object - messy!
name1 = "John"
age1  = 20
name2 = "Mary"
age2  = 22
name3 = "Ali"
age3  = 19

With object - clean and bundled:
s1 = Student("John", 20)  # everything about John in ONE place
s2 = Student("Mary", 22)  # everything about Mary in ONE place
s3 = Student("Ali",  19)  # everything about Ali  in ONE place
That's it. Objects just keep related data together.

## HOW self stores data:
When you write:

s1 = Student("John", 20)

Python does this internally:
1. creates empty box 📦 names s1 
2. puts "John" in box → box.name = "John"
3. puts 20 in box    → box.age  = 20
4. gives box to s1

## Why self in __init__(self,name,age)
self is just Python's way of saying "put this inside the box":
pythonself.name = "John"  # put "John" inside the box
self.age  = 20      # put 20 inside the box

## What i understood
 s1 is instance of the class student , instead of creating multiple varibles for diff students for multiple paratmetrs like name , marks , age , we created a box named s1 for 1 student there by we declare 3 varible store in that s1 object


 class is the the code that we write once then reuse  by creating an usable instance of that which is called object here s1 is the object

 if s1 is object the instance o fthe class then John , 20 are
  the data/values you're passing into the box when creating it!



  # what you write:
class Student:
    def __init__(self, name, age):
        self.name = name

# what python does internally:
class Student:
    def __init__(s1, name, age):
        s1.name = name

s1.greet()
Python secretly does → Student.greet(s1)
                                       ↑
                               s1 passed as self
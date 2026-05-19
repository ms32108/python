from hello import hello

def test_hello():
    hello("Sai") == "hello, Sai"

"""
 
def test_hello():
    hello("Sai") == "Hello, Sai"
o/p--
====================== no tests ran in 0.03s =======================
***THE REASON IS hello() fuction just prints "hell0, sai"(printing a side effect of print fun) 

        def hello(to="World"):
            print("Hello,",to) # just printing not returning

    BUT WE NEED IT AS A ENTITY TO COMPARE (==) 

"""
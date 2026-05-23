import re
email = input("Email=================").strip()

print(email)

if re.search(r"^  [^@]+ @ [^@]+ \.edu  $",email,re.X):
    print("valid")
else:
    print("invalid") 
    


#r - helps print literal special symbols like /n ,/t here . * +
#if re.search(".*@.*",email)
#if re.search("..*@..*",email)#same as below
#if re.search(".+@.+",email):
#if re.search(r".+@.+\.edu",email):
#if re.search(r"^.+@.+\.edu$",email): #strict whole string match not partially  
#[]- any character [^]- except these charchers {set of char}
#r.X  or re.VERBOSE helps in readbilty by adding spaces(ingones blacks asliteral characters 
# # eg: 

'''

re.search(r"""
    ^                    # start of string
    [a-zA-Z0-9_.+-]+     # local part (letters, digits, dots, etc.)
    @                    # at symbol
    [a-zA-Z0-9-]+        # domain name
    \.                   # dot
    [a-zA-Z]{2,}         # TLD (at least 2 letters)
    $                    # end of string, email, re.VERBOSE)

    
***The """ is just Python's triple-quoted string — it lets you write a string across multiple lines
 without needing \n or line continuation.

'''
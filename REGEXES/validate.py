print("what is ur email?")
email = input().strip()

"""
if "@" in email and "." in email:
    print("Valid")
else:
    print("invalid")

"""

username,domain =email.split("@")
# two diff boolean exppre not 1 usersame in domain, ". in domain"
#if username and "." in domain:
# empty value of varialble return false if of used

"""if (username) and ("." in domain):
    print ("Valid")
else:
    print("Invalid")"""


## ✅ Just a string
#domain.endswith(".com")

# ✅ Tuple only needed for multiple
#domain.endswith((".com", ".org", ".gmail.com"))

if username and domain.endswith(("gmail.com",".org",".com")):
    print ("Valid")
else:
    print("Invalid")

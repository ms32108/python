import re 
email = input("Email==").strip()

#if re.search(r"^\w+@\w+\.edu$")  \w=a-zA-Z0-9_
#if re.search(r"^[a-zA-Z0-9_]+@[a-zA-Z0-9_]+\.edu$",email):
if re.search(r"^[a-zA-Z0-9_]+@[a-zA-Z0-9_]+\.(com|edu|net|org)$",email):
    print("valid")
else:
    print("invalid")
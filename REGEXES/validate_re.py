import re 
email = input("Email==").strip()

#if re.search(r"^\w+@\w+\.edu$")  \w=a-zA-Z0-9_
#if re.search(r"^[a-zA-Z0-9_]+@[a-zA-Z0-9_]+\.edu$",email):
#if re.search(r"^[a-zA-Z0-9_]+@[a-zA-Z0-9_]+\.(com|edu|net|org)$",email.lower()):
"""if re.search(r"^[a-zA-Z0-9_]+@[a-zA-Z0-9_]+\.(com|edu|net|org)$",email,re.IGNORECASE):
    print("valid")
else:
    print("invalid")
""" 
#(\w+\.)? -- for sub domain  ?- o or 1 repetetion eg = mani@gamial.gmail.com
if re.search(r"^\w+@(\w+\.)?\w+\.edu$",email,re.IGNORECASE):
    print("valid")
else:
    print("invalid")
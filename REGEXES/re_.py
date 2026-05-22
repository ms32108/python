import re
email = input("Email=================").strip()

print(email)
#if re.search(".*@.*",email)
#if re.search(".+@.+",email):
if re.search(r".+@.+\.edu",email):
    print("valid")
else:
    print("invalid")
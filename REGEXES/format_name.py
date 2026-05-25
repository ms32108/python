# our input should be firstname lastname
#if fname, lname - icoorect format 
# we make the incorrect to corect then print hello full name using re

import re
name = input("enter name==").strip()

result=re.search(r"^(.+), (.+)$",name)


#groups()== takes values from ((f),(l)) in re.search()
if result:
    l,f=result.groups()
    name=f"{f} {f}"
    #name = matches.group(2) +" "+ matches.group(1)
print (f"hello,{name}")



"""

result = re.search(r"^\w+@(\w+\.)?\w+\.edu$", "user@university.edu")

print(result)          # <re.result object; span=(0, 19), result='user@university.edu'>
print(result.group())  # user@university.edu


result = re.search(r"^(\w+)@(\w+)\.edu$", "user@university.edu")

result.group(0)  # 'user@university.edu'  → entire result
result.group(1)  # 'user'                 → first  ()
result.group(2)  # 'university'           → second ()
result.groups()  # ('user', 'university') → all () as tuple

"""
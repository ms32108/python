#using re.sub(pattern,repl,string,count=o,flags=0)


import re 
url=input("URL:").strip()

#username=re.sub(r"https://twitter\.com/","",url)
#username=re.sub(r"https?://twitter\.com/","",url)
#username=re.sub(r"https?://(www\.)twitter\.com/","",url)
username=re.sub(r"^(https?://)?(www\.)twitter\.com/","",url)

print(username)








#Basic
"""url=input("URL:").strip()

username=url.replace("http://twitter.com/","")
or
username=url.removeprefix("http://twitter.com/")
print(username)

"""
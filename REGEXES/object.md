
match=re.search(r"^(.+), (.+)$",name)
match variable  has  all below data and funtion stores in it


📦 Match object
 ├── DATA (attributes)
 │    ├── .string  → the original string you searched in
 │    └── .span()  → start and end position
 │
 └── FUNCTIONS (methods)  
      ├── .group()   → gives you the actual matched text
      ├── .groups()  → gives you all () groups as tuple
      └── .start()   → start position
      └── .end()     → end position
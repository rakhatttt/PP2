import re 

def tosnake(a):
    p=re.sub(r"([a-z])([A-Z])",r"\1_\2",a).lower()
    return p

a=input()
f=tosnake(a)
print(f)

import re 

def upp(a):

    x=re.sub(r'(?<!^)([A-Z])', r' \1', a)

    return x
b=input()
find=upp(b)
print(find)
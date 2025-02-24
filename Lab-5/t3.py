import re 

def seq(a):

    pattern = r"\b[a-z]+_[a-z]+\b"
    
    m=re.findall(pattern, a)

    return m

a=input()

find=seq(a)
print(find)
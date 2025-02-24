import re

def uplow(a):
    pattern=r"\b[A-Z][a-z]+\b"

    m=re.findall(pattern, a)

    return m

a=input()

seq=uplow(a)
print(seq)
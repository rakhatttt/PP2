import math

def regpol(n,s):
    p=math.pi
    S=p*(s**2)/4*math.tan(p/n)
    
n,s=float(input()),float(input())
print()

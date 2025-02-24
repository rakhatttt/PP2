import re

def repl(a):

    x=re.sub( "\s" , ":" , a )
    return x

a=input()

f=repl(a)
print(f)
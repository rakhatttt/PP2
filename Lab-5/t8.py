import re 
def upp(a):
    pattern = re.findall("[A-Z][^A-Z]*", a)
    return pattern

a=input()
find=upp(a)
print(find)
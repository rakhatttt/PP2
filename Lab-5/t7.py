import re

s= input()

res = re.sub(r'_([a-z])', lambda x : x.group(1).upper(),s)
print(res)



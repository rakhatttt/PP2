import re

pattern=r"^a.*b$"

testing=input()

if(re.search(pattern,testing)):
    print(testing,True)
else:
    print(testing,False)

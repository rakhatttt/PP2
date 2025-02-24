import re

pattern = r'^ab*$'

testing=input()

if(re.search(pattern,testing)):
    print(testing,True)
else:
    print(testing,False)

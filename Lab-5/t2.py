import re
pattern=r"^ab{2}$"

testing=input()

if(re.search(pattern,testing)):
    print(True)
else:
    print(False)
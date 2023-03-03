import re

regxObj = re.compile(r'\d\d\d')
mo = regxObj.search("This is a 3 digit number for this exercise: 232")
num = mo.group()

print(num)


regxObj2 = re.compile(r'^[\w\s]+\d\d$')
mo2 = regxObj2.search("Validate number of digit is equal to 34")
result = mo2.group()

print(result)
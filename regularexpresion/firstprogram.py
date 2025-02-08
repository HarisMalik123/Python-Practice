import re
string = "abc"
pattern = "ac"
##from right starting
print(re.match(pattern=pattern, string=string))

str1="bca"
pat1="a"
##now it will not match for entire string we use search
if re.search(pat1,str1):
    print("FOund")
else:
    print("Not FOund ")
#special set of character which do not match themselves instead they create some pattern which should be matched
#*,+ like this
import re
## "*" maje sure that a particular character 
##preceding it present 0 or more time in a string
## "+ means one time"
string ="abbbbbbbbbbc"
patern=r"ab*c"
print(re.match(pattern=patern, string=string))
string ="abbbbbbbbbb"
patern=r"ab*c"
## will print not found
print(re.match(pattern=patern, string=string))
string ="abbbbbbaaaaaabbbbbbbbbc"
patern=r"ab*c"
## will print not found because there should not be a in between
print(re.match(pattern=patern, string=string))
string ="bbbbbbbbbbbbbbc"
patern=r"ab*c"
## will print not found because there should be a in starting
print(re.match(pattern=patern, string=string))
##"{}" A Curly Braces tell the computer to repeat the preceding as many number of times as value inside the bracket
patern=r"ab{2}"
string="abb"
##found
string="ab"
##not found
#"." it states that the . symbol can take place of any other symbol
patern=r"a.b" # means that we can place any charater between a and b just one char
#"? " it may or may not be present character preceding it
patern=r"a-?b"
string="ab"
print(re.match(pattern=patern, string=string))
##"^"means string starting from this patern for example 
patern=r"92"
string="923108423618"
print(re.match(pattern=patern, string=string))
#character classs
string="Python"
patern=r"[pP]ython"
print(re.match(pattern=patern, string=string))
string="python"
patern=r"[a-z]"
print(re.match(pattern=patern, string=string))
string="ABCD"
patern=r"[A-Z]"
print(re.match(pattern=patern, string=string))
string="ABCDa"
patern=r"[A-Za-z]"
print(re.match(pattern=patern, string=string))

string="123"
patern=r"[0-9]"
print(re.match(pattern=patern, string=string))




import re

text_to_search = ''''
abcdefghijklmnopqrstuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890

Ha HaHa

MetaCharacters (Need to be escaped):
. ^ $ * + ? { } [ ] \ | ( )

coreyms.com

321-555-4321
123.555.1234
125*554*1255
800-555-4321
900.555.1234


Mr. Schafer
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T

cat
mat
bat
'''
sentence = 'Start a sentence and then bring it to an end'

#pattern = re.compile(r'abc')
#pattern = re.compile(r'.') any character except the newline

#pattern = re.compile(r'coreyms\.com')
#pattern = re.compile(r'\d') # match for digit 0 to 9
# pattern = re.compile(r'\D') # for not a digit 0 to 9
# pattern = re.compile(r'\w') # for a-z , A-Z, 0-9, _)
# pattern = re.compile(r'\W') # for not a word character
# pattern = re. compile(r'\s') # for whitespace(space, tab, newline)
# pattern = re. compile(r'\S') # for not whitespace(space, tab, newline)
# pattern = re.compile(r'\bHa') # for word boundary
# pattern = re.compile(r'\BHa') # for word boundary
#pattern = re.compile(r'\B') # for not a word boundary
#pattern = re.compile(r'^Start') # for beginning of a string
# pattern = re.compile(r'end$') # for end of a string
# pattern = re.compile(r'end$') # for end of a string


## to match phone number
#pattern = re.compile(r'\d\d\d.\d\d\d.\d\d\d\d')

# to match only those character those we wants
# pattern = re.compile(r'\d\d\d[-.]\d\d\d[-.]\d\d\d\d')
#
# # to match fisrt number or any other number
# pattern = re.compile(r'[89]\d\d[-.]\d\d\d[-.]\d\d\d\d')

# to match between a char to other char  in all text
#pattern = re.compile(r'[1-9]')
# to match a word
#pattern = re.compile(r'[^b]at')

# quantifiers:
# * = 0 or more
# + = 1 or more
# ? = 0 or one
# {3} = exact number
# {3,4} = range of numbers(minimum, maximum)


#### using quantifiers
# pattern = re.compile(r'\d{3}.\d{3}.\d{4}')
# pattern = re.compile(r'Mr\.?\s[A-Za-z]\w*')
#pattern = re.compile(r'M(r|s|rs)\.?\s[A-Za-z]\w*')


# using flag***********
pattern = re.compile(r'start',re.I)

matches = pattern.finditer(sentence)

for match in matches:
    print(match)

# with open('data.txt','r',encoding = 'utf-8') as f:
#     contents = f.read()
#
#     matches = pattern.finditer(contents)
#     for match in matches:
#         print(match)
#print(text_to_search[2 :5])
#print(text_to_search[143:154])

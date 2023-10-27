########## to match emails #############333
import re
email = '''
CoreyMSchafer@gmail.com
corey.schafer@university.edu
corey-321-schafer@my-work.net
'''

pattern = re.compile(r'[a-zA-Z0-9.-]+@[a-zA-Z-]+\.(com|edu|net)')
pattern = re.compile(r'[a-zA-Z0-9.-]+@[a-zA-Z-]+\.[a-zA-Z0-9-.]+')

matches = pattern.finditer(email)

for match in matches:
    print(match)
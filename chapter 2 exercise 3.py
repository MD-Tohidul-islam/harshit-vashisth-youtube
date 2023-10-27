name,char = input('enter your name: ,character with comma separated ').split(',')
print(f'length of your name is {len(name)}')
print(f'character count: {name.count(char)}')
print(',,,,,,,,,,,')
print(f'character count: {name.lower().count(char)}')
print(',,,,,,,,,,,')
name1=name.lower()
print(f'character count: {name1.count(char)}')


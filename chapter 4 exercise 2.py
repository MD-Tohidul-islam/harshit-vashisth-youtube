word = input('enter a word: ')
if word == word[::-1]:
    print(word, 'is palindrome !!')
else:
    print(word, 'is not palindrome')
def is_palindrome(words):
    reversed_word = words[::-1]
    if words == words[::-1]:
        return words, 'is palindrome !!'
    else:
        return words, 'is not palindrome'

print(is_palindrome(word))
def reverse_word(l):
    re_word = []
    for i in range(len(l)):
        re_word.append(l[i][::-1])
    return re_word


v = ['abc','def','ghi','jkl']
print(reverse_word(v))
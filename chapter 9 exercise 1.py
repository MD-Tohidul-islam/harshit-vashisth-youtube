def re_string(n):
    v = [n[i][::-1] for i in range(len(n))]
    return v

c =['abc','def','ghi']
print(re_string(c))
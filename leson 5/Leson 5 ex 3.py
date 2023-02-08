import random

a = input("Print the word :")
i = 0
b = ''
c = ''
d = ''
e = ''
f = ''
if len(a) < 5:
    print("it`s to short")
else:
    while i != len(a):
        b = b + random.choice(a)
        c = c + random.choice(a)
        d = d + random.choice(a)
        e = e + random.choice(a)
        f = f + random.choice(a)
        i += 1
    print('"' + b, c, d, e, f, sep='"\n"', end='"')

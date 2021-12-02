l = ['a', 25, 'hola', True]

i = 0
while i < len(l):
    print(i, l[i])
    i += 1

for i, e in enumerate(l, 9):
    print(i, e)

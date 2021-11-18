def rectangulo(n):
    i = 0
    while i < n:
        print('*****')
        i += 1

def rectangulo2(n):
    print('*****\n' * n, end='')

def rectangulo3(n):
    if n > 0:
        print('*****')
        rectangulo3(n - 1)

def diagonal(n):
    i = 1
    while i <= n:
        print((' ' * i) + '*')
        i += 1

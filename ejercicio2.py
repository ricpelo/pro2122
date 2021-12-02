def rectangulo(n):
    for i in range(n):
        print('*****')

def rectangulo2(n):
    print('*****\n' * n, end='')

def rectangulo3(n):
    if n > 0:
        print('*****')
        rectangulo3(n - 1)

def diagonal(n):
    for i in range(1, n + 1):
        print((' ' * i) + '*')


def arbol(n):
    def ancho(n):
        return 2 * n - 1

    if n > 0:
        an = ancho(n)
        for i in range(1, n):
            a = '*' * ancho(i)
            print(a.center(an))
        print('*'.center(an))

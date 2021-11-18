# suma = lambda n: n + suma(n - 1) if n > 0 else 0

# Versión que genera un proceso recursivo lineal
fact_rec = lambda n: n * fact_rec(n - 1) if n > 0 else 1

# Versión que genera un proceso iterativo lineal
fact = lambda n: fact_iter(n, 1)
fact_iter = lambda n, acc: acc if n == 0 else \
                           fact_iter(n - 1, acc * n)

# Versión que genera un proceso recursivo en árbol
fib_rec = lambda n: 0 if n == 0 else \
                1 if n == 1 else \
                fib_rec(n - 1) + fib_rec(n - 2)

# Versión que genera un proceso iterativo lineal
fib = lambda n: fib_iter(n, 0, 1)
fib_iter = lambda n, a, b: a if n == 0 else \
                           fib_iter(n - 1, b, a + b)

longitud = lambda c: 0 if c == '' else 1 + longitud(c[1:])

long_tupla = lambda c: 0 if c == () else 1 + long_tupla(c[1:])

suma_tupla = lambda t: 0 if t == () else t[0] + suma_tupla(t[1:])

sum_tup = lambda t: suma_tupla_iter(t, 0)
suma_tupla_iter = lambda t, acc: acc if t == () else \
                                 suma_tupla_iter(t[1:], acc + t[0])

filtra_mayus = \
    lambda c: '' if c == '' else \
              quita_si_mayus(c[0]) + filtra_mayus(c[1:])

quita_si_mayus = lambda c: '' if c.isupper() else c

"""
filtra_mayus = \
    lambda c: '' if c == '' else \
              filtra_mayus(c[1:]) if c[0].isupper() else \
              c[0] + filtra_mayus(c[1:])
"""

suma = lambda f, a, b: 0 if a > b else f(a) + suma(f, a + 1, b)

from math import sqrt

suma_enteros = lambda a, b: suma(lambda n: n, a, b)
suma_cubos = lambda a, b: suma(lambda n: n ** 3, a, b)
suma_raices = lambda a, b: suma(sqrt, a, b)

mcd = lambda a, b: b if a % b == 0 else mcd(b, a % b)

eleva_cuadrado = \
    lambda t: () if t == () else \
              (t[0] ** 2,) + eleva_cuadrado(t[1:])

eleva_cuarta = \
    lambda t: () if t == () else \
              (t[0] ** 4,) + eleva_cuarta(t[1:])

aplicar_raiz = \
    lambda t: () if t == () else \
              (sqrt(t[0]),) + aplicar_raiz(t[1:])

aplicar = \
    lambda f, t: () if t == () else \
                 (f(t[0]),) + aplicar(f, t[1:])

from functools import reduce

factorial = \
    lambda n: reduce(lambda acc, x: acc * x, range(1, n + 1), 1)

# invertir = lambda t: () if t == () else invertir(t[1:]) + (t[0],)

inv_iter = lambda t, acc: acc if t == () else \
                          inv_iter(t[1:], (t[0],) + acc)
invertir = lambda t: inv_iter(t, ())

inv_reduce = \
    lambda t: reduce(lambda acc, x: (x,) + acc, t, ())

hanoi = \
    lambda a, b, c, n: '' if n == 0 else \
        hanoi(a, c, b, n - 1) + \
        '  --  Mover 1 disco del ' + a + ' al ' + c + \
        hanoi(b, a, c, n - 1)

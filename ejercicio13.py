def es_primo(n):
    def divisores(n):
        def es_divisor_de(a, b):
            return b % a == 0

        num_div = 0
        i = 1
        while i <= n:
            if es_divisor_de(i, n):
                num_div += 1
            i += 1
        return num_div
    return divisores(n) == 2


while True:
    try:
        n = int(input('Introduzca un número entero positivo: '))
        if n <= 0:
            print('El número debe ser mayor que cero.')
        else:
            break
    except ValueError:
        print('El número introducido no es correcto.')

def primos(n):
    def primos_iter(i):
        nonlocal cuantos
        if cuantos == n:
            return acc
        if es_primo(i):
            cuantos += 1
            acc.append(i)
        return primos_iter(i + 1)

    cuantos = 0
    acc = []

    return primos_iter(1)

print(primos(n))

"""i = 1
primos = 0
while i < n:
    if es_primo(i):
        primos += 1
        print(i, end=' ')
    i += 1
"""

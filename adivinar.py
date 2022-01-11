"""
Adivinar un número.
"""

import random

numero_a_adivinar = random.randint(1, 100)

while True:
    try:
        numero = int(input('Introduzca su número: '))
        if numero == numero_a_adivinar:
            print('¡Acertó!')
            break
        if numero < numero_a_adivinar:
            print('Ese número demasiado pequeño')
        else:
            print('Ese número es demasiado grande')
    except ValueError:
        print('Debe introducir un número válido')

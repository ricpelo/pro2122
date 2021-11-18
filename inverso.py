while True:
    try:
        num = int(input('Introduce el número: '))
        res = 1 / num
        break
    except ValueError:
        print('Número incorrecto introducido.')
    except ZeroDivisionError:
        print('No se puede dividir entre cero.')

print('El inverso de', num, 'es', res)

def factura():
    """Ejercicio 3"""

    with open('factura.txt') as f:
        lineas = [x.rstrip() for x in f.readlines()]

    resultado = [
        lineas[0] + ' Importe\n',
        lineas[1] + ' -------\n'
    ]

    total = 0

    for linea in lineas[2:]:
        linea = linea.split()
        uds = int(linea[0])
        desc = linea[1]
        pun = float(linea[2])
        imp = uds * pun
        total += imp
        resultado.append(f'{uds:2} {desc:15} {pun:6.2f} {imp:7.2f}\n')

    resultado.append('---------------------------------\n')
    resultado.append(f'TOTAL:             {total:14.2f}\n')

    with open('resultado.txt', 'w') as f:
        f.writelines(resultado)

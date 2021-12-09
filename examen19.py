"""
Examen tirao.
"""

def sobre(m, n):
    """
    Calcula m sobre n.

    >>> sobre(3, 1)
    3
    >>> sobre(4, 2)
    6
    """
    if m == 0 and n > 0:
        return 0
    if m >= 0 and n == 0:
        return 1
    return sobre(m - 1, n - 1) + sobre(m - 1, n)

def lista_sobre_A(ultima_fila):
    """
    >>> lista_sobre_A(2)
    [[1], [1, 1], [1, 2, 1]]
    >>> lista_sobre_A(3)
    [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1]]
    >>> lista_sobre_A(4)
    [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
    """
    if ultima_fila == 0:
        return [[1]]
    triangulo = lista_sobre_A(ultima_fila - 1)
    ultima = triangulo[-1]
    copia = ultima
    ultima = [0] + ultima
    copia = copia + [0]
    nueva = list(map(lambda x, y: x + y, ultima, copia))
    triangulo.append(nueva)
    return triangulo

def triangulo_A(numero_filas):
    triangulo = lista_sobre_A(numero_filas - 1)
    for fila in triangulo:
        res = ''
        for e in fila:
            res += f'{e:6}'
        print(res.center(50).rstrip())

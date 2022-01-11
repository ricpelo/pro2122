"""
Ejercicio del tema 7.
"""

def pasa_pasa(l):
    """
    Pasa el último dígito del primer número al final del segundo.
    Modifica su argumento.

    Args:
        l (list): La lista con los dos números

    >>> lista = [12345, 0]
    >>> pasa_pasa(lista)
    >>> lista
    [1234, 5]
    >>> pasa_pasa(lista)
    >>> lista
    [123, 54]
    """
    l[1] = l[1] * 10 + (l[0] % 10)
    l[0] = l[0] // 10    # l[0] //= 10

def invierte(l):
    """
    Invierte el primer número de la lista sobre el segundo.

    Args:
        l (list): La lista con los dos números.

    >>> numeros = [1234, 5]
    >>> invierte(numeros)
    [1234, 5]
    [123, 54]
    [12, 543]
    [1, 5432]
    [0, 54321]
    >>> numeros
    [0, 54321]
    """
    print(l)
    while l[0] != 0:
        pasa_pasa(l)
        print(l)

numeros = [1234, 5]
pasa_pasa(numeros)
print(numeros)
numeros = [12345, 0]
invierte(numeros)
print(numeros)

"""
Ejercicios de rectángulos
"""

def rectangulo(n):
    """Escribe un rectángulo de * con el número de líneas indicado"""
    for _ in range(n):
        print('*****')

def rectangulo2(n):
    """[summary]

    Args:
        n ([type]): [description]
    """
    print('*****\n' * n, end='')

def rectangulo3(n):
    """Dibuja un rectángulo.

    Dibuja un rectángulo con asteriscos.

    Args:
        n (int): La altura del rectángulo

    """
    if n > 0:
        print('*****')
        rectangulo3(n - 1)

def diagonal(n):
    """[summary]

    Args:
        n ([type]): [description]
    """
    for i in range(1, n + 1):
        print((' ' * i) + '*')


def arbol(n):
    """Dibuja un árbol de navidad con la altura indicada"""
    def ancho(n):
        """Calcula el ancho del árbol según su altura.

        Args:
            n (int): La altura del árbol.

        Returns:
            int: El ancho del árbol.
        """
        return 2 * n - 1

    if n > 0:
        an = ancho(n)
        for i in range(1, n):
            a = '*' * ancho(i)
            print(a.center(an))
        print('*'.center(an))

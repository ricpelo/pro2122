"""
El módulo que analiza la entrada del jugador.
"""

import vocabulario as v

verbo = None
nombre = None

def analizar(entrada: str) -> bool:
    """
    Analiza la entrada del jugador.

    Una entrada válida es aquella que satisface la siguiente
    gramática:

    <entrada> ::= [ VERBO [ NOMBRE ] ]

    Modifica las variables 'verbo' y 'nombre' si y sólo si la
    entrada es válida. En caso contrario, le asigna a ambas el
    valor None.

    Args:
        entrada (str): La entrada del jugador.

    Returns:
        bool: True si se ha encontrado una entrada válida.
              False en caso contrario.
    """
    global verbo
    global nombre

    lexemas = entrada.upper().split()
    verbo, nombre = None, None

    if len(lexemas) == 0:
        return True

    try:
        palabra = v.VOCABULARIO[lexemas[0]]
        if palabra[v.TIPO] == v.TIPO_VERBO:
            verbo = palabra[v.TOKEN]
            if len(lexemas) == 1:
                return True

            if len(lexemas) == 2:
                palabra = v.VOCABULARIO[lexemas[1]]
                if palabra[v.TIPO] == v.TIPO_NOMBRE:
                    nombre = palabra[v.TOKEN]
                    return True
                else:
                    verbo, nombre = None, None
                    return False
            else:
                verbo, nombre = None, None
                return False
        else:
            return False
    except KeyError:
        verbo, nombre = None, None
        return False

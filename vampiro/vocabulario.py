"""
El vocabulario del juego.
"""

class Tipo:
    pass

TIPO_VERBO = Tipo()
TIPO_NOMBRE = Tipo()

class Palabra:
    # tipo
    # token ?
    # lexemas
    def __init__(self, tipo, lexemas):
        self.__tipo = tipo
        self.__lexemas = lexemas

    def tipo(self):
        return self.__tipo

    def lexemas(self):
        return self.__lexemas[:]

COGER = Palabra(TIPO_VERBO, ['COGER', 'TOMAR'])
CUCHILLO = Palabra(TIPO_NOMBRE, ['CUCHILLO', 'NAVAJA'])

class Vocabulario:
    # palabras
    def __init__(self):
        self.__palabras = {}

    def meter_palabra(self, palabra):
        for lexema in palabra.lexemas():
            self.__palabras[lexema] = palabra

    def meter_palabras(self, palabras):
        for palabra in palabras:
            self.meter_palabra(palabra)

    def buscar_palabra(self, lexema):
        return self.__palabras[lexema]

vocabulario = Vocabulario()
vocabulario.meter_palabras([COGER, CUCHILLO])


# # Vocabulario:
# _VOCABULARIO = {
#     COGER: (TIPO_VERBO, ['COGER', 'TOMAR']),
#     NORTE: (TIPO_VERBO, ['NORTE', 'N']),
#     SUR: (TIPO_VERBO, ['SUR', 'S']),
#     ESTE: (TIPO_VERBO, ['ESTE', 'E']),
#     OESTE: (TIPO_VERBO, ['OESTE', 'O']),
#     FIN: (TIPO_VERBO, ['FIN', 'ACABAR', 'TERMINAR', 'FINALIZAR']),
#     CUCHILLO: (TIPO_NOMBRE, ['CUCHILLO', 'NAVAJA']),
#     MIRAR: (TIPO_VERBO, ['MIRAR', 'M', 'L'])
# }

# _vocabulario = {}

# def crear_vocabulario():
#     global _vocabulario

#     for token, tupla in _VOCABULARIO.items():
#         tipo, lexemas = tupla
#         palabra = { TOKEN: token, TIPO: tipo }
#         for lexema in lexemas:
#             _vocabulario[lexema] = palabra

# def buscar(lexema):
#     """
#     Busca una palabra en el diccionario a partir de un lexema.

#     Args:
#         lexema (str): El lexema de la palabra a buscar.

#     Returns:
#         La palabra.

#     Raises:
#         KeyError: Si en el diccionario no hay ninguna palabra
#                   con ese lexema.
#     """
#     return _vocabulario[lexema]

# def tipo(palabra):
#     """
#     Devuelve el tipo de la palabra recibida como argumento.

#     Precondición:
#         La palabra recibida debe ser una palabra válida y
#         correctamente formada. Eso significa que:

#         - No puede ser None.
#         - Debe contener un Tipo y un Token.

#     Args:
#         palabra: La palabra.

#     Returns:
#         El tipo de la palabra.
#     """
#     return palabra[TIPO]

# def token(palabra):
#     """
#     Devuelve el token de la palabra recibida como argumento.

#     Precondición:
#         La palabra recibida debe ser una palabra válida y
#         correctamente formada. Eso significa que:

#         - No puede ser None.
#         - Debe contener un Tipo y un Token.

#     Args:
#         palabra: La palabra.

#     Returns:
#         El token de la palabra.
#     """
#     return palabra[TOKEN]

# crear_vocabulario()

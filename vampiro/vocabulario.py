"""
El vocabulario del juego.
"""

class Tipo:
    def __init__(self, tipo):
        self.__tipo = tipo

    def __eq__(self, otro):
        if not isinstance(otro, type(self)):
            return NotImplemented
        return self.__tipo == otro.__tipo

    def __hash__(self):
        return hash(self.__tipo)

    def __repr__(self):
        return f'Tipo({self.__tipo!r})'

TIPO_VERBO = Tipo('VERBO')
TIPO_NOMBRE = Tipo('NOMBRE')

class Palabra:
    __palabras = []

    # @staticmethod
    # def buscar(lexema):
    #     for palabra in Palabra.__palabras:
    #         if lexema in palabra.lexemas():
    #             return palabra
    #     return None

    @staticmethod
    def palabras():
        return Palabra.__palabras[:]

    def __init__(self, tipo, lexemas):
        self.__tipo = tipo
        self.__lexemas = frozenset(lexemas)
        if self in Palabra.__palabras:
            raise ValueError('Esa palabra ya existe.')
        Palabra.__palabras.append(self)

    def __eq__(self, otro):
        """
        Dos palabras son iguales si tienen, al menos, un
        lexema en común.
        """
        if not isinstance(otro, type(self)):
            return NotImplemented
        return self.lexemas() & otro.lexemas() != frozenset()

    def __repr__(self):
        return f'Palabra({self.tipo()!r}, {self.lexemas()!r})'

    def tipo(self):
        return self.__tipo

    def lexemas(self):
        return self.__lexemas

class Vocabulario:
    def __init__(self):
        self.__palabras = {}

    def meter_palabra(self, palabra):
        for lexema in palabra.lexemas():
            self.__palabras[lexema] = palabra

    def meter_palabras(self, palabras):
        for palabra in palabras:
            self.meter_palabra(palabra)

    def buscar_palabra(self, lexema):
        return self.__palabras.get(lexema)

    def palabras(self):
        return self.__palabras.copy()

COGER    = Palabra(TIPO_VERBO, ['COGER', 'TOMAR'])
CUCHILLO = Palabra(TIPO_NOMBRE, ['CUCHILLO', 'NAVAJA'])
NORTE    = Palabra(TIPO_VERBO, ['NORTE', 'N'])
SUR      = Palabra(TIPO_VERBO, ['SUR', 'S'])
ESTE     = Palabra(TIPO_VERBO, ['ESTE', 'E'])
OESTE    = Palabra(TIPO_VERBO, ['OESTE', 'O'])
FIN      = Palabra(TIPO_VERBO, ['FIN', 'ACABAR', 'TERMINAR', 'FINALIZAR'])
MIRAR    = Palabra(TIPO_VERBO, ['MIRAR', 'M', 'L'])

vocabulario = Vocabulario()
vocabulario.meter_palabras(Palabra.palabras())

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

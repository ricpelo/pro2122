class Cliente:
    def __init__(self, dni, nombre, apellidos, telefono):
        self.__set_dni(dni)
        self.set_nombre(nombre)
        self.set_apellidos(apellidos)
        self.set_telefono(telefono)

    def __eq__(self, otro):
        if not isinstance(otro, type(self)):
            return NotImplemented

        return self.dni() == otro.dni()

    def __hash__(self):
        return hash(self.dni())

    def __repr__(self):
        d = self.dni()
        n = self.nombre()
        a = self.apellidos()
        t = self.telefono()
        return f'Cliente({d!r},{n!r},{a!r},{t!r})'

    def dni(self):
        return self.__dni

    def __set_dni(self, dni):
        self.__dni = dni

    def nombre(self):
        return self.__nombre

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def apellidos(self):
        return self.__apellidos

    def set_apellidos(self, apellidos):
        self.__apellidos = apellidos

    def telefono(self):
        return self.__telefono

    def set_telefono(self, telefono):
        if len(str(telefono)) != 9:
            raise ValueError('El teléfono debe tener 9 dígitos.')
        self.__telefono = telefono

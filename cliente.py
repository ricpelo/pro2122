class Cliente:
    def __init__(self, dni, nombre, apellidos, telefono):
        self._dni = dni
        self._nombre = nombre
        self._apellidos = apellidos
        self._telefono = telefono

    def __eq__(self, otro):
        if type(self) != type(otro):
            return NotImplemented

        return self.dni() == otro.dni()

    def __hash__(self):
        return hash(self.dni())

    def __repr__(self):
        d = self._dni
        n = self._nombre
        a = self._apellidos
        t = self._telefono
        return f'Cliente({d!r},{n!r},{a!r},{t!r})'

    def dni(self):
        return self._dni

    def nombre(self):
        return self._nombre

    def apellidos(self):
        return self._apellidos

    def telefono(self):
        return self._telefono

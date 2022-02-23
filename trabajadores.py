class Trabajador:
    """Trabajador es la superclase"""
    def set_nombre(self, nombre):
        self.__nombre = nombre

    def get_nombre(self):
        return self.__nombre

class Docente(Trabajador):
    """Docente es subclase de Trabajador"""
    def set_nrp(self, nrp):
        self.__nrp = nrp

    def get_nrp(self):
        return self.__nrp

class Investigador(Docente):
    """Investigador es subclase directa de Docente"""
    def set_proyecto(self, proyecto):
        self.__proyecto = proyecto

    def get_proyecto(self):
        return self.__proyecto

class Fecha:
    def __init__(self, dia, mes, anyo):
        self.set_dia(dia)
        self.set_mes(mes)
        self.set_anyo(anyo)

    def set_dia(self, dia):
        self.__dia = dia

    def get_dia(self):
        return self.__dia

    def set_mes(self, mes):
        self.__mes = mes

    def get_mes(self):
        return self.__mes

    def set_anyo(self, anyo):
        self.__anyo = anyo

    def get_anyo(self):
        return self.__anyo

    def comprobar(self):
        return self.get_dia() in range(1, 32) and \
            self.get_mes() in range(1, 13) and \
            self.get_anyo() in range(1000, 10000)


class Timestamp(Fecha):
    def __init__(self, dia, mes, anyo, horas, minutos, segundos):
        super().__init__(dia, mes, anyo)
        self.set_horas(horas)
        self.set_minutos(minutos)
        self.set_segundos(segundos)

    def set_horas(self, horas):
        self.__horas = horas

    def get_horas(self):
        return self.__horas

    def set_minutos(self, minutos):
        self.__minutos = minutos

    def get_minutos(self):
        return self.__minutos

    def set_segundos(self, segundos):
        self.__segundos = segundos

    def get_segundos(self):
        return self.__segundos

    def comprobar(self):
        return super().comprobar() and \
            self.get_horas() in range(0, 25) and \
            self.get_minutos() in range(0, 60) and \
            self.get_segundos() in range(0, 60)

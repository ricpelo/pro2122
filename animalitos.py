class Animal:
    def __init__(self, nombre):
        self.set_nombre(nombre)

    def get_nombre(self):
        return self.__nombre

    def set_nombre(self, nombre):
        self.__nombre = nombre

class Terrestre(Animal):
    def get_patas(self):
        return self.__patas

    def set_patas(self, patas):
        self.__patas = patas

    def caminar(self):
        print('Caminando voy...')

class Acuatico(Animal):
    def get_aletas(self):
        return self.__aletas

    def set_aletas(self, aletas):
        self.__aletas = aletas

    def nadar(self):
        print('Glu glu glu...')

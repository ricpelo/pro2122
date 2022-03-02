from coleccion import Coleccion
from lector import Lector
from fondos import Libro
from prestamos import Prestamo

lectores = Coleccion()
fondos = Coleccion()
numero_pepe = lectores.insertar(Lector('Pepe'))
numero_historia = fondos.insertar(Libro('X74H', 'La historia interminable', 'Michael Ende', 574))
prestamos = Coleccion()
pepe_historia = Prestamo(
    lectores.buscar(numero_pepe),
    fondos.buscar(numero_historia)
)
prestamos.insertar(pepe_historia)

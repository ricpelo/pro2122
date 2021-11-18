ARCHIVO = 'archivo.txt'

def anyadir():
    cadena = input('Introduzca la cadena a añadir al archivo: ')
    with open(ARCHIVO, 'a') as f:
        print(cadena, file=f)


def cambiar():
    def pedir_numero():
        while True:
            try:
                num_linea = int(input('Introduzca el número de línea a cambiar: '))
                if num_linea >= 1:
                    break
                print('El número de línea debe ser, al menos, 1.')
            except ValueError:
                print('Debe introducir un número')
        return num_linea

    num_linea = pedir_numero()
    with open(ARCHIVO, 'r+') as f:
        i = 1
        pos = 0
        linea = ''
        while i <= num_linea:
            pos = f.tell()
            linea = f.readline()
            if linea == '':
                print('ERROR: No hay tantas líneas')
                break
            linea = linea[:-1]
            i += 1
        f.seek(pos)
        long = len(linea)
        if linea == '':
            print('No se puede cambiar una línea vacía.')
        else:
            while True:
                print('Debe introducir una cadena con', long, 'caracteres.')
                cadena = input('Introduzca la nueva cadena: ')
                if len(cadena) == long:
                    print(cadena, file=f)
                    break


def mostrar():
    with open(ARCHIVO, 'r') as f:
        while True:
            cadena = f.readline().rstrip()
            if cadena == '':
                break
            print(cadena)


while True:
    print("""
    1. Añadir un elemento a un archivo.
    2. Cambiar el valor de un elemento de un archivo.
    3. Eliminar un elemento de un archivo.
    4. Eliminar todos los elementos de un archivo.
    5. Mostrar los elementos de un archivo.
    0. Salir del programa.
    """)

    opcion = input('Introduzca una opción: ')

    if opcion == '1':
        anyadir()
    elif opcion == '2':
        cambiar()
    elif opcion == '3':
        eliminar_uno()
    elif opcion == '4':
        eliminar_todos()
    elif opcion == '5':
        mostrar()
    elif opcion == '0':
        break
    else:
        print('Opción incorrecta')

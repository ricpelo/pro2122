"""
Ejercicios de facturas almacenadas en XML.
"""

import xml.etree.ElementTree as ET
import re

ARCHIVO_XML = 'facturas.xml'

def imprimir_factura(factura: ET.Element):
    """Imprime una factura por la salida.

    Args:
        factura (ET.Element): El nodo que representa la factura.
    """
    print()
    print('Número de factura: ', end='')
    print(factura.get('numero'))
    print('Datos del cliente:')
    dni = factura.find('cliente/dni').text
    nombre = factura.find('cliente/nombre').text
    total = 0.0
    print(f'DNI: {dni} - {nombre}')
    print()
    print('Núm. Denominación         Cantidad Precio    Importe')
    print('----------------------------------------------------')
    for articulo in factura.findall('articulo'):
        numero = articulo.get('numero')
        denominacion = articulo.find('denominacion').text
        cantidad = float(articulo.find('cantidad').text)
        precio = float(articulo.find('precio').text)
        importe = cantidad * precio
        total += importe
        print(f'{numero} {denominacion:20} {cantidad:8} {precio:6} € {importe:6} €')
    print('----------------------------------------------------')
    print(f'TOTAL:                                      {total:6} €')
    print()


def imprimir_facturas(facturas):
    """Imprime todas las facturas que cuelgan de su argumento.

    Args:
        facturas (ET.Element): El nodo del que cuelgan todas las facturas.
    """
    for factura in facturas.findall('factura'):
        imprimir_factura(factura)


def dni_valido(dni):
    regex = re.compile(r'^\d{8}[A-Z]$')
    return regex.search(dni) is not None

def validar_dnis(raiz):
    for dni in raiz.iter('dni'):
        nif = dni.text
        print(f'{nif}: ', end='')
        if dni_valido(nif):
            print('CORRECTO')
        else:
            print('¡¡¡INCORRECTO!!!')

def cambiar_dni_segun_numero(raiz):
    numero = input('Introduzca el número del cliente: ')
    nuevo_dni = input('Introduzca el nuevo DNI del cliente: ')
    for dni in raiz.findall(f'.//cliente[@numero="{numero}"]/dni'):
        print(f'Encontrado cliente con DNI {dni.text}')
        dni.text = nuevo_dni


def guardar_archivo(arbol):
    arbol.write(ARCHIVO_XML)


arbol = ET.parse(ARCHIVO_XML)
raiz = arbol.getroot()

while True:
    print()
    print('MENÚ PRINCIPAL')
    print('--------------')
    print()
    print('1. Mostrar todas las facturas.')
    print('2. Validar DNIs de los clientes.')
    print('3. Cambiar el DNI de un cliente dado su número.')
    print('4. Cambiar el DNI de un cliente dado un número de factura.')
    print('9. Guardar los datos en el disco.')
    print('0. Salir.')
    print()
    opcion = input('Seleccione la opción: ')
    print()
    if opcion == '1':
        imprimir_facturas(raiz)
    elif opcion == '2':
        validar_dnis(raiz)
    elif opcion == '3':
        cambiar_dni_segun_numero(raiz)
    elif opcion == '9':
        guardar_archivo(arbol)
    elif opcion == '0':
        break
    else:
        print('Opción incorrecta')
        print()

def adn_a_arn(adn):
    """Ejercicio 1"""
    codigo = {'A': 'U', 'G': 'C', 'C': 'G', 'T': 'A'}
    return ''.join(codigo[x] for x in adn)

def sumas():
    """Ejercicio 2"""
    with open('entrada.txt') as f:
        entrada = [int(x.split()[0]) for x in f.readlines()]
    res = []
    suma = 0
    for e in entrada:
        suma += e
        res.append(f'{e:4} {suma:9}\n')
    res.append('-' * 14 + '\n')
    res.append(f'SUMA: {suma:8}\n')
    with open('salida.txt', 'w') as f:
        f.writelines(res)

import xml.etree.ElementTree as ET

def agrupar(arbol):
    """Ejercicio 3"""
    raiz = arbol.getroot()
    alumnos = raiz.find('alumnos')
    grupos = ET.SubElement(raiz, 'grupos')
    for alumno in raiz.findall('./alumnos/alumno'):
        nivel = int(alumno.get('edad')) - 5
        grupo = raiz.find(f"./grupos/grupo[@nivel='{nivel}']")
        if grupo is None:
            grupo = ET.SubElement(grupos, 'grupo', {'nivel': str(nivel)})
        grupo.append(alumno)
        alumnos.remove(alumno)
    raiz.remove(alumnos)
    return arbol

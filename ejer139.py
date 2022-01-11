import xml.etree.ElementTree as ET
arbol = ET.parse('club.xml')
raiz = arbol.getroot()

dic = {}

for socio in raiz.iter('socio'):
    nombre = socio.find('nombre').text
    alta = socio.find('alta').text
    dic[nombre] = alta

res = sorted(dic.items(), key=lambda x: x[1])

for nombre, _ in res:
    print(nombre)

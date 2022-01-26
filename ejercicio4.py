import xml.etree.ElementTree as ET

def cita(arbol, socio, especialidad):
    """Ejercicio 4"""
    raiz = arbol.getroot()
    socio = raiz.find(f".//socios/socio[@id='{socio}']")
    compania = socio.find('./compania').text
    for medico in raiz.findall('.//medicos/medico'):
        if medico.find('./especialidad').text == especialidad:
            for compania_medico in medico.findall('.//companias/compania'):
                if compania_medico.text == compania:
                    ET.SubElement(socio, 'cita', {'med': medico.get('id')})
                    return arbol
    return arbol

arbol = ET.parse("clinica.xml")

import xml.etree.ElementTree as ET

documento = """<?xml version="1.0"?>
<data>
    <alumno numero="999" altura="185">
        <dni>48825438Z</dni>
        <nombre>
            <propio>Manolo</propio>
            <apellidos>García</apellidos>
        </nombre>
        <telefono>666555444</telefono>
        <nota>7</nota>
    </alumno>
    <alumno numero="777">
        <dni>99988877K</dni>
        <nombre>
            <propio>María</propio>
            <apellidos>Pérez</apellidos>
        </nombre>
        <telefono>666444222</telefono>
        <nota>9</nota>
    </alumno>
    <padre>
        <dni>777766662J</dni>
        <nombre>Antonio García</nombre>
        <num_hijos>2</num_hijos>
    </padre>
</data>
"""

var = ET.fromstring(documento)
print(type(var))

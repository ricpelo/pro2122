nombre = 'Ricardo Pérez'
edad = 25
altura = 1.73
peso = 60.0
# Cálculo del IMC = peso / estatura^2
imc = peso / (altura ** 2)
# Si la altura es > 1.80 => el deporte es Baloncesto
# Si 1.50 < altura <= 1.80 => el deporte es Tenis
# Si no, es Golf
deporte = 'Baloncesto' if altura > 1.80 else \
          'Tenis' if altura <= 1.80 and altura > 1.50 else \
          'Golf'

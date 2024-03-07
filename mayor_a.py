#Convertir lista de valores a diccionario
#Filtrar los meses con valores mayores a...

valores = { 
    "Enero": 15000, 
    "Febrero": 22000, 
    "Marzo": 12000, 
    "Abril": 17000, 
    "Mayo": 81000, 
    "Junio": 13000, 
    "Julio": 21000, 
    "Agosto": 41200, 
    "Septiembre": 25000, 
    "Octubre": 21500, 
    "Noviembre": 91000, 
    "Diciembre": 21000
    }

filtrado = {}

for clave, valor in valores.items():
  if valor >50000:
    filtrado[clave] = valor
    
print(filtrado)
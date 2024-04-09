import sys

numero_comparacion = int(sys.argv[1])

ventas = {
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
 "Diciembre": 21000,
}

resultado = "{"

for mes in ventas:
    
    if ventas[mes] > numero_comparacion:
        resultado += f"'{mes}': {ventas[mes]}, "

impresion = ""

# quitar el ", " del final
for i in range (0, len(resultado) - 2):
    impresion += resultado[i]
        
impresion += "}"

print(impresion)
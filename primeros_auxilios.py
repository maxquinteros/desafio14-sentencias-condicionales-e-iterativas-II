respuesta = ""

print("Recuerde solo contestar con si/no\n")

respuesta1 = (input("¿El paciente responde a estímulos?\n>")).lower()

respuesta4 = ""

if respuesta1 == "si":
    print("Valorar la necesidad de llevarlo al hospital más cercano")
    
elif respuesta1 == "no":
    print("Abrir la vía Aérea")
    respuesta2 = (input("¿Respira?\n>")).lower()
    
    if respuesta2 == "si":
        print("Permitirle posición de suficiente ventilación")
        
    elif respuesta2 == "no":
        print("Administrar 5 Ventilaciones y llamar a Ambulancia")
        
        while respuesta4 != "si":
            respuesta3 = (input("¿Signos de Vida?\n>")).lower()
            
            if respuesta3 == "si":
                print("Reevaluar la espera de la Ambulancia")
            elif respuesta3 == "no":
                print("Administrar Compresiones Torácicas hasta que llegue ambulancia")
            else:
                print("Ha ingresado una respuesta distinta a si/no")
                
            respuesta4 = (input("¿Llegó la Ambulancia?\n>")).lower()
        
    else:
        print("Ha ingresado una respuesta distinta a si/no")
        
else:
    print("Ha ingresado una respuesta distinta a si/no")

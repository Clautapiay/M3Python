#pasos a seguir segun respuestas en primeros auxilios

"""INICIO"""
print("Pasos a seguir en primeros auxilios")
print ("")


respuesta = {"si", "no"}

persona = input("¿La persona responde a estimulos?").lower()
if persona == "si":
    input("¿Es necesario llevarlo a un hospital?")
    if persona == "si":
        print("Fin ciclo")
elif persona == "no":
        print("Abrir vía aérea")
        input("¿La persona respira?")
        if persona == "si":
             print("Permitale una posición de suficiente respiración")
             print("Fin ciclo")
        elif persona == "no":
             print("Administre 5 ventilaciones y llame a la ambulancia")
    #AQUIIIIIIIII#
             input("Signos de Vida?")
             if persona == "si" or "no":
                input("LLegó la ambulancia?")
                if persona == "si":
                    print("Fin del ciclo")
                elif persona == "no":
                    print("signos de vida? reevaluar nuevamente")
                      

else:
    print("Debe responder con SI/NO")
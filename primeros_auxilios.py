#pasos a seguir segun respuestas en primeros auxilios

"""INICIO"""
print("Pasos a seguir en primeros auxilios")
print ("")
print("Debe responder con SI/NO")

respuesta = {"si", "no"}

persona = input("¿La persona responde a estímulos? ").lower()
print(persona)
if persona == "si":
    print("Valorar la necesidad de llevarlo al hospital más cercano")
    print("FIN CICLO")
elif persona == "no":
    print("Abrir vía aérea")
    respira = input("¿La persona respira? ").lower()
    print(respira)
    if respira == "si":
        print("Permitirle una posición de suficiente respiración")
        print("Fin ciclo")
    elif respira == "no":
        print("Administrar 5 ventilaciones y llamar a la ambulancia")
        ambulancia = "no"
        while ambulancia != "si":
            hay_ambulancia = input("¿Hay signos de vida? ").lower()
            print(hay_ambulancia)
            ambulancia = "si"
            if hay_ambulancia == "no":
                print("Administrar compresiones torácicas hasta que llegue la ambulancia")
            elif hay_ambulancia == "si":
                print("Reevaluar a la espera de la ambulancia") 
            llega_ambulancia = input("¿Llegó la ambulancia? ").lower()
            print(llega_ambulancia) 
            if llega_ambulancia == "no":
                print("Reevaluar nuevamente ¿hay signos de vida?")
            elif llega_ambulancia == "si":
                print("Fin del ciclo")
            else:
                print("Debe responder con SI/NO") 
        else: 
            print("Debe responder con SI/NO")     
    else:
        print("Debe responder con SI/NO")
else:
    print("Debe responder con SI/NO")



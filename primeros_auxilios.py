#pasos a seguir segun respuestas en primeros auxilios

"""INICIO"""
print("Pasos a seguir en primeros auxilios")
print ("")


respuesta = {"si", "no"}


persona = input("¿La persona responde a estimulos? ").lower()
print(persona)
if persona == "si":
    persona = input("¿Es necesario llevarlo a un hospital? ")
    print(persona)
    if persona == "si" or "no":
        print("Fin ciclo")
elif persona == "no":
        print("Abrir vía aérea")
        persona = input("¿La persona respira? ")
        print(persona)
        if persona == "si":
             print("Permitale una posición de suficiente respiración")
             print("Fin ciclo")
        elif persona == "no":
             print("Administre 5 ventilaciones y llame a la ambulancia")
        persona = input("Signos de Vida? ")
        print(persona)
        if persona == "no":
                print("Administrar compresiones toracicas hasta que llegue la ambulancia")
        elif persona == "si":
            print("Reevaluar a la espera de la ambulancia")       
            persona = input("LLegó la ambulancia? ")  
            print(persona) 
            if persona == "no":
                    print("reevaluar nuevamente ¿signos de vida? ")
            elif persona == "si":
                      print("Fin del ciclo")
                     

            
            
        
     
                      

else:
    print("Debe responder con SI/NO")



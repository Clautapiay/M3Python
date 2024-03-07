#pasos a seguir segun respuestas en primeros auxilios

"""INICIO"""
print("Pasos a seguir en primeros auxilios")
print ("")


respuesta = {"si", "no"}

persona = input("¿La persona responde a estimulos?").lower()
if persona == "si":
    input("¿Es necesario llevarlo a un hospital?")
    if persona == "si" or "no":
        print("Fin ciclo")
elif persona == "no":
        print("Abrir vía aérea")
        input("¿La persona respira?")
        if persona == "si":
             print("Permitale una posición de suficiente respiración")
             print("Fin ciclo")
        elif persona == "no":
             print("Administre 5 ventilaciones y llame a la ambulancia")

             
while persona == "no":
             input("Signos de Vida?")
             if persona == "no":
                print("Administrar compresiones toracicas hasta que llegue la ambulancia")
                input("LLegó la ambulancia?")    
                if persona == "no":
                    print("reevaluar nuevamente ¿signos de vida? ")
                else:
                    print("Reevaluar a la espera de la ambulancia")
                     

            
            
        
     
                      

else:
    print("Debe responder con SI/NO")
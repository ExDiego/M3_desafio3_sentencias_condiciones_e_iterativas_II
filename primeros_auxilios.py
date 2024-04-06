respuesta=input("Responde a estímulos): ")
ambulancia="no"

if (respuesta) =="si":
    print("Valorar la necesidad de llevarlo al hospital más cercano")
else:
    print("abrir las vías aéreas")
    respuesta2=input("respira?")
    if respuesta2=="si":
        print("permitirle posicion de suficiente ventilación")
    else:
        print("Administrar 5 ventilaciones y llamar a Ambulancia")
        while ambulancia =="no":
        
            respuesta3=input("¿signos de vida?")
            if respuesta3=="si":
                print("reevaluar a la espera de la ambulancia")
            else:
                print("administrar compresiones torácicas hasta que llegue la ambulancia")
            ambulancia=input("llego la ambulancia?")
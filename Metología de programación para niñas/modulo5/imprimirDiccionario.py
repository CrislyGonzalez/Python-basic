
#definimos un diccionario
diccionario = {"nombre": "Carla", "edad": "20"}, {"nombre": "Marta", "edad": 20}

#lectura de diccionario principiante
print("Primer diccionario",diccionario[0])
print("El nombre es: ",diccionario[0]["nombre"])
print("La edad es: ",diccionario[0]["edad"])
print("\n \n")


print("Segundo diccionario",diccionario[1])
print("El nombre es: ",diccionario[1]["nombre"])
print("La edad es: ",diccionario[1]["edad"])




#lectura de diccionario avanzada

print("\n \n")

print("\n Imprimiendo solo la información de todos\n")
for i in diccionario:
        print("Nombre: ", i["nombre"],"\n"
                                      "Edad: ", i["edad"])


print("\n Imprimiendo solo la información de carla\n")
for i in diccionario:
    if i["nombre"]== "Carla":
        print("Nombre: ", i["nombre"],"\n"
                                      "Edad: ", i["edad"])
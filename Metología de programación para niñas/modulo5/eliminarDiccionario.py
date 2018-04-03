
lista = []

#solicitamos datos a los usuarios
nombre = input("Digite el nombre suyo: ")
edad = input("Digite su edad: ")


#declaramos el diccionario
diccionario = {}
diccionario["nombre"] = nombre # se crean las posiciones que tendrá el diccionario y se le asigna el valor que ingresa el usuario
diccionario["edad"] = edad
lista.append(diccionario)

print("La lista es: ",lista)

lista=[{"nombre": "Carla", "edad": "20"}]

# eliminando diccionario
for i in lista:
    lista.remove(i) #se eliminan los diccionario

print("VERIFIQUE, la lista ha quedado vacía luego de elimiar diccionarios: ",lista)


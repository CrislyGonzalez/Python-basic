import random

lista=[]


"""
Funcion que genera 5 numeros aleatorios y los agrega a una lista
"""
def generarNum():

    cont=1

    while (cont <= 5):
        numeroGenerado= random.randint(1, 100)
        lista.append(numeroGenerado)
        print(numeroGenerado)
        cont= cont+1

    print("\n Numeros generados e incluidos en la lista",lista)



generarNum()
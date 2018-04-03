
lista = []


def obtenerNumeros():

    contador=0
    while(contador<5):
        numero= int(input("Digite un numero "))
        agregarNumeroLista(numero)
        contador+=1

    imprimirLista()


def agregarNumeroLista(numero):
    lista.append(numero)


def imprimirLista():

    print("\n imprimiendo lista de numero \n")
    for i in lista:
        print("Numeros en la lista son: ", i)


obtenerNumeros()
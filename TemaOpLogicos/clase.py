
def obtenerNumeros():
    print("\nBienvenido al sistema \n")
    numero1 = int(input("Digite el primer numero: "))
    numero2 = int(input("Digite el segundo numero "))
    opcion= int(input("1. Suma\n"
                      "2. Resta\n"
                      "3. Multiplicar\n"
                      "Opcion:"))
    if opcion == 1:
        print(" Hagamos una suma ")
        sumar(numero1,numero2)
        print("\n")
        obtenerNumeros()

    if opcion == 2:
        print(" Hagamos una resta")
        restar(numero1,numero2)
        print("\n")
        obtenerNumeros()

    if opcion == 3:
        print("Hagamos una multiplicación")
        multiplicacion(numero1,numero2)
        print("\n")
        obtenerNumeros()

def multiplicacion(numero1, numero2):

    resultado = numero1 * numero2
    print("El resultado de la multiplicación es: " ,resultado)


def restar(numero1, numero2):

    resultado = numero1 - numero2
    print("El resultado de la resta es: " ,resultado)


def sumar(numero1, numero2):

    resultado = numero1 + numero2
    print("El resultado de la suma es: " ,resultado)


obtenerNumeros()
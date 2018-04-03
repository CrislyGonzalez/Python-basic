
def obtenerNumeros():
    numeroUno = int(input("Ingrese el numero 1 "))
    numeroDos = int(input("Ingrese el numero 2 "))
    suma(numeroUno,numeroDos)


def suma(num1,num2):

    resultado = num1+num2
    print("El resultado de la suma es de: ",resultado)


def resta(num1,num2):
    resultados = num1+num2
    print("El resultado de la resta es de: ", resultados)


def multiplicacion(num1,num2):
    resultado = num1*num2

    print("El resultado de la multiplicación es de: ",resultado)


def verificarNumeroMayor(num1, num2):
    if(num1>num2):
        print("El numero 1 ", num1 , "es mayor que ",num2)
    else:
        print("El numero 2 ", num2, "es mayor que el ",num1)



obtenerNumeros()
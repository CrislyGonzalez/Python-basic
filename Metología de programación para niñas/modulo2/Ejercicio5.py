#Operacion de Suma
def suma():
    numeroUno= 2
    numeroDos= 2
    resultadoSuma= numeroUno + numeroDos
    print("El resultado de la suma es: ",resultadoSuma)

#Operacion de Resta
def resta():
    numeroUno= 5
    numeroDos= 1
    resultadoResta= numeroUno - numeroDos



#Operacion de Multiplicación
def multiplicacion():
    numeroUno= 2
    numeroDos= 4
    resultadoMultiplicacion= numeroUno * numeroDos
    print("El resultado de la multiplicación es: ",resultadoMultiplicacion)


#Operacion de División
def division():

    numeroUno= 8
    numeroDos= 4
    resultadoDivision= numeroUno / numeroDos
    print("El resultado de la división es: ",resultadoDivision)

#Operacion raiz cuadrada
def raizCuadrada():

    numero = 2
    raizCuadrada= numero**2
    print("El resultado de la raiz cuadrada es: ",raizCuadrada)

#menu
def menu():
    opcion= input("Digite la operación que quiere realizar: \n"
                  "1.Suma\n"
                  "2.Resta\n"
                  "3.Multiplicación\n"
                  "4.División\n"
                  "5.Raiz Cuadrada\n"
                  "")

    if opcion == "1":
        suma()
        menu()

    elif opcion == "2":
        resta()
        menu()

    elif opcion == "3":
        multiplicacion()
        menu()

    elif opcion == "4":
        division()
        menu()

    elif opcion == "5":
        raizCuadrada()
        menu()

menu()
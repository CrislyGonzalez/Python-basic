from Globales import  *
listaPersonas=[]
Matriz = []

def imprimirMatriz():


    i = 0
    while i < len(Matriz):
        print(Matriz[i])
        i += 1



def leerArchivo():

    global nombreA
    global apellidoA
    global profesion
    global edadA

    file = open("informacion.txt", "r")

    lineadatos = file.readlines()

    for line in lineadatos:


        info = line.split(",")
        #print(info[1])
        #print(info)

        if(info[0]== "nombre"):
            nombreA=info[1]


        if(info[0]== "apellido"):
            apellidoA= info[1]

        if(info[0]== "edad"):
            edadA= int(info[1])

        if(info[0]== "profesion"):
            profesion= info[1]



    nombreB= nombreA.split("\n")
    apellidoB= apellidoA.split("\n")
    profesionB= profesion.split("\n")

   # print("\nnombre: ",nombreA,"\napellido: ",apellidoA,"\nprofesion: ",profesion,"\nedad: ",edadA )
    construir(nombreB[0],apellidoB[0],edadA,profesionB[0])


    file.close()

def construir(nombreA,apellidoA,edadA,profesion):
    nuevoDiccionario= {}
    nuevoDiccionario["nombre"]=nombreA
    nuevoDiccionario["apellido"]=apellidoA
    nuevoDiccionario["edad"]=edadA
    nuevoDiccionario["profesion"]=profesion

    listaPersonas.append(nuevoDiccionario)


def crearMatriz(size):
    """
receives the size of the matrix
while j(small list) sizeMatrix: then creates an empty row which is then inserted into
the matrix which will be inserting row in matrix while not exceeding the size
    :param size: size the matrix
    """

    i = 0
    while i < size:
        j = 0
        row = []
        while j < size:
            row.append(0)
            j += 1
        Matriz.append(row)
        i += 1



def escribirArchivo(nombre, edad,apellido, profesion):


    """
    metodo para escribir en un archivo
    :param nombre2: nombre de la persona
    :param edad2: edad de la persona
    :param lista: lista (opcional)
    """
    file = open("informacion.txt", "w")

    nombre2 = "nombre" + "," + nombre
    file.write(nombre2 + "\n")

    apellido2 = "apellido" + "," + apellido
    file.write(apellido2 + "\n")

    profesion2 = "profesion" + "," + profesion
    file.write(profesion2 + "\n")

    ed= str(edad)
    edad2 = "edad" + "," + ed
    edadS = str(edad2)
    file.write(edadS + "\n")

    print("agregado al archivo")
    file.close()


def informacion():
    nombre= input("ingrese el nombre: ")
    apellido= input("ingrese el apellido: ")
    edad= int(input("ingrese la edad: "))
    profesion= input("ingrese la profesion: ")

    escribirArchivo(nombre,edad,apellido,profesion)


def llamadasMetodos():
    informacion()
    leerArchivo()
    print("\n",listaPersonas)


def funcionesmatriz():
    crearMatriz(6)
    imprimirMatriz()


#funcionesmatriz()

llamadasMetodos()
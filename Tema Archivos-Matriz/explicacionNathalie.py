Matriz=[]
listaPersonas=[]

nombreA=""
apellidoA=""
profesion=""
edadA=0


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



def leerArchivo():

    global nombreA
    global apellidoA
    global profesion
    global edadA

    file = open("informacionNathalie.txt", "r")

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

def construir(nombre,apellido,edad,profesion):
    nuevoDiccionario= {}
    nuevoDiccionario["nombre"]=nombre
    nuevoDiccionario["apellido"]=apellido
    nuevoDiccionario["edad"]=edad
    nuevoDiccionario["profesion"]=profesion

    listaPersonas.append(nuevoDiccionario)



def escribirArchivo(nombre, edad,apellido, profesion):

    """

    :param nombre:
    :param edad:
    :param apellido:
    :param profesion:
    """


    file = open("informacionNathalie.txt", "a")

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



#escribirArchivo("nathalie",20,"Rojas","estudiante")
leerArchivo()
print(listaPersonas)


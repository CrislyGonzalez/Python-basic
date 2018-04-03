

listaProductos= [{"ID":2,"Nombre":"Bombillo","Cantidad": 5,"Descripcion":"generico","Precio":500}]



def crearProducto(pnombre,pcantidad,pdescripcion,pPrecio,pid):


    nuevoDiccionario= {}
    nuevoDiccionario["ID"]=pid
    nuevoDiccionario["Nombre"]=pnombre
    nuevoDiccionario["Cantidad"]=pcantidad
    nuevoDiccionario["Descripcion"]=pdescripcion
    nuevoDiccionario["Precio"]= pPrecio
    listaProductos.append(nuevoDiccionario)
    print("\nListo lo agregamos xD")



def solicitarinformacionProductos():

    print("\n Informacion de producto \n ")
    id= int(input("Ingrese un el id del producto: "))
    nombre= input("Ingrese el nombre del producto: ")
    cantidad= int(input("Ingrese la cantidad de productos: "))
    descripcion= input("Ingrese una breve descripcion: ")
    precio= float(input("Ingrese el precio del producto: "))
    crearProducto(nombre,cantidad,descripcion,precio,id)



def imprimirProductos():
    for i in listaProductos:
        print("\n\n\n")
        print("ID: ",i["ID"],"\n"
              "Nombre: ",i["Nombre"],"\n"
              "Cantidad",i["Cantidad"],"\n"
              "Descripcion",i["Descripcion"],"\n"
              "Precio",i["Precio"])



def buscarProductos(pID):
    for i in listaProductos:
        if(i["ID"]== pID):
            print("\n\n\n")
            print("ID: ",i["ID"],"\n"
                  "Nombre: ",i["Nombre"],"\n"
                  "Cantidad",i["Cantidad"],"\n"
                  "Descripcion",i["Descripcion"],"\n"
                  "Precio",i["Precio"])


def eliminarProductos(pid):
    for i in listaProductos:
        if(i["ID"]==pid):
            listaProductos.remove(i)
            print("\n Diccionario Eliminado")


def menu():
    opcion= int(input("Bienvenido \n"
                      "1.Ingresar productos \n"
                      "2.Buscar productos\n"
                      "3.imprimir productos\n"
                      "4.Eliminar productos\n"
                      "Opcion: "))


    if(opcion==1):
        solicitarinformacionProductos()
        print("\n\n\n\n")
        menu()

    elif(opcion==2):
        opt= int(input("Ingrese el id a buscar"))
        buscarProductos(opt)
        print("\n\n\n\n")
        menu()

    elif(opcion==3):
        imprimirProductos()
        print("\n\n\n\n")
        menu()

    else:
        opt= int(input("Ingrese el id a eliminar"))
        eliminarProductos(opt)
        print("\n\n\n\n")
        menu()



menu()
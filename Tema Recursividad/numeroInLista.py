def elMayor(lista):
    if lista== []:
        return []
    else:
        return mayorAux(lista,lista[0])


def mayorAux(lista,resultado):
    if lista== []:
        return resultado
    elif lista[0]>resultado:
        return mayorAux(lista[1:],lista[0])
    else:
        return mayorAux(lista[1:],resultado)


print("Mayor de la lista [3,6,5,4,8,20] ")
print(elMayor([3,6,5,4,8,20]))



def eliminarNumLista(lista, elemento):
    if lista==[]:
        return []
    elif lista[0]== elemento:
        return eliminarNumLista(lista[1:], elemento)

    else:
        return [lista[0]] + eliminarNumLista(lista[1:], elemento)


print("\nNumero eliminado")
print(eliminarNumLista([3, 1, 5, 4, 5], 5))


def numeroAumentadoLista(lista,cantidad,num):
    if lista==[]:
        return []

    elif lista[0]== num:
        if(cantidad==0):
            return numeroAumentadoLista(lista[1:],cantidad,num)
        else:
            return [num]+ numeroAumentadoLista(lista,cantidad-1,num)


    else:
        return [lista[0]]+ numeroAumentadoLista(lista[1:],cantidad,num)


print("\nNumero aumentado en la lista")
print(numeroAumentadoLista([5,3,2,1],3,2))




listaPersonas=[{"id":"02","nombre":"cris","tipo":"estudiante"},{"id":"03","nombre":"nathalie","tipo":"estudiante"}]

listaCursos=[{"id":"10","nombre":"intro","miembros":["02","03"]}]


def imprimirCursos(id):
    for i in listaCursos:
        if(i["miembros"]!=[]):
            for e in i["miembros"]:
                if(e == id):
                    for j in listaPersonas:
                        if(j["id"] == e):
                            print("\nid: ", j["id"], "\nnombre: ",j["nombre"],"\ntipo: ",j["tipo"], "\ncurso: ", i["nombre"])




imprimirCursos("02")
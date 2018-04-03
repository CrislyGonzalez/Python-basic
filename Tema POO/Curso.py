from Materia import *

class Curso:
    nombre=""
    idCurso=""


    def __init__(self,nombre,id, materia):
        self.nombre =nombre
        self.idCurso = id
        self.materia=materia



    def setNombre(self,nuevoNombre):
        self.nombre= nuevoNombre

    def setIdCurso(self,nId):
        self.idCurso=nId


    def getNombre(self):
        return self.nombre

    def getIdCurso(self):
        return self.idCurso

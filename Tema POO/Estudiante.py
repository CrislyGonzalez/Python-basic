from Persona import *

class Estudiante(Persona):
    #Atributos
    carne=""
    cursosMatriculados=[]


    #Metodo constructor
    def __init__(self, nombre, edad,carne):
        super().__init__(nombre, edad)
        self.carne=carne


    #Metodos set y get
    def getEdad(self):
        return super().getEdad()

    def AgregarCurso(self, Curso):
        self.cursosMatriculados.append(Curso)

    def setEdad(self, nuevoEdad):
        super().setEdad(nuevoEdad)

    def getNombre(self):
        return super().getNombre()

    def setNombre(self, nuevoNombre):
        super().setNombre(nuevoNombre)


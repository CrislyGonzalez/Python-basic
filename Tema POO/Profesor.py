from Persona import *

class Profesor(Persona):

    salario=0

    def __init__(self, nombre, edad, salario):
        super().__init__(nombre, edad)

        self.salario=salario


    def getSalario(self):
        return self.salario

    def setSalario(self,nuevoSalario):
        self.salario=nuevoSalario

    def getEdad(self):
        return super().getEdad()

    def setEdad(self, nuevoEdad):
        super().setEdad(nuevoEdad)

    def getNombre(self):
        return super().getNombre()

    def setNombre(self, nuevoNombre):
        super().setNombre(nuevoNombre)








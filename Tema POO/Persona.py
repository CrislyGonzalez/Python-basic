

class Persona:
    #no es necesario indicarlos aqui
    nombre= ""
    edad=0

    def __init__(self, nombre, edad ):
        self.nombre =nombre
        self.edad=edad


    def getNombre(self):
        return self.nombre

    def getEdad(self):
        return self.edad


    def setNombre(self,nuevoNombre):
        self.nombre=nuevoNombre

    def setEdad(self,nuevoEdad):
        self.edad=nuevoEdad







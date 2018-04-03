from Estudiante import *
from Curso import *


#Estudiantes
Estudiante1 = Estudiante("Crisly", 22,"2013")
Estudiante2 = Estudiante("Nathalie", 17,"2015")
Estudiante3 = Estudiante("Kembly", 20,"2016")
Estudiante4 = Estudiante("Laura", 28,"2017")
Estudiante5 = Estudiante("Carolina", 10,"2018")
print(Estudiante1.getNombre())

Materia1= Materia("Conceptos de orientacion a objetos")
Materia2= Materia("Recursividad")
Materia3= Materia("POO")


Curso1 = Curso("Introduccion","2017-IC",Materia3)
Curso2 = Curso("Taller","25-IC",Materia2)


#Agregando Cursos a un estudiante
Estudiante1.AgregarCurso(Curso1)

Estudiante2.AgregarCurso(Curso1)
Estudiante2.AgregarCurso(Curso2)







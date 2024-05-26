import random
class Estudiante:
    def __init__(self, id, carrera):
        self.id = id
        self.cursos_aprobados = []
        self.cursos_semestre = []
        self.carrera = carrera
        self.materias_vistas = 0
        
    def materias_semestres(self, malla):
        #generar el número de materias a inscrbir
        materias = self.numero_materias_ver()
        #Reiniciar los cursos que puede ver
        self.cursos_semestre = []
        
        #Bsucar que materias puede ver
    
        for materia in malla:
            if materia not in self.cursos_aprobados:
                #Verificar si cumple los prerequisitos o si no tiene
                #Los prerequistios dependen de la carrera
                
                prerequisitosCarreraMateria = materia.prerequisitos.get(self.carrera)
               
                
                
                #¿Como verifico? pues porque ya los cursó
                if prerequisitosCarreraMateria == []:
                    self.cursos_semestre.append(materia)
                    materia.inscritos+=1
                    #print("El estudiante inscribe "+ materia.nombre)
                else:
                    # Convertir las listas a conjuntos para realizar operaciones de conjuntos
                    prerequisitos = set(prerequisitosCarreraMateria)
                    cursos_aprobados = set(self.cursos_aprobados)

                    # Verificar si todos los prerequisitos están en los cursos aprobados
                    if prerequisitos.issubset(cursos_aprobados):
                        self.cursos_semestre.append(materia)
                        materia.inscritos+=1
                        #print("El estudiante inscribe "+ materia.nombre)
            if len(self.cursos_semestre) == materias:
                break
            
    def numero_materias_ver(self):
        
        #Generar un numero aleatorio
        n = random.random()
        materias = 0
        
        #Un estudiante va a iscribir 4, 5 o 6 materias
        #Inscribir 4 materias tiene un 20 % de probabilidad
        
        if(n<=0.2):
            materias = 4
        elif( n<= 0.7):
            materias = 5
        else:
            materias = 6
        
        return materias
            
      
    #Verificar si las pierde o no
    def final_semestre(self):
        
        #Iterar sobre las materias inscritas e ir generando el número aleatorio
        randNumber = 0
        
        for materia in self.cursos_semestre:
            randNumber = random.random()
            
            if(randNumber<=materia.pasar):
                self.cursos_aprobados.append(materia)
                self.materias_vistas+=1
                #print("El estudiante aprueba "+ materia.nombre)
            else:
                continue
                #print("El estudiante pierde "+ materia.nombre)
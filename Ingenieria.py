from MallaIngenieria import MallaIngenieria
from Estudiante import Estudiante

class Ingenieria:
    
    def __init__(self):
        self.estudiantes = []
        self.key = 0
        self.periodo = 0
        
        #nombres carreras
        
        self.sistemas ="ingenieria_de_sistemas"
        
        #Constantes para el número de admitidos
        self.admitidos_agricola =70
        self.admitidos_civil = 105
        self.admitidos_sistemas = 110
        self.admitidos_electrica = 60
        self.admitidos_electronica = 58
        self.admitidos_industrial = 45
        self.admitidos_mecanica = 82
        self.admitidos_mecatronica = 43
        self.admitidos_quimica = 120
    
        
        #Crear materias de ingenieria
        self.materias_ingenieria = MallaIngenieria()

    def semestre(self):
        
        #Nuevos Admitidos
        self.nuevos_admitidos()
        
        #Cada estudiante inscribira sus materias
        self.inscribir_materias()
        
        #Terminar semestre y ver quienes perdieron
        self.calificaciones()
        
        #Graduar gente
        self.graduados()
        
        #Hacer reporte
        self.reporte()
        
        #Actualizar periodo
        self.periodo+=1
            
    def inscribir_materias(self):
        for estudiante in self.estudiantes:
            
            #print("El estudiante con codigo "+str(estudiante.id)+" de la carrera de "+ estudiante.carrera+" inscribe:")
            if(estudiante.carrera==self.sistemas):
            
                estudiante.materias_semestres(self.materias_ingenieria.materias_sistemas)
                
                
    def calificaciones(self):
        
        for estudiante in self.estudiantes:
            #print("Reporte estudiante con codigo "+str(estudiante.id))
            estudiante.final_semestre()
    
    def graduados(self):
        
        indexList = []
        
        for i in range(0, len(self.estudiantes)):
            
            student = self.estudiantes[i]
            
            if(student.carrera == self.sistemas):
                if(student.materias_vistas == self.materias_ingenieria.materias_totales_sistemas):
                    #Sacarlo de la lista de estudiantes
                    indexList.append(i)
                    
        #Borrarlos
        for i in range(0,len(indexList)):
            self.estudiantes.pop(indexList[i])
    
    def reporte(self):
        self.materias_ingenieria.reporteInscripciones()
        
        
    def nuevos_admitidos(self):
        
        #admitidos por sistemas
        
        for i in range(0,self.admitidos_sistemas):
            
            student = Estudiante(self.key,self.sistemas)
            self.estudiantes.append(student)
            self.key+=1
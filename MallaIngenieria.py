from Curso import Curso

class MallaIngenieria:
    
    def __init__(self):
        
        #nombres
        self.sistemas ="ingenieria_de_sistemas"
        
        #Materias
        #Materias primer Semestre
        self.calculo_diferencial = Curso("Calculo diferencial",0.7,{self.sistemas:[]})
        self.introduccion_a_la_ingenieria_de_sistemas = Curso("Introducción a la ingeniería de sistemas y computación",0.9,{self.sistemas:[]})
        self.programacion_de_computadores = Curso("Programación de computadores",0.9,{self.sistemas:[]})
        self.pensamiento_sistemico = Curso("Pensamiento Sistemico",0.9,{self.sistemas:[]})

        # Materias segundo Semestre 
        self.fundamentos_de_mecanica = Curso("Fundamentos de mecanica",0.7,{self.sistemas:[self.calculo_diferencial]})
        self.calculo_integral = Curso("Calculo Integral",0.7,{self.sistemas:[self.calculo_diferencial]})
        self.algebra_lineal = Curso("Álgebra lineal",0.6,{self.sistemas:[self.calculo_diferencial]})
        self.programacion_orientada_a_objetos = Curso("Programación orientada a objetos",0.92,{self.sistemas:[self.programacion_de_computadores]})

        # Materias tercer Semestre
        self.fundamentos_de_electricidad_y_magnetismo = Curso("Fundamentos de electricidad y magnetismo",0.7,{self.sistemas:[self.fundamentos_de_mecanica,self.calculo_integral]}) 
        self.calculo_en_varias_variables = Curso("Cálculo en varias variables",0.7,{self.sistemas:[self.calculo_integral]})
        self.matematicas_discretas_I = Curso("Matemáticas discretas I",0.89,{self.sistemas:[self.algebra_lineal]})
        self.bases_de_datos = Curso("Base de datos",0.7,{self.sistemas:[self.programacion_orientada_a_objetos]})
        self.elementos_de_computadores = Curso("Elementos de computadores",0.7,{self.sistemas:[self.introduccion_a_la_ingenieria_de_sistemas]})

        # Materias cuarto Semestre
        self.probabilidad_y_estadistica_fundamental = Curso("Probabilidad y Estadística fundamental",0.85,{self.sistemas:[self.calculo_integral]})  
        self.ingenieria_economica = Curso("Ingeniería económica",0.95,{self.sistemas:[self.calculo_integral]})
        self.matematicas_discretas_II = Curso("Matemáticas discretas II",0.89,{self.sistemas:[self.matematicas_discretas_I]})
        self.estructuras_de_datos = Curso("Estructuras de datos",0.95,{self.sistemas:[self.programacion_orientada_a_objetos]})
        self.arquitectura_de_computadores = Curso("Arquitectura de computadores",0.80,{self.sistemas:[self.elementos_de_computadores]})

        # Materias quinto Semestre
        self.modelos_y_simulacion = Curso("Modelos y Simulación", 0.80, {self.sistemas: [self.programacion_orientada_a_objetos, self.probabilidad_y_estadistica_fundamental, self.calculo_en_varias_variables, self.matematicas_discretas_II]})
        self.gerencia_y_gestion_de_proyectos = Curso("Gerencia y gestión de proyectos", 0.95, {self.sistemas: [self.ingenieria_economica]})
        self.redes_de_computadores = Curso("Redes de computadores", 0.70, {self.sistemas: [self.fundamentos_de_electricidad_y_magnetismo, self.estructuras_de_datos, self.arquitectura_de_computadores]})
        self.ingenieria_de_software_I = Curso("Ingeniería de software I", 0.80, {self.sistemas: [self.estructuras_de_datos, self.pensamiento_sistemico, self.bases_de_datos]})
        self.introduccion_a_la_teoria_de_la_computacion = Curso("Introducción a la teoría de la computación", 0.70, {self.sistemas: [self.matematicas_discretas_I]})

        # Materias Sexto Semestre
        self.optimizacion = Curso("Optimización", 0.80, {self.sistemas: [self.modelos_y_simulacion]})
        self.sistemas_de_informacion = Curso("Sistemas de información", 0.80, {self.sistemas: [self.pensamiento_sistemico, self.gerencia_y_gestion_de_proyectos, self.bases_de_datos]})
        self.metodos_numericos = Curso("Métodos numéricos", 0.80, {self.sistemas: [self.calculo_en_varias_variables]})
        self.ingenieria_de_software_II = Curso("Ingeniería de software II", 0.80, {self.sistemas: [self.redes_de_computadores, self.ingenieria_de_software_I]})
        self.algoritmos = Curso("Algoritmos", 0.80, {self.sistemas: [self.matematicas_discretas_I, self.matematicas_discretas_II, self.estructuras_de_datos]})
        self.sistemas_operativos = Curso("Sistemas operativos", 0.80, {self.sistemas: [self.arquitectura_de_computadores]})
        
        # Materias Septimo Semestre
        self.modelos_estocasticos_y_simulacion_en_computacion_y_comunicaciones = Curso("Modelos estocásticos y simulación en computación y comunicaciones", 0.80, {self.sistemas: [self.optimizacion]})
        self.arquitectura_de_infraestructura_y_gobierno_de_TICs = Curso("Arquitectura de infraestructura y gobierno de TICs", 0.80, {self.sistemas: [self.sistemas_de_informacion, self.ingenieria_de_software_II]})
        self.teoria_de_la_informacion_y_sistemas_de_comunicaciones = Curso("Teoría de la información y sistemas de comunicaciones", 0.80, {self.sistemas: [self.probabilidad_y_estadistica_fundamental, self.redes_de_computadores]})
        self.arquitectura_de_software = Curso("Arquitectura de software", 0.80, {self.sistemas: [self.ingenieria_de_software_II]})
        self.introduccion_a_los_sistemas_inteligentes = Curso("Introducción a los sistemas inteligentes", 0.80, {self.sistemas: [self.algoritmos]})
        self.lenguajes_de_programacion = Curso("Lenguajes de programación", 0.80, {self.sistemas: [self.introduccion_a_la_teoria_de_la_computacion, self.estructuras_de_datos]})

        # Materias Octavo Semestre
        self.taller_de_proyectos_interdisciplinarios = Curso("Taller de proyectos Interdisciplinarios", 0.80, {self.sistemas: []})
        self.computacion_paralela_y_distribuida = Curso("Computación paralela y distribuida", 0.80, {self.sistemas: [self.algoritmos]})
        self.introduccion_a_la_criptografia_y_a_la_seguridad_de_la_informacion = Curso("Introducción a la criptografía y a la seguridad de la información", 0.80, {self.sistemas: [self.algoritmos]})
        self.computacion_visual = Curso("Computación visual", 0.80, {self.sistemas: [self.algoritmos]})


        self.materias = [
            self.calculo_diferencial,
            self.introduccion_a_la_ingenieria_de_sistemas,
            self.programacion_de_computadores,
            self.pensamiento_sistemico,
            self.fundamentos_de_mecanica,
            self.calculo_integral,
            self.algebra_lineal,
            self.programacion_orientada_a_objetos,
            self.fundamentos_de_electricidad_y_magnetismo,
            self.calculo_en_varias_variables,
            self.matematicas_discretas_I,
            self.bases_de_datos,
            self.elementos_de_computadores,
            self.probabilidad_y_estadistica_fundamental,
            self.ingenieria_economica,
            self.matematicas_discretas_II,
            self.estructuras_de_datos,
            self.arquitectura_de_computadores,
            self.modelos_y_simulacion,
            self.gerencia_y_gestion_de_proyectos,
            self.redes_de_computadores,
            self.ingenieria_de_software_I,
            self.introduccion_a_la_teoria_de_la_computacion,
            self.optimizacion,
            self.sistemas_de_informacion,
            self.metodos_numericos,
            self.ingenieria_de_software_II,
            self.algoritmos,
            self.sistemas_operativos,
            self.modelos_estocasticos_y_simulacion_en_computacion_y_comunicaciones,
            self.arquitectura_de_infraestructura_y_gobierno_de_TICs,
            self.teoria_de_la_informacion_y_sistemas_de_comunicaciones,
            self.arquitectura_de_software,
            self.introduccion_a_los_sistemas_inteligentes,
            self.lenguajes_de_programacion,
            self.taller_de_proyectos_interdisciplinarios,
            self.computacion_paralela_y_distribuida,
            self.introduccion_a_la_criptografia_y_a_la_seguridad_de_la_informacion,
            self.computacion_visual
        ]

        
        
        
        #mallas
        self.materias_sistemas = [
                        # Primer Semestre
                        self.calculo_diferencial,
                        self.introduccion_a_la_ingenieria_de_sistemas,
                        self.programacion_de_computadores,
                        self.pensamiento_sistemico,

                        # Segundo Semestre
                        self.fundamentos_de_mecanica,
                        self.calculo_integral,
                        self.algebra_lineal,
                        self.programacion_orientada_a_objetos,

                        # Tercer Semestre
                        self.fundamentos_de_electricidad_y_magnetismo,
                        self.calculo_en_varias_variables,
                        self.matematicas_discretas_I,
                        self.bases_de_datos,
                        self.elementos_de_computadores,

                        # Cuarto Semestre
                        self.probabilidad_y_estadistica_fundamental,
                        self.ingenieria_economica,
                        self.matematicas_discretas_II,
                        self.estructuras_de_datos,
                        self.arquitectura_de_computadores,

                        # Quinto Semestre
                        self.modelos_y_simulacion,
                        self.gerencia_y_gestion_de_proyectos,
                        self.redes_de_computadores,
                        self.ingenieria_de_software_I,
                        self.introduccion_a_la_teoria_de_la_computacion,

                        # Sexto Semestre
                        self.optimizacion,
                        self.sistemas_de_informacion,
                        self.metodos_numericos,
                        self.ingenieria_de_software_II,
                        self.algoritmos,
                        self.sistemas_operativos,

                        # Séptimo Semestre
                        self.modelos_estocasticos_y_simulacion_en_computacion_y_comunicaciones,
                        self.arquitectura_de_infraestructura_y_gobierno_de_TICs,
                        self.teoria_de_la_informacion_y_sistemas_de_comunicaciones,
                        self.arquitectura_de_software,
                        self.introduccion_a_los_sistemas_inteligentes,
                        self.lenguajes_de_programacion,

                        # Octavo Semestre
                        self.taller_de_proyectos_interdisciplinarios,
                        self.computacion_paralela_y_distribuida,
                        self.introduccion_a_la_criptografia_y_a_la_seguridad_de_la_informacion,
                        self.computacion_visual
        ]
        #materias totales
        self.materias_totales_sistemas = len(self.materias_sistemas)
    
    def reporteInscripciones(self):
        
        for materia in self.materias:
            print("la materia "+materia.nombre+" recibio "+str(materia.inscritos)+" inscripciones")
            #Reiniciar reportes
            materia.inscritos = 0
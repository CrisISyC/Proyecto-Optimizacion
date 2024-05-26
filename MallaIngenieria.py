from Curso import Curso

class MallaIngenieria:
    
    def __init__(self):
        
        #nombres
        self.sistemas ="ingenieria_de_sistemas"
        self.industrial ="ingenieria_industrial"

        #Materias
        #Materias primer Semestre
        self.calculo_diferencial = Curso("Calculo diferencial",0.7,{self.sistemas:[],self.industrial: []})
        self.introduccion_a_la_ingenieria_de_sistemas = Curso("Introducción a la ingeniería de sistemas y computación",0.9,{self.sistemas:[]})
        self.programacion_de_computadores = Curso("Programación de computadores",0.9,{self.sistemas:[],self.industrial: []})
        self.pensamiento_sistemico = Curso("Pensamiento Sistemico",0.9,{self.sistemas:[]})

        # Materias segundo Semestre 
        self.fundamentos_de_mecanica = Curso("Fundamentos de mecanica",0.7,{self.sistemas:[self.calculo_diferencial],self.industrial: [self.calculo_diferencial]})
        self.calculo_integral = Curso("Calculo Integral",0.7,{self.sistemas:[self.calculo_diferencial],self.industrial: [self.calculo_diferencial]})
        self.algebra_lineal = Curso("Álgebra lineal",0.6,{self.sistemas:[self.calculo_diferencial],self.industrial: [self.calculo_diferencial]})
        self.programacion_orientada_a_objetos = Curso("Programación orientada a objetos",0.92,{self.sistemas:[self.programacion_de_computadores],self.industrial:[self.programacion_de_computadores]})

        # Materias tercer Semestre
        self.fundamentos_de_electricidad_y_magnetismo = Curso("Fundamentos de electricidad y magnetismo",0.7,{self.sistemas:[self.fundamentos_de_mecanica,self.calculo_integral],self.industrial: [self.fundamentos_de_mecanica,self.calculo_integral]}) 
        self.calculo_en_varias_variables = Curso("Cálculo en varias variables",0.7,{self.sistemas:[self.calculo_integral],self.industrial: [self.calculo_integral]})
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
        #self.modelos_y_simulacion = Curso("Modelos y Simulación", 0.80, {self.sistemas: [self.programacion_orientada_a_objetos, self.probabilidad_y_estadistica_fundamental, self.calculo_en_varias_variables, self.matematicas_discretas_II],self.industrial: [self.taller_de_herramientas_y_problemas_en_ingenieria_industrial, self.calculo_en_varias_variables, self.probabilidad_fundamental]})
        #self.gerencia_y_gestion_de_proyectos = Curso("Gerencia y gestión de proyectos", 0.95, {self.sistemas: [self.ingenieria_economica],self.industrial: [self.ingenieria_economica_y_analisis_de_riesgos]})
        self.redes_de_computadores = Curso("Redes de computadores", 0.70, {self.sistemas: [self.fundamentos_de_electricidad_y_magnetismo, self.estructuras_de_datos, self.arquitectura_de_computadores]})
        self.ingenieria_de_software_I = Curso("Ingeniería de software I", 0.80, {self.sistemas: [self.estructuras_de_datos, self.pensamiento_sistemico, self.bases_de_datos]})
        self.introduccion_a_la_teoria_de_la_computacion = Curso("Introducción a la teoría de la computación", 0.70, {self.sistemas: [self.matematicas_discretas_I]})

        # Materias Sexto Semestre
        #self.optimizacion = Curso("Optimización", 0.80, {self.sistemas: [self.modelos_y_simulacion],self.industrial: [self.algebra_lineal, self.calculo_en_varias_variables]})
        #self.sistemas_de_informacion = Curso("Sistemas de información", 0.80, {self.sistemas: [self.pensamiento_sistemico, self.gerencia_y_gestion_de_proyectos, self.bases_de_datos],self.industrial: [self.gerencia_y_gestion_de_proyectos]})
        self.metodos_numericos = Curso("Métodos numéricos", 0.80, {self.sistemas: [self.calculo_en_varias_variables]})
        self.ingenieria_de_software_II = Curso("Ingeniería de software II", 0.80, {self.sistemas: [self.redes_de_computadores, self.ingenieria_de_software_I]})
        self.algoritmos = Curso("Algoritmos", 0.80, {self.sistemas: [self.matematicas_discretas_I, self.matematicas_discretas_II, self.estructuras_de_datos]})
        self.sistemas_operativos = Curso("Sistemas operativos", 0.80, {self.sistemas: [self.arquitectura_de_computadores]})
        
        # Materias Septimo Semestre
        #self.modelos_estocasticos_y_simulacion_en_computacion_y_comunicaciones = Curso("Modelos estocásticos y simulación en computación y comunicaciones", 0.80, {self.sistemas: [self.optimizacion]})
        #self.arquitectura_de_infraestructura_y_gobierno_de_TICs = Curso("Arquitectura de infraestructura y gobierno de TICs", 0.80, {self.sistemas: [self.sistemas_de_informacion, self.ingenieria_de_software_II]})
        self.teoria_de_la_informacion_y_sistemas_de_comunicaciones = Curso("Teoría de la información y sistemas de comunicaciones", 0.80, {self.sistemas: [self.probabilidad_y_estadistica_fundamental, self.redes_de_computadores]})
        self.arquitectura_de_software = Curso("Arquitectura de software", 0.80, {self.sistemas: [self.ingenieria_de_software_II]})
        self.introduccion_a_los_sistemas_inteligentes = Curso("Introducción a los sistemas inteligentes", 0.80, {self.sistemas: [self.algoritmos]})
        self.lenguajes_de_programacion = Curso("Lenguajes de programación", 0.80, {self.sistemas: [self.introduccion_a_la_teoria_de_la_computacion, self.estructuras_de_datos]})

        # Materias Octavo Semestre
        self.taller_de_proyectos_interdisciplinarios = Curso("Taller de proyectos Interdisciplinarios", 0.80, {self.sistemas: []})
        self.computacion_paralela_y_distribuida = Curso("Computación paralela y distribuida", 0.80, {self.sistemas: [self.algoritmos]})
        self.introduccion_a_la_criptografia_y_a_la_seguridad_de_la_informacion = Curso("Introducción a la criptografía y a la seguridad de la información", 0.80, {self.sistemas: [self.algoritmos]})
        self.computacion_visual = Curso("Computación visual", 0.80, {self.sistemas: [self.algoritmos]})

        ###############################################INDUSTRIAL#########################################


        #Materias
        #Materias primer Semestre
        self.sociologia_especial_industrial_y_del_trabajo = Curso("Sociología especial: industrial y del trabajo", 0.8, {self.industrial: []})
        self.introduccion_a_la_ingenieria_industrial = Curso("Introducción a la ingeniería industrial", 0.8, {self.industrial: []})

        # Materias segundo Semestre
        self.taller_de_invencion_y_creatividad = Curso("Taller de invención y creatividad", 0.8, {self.industrial: [self.introduccion_a_la_ingenieria_industrial]})

        # Materias tercer Semestre
        self.economia_general = Curso("Economía general", 0.8, {self.industrial: [self.calculo_diferencial, self.introduccion_a_la_ingenieria_industrial]})
        self.taller_de_herramientas_y_problemas_en_ingenieria_industrial = Curso("Taller de herramientas y problemas en Ingeniería Industrial", 0.8, {self.industrial: [self.calculo_diferencial, self.introduccion_a_la_ingenieria_industrial]})
        self.probabilidad_fundamental = Curso("Probabilidad fundamental", 0.8, {self.industrial: [self.calculo_integral]})
        
        # Materias cuarto Semestre
        self.ecuaciones_diferenciales = Curso("Ecuaciones diferenciales", 0.8, {self.industrial: [self.calculo_integral, self.algebra_lineal]})
        self.sistema_de_costos = Curso("Sistema de costos", 0.8, {self.industrial: [self.taller_de_herramientas_y_problemas_en_ingenieria_industrial]})
        self.gestion_empresarial = Curso("Gestión empresarial", 0.8, {self.industrial: [self.economia_general, self.taller_de_invencion_y_creatividad]})
        self.taller_de_ciencia_y_tecnologia_de_materiales = Curso("Taller de ciencia y tecnología de materiales", 0.8, {self.industrial: [self.fundamentos_de_mecanica]})

        # Materias quinto Semestre
        self.modelos_y_simulacion = Curso("Modelos y Simulación", 0.80, {self.sistemas: [self.programacion_orientada_a_objetos, self.probabilidad_y_estadistica_fundamental, self.calculo_en_varias_variables, self.matematicas_discretas_II],self.industrial: [self.taller_de_herramientas_y_problemas_en_ingenieria_industrial, self.calculo_en_varias_variables, self.probabilidad_fundamental]})
        self.optimizacion = Curso("Optimización", 0.80, {self.sistemas: [self.modelos_y_simulacion],self.industrial: [self.algebra_lineal, self.calculo_en_varias_variables]})
        self.ingenieria_economica_y_analisis_de_riesgos = Curso("Ingeniería económica y análisis de riesgos", 0.8, {self.industrial: [self.calculo_en_varias_variables]})
        self.taller_de_procesos_quimicos_y_biotecnologicos = Curso("Taller de procesos químicos y biotecnológicos", 0.8, {self.industrial: [self.taller_de_ciencia_y_tecnologia_de_materiales]})
        self.taller_de_procesos_metalmecanicos = Curso("Taller de procesos metalmecánicos", 0.8, {self.industrial: [self.taller_de_ciencia_y_tecnologia_de_materiales]})
        self.inferencia_estadistica_fundamental = Curso("Inferencia estadística fundamental", 0.8, {self.industrial: [self.probabilidad_fundamental]})

        # Materias sexto Semestre
        self.modelos_estocasticos_para_procesos_de_manufactura_y_sistemas_de_servicio = Curso("Modelos estocásticos para procesos de manufactura y sistemas de servicio", 0.8, {self.industrial: [self.inferencia_estadistica_fundamental, self.modelos_y_simulacion]})
        self.finanzas = Curso("Finanzas", 0.8, {self.industrial: [self.ingenieria_economica_y_analisis_de_riesgos]})
        self.taller_de_ergonomia_e_ingenieria_de_metodos = Curso("Taller de ergonomía e ingeniería de métodos", 0.8, {self.industrial: [self.taller_de_procesos_metalmecanicos, self.optimizacion]})
        self.control_y_gestion_de_calidad = Curso("Control y gestión de calidad", 0.8, {self.industrial: [self.inferencia_estadistica_fundamental]})
        self.gerencia_y_gestion_de_proyectos = Curso("Gerencia y gestión de proyectos", 0.95, {self.sistemas: [self.ingenieria_economica],self.industrial: [self.ingenieria_economica_y_analisis_de_riesgos]})
        
        # Materias séptimo Semestre
        self.taller_de_simulacion_de_procesos_de_manufactura_y_sistemas_de_servicios = Curso("Taller de simulación de procesos de manufactura y sistemas de servicios", 0.8, {self.industrial: [self.modelos_estocasticos_para_procesos_de_manufactura_y_sistemas_de_servicio]})
        self.sistemas_de_informacion = Curso("Sistemas de información", 0.80, {self.sistemas: [self.pensamiento_sistemico, self.gerencia_y_gestion_de_proyectos, self.bases_de_datos],self.industrial: [self.gerencia_y_gestion_de_proyectos]})
        self.seguridad_industrial = Curso("Seguridad Industrial", 0.8, {self.industrial: [self.fundamentos_de_electricidad_y_magnetismo]})
        self.taller_de_ingenieria_de_la_produccion = Curso("Taller de ingeniería de la producción", 0.8, {self.industrial: [self.modelos_estocasticos_para_procesos_de_manufactura_y_sistemas_de_servicio]})
        self.taller_de_metodologia_de_la_investigacion = Curso("Taller de metodología de la investigación", 0.8, {self.industrial: [self.inferencia_estadistica_fundamental, self.taller_de_invencion_y_creatividad]})

        # Materias octavo Semestre
        self.logistica = Curso("Logística", 0.8, {self.industrial: [self.taller_de_simulacion_de_procesos_de_manufactura_y_sistemas_de_servicios]})
        self.gestion_tecnologica = Curso("Gestión tecnológica", 0.8, {self.industrial: [self.sistemas_de_informacion]})
        self.gerencia_de_recursos_humanos = Curso("Gerencia de recursos humanos", 0.8, {self.industrial: [self.seguridad_industrial]})
        self.taller_de_diseno_de_plantas = Curso("Taller de diseño de plantas", 0.8, {self.industrial: [self.taller_de_ingenieria_de_la_produccion, self.sistemas_de_informacion, self.seguridad_industrial]})


        #Toco aqui por que la de industrial cambio esto
        self.modelos_estocasticos_y_simulacion_en_computacion_y_comunicaciones = Curso("Modelos estocásticos y simulación en computación y comunicaciones", 0.80, {self.sistemas: [self.optimizacion]})
        self.arquitectura_de_infraestructura_y_gobierno_de_TICs = Curso("Arquitectura de infraestructura y gobierno de TICs", 0.80, {self.sistemas: [self.sistemas_de_informacion, self.ingenieria_de_software_II]})
        
       
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

        self.materias_industrial = [
                        # Materias primer Semestre
                        self.calculo_diferencial,
                        self.sociologia_especial_industrial_y_del_trabajo,
                        self.introduccion_a_la_ingenieria_industrial,
                        self.programacion_de_computadores,

                        # Materias segundo Semestre
                        self.calculo_integral,
                        self.algebra_lineal,
                        self.taller_de_invencion_y_creatividad,
                        self.programacion_orientada_a_objetos,

                        # Materias tercer Semestre
                        self.calculo_en_varias_variables,
                        self.fundamentos_de_mecanica,
                        self.economia_general,
                        #self.taller_de_herramientas_y_problemas_en_ingenieria_industrial,
                        self.probabilidad_fundamental,

                        # Materias cuarto Semestre
                        self.ecuaciones_diferenciales,
                        self.fundamentos_de_electricidad_y_magnetismo,
                        self.sistema_de_costos,
                        self.gestion_empresarial,
                        self.taller_de_ciencia_y_tecnologia_de_materiales,

                        # Materias quinto Semestre
                        self.modelos_y_simulacion,
                        self.optimizacion,
                        self.ingenieria_economica_y_analisis_de_riesgos,
                        self.taller_de_procesos_quimicos_y_biotecnologicos,
                        self.taller_de_procesos_metalmecanicos,
                        self.inferencia_estadistica_fundamental,

                        # Materias sexto Semestre
                        self.modelos_estocasticos_para_procesos_de_manufactura_y_sistemas_de_servicio,
                        self.gerencia_y_gestion_de_proyectos,
                        self.finanzas,
                        self.taller_de_ergonomia_e_ingenieria_de_metodos,
                        self.control_y_gestion_de_calidad,

                        # Materias séptimo Semestre
                        self.taller_de_simulacion_de_procesos_de_manufactura_y_sistemas_de_servicios,
                        self.sistemas_de_informacion,
                        self.seguridad_industrial,
                        self.taller_de_ingenieria_de_la_produccion,
                        self.taller_de_metodologia_de_la_investigacion,

                        # Materias octavo Semestre
                        self.logistica,
                        self.gestion_tecnologica,
                        self.gerencia_de_recursos_humanos,
                        self.taller_de_diseno_de_plantas
        ]

        self.materias = []

        # Agregar las materias de self.materias_sistemas
        self.materias.extend(self.materias_sistemas)
        # Agregar las materias de self.materias_industrial
        self.materias.extend(self.materias_industrial)

        #materias totales
        self.materias_totales_sistemas = len(self.materias_sistemas)
        self.materias_totales_industrial = len(self.materias_industrial)
    
    def reporteInscripciones(self):
        
        for materia in self.materias:
            print("la materia "+materia.nombre+" recibio "+str(materia.inscritos)+" inscripciones")
            #Reiniciar reportes
            materia.inscritos = 0

        print(self.materias_totales_industrial)
        print(self.materias_totales_sistemas)
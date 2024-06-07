class Persona:
    def __init__(self,nombre,edad):
        self.nombre = nombre
        self.edad = edad

    def presentarse(self):
        print(f"Mi nombre es {self.nombre} y tengo {self.edad} años")    
        
class Estudiante(Persona):
    def __init__(self,nombre,edad,carrera):
        super().__init__(nombre,edad)
        self.carrera = carrera
        
    def estudiar(self):
        print(f"Estoy estudiando {self.carrera}")

estudiante = Estudiante('Jhohan', 24,'Ingenieria')
estudiante.presentarse()
estudiante.estudiar()


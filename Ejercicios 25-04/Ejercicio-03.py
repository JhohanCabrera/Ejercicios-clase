class Persona:
    def __init__(self,nombre,edad):
        self.nombre = nombre
        self.edad = edad

    def presentarse(self):
        print(f"Hola, Mi nombre es {self.nombre} y tengo {self.edad} años")    
        
class Estudiante(Persona):
    def __init__(self,nombre,edad,especialidad):
        super().__init__(nombre,edad)
        self.especialidad = especialidad
        
    def enseñar(self):
        print(f"Estoy enseñando {self.especialidad}")

estudiante = Estudiante('Orlando', 35,'Ciberseguridad')
estudiante.presentarse()
estudiante.enseñar()
class Persona:
    
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        
class Alumno(Persona):
    pass

alumno1 = Alumno('Jhohan',24)
class Persona:
    def __init__(self,nombre,edad):
        self.nombre = nombre
        self.edad = edad

    def presentarse(self):
        print(f"Mi nombre es {self.nombre} y tengo {self.edad} años")    
        
persona = Persona('Jhohan', 24)
persona.presentarse()

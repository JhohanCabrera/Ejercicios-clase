class Auto:
    
    def __init__(self,marca,modelo,año,color):
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.color = color
    
    def encendido(self,estado):
        print(f"El auto se encuentra {estado}")
        
chevrolet = Auto('Chevrolet','ISC202',2014,'verde')
chevrolet.encendido('encendido')
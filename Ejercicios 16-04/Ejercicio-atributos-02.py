class Cubo:
    caras = 6
    
    def __init__(self, color):
        self.color = color
        
cubo_rojo = Cubo('rojo')

print(cubo_rojo.color)
print(f"Mi cubo es de color {cubo_rojo.color}")
class Casa:
    def __init__(self, color, cantidad_pisos):
        self.color = color
        self.cantidad_pisos = cantidad_pisos
        
casa_blanca = Casa('blanco', '4')

print(casa_blanca.color)
print(casa_blanca.cantidad_pisos)
print(f"Mi casa es de color {casa_blanca.color} y tiene {casa_blanca.cantidad_pisos} pisos")
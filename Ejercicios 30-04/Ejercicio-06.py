class Producto:
    
    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad
        
class Venta:
    
    def __init__(self):
        self.productos_vendidos = []
        
        
    def agregar_productos(self, producto):
        self.productos_vendidos.append(producto)    
        
    def calcular_total_venta(self):
        return sum(producto.precio * producto.cantidad for producto in self.productos_vendidos) 
    
venta = Venta()
venta.agregar_productos(Producto("Camisa", 20000, 2))
venta.agregar_productos(Producto("Pantalon", 50000, 1))
print("Total de la venta", venta.calcular_total_venta())  
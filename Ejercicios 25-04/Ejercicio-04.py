class Empleado:
    
    def __init__(self, nombre, puesto, salario):
        self.nombre = nombre
        self.puesto = puesto
        self.salario = salario
        
class Empresa:
    
    def __init__(self):
        self.empleado = []
    
    #Funcion para agregar empleado
    def agregar_empleado(self,empleado):
        self.empleado.append(empleado)
    
    def calcular_salario_total(self):
        
        #Sumar el salario total de todos los empleados en una sola línea
        return sum(empleado.salario for empleado in self.empleado)
        
    def mostrar_informacion_empleado(self): 
        for empleado in self.empleado:
            print(f"Nombre {empleado.nombre}, Puesto:  {empleado.puesto}, Salario: {empleado.salario}")
            
empresa = Empresa()
empresa.agregar_empleado(Empleado("Juan","Desarrollador",3000))
empresa.agregar_empleado(Empleado("Maria","Diseñadora",2500))
print("SALARIO TOTAL DE LA EMPRESA: ", empresa.calcular_salario_total())
empresa.mostrar_informacion_empleado()

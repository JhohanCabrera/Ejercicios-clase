class Banco:
    
    def __init__(self, titular, saldo, metodo):
        self.titular = titular,
        self.saldo = saldo,
        self.metodo = metodo
        
        
class Cuenta:
    
    def __init__(self): 
        self.cuentas = [] 
        
    def agregar_cuenta(self, cuenta):
        self.cuentas.append(cuenta)
        
    def eliminar_cuenta(self, cuenta):
        self.cuentas.remove(cuenta)
        
    def mostrar_cuenta(self):
        for cuenta in self.cuentas:
            print(f"Titular: {cuenta.titular}, Saldo: {cuenta.saldo}, Método: {cuenta.metodo}")
            
cliente1 = Banco("Juan", 1500, "Transferencia")
cliente2 = Banco("Maria", 1400, "Tarjeta")

cuenta1= Cuenta()
cuenta1.agregar_cuenta(cliente1)
cuenta1.agregar_cuenta(cliente2)
#cuenta1.eliminar_cuenta(cliente2)
cuenta1.mostrar_cuenta()
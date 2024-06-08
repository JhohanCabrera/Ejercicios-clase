
class Pelicula:
    
    def __init__(self, titulo, vista=False):
        self.titulo = titulo
        self.vista = vista
    
class ListaPeliculas:
    
    def __init__(self):
        self.peliculas = []
        
    def agregar_pelicula(self, pelicula):
        self.peliculas.append(pelicula)
        
    def marcar_vista(self, indice):
        if 0 <= indice < len(self.peliculas):
            self.peliculas[indice].vista = True
            print("Pelicula marcada como vista")
        else:
            print("El indice de la pelicula no es valido")
            
    def mostrar_peliculas(self):
        print("Lista de peliculas: ")
        for idx, pelicula in enumerate(self.peliculas, start=1):
            if pelicula.vista:
                estado = "Vista"
            else:
                estado = "No vista"    
            print(f"{idx} {pelicula.titulo} {estado}")
            
            
def mostrar_menu():
    print("\n=== Menu ===")
    print("1. Agregar pelicula")
    print("2. Marcar pelicula como vista")
    print("3. Mostrar peliculas")
    print("4. Salir")
    
lista_peliculas = ListaPeliculas()

opcion = ""

while opcion != "4":
    print("\n===Menu===")
    mostrar_menu()
    opcion = input("Seleccione una opcion: ")
    
    if opcion == "1":
        titulo = input("Ingrese el titulo de la pelicula: ")
        pelicula = Pelicula(titulo)  
        lista_peliculas.agregar_pelicula(pelicula)
        print("Pelicula agregada con exito")
    
    elif opcion == "2":
        lista_peliculas.mostrar_peliculas()
        indice = int(input("Selecciona la pelicula a marcar como vista --> "))-1
        lista_peliculas.marcar_vista(indice)
        
    elif opcion == "3":
        lista_peliculas.mostrar_peliculas()
        
    elif opcion == "4":
        print("Saliendo del programa....")
        
    else:
        print("Opcion invalida. Por favor, selecciones una opcion valida")    
        
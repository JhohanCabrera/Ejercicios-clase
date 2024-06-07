#EJEMPLO GUIA
# class Libro:
#     def __init__(self,autor,titulo,cant_paginas):
#         self.autor = autor
#         self.tiulo = titulo
#         self.cant_paginas = cant_paginas
        
#     def __str__(self) -> str:
#         return f'Titulo: "{self.titulo}",escrito por {self.autor}'
    
#     def __len__(self):
#         return self.cant_paginas
    
# libro1 = Libro("Stephen","It",1032)
# print(str(libro1))
# print(len(libro1))

#APUNTES CLASE

class CD:
    
    def __init__(self,autor,titulo,canciones):
        self.autor = autor
        self.titulo = titulo
        self.canciones = canciones
        
    def __str__(self):
        return f"Album: {self.titulo} de {self.autor}"
    
    def __len__(self):
        return self.canciones
    
mi_cd = CD("Pink Floyd","The Wall",24)
print(str(mi_cd))
print(len(mi_cd))
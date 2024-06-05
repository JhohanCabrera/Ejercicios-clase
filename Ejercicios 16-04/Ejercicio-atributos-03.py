class Personaje:
    real = False
    
    def __init__(self, especie, magico, edad):
        self.especie = especie
        self.magico = magico
        self.edad = edad
        
harry_potter = Personaje('Humano', True, '17')
print(harry_potter.especie)
print(harry_potter.magico)
print(harry_potter.edad)
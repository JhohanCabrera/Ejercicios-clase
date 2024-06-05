class Alarma:
    def postergar(self,cantidad_minutos):
        print(f"La alarma ha sido propuesta {cantidad_minutos} minutos")
        
reloj = Alarma()
reloj.postergar(10)
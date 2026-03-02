from Aventurero import Aventurero

class Asesino(Aventurero):
    
    print("\n======================== ASESINO ==================================")
     
    def __init__(self, nombre, nivel, dagas, sigilo):
        super().__init__(nombre, nivel)
        self.dagas = dagas
        self.sigilo = sigilo # Porcentaje o nivel de sigilo
        
    def usar_habilidad(self):
        super().usar_habilidad()
        print(f"{self.nombre} se desvanece en las sombras con sus {self.dagas}.")
        print(f"¡Ataque crítico ejecutado con {self.sigilo}% de sigilo!")
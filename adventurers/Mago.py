from Aventurero import Aventurero

class Mago(Aventurero):
   
    print("\n======================== MAGO ==================================")
    
    def __init__(self, nombre, nivel, hechizo, mana):
        super().__init__(nombre, nivel)
        self.hechizo = hechizo
        self.mana = mana 
    
    def usar_habilidad(self):
        if self.mana >= 10:
            super().usar_habilidad()
            self.mana -= 10
            print(f"{self.nombre} invoca el hechizo {self.hechizo}!")
            print(f"Mana restante: {self.mana}")
        else:
            print(f"¡{self.nombre} no tiene suficiente mana para lanzar {self.hechizo}!")
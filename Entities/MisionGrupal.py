# MisionGrupal

from Misiones import Misiones

class MisionGrupal(Misiones):
    def __init__(self, nombre, rango, recompensa, completado, min_miembros):
        super().__init__(nombre, rango, recompensa, completado, "Grupal")
        self.min_miembros = min_miembros

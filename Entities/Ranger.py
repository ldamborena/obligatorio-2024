# Clase derivada para Ranger
from Entities.Aventurero import Aventurero
from Entities.Mascota import Mascota

class Ranger(Aventurero):

    def __init__(self, nombre, id, puntos_habilidad, experiencia, dinero, mascota=None):
        super().__init__(nombre, id, puntos_habilidad, experiencia, dinero)
        self.mascota = mascota

    def asignar_mascota(self, mascota):
        self.mascota = mascota

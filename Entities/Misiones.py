# Mision.py
from abc import ABC

class Misiones(ABC):
    def __init__(self, nombre, rango, recompensa, completado, tipo_mision):
        self.nombre = nombre
        self.rango = rango
        self.recompensa = recompensa
        self.completado = completado
        self.tipo_mision = tipo_mision
        
    def __eq__(self, other):
        return self.nombre == other.nombre

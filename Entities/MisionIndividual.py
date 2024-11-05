# MisionIndividual.py

from Misiones import Misiones

class MisionIndividual(Misiones):
    def __init__(self, nombre, rango, recompensa, completado=False): #Inicializo la mision con completado en false porque una nueva mision esta sin completar.
        super().__init__(nombre, rango, recompensa, completado, "Individual")

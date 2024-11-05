# Clase derivada para Guerrero, añade característica a guerrero

from Entities.Aventurero import Aventurero

class Guerrero(Aventurero):

    def __init__(self, nombre, id, puntos_habilidad, experiencia, dinero, fuerza):
        super().__init__(nombre, id, puntos_habilidad, experiencia, dinero) #hereda las caracteristicas de de aventurero
        self.fuerza = fuerza #agrega atributo

        # if not (1<=fuerza<=100):
        #     print ("Fuerza mayor a 100")
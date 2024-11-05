# Clase para Mascota

class Mascota:

    def __init__(self, nombre, puntos_habilidad):
        self.nombre = nombre
        self.puntos_habilidad = puntos_habilidad

        # if not (1 <= puntos_habilidad <= 50):
        #     print ("Los puntos de habilidad de la mascota deben estar entre 1 y 50.")
#Clase base para Aventurero: representamos todas las caracteristicas (atributos) de los aventureros

class Aventurero:

    def __init__(self, nombre, id, puntos_habilidad, experiencia, dinero): #Creamos en aventurero
        self.nombre = nombre
        self.id = id
        self.puntos_habilidad = puntos_habilidad
        self.experiencia = experiencia
        self.dinero = dinero
        
        # if not (1<=puntos_habilidad<=1000):
        #     print ("Puntos de habilidad mayores a 1000")
from Entities.Aventurero import Aventurero

class Mago(Aventurero):

    def __init__(self, nombre, id, puntos_habilidad, experiencia, dinero, mana):
        super().__init__(nombre, id, puntos_habilidad, experiencia, dinero) #llamamos al constructor de la clase aventurero
        self.mana = mana #agregamos poder magico


        # if not (1 <= mana <= 1000):
        #     print ("El mana debe estar entre 1 y 1000.")
        
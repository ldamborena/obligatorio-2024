# obligatorio-2024
#Clase base para Aventurero: representamos todas las caracteristicas (atributos) de los aventureros
class Aventurero:
    def __init__(self, nombre, id, puntos_habilidad, experiencia, dinero): #Creamos en aventurero
        if not (1<=puntos_habilidad<=1000):
            print ("Puntos de habilidad mayores a 1000")
        self.nombre = nombre
        self.id = id
        self.puntos_habilidad = puntos_habilidad
        self.experiencia = experiencia
        self.dinero = dinero

# Clase derivada para Guerrero, añade característica a guerrero
class Guerrero(Aventurero):
    def __init__(self, nombre, id, puntos_habilidad, experiencia, dinero, fuerza):
        super().__init__(nombre, id, puntos_habilidad, experiencia, dinero) #hereda las caracteristicas de de aventurero
        self.fuerza = fuerza #agrega atributo
        if not (1<=fuerza<=100):
            print ("Fuerza mayor a 100")
# Clase derivada para Mago
class Mago(Aventurero):
    def __init__(self, nombre, id, puntos_habilidad, experiencia, dinero, mana):
        super().__init__(nombre, id, puntos_habilidad, experiencia, dinero) #llamamos al constructor de la clase aventurero
        self.mana = mana #agregamos poder magico
        if not (1 <= mana <= 1000):
            print ("El mana debe estar entre 1 y 1000.")
        

# Clase para Mascota
class Mascota:
    def __init__(self, nombre, puntos_habilidad):
        self.nombre = nombre
        self.puntos_habilidad = puntos_habilidad
        if not (1 <= puntos_habilidad <= 50):
            print ("Los puntos de habilidad de la mascota deben estar entre 1 y 50.")
        

# Clase derivada para Ranger
class Ranger(Aventurero):
    def __init__(self, nombre, id, puntos_habilidad, experiencia, dinero, mascota=None):
        super().__init__(nombre, id, puntos_habilidad, experiencia, dinero)
        self.mascota = mascota

    def asignar_mascota(self, mascota):
        self.mascota = mascota


guerrero = Guerrero("pepe", 1, 80, 1000, 200.0, 95)
mago = Mago("merlin", 2, 90, 2000, 300.0, 800)
mascota = Mascota("perro", 40)
ranger = Ranger("arturo", 3, 85, 1800, 250.0, mascota)

print(f"Guerrero: {guerrero.nombre}, Fuerza: {guerrero.fuerza}")
print(f"Mago: {mago.nombre}, Mana: {mago.mana}")
print(f"Ranger: {ranger.nombre}, Mascota: {ranger.mascota.nombre if ranger.mascota else 'Ninguna'}")

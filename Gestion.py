from Entities.Guerrero import Guerrero
from Entities.Mago import Mago
from Entities.Ranger import Ranger
from Entities.Mascota import Mascota
from Entities.Misiones import Misiones
from Entities.MisionIndividual import MisionIndividual
from Entities.MisionGrupal import MisionGrupal
from Exceptions.Exceptions import DatosInvalidos, EntidadYaExiste

class Gestion:
    def __init__(self):
        self.aventureros = []
        self.misiones = []

    def registrar_aventurero(self, nombre, id, puntos_habilidad, experiencia, dinero, clase, atributos_adicionales):
        # Validación de datos de aventurero
        if not (1 <= puntos_habilidad <= 100):
            raise DatosInvalidos("Puntos de habilidad deben estar entre 1 y 100.")
            
        # Validación de datos de Guerrero
        if clase == "Guerrero":
            if not (1 <= atributos_adicionales <= 100): # En este caso es fuerza
                raise DatosInvalidos("Fuerza debe estar entre 1 y 100.")
            nuevo_aventurero = Guerrero(nombre, id, puntos_habilidad, experiencia, dinero, atributos_adicionales)
            
        # Validación de datos de Mago
        if clase == "Mago":
            if not (1 <= atributos_adicionales <= 1000): # En este caso es mana
                raise DatosInvalidos("Mana debe estar entre 1 y 1000.")
            nuevo_aventurero = Mago(nombre, id, puntos_habilidad, experiencia, dinero, atributos_adicionales)
            
        # Validación de datos de Ranger
        if clase == "Ranger":
            if atributos_adicionales is None:
        # Si el Ranger no tiene mascota, lo asignamos como tal
                nuevo_aventurero = Ranger(nombre, id, puntos_habilidad, experiencia, dinero)
            elif isinstance(atributos_adicionales, Mascota):
                if not (1 <= atributos_adicionales.puntos_habilidad <= 50):
                    raise DatosInvalidos("Los puntos de habilidad de la mascota deben estar entre 1 y 50.")
                    nuevo_aventurero = Ranger(nombre, id, puntos_habilidad, experiencia, dinero, atributos_adicionales)
                else:
                    raise DatosInvalidos("El atributo adicional debe ser del tipo mascota.")

            
        if nuevo_aventurero in self.aventureros:
            raise EntidadYaExiste("El aventurero ya se encuentra registrado.")
    
        self.aventureros.append(nuevo_aventurero)

    def registrar_mision(self, nombre, rango, recompensa, completado, tipo_mision, min_miembros=None):
        # Validación de datos de mision
        if not (1 <= rango <= 5):
            raise DatosInvalidos("Rango debe estar entre 1 y 5.")
        if not isinstance(completado, bool):
            raise DatosInvalidos("Completado debe ser un T o F.")
        
        # Validación de datos de mision Grupal

        if tipo_mision == "Grupal":
            if min_miembros <= 1:
                raise DatosInvalidos("El número mínimo de miembros debe ser mayor a 1.")
            nueva_mision = MisionGrupal(nombre, rango, recompensa, completado, min_miembros)
        
        if tipo_mision == "Individual":
            nueva_mision = MisionIndividual(nombre, rango, recompensa, completado)

        if nueva_mision in self.misiones:
            raise EntidadYaExiste("La mision ya se encuentra registrada.")
        
        self.misiones.append(nueva_mision)


    def calcular_rango(self, aventurero):
        habilidad_total = 0

        if isinstance(aventurero, Ranger):
            habilidad_total = aventurero.puntos_habilidad
            if aventurero.mascota:
                habilidad_total += aventurero.mascota.puntos_habilidad

        elif isinstance(aventurero, Mago):
            habilidad_total = aventurero.puntos_habilidad + (aventurero.mana /10)

        elif isinstance(aventurero, Guerrero):
            habilidad_total = aventurero.puntos_habilidad + (aventurero.fuerza / 2)

        if habilidad_total <= 20:
            return 1
        elif habilidad_total <= 40:
            return 2
        elif habilidad_total <= 60:
            return 3
        elif habilidad_total <= 80:
            return 4
        else:
            return 5

    def buscar_aventurero_por_id(self, id):
        for aventurero in self.aventureros:
            if aventurero.id == id:
                return aventurero
            return False
    
    def realizar_mision(self, misiones):
        aventureros_registrados = []
        while True:
            id_aventurero = int(input("Ingrese el ID del aventurero: "))
            aventurero = self.buscar_aventurero_por_id(id_aventurero)
            if aventurero:
                rango_aventurero = self.calcular_rango(aventurero)
                if rango_aventurero >= misiones.rango:
                    aventureros_registrados.append(aventurero)
                    print(f"Aventurero {aventurero.nombre} agregado a la misión.")
                else:
                    print(f"El aventurero {aventurero.nombre} no cumple con el rango mínimo de la misión.")
            else:
                print("Aventurero no encontrado.")

            continuar = input("¿Registrar otro aventurero? (S/N):")
            if continuar.upper() != "S":
                break

        if len(aventureros_registrados) == 0:
            print("No hay aventureros registrados")
            return
        
        misiones.completado = True

        recompensa_por_aventurero = misiones.recompensa / len(aventureros_registrados)
        for aventurero in aventureros_registrados:
            aventurero.dinero += recompensa_por_aventurero

        puntos_experiencia = 0
        if misiones.rango == 1:
            puntos_experiencia = 5
        elif misiones.rango == 2:
            puntos_experiencia = 10
        elif misiones.rango == 3:
            puntos_experiencia = 20
        elif misiones.rango == 4:
            puntos_experiencia = 50
        elif misiones.rango == 5:
            puntos_experiencia = 100

        for aventurero in aventureros_registrados:
            aventurero.experiencia += puntos_experiencia

     def top_10_aventureros_misiones(self):
        if not self.aventureros:
            print ("no hay aventureros registrados")
            return
        aventureros_ordenados=sorted(self.aventureros,key=lambda aventurero:(-aventurero.misiones_resueltas, aventurero.nombre))
        print("Top aventureros con mas misiones resueltas:")
        for i, aventurero in enumerate(aventureros_ordenados[:10],start=1):
            print(f"{i}.{aventurero.nombre} - Misiones completadas: {aventurero.misiones_resueltas}")
                    

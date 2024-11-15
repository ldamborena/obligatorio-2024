from Entities.Guerrero import Guerrero
from Entities.Mago import Mago
from Entities.Ranger import Ranger
from Entities.Mascota import Mascota
from Entities.Misiones import Misiones
from Entities.MisionIndividual import MisionIndividual
from Entities.MisionGrupal import MisionGrupal
from Exceptions.Exceptions import DatosInvalidos, EntidadYaExiste

class Gremio:
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
        if clase == "Ranger": # No entiendo que pasa si no tiene Mascota
            if not isinstance(atributos_adicionales, Mascota):
                raise DatosInvalidos("El atributo adicional debe ser del tipo mascota.")
            if not (1 <= atributos_adicionales.puntos_habilidad <= 50):
                raise DatosInvalidos("Los puntos de habilidad de la mascota deben estar entre 1 y 50.")
            nuevo_aventurero = Ranger(nombre, id, puntos_habilidad, experiencia, dinero, atributos_adicionales)

            
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
        
def mostrar_top_aventureros_misiones(self):
    # Ordenar aventureros por misiones resueltas (descendente) y por nombre (ascendente)
    top_aventureros = sorted(self.aventureros, key=lambda a: (-a.misiones_completadas, a.nombre))
    print("\n--- Top 10 Aventureros con Más Misiones Resueltas ---")
    for i, aventurero in enumerate(top_aventureros[:10], start=1):
        print(f"{i}. {aventurero.nombre} - Misiones completadas: {aventurero.misiones_completadas}")

def mostrar_top_aventureros_habilidad(self):
    # Ordenar aventureros por habilidad total (descendente) y por nombre (ascendente)
    top_aventureros = sorted(self.aventureros, key=lambda a: (-a.calcular_habilidad_total(), a.nombre))
    print("\n--- Top 10 Aventureros con Mayor Habilidad ---")
    for i, aventurero in enumerate(top_aventureros[:10], start=1):
        print(f"{i}. {aventurero.nombre} - Habilidad total: {aventurero.calcular_habilidad_total()}")

def mostrar_top_misiones_recompensa(self):
    # Ordenar misiones por recompensa (descendente) y por nombre (ascendente)
    top_misiones = sorted(self.misiones, key=lambda m: (-m.recompensa, m.nombre))
    print("\n--- Top 5 Misiones con Mayor Recompensa ---")
    for i, mision in enumerate(top_misiones[:5], start=1):
        print(f"{i}. {mision.nombre} - Recompensa: {mision.recompensa}")

def mostrar_aventureros_por_tipo(self):
    # Agrupar aventureros por tipo y ordenar por nombre
    print("\n--- Aventureros por Tipo ---")
    tipos = {"Guerrero": [], "Mago": [], "Ranger": []}
    for aventurero in self.aventureros:
        tipos[type(aventurero).__name__].append(aventurero.nombre)
    
    for tipo, nombres in tipos.items():
        print(f"\nTipo: {tipo}")
        for nombre in sorted(nombres):
            print(f"- {nombre}")
        
        

            
    
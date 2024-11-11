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

    def rango_minimo_habilidad(rango):
     #Devuelve el valor mínimo de habilidad total para cada rango
        if rango == 1:
            return 1
        elif rango == 2:
            return 21
        elif rango == 3:
             return 41
        elif rango == 4:
            return 61
        elif rango == 5:
            return 81

    def obtener_experiencia(rango_mision):
    #Asigna experiencia dependiendo del rango de la misión
        if rango_mision == 1:
            return 5
        elif rango_mision == 2:
            return 10
        elif rango_mision == 3:
            return 20
        elif rango_mision == 4:
            return 50
        elif rango_mision == 5:
            return 100

    def realizar_mision(gremio, mision):
    participantes = []
    recompensa_total = mision.recompensa
    rango_mision = mision.rango
    
    # Verificamos si la misión es individual o grupal
    if mision.tipo_mision == "MisionGrupal":
        while True:
            # Pedimos el ID del aventurero
            id_aventurero = int(input("Ingrese el ID del aventurero: "))
            # Buscamos el aventurero por ID
            aventurero = next((a for a in gremio.aventureros if a.id == id_aventurero), None)
            
            if not aventurero:
                print("Aventurero no encontrado. Intente de nuevo.")
                continue
            
            # Validamos el rango del aventurero
            if not validar_rango(aventurero, rango_mision):
                print(f"El aventurero {aventurero.nombre} no cumple con el rango mínimo de la misión.")
            else:
                participantes.append(aventurero)
                print(f"Aventurero {aventurero.nombre} agregado a la misión.")
            
            # Preguntamos si queremos registrar otro aventurero
            otra_opcion = input("¿Registrar otro aventurero? (S/N): ").strip().upper()       
            if otra_opcion == "N":
                break
        
    elif mision.tipo_mision == "MisionIndividual":
        # Para misiones individuales solo se asigna un aventurero
        id_aventurero = int(input("Ingrese el ID del aventurero: "))
        aventurero = next((a for a in gremio.aventureros if a.id == id_aventurero), None)
        
        if not aventurero:
            print("Aventurero no encontrado.")
        elif not validar_rango(aventurero, rango_mision):
            print(f"El aventurero {aventurero.nombre} no cumple con el rango mínimo de la misión.")
        else:
            participantes.append(aventurero)
            print(f"Aventurero {aventurero.nombre} agregado a la misión.")
    
    # Si todos los aventureros cumplen los requisitos, completamos la misión
    if len(participantes) > 0:
        for aventurero in participantes:
            # Repartimos la recompensa entre todos los participantes
            recompensa = recompensa_total / len(participantes)
            aventurero.dinero += recompensa
            print(f"Recompensa de {recompensa} repartida al aventurero {aventurero.nombre}.")
            
            # Asignamos experiencia al aventurero
            experiencia = obtener_experiencia(rango_mision)
            aventurero.experiencia += experiencia
            print(f"{aventurero.nombre} recibe {experiencia} puntos de experiencia.")
        
        # Cambiamos el estado de la misión a completada
        mision.completado = True
        print(f"Misión {mision.nombre} completada con éxito.")
    else:
        print("Ningún aventurero cumple con los requisitos para la misión.")
            
    

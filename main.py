from Gestion import Gestion
from static.menus import options
from Exceptions.optionException import mainMenuException

def action(opcion_a, gremio):
    if opcion_a == "4":
        while True:
            print(options["otherOptions"])
            opcion_b = input("Seleccione una opcion: ")
            if not opcion_b.isdigit() or int(opcion_b) != "4" or int(opcion_b) not in range(1, 6):
                raise mainMenuException("Opción inválida, elija una de las opciones mostradas.")
            elif opcion_b == "5":
                break
            else:
                print("Opcion elegida: ", opcion_b)
    elif opcion_a == "1":
        while True:
            print(options["selectGuerrero"])
            opcion_b = input("Seleccione una opcion: ")
            if not opcion_b.isdigit() or int(opcion_b) not in range(1, 4):
                raise mainMenuException("Opción inválida, elija una de las opciones mostradas.")
            else:
                clase = {"1": "Guerrero","2": "Mago","3": "Ranger"}
                nombre = input("Ingrese el nombre del aventurero: ")
                id = input("Ingrese el id del aventurero: ")
                puntos_habilidad = input("Ingrese los puntos de habilidad del aventurero: ")
                experiencia = input("Ingrese la experiencia del aventurero: ")
                dinero = input("Ingrese el dinero del aventurero: ")
                atributos_adicionales = input("Ingrese los atributos adicionales del aventurero: ")
                gremio.registrar_aventurero(nombre, int(id), int(puntos_habilidad), int(experiencia), int(dinero), clase, atributos_adicionales)
                print("Aventurero registrado con éxito!")
                print(gremio.aventureros)
                break


def main():
    gremio_actual = Gestion()
    while True:
        print(options["main"])
        opcion = input("Seleccione una opcion: ")
        try:
            if not opcion.isdigit() or int(opcion) not in range(1, 6):
                raise mainMenuException("Opción inválida, elija una de las opciones mostradas.")
            elif opcion == "5":
                print(options["end"])
                break
            else:
                action(opcion, gremio_actual)
        except mainMenuException as e:
            print(e.message)
            continue

if __name__  == "__main__":
    main()

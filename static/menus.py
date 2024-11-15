def mostrar_menu_principal():
    print("\nBienvenido al Simulador de Gremio de Aventureros")
    print("1. Registrar Aventurero")
    print("2. Registrar Misión")
    print("3. Realizar Misión")
    print("4. Otras Consultas")
    print("5. Salir")
    
    try:
        opcion = int(input("Seleccione una opción: "))
        return opcion
    except ValueError:
        raise OpcionInvalida("Debe ingresar un número entre 1 y 5.")

def mostrar_menu_consultas(gremio):
    while True:
        print("\n--- Otras Consultas ---")
        print("1. Ver Top 10 Aventureros con Más Misiones Resueltas")
        print("2. Ver Top 10 Aventureros con Mayor Habilidad")
        print("3. Ver Top 5 Misiones con Mayor Recompensa")
        print("4. Ver Aventureros por Tipo")
        print("5. Volver al Menú Principal")
        
        try:
            opcion = int(input("Seleccione una opción: "))
            
            if opcion == 1:
                gremio.mostrar_top_aventureros_misiones()
            elif opcion == 2:
                gremio.mostrar_top_aventureros_habilidad()
            elif opcion == 3:
                gremio.mostrar_top_misiones_recompensa()
            elif opcion == 4:
                gremio.mostrar_aventureros_por_tipo()
            elif opcion == 5:
                break
            else:
                raise OpcionInvalida("Opción no válida. Intente nuevamente.")
        
        except Exception as e:
            print(f"Error: {e}")





options = {
    "main": """
    Bienvenido al Simulador de Gremio de Aventureros!
    Seleccione una opción:
    1. Registrar Aventurero
    2. Registrar Misión
    3. Realizar Misión
    4. Otras Consultas
    5. Salir
    """,
    "end": """
    Hasta la proxima!
    """,
    "otherOptions": """
    1. Ver Top 10 Aventureros con Más Misiones Resueltas
    2. Ver Top 10 Aventureros con Mayor Habilidad
    3. Ver Top 5 Misiones con Mayor Recompensa
    5. Volver al Menú Principal
    """,
    "selectGuerrero": """
    Elija la clase del aventurero:
    1. Guerrero
    2. Mago
    3. Ranger
    """
}
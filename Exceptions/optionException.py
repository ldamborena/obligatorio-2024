class mainMenuException(Exception):
    def __init__(self, message):
        self.message = message
        
class OpcionInvalida(Exception):
    """Excepción lanzada cuando el usuario ingresa una opción no válida en el menú."""
    def __init__(self, mensaje="Opción no válida. Por favor, seleccione una opción correcta."):
        super().__init__(mensaje)
        
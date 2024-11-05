class DatosInvalidos(Exception):
    def __init__(self, descripcion):
        self.descripcion = descripcion
    pass

class EntidadYaExiste(Exception):
    def __init__(self, descripcion):
        self.descripcion = descripcion
    pass


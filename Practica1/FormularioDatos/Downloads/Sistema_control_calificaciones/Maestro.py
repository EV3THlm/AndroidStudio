from Persona import Persona
class Maestro(Persona):
    def __init__(self, nombre, apellido, password, rfc):
        super().__init__(nombre, apellido, password)
        self.rfc = rfc
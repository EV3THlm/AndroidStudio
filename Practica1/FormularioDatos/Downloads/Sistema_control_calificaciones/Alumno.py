from Persona import Persona
class Alumno(Persona):
    def __init__(self, nombre, apellido, password, no_control, calificacion=0):
        super().__init__(nombre, apellido, password)
        self.no_control = no_control
        self.calificacion = calificacion

    def imprimir(self):
        print("\n================================")
        print(f"Nombre: {self.nombre} {self.apellido}"+
              f"\nNumero de control: {self.no_control}"+
              f"\nCalificacion: {self.calificacion}")
        print("================================")

    def cambiar_calificacion(self, nueva_calificacion):
        self.calificacion = nueva_calificacion
        print(f"\nSe actualizo la calificacion del alumno {self.nombre}, su calificacion ahora es: {self.calificacion}")
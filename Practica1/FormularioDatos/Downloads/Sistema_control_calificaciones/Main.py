from Alumno import Alumno
from Maestro import Maestro

def main():

    # Lista provicional de Alumnos
    lista_alumnos = []
    lista_alumnos.append(Alumno("Ebeth", "Mejia Chavez", "Ev3th7863+", 22590434))
    lista_alumnos.append(Alumno("Juan", "Perez Garcia", "Juan1234+", 22670456, 85))
    lista_alumnos.append(Alumno("Maria", "Lopez Ruiz", "Maria9876+", 22670567, 90))
    lista_alumnos.append(Alumno("Carlos", "Hernandez Diaz", "Carlos2468+", 22670678, 88))
    lista_alumnos.append(Alumno("Ana", "Gomez Sanchez", "Ana1357+", 22670789, 92))
    lista_alumnos.append(Alumno("Luis", "Martinez Torres", "Luis8642+", 22670890, 87))
    lista_alumnos.append(Alumno("Sofia", "Ramirez Flores", "Sofia9753+", 22670901, 93))
    lista_alumnos.append(Alumno("Miguel", "Santos Vela", "Miguel1923+", 22671012, 86))
    lista_alumnos.append(Alumno("Laura", "Ortiz Herrera", "Laura4839+", 22671123, 91))
    lista_alumnos.append(Alumno("David", "Mendoza Paredes", "David6071+", 22671234, 89))
    lista_alumnos.append(Alumno("Elena", "Castillo Rios", "Elena5621+", 22671345, 94))


    # Lista provicional de Maestros
    lista_maestros = []
    lista_maestros.append(Maestro("Maria Fernanda", "Mejia Chavez", "FER123", "FERRFC"))
    lista_maestros.append(Maestro("Juan Carlos", "Lopez Martinez", "JCL456", "LOPMTC"))
    lista_maestros.append(Maestro("Ana Isabel", "Ramirez Gutierrez", "AIR789", "RAMGUT"))
    lista_maestros.append(Maestro("Roberto", "Sanchez Diaz", "RSD321", "SNDIAZ"))
    lista_maestros.append(Maestro("Carmen Lucia", "Hernandez Morales", "CLH654", "HRZMOR"))
    lista_maestros.append(Maestro("Luis Fernando", "Gomez Torres", "LFG987", "GOMTOR"))
    lista_maestros.append(Maestro("Sofia Alejandra", "Vega Ruiz", "SAV741", "VEGRUI"))
    lista_maestros.append(Maestro("Ricardo", "Mendoza Perez", "RMP852", "MENPER"))
    lista_maestros.append(Maestro("Patricia", "Ortiz Rodriguez", "POR963", "ORTROD"))
    lista_maestros.append(Maestro("Miguel Angel", "Castro Herrera", "MCH159", "CASHER"))
    lista_maestros.append(Maestro("Daniela", "Montes Pineda", "DMP753", "MONPIN"))

    
    while True:
        print("\n1) Entrar como alumno"+
              "\n2) Entrar como maestro"+
              "\n0) Salir")
        opcion = int (input("Ingresa tu opcion: "))

        if opcion == 1:
            no_control = int (input("Ingresa tu numero de control: "))
            password = str (input("Ingresa tu contraseña: "))

            for i in lista_alumnos:
                if no_control == i.no_control and password == i.password :
                    print(f"\n¡Bienvenido! {i.nombre}. Su calificacino actual es: {i.calificacion}")
                    break
            else:
                print("\n¡Lo siento!, datos no validos...")
        elif opcion == 2:
            rfc = str (input("Ingresa tu rfc: "))
            password = str (input("Ingresa tu contraseña: "))

            for i in lista_maestros:
                if rfc == i.rfc and password == i.password :
                    print(f"\n¡Bienvenido! {i.nombre}.")
                    while True:
                        print("\n1) Ver lista de alumnos"+
                            "\n2) Asignar/Cambiar calificacion a un alumno"+
                            "\n0) Salir")
                        opcion2 = int (input("Ingresa tu opcion: "))
                        if opcion2 == 1:
                            for i in lista_alumnos:
                                i.imprimir();
                        elif opcion2 == 2:
                            no_control = int (input("Ingresa el numero de control del alumno: "))
                            for i in lista_alumnos:
                                if no_control == i.no_control:
                                    calificacion = int (input("Ingresa la nueva calificacion del alumno: "))
                                    i.cambiar_calificacion(calificacion)
                        elif opcion2 == 0:
                            break
                        else:
                            print("\n¡Lo siento!, opcion no valida.... \nCERRANDO.....");
                    break
            else:
                print("\n¡Lo siento!, datos no validos...")
        elif opcion == 0:
            break
        else:
            print("\n¡Lo siento!, opcion no valida, intenta nuevamente")

if __name__ == "__main__":
    main()
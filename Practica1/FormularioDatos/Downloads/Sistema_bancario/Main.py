from Usuario import Usuario
def main():

    # Lista de usuarios
    lista_usuarios = []
    lista_usuarios.append(Usuario("Ebeth", "Mejia Chavez", "MECE010203", "1234", 1000))
    lista_usuarios.append(Usuario("Fany", "Ruiz Chavez", "FRUC010203", "4321", 10000))

    usuario = str (input("Ingresa tu numero de cuenta: "))
    password = str (input("Ingresa tu contraseña: "))

    # Recorrido para validar los datos
    for i in lista_usuarios:
        if usuario == i.no_cuenta and password == i.password:
            print(f"\n¡Bienvenido! {i.nombre}")
            while True:
                print("\n1) Ver saldo disponible: "+
                    "\n2) Depositar"+
                    "\n3) Retirar"+
                    "\n4) Transferir saldo"+
                    "\n0) Salir")
                opcion = int (input("Ingrea tu opcion: "))
                if opcion == 1:
                    print(f"\nSu saldo es: {i.saldo}")
                elif opcion == 2:
                    cantidad = int (input("\nIngrese la cantidad a depositar: "))
                    i.depositar(cantidad)
                elif opcion == 3:
                    cantidad = int (input("\nIngrese la cantidad que desea retirar: "))
                    # Hacemos una validacion para que el usuario no pueda retirar mas dinero del que hay en la cuenta
                    while cantidad > i.saldo:
                        print(f"\n¡Lo siento!, saldo insuficiente. tu saldo actual es {i.saldo}")
                        cantidad = int (input("Ingresa nuevamente una cantidad: "))
                    i.retirar(cantidad)
                elif opcion == 4:
                    usuario_a_transferir = str (input("Ingresa el numero de cuenta: "))
                    # Hacemos una segunda validacion dentro de la lista.
                    for n in lista_usuarios:
                        if usuario_a_transferir == n.no_cuenta:
                            cantidad = int (input("Ingresa la cantidad a depositar: "))
                            # Hacemos una validacion para que el usuario no pueda depositar una cantidad mayor a su saldo actual
                            while cantidad > i.saldo:
                                print(f"¡Lo siento!, saldo insuficiente. tu saldo actual es {i.saldo}")
                                cantidad = int (input("Ingresa nuevamente una cantidad: "))
                            n.depositar(cantidad)
                            i.retirar(cantidad)
                            print("\n¡Transferencia exitosa!"+
                                  f"\nEl usuario {i.nombre} transfirio {cantidad} a : {n.nombre}"+
                                  f"\nSaldo de {i.nombre}: {i.saldo}"+
                                  f"\nSaldo de {n.nombre}: {n.saldo}")
                            break
                    else:
                        print("\n¡Lo siento!, el numero de cuenta no existe")
                elif opcion == 0:
                    break
                else:
                    print("\n¡ERROR! Opcion no valida, intenta nuevamente")
        break # El bucle de validacion de datos (no. cuenta y contraseña se rompe aqui)
                # Para que una ves encuentre al usuario no se repita mas veces
    else:
        print("¡Error!, Datos no validos")
if __name__ == "__main__":
    main()
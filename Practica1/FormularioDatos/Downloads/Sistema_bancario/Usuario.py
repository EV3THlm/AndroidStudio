class Usuario:
    def __init__(self, nombre, apellido, no_cuenta, password, saldo):
        self.nombre = nombre
        self.apellido = apellido
        self.no_cuenta = no_cuenta
        self.password = password
        self.saldo = saldo

    # metodo para imprimir datos PRUEBA
    def imprimir(self):
        print(f"\nNombre del cliente: {self.nombre} {self.apellido}"+
              f"\nSaldo: {self.saldo}")
        
    # Metodo para depositar saldo
    def depositar(self, cantidad):
        self.saldo += cantidad
    
    # Metodo para retirar saldo
    def retirar(self, cantidad):
        self.saldo -= cantidad
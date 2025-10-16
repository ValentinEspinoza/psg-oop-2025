class CuentaBancaria:
    def __init__(self, numero_cuenta, titular, saldo_inicial=0.0):
        self.__numero_cuenta = numero_cuenta   # Privado
        self.__saldo = saldo_inicial           # Privado
        self.__titular = titular               # Privado

    # propiedades
    @property
    def numero_cuenta(self):
        return self.__numero_cuenta

    @property
    def saldo(self):
        return self.__saldo

    @property
    def titular(self):
        return self.__titular

    @titular.setter
    def titular(self, nuevo_titular):
        self.__titular = nuevo_titular

    # metodos
    def depositar(self, monto):
        if monto > 0:
            self.__saldo += monto
            print(f"Deposito de Bs {monto}. Nuevo saldo: Bs {self.__saldo}")
        else:
            print("Monto invalido.")

    def retirar(self, monto):
        if 0 < monto <= self.__saldo:
            self.__saldo -= monto
            print(f"Retiro de Bs {monto}. Saldo restante: Bs {self.__saldo}")
        else:
            print("Fondos insuficientes o monto invalido.")


# implementando la clase
cuenta = CuentaBancaria("1-5555555", "Juan Perez", 5000)
print(f"Cuenta: {cuenta.numero_cuenta}, Titular: {cuenta.titular}, Saldo: Bs {cuenta.saldo}")

cuenta.depositar(200)
cuenta.retirar(500)
cuenta.titular = "Jhon Perez"
print(f"Nuevo titular: {cuenta.titular}")

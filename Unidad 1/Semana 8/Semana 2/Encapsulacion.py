class CuentaBancaria:
    def __init__(self, saldo_inicial=0):
        self.__saldo = saldo_inicial  # Atributo privado

    def depositar(self, cantidad):
        if cantidad > 0:
            self.__saldo += cantidad
            print(f"Depósito exitoso. Saldo actual: {self.__saldo}")
        else:
            print("Cantidad inválida.")

    def obtener_saldo(self):
        return self.__saldo

# Uso
cuenta = CuentaBancaria(100)
cuenta.depositar(50)          # Salida: Depósito exitoso. Saldo actual: 150
print(cuenta.obtener_saldo())  # Salida: 150
# print(cuenta.__saldo)        # Error: Atributo privado (no accesible directamente).
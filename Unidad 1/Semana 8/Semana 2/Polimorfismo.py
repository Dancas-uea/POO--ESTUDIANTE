class Pajaro:
    def volar(self):
        print("El pájaro vuela.")

class Avion:
    def volar(self):
        print("El avión vuela con motor.")

def hacer_volar(objeto):
    objeto.volar()

# Uso
pajaro = Pajaro()
avion = Avion()

hacer_volar(pajaro)  # Salida: El pájaro vuela.
hacer_volar(avion)   # Salida: El avión vuela con motor.
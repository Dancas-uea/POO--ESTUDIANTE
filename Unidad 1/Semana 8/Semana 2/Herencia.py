class Vehiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def descripcion(self):
        return f"{self.marca} {self.modelo}"

class Coche(Vehiculo):
    def __init__(self, marca, modelo, num_puertas):
        super().__init__(marca, modelo)
        self.num_puertas = num_puertas

    def descripcion(self):
        return f"{super().descripcion()}, {self.num_puertas} puertas"

# Uso
mi_coche = Coche("Toyota", "Corolla", 4)
print(mi_coche.descripcion())  # Salida: Toyota Corolla, 4 puertas
class Mascota:
    def __init__(self, nombre, tipo):
        self.nombre = nombre
        self.tipo = tipo
        print(f'Se creó una mascota: {self.nombre} ({self.tipo})')

    def __del__(self):
        """Destructor simple"""
        print(f'La mascota {self.nombre} se ha ido :(')

mi_mascota = Mascota("Firulais", "perro")

class Flor:
    def __init__(self, nombre, color):
        self.nombre = nombre
        self.color = color
        print(f'Ha nacido una {self.nombre} de color {self.color}!')

    def __del__(self):
        print(f'La flor {self.nombre} se ha marchitado...')

mi_flor = Flor("rosa", "rojo")

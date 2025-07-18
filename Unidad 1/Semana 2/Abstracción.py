from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def hacer_sonido(self):
        pass

class Perro(Animal):
    def hacer_sonido(self):
        print("¡Guau guau!")

class Gato(Animal):
    def hacer_sonido(self):
        print("¡Miau!")

# Uso
mi_perro = Perro()
mi_perro.hacer_sonido()  # Salida: ¡Guau guau!

mi_gato = Gato()
mi_gato.hacer_sonido()   # Salida: ¡Miau!
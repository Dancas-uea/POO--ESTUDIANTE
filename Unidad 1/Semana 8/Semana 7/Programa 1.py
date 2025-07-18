class Persona:
    def __init__(self, nombre, edad):
        """Constructor - Se ejecuta al crear el objeto"""
        self.nombre = nombre
        self.edad = edad
        print(f"Se creó una persona: {self.nombre}")

    def __del__(self):
        """Destructor - Se ejecuta al eliminar el objeto"""
        print(f"Se elimina a {self.nombre} de la memoria")

    def presentarse(self):
        """Método normal de la clase"""
        print(f"Hola, soy {self.nombre} y tengo {self.edad} años")


# Creación de objetos (se llama al constructor)
persona1 = Persona("Juan", 25)
persona2 = Persona("María", 30)

# Usamos los objetos
persona1.presentarse()
persona2.presentarse()

# Los destructores se llamarán automáticamente
# cuando el programa termine o los objetos se eliminen
print("Fin del programa")
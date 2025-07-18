# Programa para calcular el promedio semanal de temperaturas usando POO
# Muestra cada día de la semana mientras el usuario ingresa las temperaturas

class SemanaClima:
    """
    Clase principal que representa una semana de registros climáticos.
    - Guarda los días de la semana y sus temperaturas.
    - Permite ingresar datos, calcular el promedio y mostrar resultados.
    """

    def __init__(self):
        """
        Constructor de la clase. Inicializa:
        - Lista de días de la semana (atributo 'dias')
        - Lista vacía para almacenar temperaturas (atributo 'temperaturas')
        """
        self.dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
        self.temperaturas = []


    def ingresar_temperaturas(self):
        """
        Método para ingresar temperaturas día por día.

        //Itera sobre cada día en 'self.dias'//
        - Pide al usuario ingresar una temperatura válida (número).
        - Si el valor no es numérico, muestra error y vuelve a pedirlo.
        - Almacena cada temperatura en 'self.temperaturas'.
        """
        print("\nIngrese las temperaturas para cada día de la semana:")

        # Usamos enumerate para numerar los días (comenzando en 1)
        for i, dia in enumerate(self.dias, 1):
            while True:  # Bucle hasta que se ingrese un valor válido
                try:
                    # Pide la temperatura mostrando el número y nombre del día (ej: "Día 1 (Lunes): ")
                    temp = float(input(f"Día {i} ({dia}): "))
                    self.temperaturas.append(temp)  # Guarda la temperatura
                    break  # Sale del bucle si el dato es válido
                except ValueError:
                    print("¡Error! Por favor ingrese un número válido.")  # Mensaje si no es número


    def calcular_promedio(self):
        """
        Calcula el promedio de temperaturas de la semana.

        - Suma todas las temperaturas.
        - Divide entre la cantidad de días (7).
        - Retorna el resultado.
        """
        return sum(self.temperaturas) / len(self.temperaturas)


    def mostrar_resumen(self):
        """
        Muestra un reporte con:
        - Todas las temperaturas ingresadas por día.
        - El promedio semanal con 2 decimales.
        """
        print("\nResumen semanal de temperaturas:")

        # Recorre días y temperaturas en paralelo con zip()
        for dia, temp in zip(self.dias, self.temperaturas):
            print(f"- {dia}: {temp}°C")  # Muestra cada día con su temperatura

        # Calcula y muestra el promedio
        promedio = self.calcular_promedio()
        print(f"\nEl promedio semanal de temperaturas es: {promedio:.2f}°C")
def main():
    """
    Función principal que ejecuta el programa:
    1. Crea un objeto SemanaClima.
    2. Llama al método para ingresar datos.
    3. Muestra el Resumen final.
    """
    semana = SemanaClima()  # Crea una nueva semana de clima
    semana.ingresar_temperaturas()  # Solicita las temperaturas
    semana.mostrar_resumen()  # Imprime el reporte


# Punto de entrada del programa
if __name__ == "__main__":
    main()  # Ejecuta la función principal
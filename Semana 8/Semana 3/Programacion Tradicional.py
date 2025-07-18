# Programa para calcular el promedio semanal de temperaturas (enfoque tradicional)

def ingresar_temperaturas():
    """
    Función para ingresar las temperaturas de cada día de la semana.
    Retorna una lista con las 7 temperaturas.
    """
    dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
    temperaturas = []

    print("Ingrese las temperaturas para cada día de la semana:")
    for dia in dias:
        while True:
            try:
                temp = float(input(f"{dia}: "))
                temperaturas.append(temp)
                break
            except ValueError:
                print("Por favor ingrese un número válido.")

    return temperaturas

def calcular_promedio(temps):
    """
    Calcula el promedio de temperaturas para la semana.
    Recibe la lista de temperaturas y retorna el promedio.
    """
    return sum(temps) / len(temps)

def mostrar_resultado(promedio):
    """
    Muestra el resultado del promedio de temperaturas.
    """
    print(f"\nEl promedio semanal de temperaturas es: {promedio:.2f}°C")

def main():
    """
    Función principal que orquesta el programa.
    """
    # Ingreso de datos
    temps_semana = ingresar_temperaturas()

    # Cálculo del promedio
    promedio = calcular_promedio(temps_semana)

    # Mostrar resultado
    mostrar_resultado(promedio)

if __name__ == "__main__":
    main()
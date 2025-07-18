"""
CALCULADORA DE ÍNDICE DE MASA CORPORAL (IMC)
---------------------------------------------
Este programa calcula el Índice de Masa Corporal (IMC) basado en el peso y altura ingresados,
y determina la categoría según los estándares de la OMS (Organización Mundial de la Salud).
Incluye validación de datos numéricos positivos.
"""

def calcular_imc(peso_kg: float, altura_m: float) -> float:
    """
    Calcula el IMC usando la fórmula estándar: peso (kg) / altura² (m).
    - peso_kg: debe ser un valor positivo en kilogramos
    - altura_m: debe ser un valor positivo en metros
    Devuelve el IMC redondeado a 2 decimales.
    """
    if peso_kg <= 0 or altura_m <= 0:
        # Validación para valores positivos
        raise ValueError("El peso y altura deben ser valores positivos")
    return round(peso_kg / (altura_m ** 2), 2)

def clasificar_imc(imc: float) -> str:
    """
    Clasifica el IMC en categorías nutricionales según la OMS:
    - Bajo peso: IMC < 18.5
    - Normal: 18.5 ≤ IMC < 25
    - Sobrepeso: 25 ≤ IMC < 30
    - Obesidad: IMC ≥ 30
    """
    if imc < 18.5:
        return "Bajo peso"
    elif 18.5 <= imc < 25:
        return "Peso normal"
    elif 25 <= imc < 30:
        return "Sobrepeso"
    else:
        return "Obesidad"

def main():
    """Función principal que maneja el flujo del programa"""

    # Entrada de datos con manejo de errores
    try:
        # Conversión de input a float (puede lanzar ValueError)
        peso = float(input("Ingrese su peso en kg: "))
        altura = float(input("Ingrese su altura en m: "))

        # Cálculo del IMC
        imc = calcular_imc(peso, altura)

        # Clasificación y resultado
        categoria = clasificar_imc(imc)
        es_obeso = categoria == "Obesidad"

        # Mostrar resultados (sin información de tipos)
        print(f"\nIMC calculado: {imc}")
        print(f"Categoría: {categoria}")
        print(f"¿Es obeso?: {'Sí' if es_obeso else 'No'}")

    except ValueError as e:
        # Manejo de errores para entradas no numéricas o valores inválidos
        print(f"Error: {str(e)}")

# Punto de entrada del programa
if __name__ == "__main__":
    main()
"""
SISTEMA DE GESTIÓN DE INVENTARIOS - INTERFAZ PRINCIPAL
Archivo: main.py
Descripción: Interfaz de usuario en consola para gestionar el inventario
"""

from producto import Producto
from inventario import Inventario


def mostrar_menu():
    """
    Muestra el menú principal del sistema con formato claro y organizado.
    """
    print("\n" + "=" * 50)
    print("       SISTEMA DE GESTIÓN DE INVENTARIOS")
    print("=" * 50)
    print("1. Añadir nuevo producto")
    print("2. Eliminar producto")
    print("3. Actualizar producto")
    print("4. Buscar producto por nombre")
    print("5. Mostrar todos los productos")
    print("6. Ver información del archivo")
    print("7. Salir")
    print("=" * 50)


def main():
    """
    Función principal que ejecuta el sistema de gestión de inventarios.
    Maneja el flujo principal y la interacción con el usuario.
    """
    # Inicializar inventario (carga automáticamente desde archivo)
    try:
        inventario = Inventario()  # Esto crea/carga el archivo automáticamente
        print("Sistema de gestión de inventarios inicializado correctamente!")
    except Exception as e:
        # Manejo de error crítico durante inicialización
        print(f"Error crítico al inicializar el sistema: {e}")
        print("El sistema no puede continuar. Verifique los permisos de archivo.")
        return  # Termina el programa si no puede inicializar

    # Bucle principal del programa
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción (1-7): ").strip()

        # ========== OPCIÓN 1: AÑADIR NUEVO PRODUCTO ==========
        if opcion == "1":
            try:
                print("\n--- Añadir Nuevo Producto ---")
                # Capturar datos del usuario con validación
                id = int(input("Ingrese el ID del producto: "))
                nombre = input("Ingrese el nombre del producto: ").strip()
                cantidad = int(input("Ingrese la cantidad inicial: "))
                precio = float(input("Ingrese el precio unitario: "))

                # Validar que el nombre no esté vacío
                if not nombre:
                    print("Error: El nombre no puede estar vacío.")
                    continue  # Volver al menú

                # Crear y agregar producto
                producto = Producto(id, nombre, cantidad, precio)
                inventario.agregar_producto(producto)

            except ValueError as e:
                print(f"Error: Entrada inválida. {e}")
            except Exception as e:
                print(f"Error inesperado: {e}")

        # ========== OPCIÓN 2: ELIMINAR PRODUCTO ==========
        elif opcion == "2":
            try:
                print("\n--- Eliminar Producto ---")
                id = int(input("Ingrese el ID del producto a eliminar: "))
                inventario.eliminar_producto(id)
            except ValueError:
                print("Error: El ID debe ser un número entero")
            except Exception as e:
                print(f"Error inesperado: {e}")

        # ========== OPCIÓN 3: ACTUALIZAR PRODUCTO ==========
        elif opcion == "3":
            try:
                print("\n--- Actualizar Producto ---")
                id = int(input("Ingrese el ID del producto a actualizar: "))
                print("Deje en blanco los campos que no desea modificar")

                # Capturar datos opcionales
                nombre = input("Nuevo nombre: ").strip()
                nombre = None if nombre == "" else nombre

                cantidad_str = input("Nueva cantidad: ").strip()
                cantidad = None if cantidad_str == "" else int(cantidad_str)

                precio_str = input("Nuevo precio: ").strip()
                precio = None if precio_str == "" else float(precio_str)

                # Intentar actualización
                inventario.actualizar_producto(id, nombre, cantidad, precio)

            except ValueError as e:
                print(f"Error: {e}. Por favor ingrese valores válidos.")
            except Exception as e:
                print(f"Error inesperado: {e}")

        # ========== OPCIÓN 4: BUSCAR POR NOMBRE ==========
        elif opcion == "4":
            try:
                print("\n--- Buscar Producto por Nombre ---")
                nombre = input("Ingrese el nombre o parte del nombre a buscar: ").strip()

                # Validar entrada
                if not nombre:
                    print("Error: Debe ingresar un término de búsqueda.")
                    continue

                # Realizar búsqueda y mostrar resultados
                productos = inventario.buscar_por_nombre(nombre)

                if productos:
                    print(f"\nSe encontraron {len(productos)} producto(s):")
                    for i, p in enumerate(productos, 1):
                        print(f"{i}. {p}")
                else:
                    print("No se encontraron productos con ese nombre")

            except Exception as e:
                print(f"Error inesperado: {e}")

        # ========== OPCIÓN 5: MOSTRAR INVENTARIO COMPLETO ==========
        elif opcion == "5":
            try:
                print("\n--- Inventario Completo ---")
                productos = inventario.mostrar_inventario()

                if productos:
                    for i, p in enumerate(productos, 1):
                        print(f"{i}. {p}")
                    print(f"\nTotal de productos: {len(productos)}")
                else:
                    print("El inventario está vacío")

            except Exception as e:
                print(f"Error inesperado: {e}")

        # ========== OPCIÓN 6: INFORMACIÓN DEL ARCHIVO ==========
        elif opcion == "6":
            try:
                print("\n--- Información del Archivo ---")
                print(f"Archivo de almacenamiento: inventario.txt")
                print(f"Productos en memoria: {len(inventario)}")
                # Podría expandirse con más información del archivo

            except Exception as e:
                print(f"Error inesperado: {e}")

        # ========== OPCIÓN 7: SALIR ==========
        elif opcion == "7":
            print("\nGracias por usar el Sistema de Gestión de Inventarios!")
            print("Saliendo del programa...")
            break  # Termina el bucle y finaliza el programa

        # ========== OPCIÓN INVÁLIDA ==========
        else:
            print("Opción no válida. Por favor seleccione una opción del 1 al 7")

        # Pausa para que el usuario pueda ver los resultados
        input("\nPresione Enter para continuar...")


# Punto de entrada del programa
if __name__ == "__main__":
    main()
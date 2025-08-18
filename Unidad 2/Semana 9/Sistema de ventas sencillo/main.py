from producto import Producto
from inventario import Inventario


def mostrar_menu():
    """Muestra el menú principal del sistema"""
    print("\n--- Sistema de Gestión de Inventarios ---")
    print("1. Añadir nuevo producto")
    print("2. Eliminar producto")
    print("3. Actualizar producto")
    print("4. Buscar producto por nombre")
    print("5. Mostrar todos los productos")
    print("6. Salir")


def main():
    inventario = Inventario()

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":  # Añadir nuevo producto
            try:
                id = int(input("Ingrese el ID del producto: "))
                nombre = input("Ingrese el nombre del producto: ")
                cantidad = int(input("Ingrese la cantidad inicial: "))
                precio = float(input("Ingrese el precio unitario: "))

                producto = Producto(id, nombre, cantidad, precio)
                if inventario.agregar_producto(producto):
                    print("Producto agregado exitosamente!")
                else:
                    print("Error: Ya existe un producto con ese ID")
            except ValueError as e:
                print(f"Error: {e}. Por favor ingrese valores válidos.")

        elif opcion == "2":  # Eliminar producto
            try:
                id = int(input("Ingrese el ID del producto a eliminar: "))
                if inventario.eliminar_producto(id):
                    print("Producto eliminado exitosamente!")
                else:
                    print("Error: No se encontró un producto con ese ID")
            except ValueError:
                print("Error: El ID debe ser un número entero")

        elif opcion == "3":  # Actualizar producto
            try:
                id = int(input("Ingrese el ID del producto a actualizar: "))
                print("Deje en blanco los campos que no desea modificar")

                nombre = input("Nuevo nombre: ")
                nombre = None if nombre == "" else nombre

                cantidad_str = input("Nueva cantidad: ")
                cantidad = None if cantidad_str == "" else int(cantidad_str)

                precio_str = input("Nuevo precio: ")
                precio = None if precio_str == "" else float(precio_str)

                if inventario.actualizar_producto(id, nombre, cantidad, precio):
                    print("Producto actualizado exitosamente!")
                else:
                    print("Error: No se encontró un producto con ese ID")
            except ValueError as e:
                print(f"Error: {e}. Por favor ingrese valores válidos.")

        elif opcion == "4":  # Buscar por nombre
            nombre = input("Ingrese el nombre o parte del nombre a buscar: ")
            productos = inventario.buscar_por_nombre(nombre)

            if productos:
                print("\nProductos encontrados:")
                for p in productos:
                    print(p)
            else:
                print("No se encontraron productos con ese nombre")

        elif opcion == "5":  # Mostrar todos los productos
            productos = inventario.mostrar_inventario()

            if productos:
                print("\n--- Inventario completo ---")
                for p in productos:
                    print(p)
                print(f"Total de productos: {len(productos)}")
            else:
                print("El inventario está vacío")

        elif opcion == "6":  # Salir
            print("Saliendo del sistema...")
            break

        else:
            print("Opción no válida. Por favor seleccione una opción del 1 al 6")


if __name__ == "__main__":
    main()
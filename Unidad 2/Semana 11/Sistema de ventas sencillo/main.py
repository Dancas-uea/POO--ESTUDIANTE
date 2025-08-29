"""
SISTEMA DE GESTIÓN DE INVENTARIOS - INTERFAZ PRINCIPAL
Este archivo contiene la interfaz de usuario en consola para el sistema de inventarios.
"""

from producto import Producto
from inventario import Inventario


class SistemaInventario:
    """
    Clase que gestiona la interfaz de usuario y el flujo del programa.
    Separa la lógica de presentación de la lógica de negocio.
    """

    def __init__(self):
        """Inicializa el sistema con una instancia de Inventario"""
        self.inventario = Inventario()  # Carga automáticamente desde archivo

    def mostrar_menu(self):
        """Muestra el menú principal del sistema"""
        print("\n" + "=" * 50)
        print("       SISTEMA DE GESTIÓN DE INVENTARIOS")
        print("=" * 50)
        print("1. 📦 Añadir nuevo producto")
        print("2. 🗑️  Eliminar producto")
        print("3. ✏️  Actualizar producto")
        print("4. 🔍 Buscar producto por nombre")
        print("5. 📋 Mostrar todos los productos")
        print("6. ❌ Salir")
        print("=" * 50)

    def limpiar_pantalla(self):
        """Limpia la pantalla de la consola para mejor legibilidad"""
        print("\n" * 3)  # Imprime 3 líneas en blanco

    def esperar_enter(self):
        """Pausa la ejecución esperando que el usuario presione Enter"""
        input("\n↵ Presione Enter para continuar...")

    def validar_entero(self, mensaje: str) -> int:
        """
        Valida que la entrada sea un número entero válido.

        Args:
            mensaje (str): Mensaje a mostrar al usuario

        Returns:
            int: Número entero validado
        """
        while True:
            try:
                return int(input(mensaje))
            except ValueError:
                print("❌ Error: Debe ingresar un número entero válido")

    def validar_decimal(self, mensaje: str) -> float:
        """
        Valida que la entrada sea un número decimal válido.

        Args:
            mensaje (str): Mensaje a mostrar al usuario

        Returns:
            float: Número decimal validado
        """
        while True:
            try:
                return float(input(mensaje))
            except ValueError:
                print("❌ Error: Debe ingresar un número decimal válido")

    def validar_nombre(self, mensaje: str) -> str:
        """
        Valida que el nombre no esté vacío.

        Args:
            mensaje (str): Mensaje a mostrar al usuario

        Returns:
            str: Nombre validado (sin espacios extras)
        """
        while True:
            nombre = input(mensaje).strip()
            if nombre:
                return nombre
            print("❌ Error: El nombre no puede estar vacío")

    def agregar_producto(self):
        """Maneja la interfaz para agregar un nuevo producto"""
        print("\n--- 📦 AÑADIR NUEVO PRODUCTO ---")

        try:
            # Validar que el ID sea único
            while True:
                id = self.validar_entero("ID del producto: ")
                if not self.inventario.existe_id(id):
                    break
                print(f"❌ Ya existe producto con ID {id}. Use otro ID.")

            # Obtener y validar los demás datos
            nombre = self.validar_nombre("Nombre del producto: ")
            cantidad = self.validar_entero("Cantidad inicial: ")
            precio = self.validar_decimal("Precio unitario: $")

            # Crear y agregar el producto
            producto = Producto(id, nombre, cantidad, precio)

            if self.inventario.agregar_producto(producto):
                print(f"✅ Producto '{nombre}' agregado exitosamente!")

        except ValueError as e:
            print(f"❌ Error de validación: {e}")
        except Exception as e:
            print(f"❌ Error inesperado: {e}")

    def eliminar_producto(self):
        """Maneja la interfaz para eliminar un producto"""
        print("\n--- 🗑️ ELIMINAR PRODUCTO ---")

        id = self.validar_entero("ID del producto a eliminar: ")

        # Obtener el producto para mostrar información
        producto = self.inventario.obtener_por_id(id)

        if producto:
            print(f"Producto a eliminar: {producto}")

            # Confirmación de eliminación
            confirmar = input("¿Está seguro? (s/n): ").lower()

            if confirmar == 's':
                self.inventario.eliminar_producto(id)
            else:
                print("❌ Eliminación cancelada")
        else:
            print(f"❌ No existe producto con ID {id}")

    def actualizar_producto(self):
        """Maneja la interfaz para actualizar un producto"""
        print("\n--- ✏️ ACTUALIZAR PRODUCTO ---")

        id = self.validar_entero("ID del producto a actualizar: ")

        # Verificar que el producto exista
        if not self.inventario.existe_id(id):
            print(f"❌ No existe producto con ID {id}")
            return

        producto = self.inventario.obtener_por_id(id)
        print(f"Producto actual: {producto}")
        print("\nDeje en blanco los campos que no desea modificar:")

        try:
            cambios = {}  # Diccionario para almacenar los cambios

            # Obtener nuevos valores (opcionales)
            nombre = input("Nuevo nombre: ").strip()
            if nombre:
                cambios['nombre'] = nombre

            cantidad_str = input("Nueva cantidad: ").strip()
            if cantidad_str:
                cambios['cantidad'] = int(cantidad_str)

            precio_str = input("Nuevo precio: $").strip()
            if precio_str:
                cambios['precio'] = float(precio_str)

            # Aplicar cambios si hay alguno
            if cambios:
                if self.inventario.actualizar_producto(id, **cambios):
                    print("✅ Producto actualizado exitosamente!")
            else:
                print("ℹ️  No se realizaron cambios")

        except ValueError as e:
            print(f"❌ Error: {e}")
        except Exception as e:
            print(f"❌ Error inesperado: {e}")

    def buscar_producto(self):
        """Maneja la interfaz para buscar productos por nombre"""
        print("\n--- 🔍 BUSCAR PRODUCTO ---")

        termino = input("Ingrese nombre o parte del nombre: ").strip()

        if not termino:
            print("❌ Debe ingresar un término de búsqueda")
            return

        # Realizar búsqueda
        resultados = self.inventario.buscar_por_nombre(termino)

        if resultados:
            print(f"\n✅ Se encontraron {len(resultados)} producto(s):")
            for i, producto in enumerate(resultados, 1):
                print(f"{i}. {producto}")
        else:
            print("❌ No se encontraron productos")

    def mostrar_todos(self):
        """Muestra todos los productos del inventario"""
        print("\n--- 📋 INVENTARIO COMPLETO ---")

        productos = self.inventario.obtener_todos()

        if productos:
            for i, producto in enumerate(productos, 1):
                print(f"{i}. {producto}")

            # Mostrar estadísticas básicas
            total_productos = len(productos)
            total_valor = sum(p.cantidad * p.precio for p in productos)
            print(f"\n📊 Total: {total_productos} productos | Valor total: ${total_valor:,.2f}")
        else:
            print("ℹ️  El inventario está vacío")

    def ejecutar(self):
        """Método principal que ejecuta el sistema"""
        print("🚀 Iniciando Sistema de Gestión de Inventarios...")

        while True:
            self.limpiar_pantalla()
            self.mostrar_menu()

            opcion = input("Seleccione una opción (1-6): ").strip()

            if opcion == "1":
                self.agregar_producto()
            elif opcion == "2":
                self.eliminar_producto()
            elif opcion == "3":
                self.actualizar_producto()
            elif opcion == "4":
                self.buscar_producto()
            elif opcion == "5":
                self.mostrar_todos()
            elif opcion == "6":
                print("\n👋 ¡Gracias por usar el sistema!")
                print("Saliendo del programa...")
                break
            else:
                print("❌ Opción no válida. Intente nuevamente.")

            self.esperar_enter()


# Punto de entrada del programa
if __name__ == "__main__":
    # Crear instancia del sistema y ejecutarlo
    sistema = SistemaInventario()
    sistema.ejecutar()
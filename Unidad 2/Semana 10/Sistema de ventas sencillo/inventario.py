"""
SISTEMA DE GESTIÓN DE INVENTARIOS - CLASE INVENTARIO
Archivo: inventario.py
Descripción: Gestiona el inventario con persistencia en archivo y manejo de excepciones
"""

from producto import Producto
import json  # Para trabajar con archivos JSON
import os  # Para operaciones del sistema de archivos


class Inventario:
    """
    Clase principal que gestiona el inventario de productos.
    Incluye persistencia automática en archivo y robusto manejo de excepciones.
    """

    def __init__(self, archivo: str = "inventario.txt"):
        """
        Constructor de la clase Inventario.
        Inicializa el inventario y carga automáticamente los datos desde archivo.

        Args:
            archivo (str, optional): Ruta del archivo de almacenamiento. Default: "inventario.txt"
        """
        self._productos = []  # Lista interna de productos
        self._archivo = archivo  # Ruta del archivo de almacenamiento
        self._cargar_desde_archivo()  # Carga automática al inicializar

    def _cargar_desde_archivo(self):
        """
        Método privado para cargar productos desde el archivo de almacenamiento.
        Maneja múltiples excepciones para robustez del sistema.
        """
        try:
            # Verificar si el archivo existe
            if not os.path.exists(self._archivo):
                # Si no existe, crear archivo vacío
                with open(self._archivo, 'w') as f:
                    json.dump([], f)  # Escribe lista vacía en JSON
                print(f"Archivo {self._archivo} creado exitosamente.")
                return

            # Leer y cargar datos del archivo existente
            with open(self._archivo, 'r') as f:
                datos = json.load(f)  # Carga datos JSON desde archivo

            # Reconstruir la lista de productos desde los datos
            self._productos = [Producto.from_dict(producto_data) for producto_data in datos]
            print(f"Inventario cargado desde {self._archivo} con {len(self._productos)} productos.")

        except FileNotFoundError:
            # Maneja caso cuando el archivo no existe (aunque ya verificamos)
            print(f"Error: El archivo {self._archivo} no fue encontrado.")
        except PermissionError:
            # Maneja falta de permisos para leer el archivo
            print(f"Error: No tienes permisos para leer el archivo {self._archivo}.")
        except json.JSONDecodeError:
            # Maneja archivos corruptos o con formato incorrecto
            print(f"Error: El archivo {self._archivo} está corrupto o tiene formato incorrecto.")
        except Exception as e:
            # Maneja cualquier otro error inesperado
            print(f"Error inesperado al cargar el inventario: {e}")

    def _guardar_en_archivo(self) -> bool:
        """
        Método privado para guardar productos en el archivo de almacenamiento.

        Returns:
            bool: True si se guardó correctamente, False si hubo error
        """
        try:
            # Convertir todos los productos a diccionarios para serialización
            datos = [producto.to_dict() for producto in self._productos]

            # Guardar en archivo con formato JSON legible
            with open(self._archivo, 'w') as f:
                json.dump(datos, f, indent=4)  # indent=4 para formato legible

            return True  # Indica éxito en la operación

        except PermissionError:
            # Maneja falta de permisos para escribir
            print(f"Error: No tienes permisos para escribir en el archivo {self._archivo}.")
            return False
        except Exception as e:
            # Maneja cualquier otro error inesperado
            print(f"Error inesperado al guardar el inventario: {e}")
            return False

    def agregar_producto(self, producto: Producto) -> bool:
        """
        Agrega un nuevo producto al inventario y guarda automáticamente en archivo.

        Args:
            producto (Producto): Producto a agregar

        Returns:
            bool: True si se agregó y guardó correctamente, False si hubo error
        """
        # Verificar que no exista producto con el mismo ID
        if self._buscar_por_id(producto.id) is None:
            self._productos.append(producto)  # Agregar a memoria

            # Intentar guardar en archivo
            if self._guardar_en_archivo():
                print("Producto agregado y guardado exitosamente!")
                return True
            else:
                # REVERSIÓN: Si falla el guardado, quitar de memoria
                self._productos.remove(producto)
                print("Error: El producto se agregó pero no se pudo guardar en el archivo.")
                return False
        else:
            print("Error: Ya existe un producto con ese ID")
            return False

    def eliminar_producto(self, id: int) -> bool:
        """
        Elimina un producto del inventario por su ID y guarda automáticamente en archivo.

        Args:
            id (int): ID del producto a eliminar

        Returns:
            bool: True si se eliminó y guardó correctamente, False si hubo error
        """
        producto = self._buscar_por_id(id)
        if producto:
            self._productos.remove(producto)  # Eliminar de memoria

            # Intentar guardar en archivo
            if self._guardar_en_archivo():
                print("Producto eliminado y guardado exitosamente!")
                return True
            else:
                # REVERSIÓN: Si falla el guardado, restaurar en memoria
                self._productos.append(producto)
                print("Error: El producto se eliminó pero no se pudo guardar en el archivo.")
                return False
        else:
            print("Error: No se encontró un producto con ese ID")
            return False

    def actualizar_producto(self, id: int, nombre: str = None, cantidad: int = None, precio: float = None) -> bool:
        """
        Actualiza los atributos de un producto y guarda automáticamente en archivo.

        Args:
            id (int): ID del producto a actualizar
            nombre (str, optional): Nuevo nombre. Default: None (no cambiar)
            cantidad (int, optional): Nueva cantidad. Default: None (no cambiar)
            precio (float, optional): Nuevo precio. Default: None (no cambiar)

        Returns:
            bool: True si se actualizó y guardó correctamente, False si hubo error
        """
        producto = self._buscar_por_id(id)
        if producto:
            # Guardar valores originales para posible reversión
            nombre_original = producto.nombre
            cantidad_original = producto.cantidad
            precio_original = producto.precio

            try:
                # Aplicar cambios solo a los campos proporcionados
                if nombre is not None:
                    producto.nombre = nombre
                if cantidad is not None:
                    producto.cantidad = cantidad
                if precio is not None:
                    producto.precio = precio

                # Intentar guardar en archivo
                if self._guardar_en_archivo():
                    print("Producto actualizado y guardado exitosamente!")
                    return True
                else:
                    # REVERSIÓN: Si falla el guardado, restaurar valores originales
                    producto.nombre = nombre_original
                    producto.cantidad = cantidad_original
                    producto.precio = precio_original
                    print("Error: El producto se actualizó pero no se pudo guardar en el archivo.")
                    return False

            except ValueError as e:
                # Maneja errores de validación (cantidad/precio negativo)
                print(f"Error: {e}")
                return False
        else:
            print("Error: No se encontró un producto con ese ID")
            return False

    def buscar_por_nombre(self, nombre: str) -> list:
        """
        Busca productos por nombre (coincidencias parciales, insensible a mayúsculas).

        Args:
            nombre (str): Nombre o parte del nombre a buscar

        Returns:
            list: Lista de productos que coinciden con el criterio de búsqueda
        """
        nombre_lower = nombre.lower()  # Convertir a minúsculas para búsqueda insensible
        return [p for p in self._productos if nombre_lower in p.nombre.lower()]

    def mostrar_inventario(self) -> list:
        """
        Devuelve todos los productos del inventario.

        Returns:
            list: Copia de la lista con todos los productos
        """
        return self._productos.copy()  # Devolver copia para evitar modificación externa

    def _buscar_por_id(self, id: int) -> Producto:
        """
        Método interno para buscar un producto por su ID.

        Args:
            id (int): ID del producto a buscar

        Returns:
            Producto: El producto encontrado o None si no existe
        """
        for producto in self._productos:
            if producto.id == id:
                return producto
        return None  # Retorna None si no encuentra el producto

    def __len__(self) -> int:
        """
        Método especial para obtener la cantidad de productos en el inventario.

        Returns:
            int: Número de productos en el inventario
        """
        return len(self._productos)
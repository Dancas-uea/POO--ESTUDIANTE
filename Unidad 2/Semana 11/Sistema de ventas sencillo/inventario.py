"""
SISTEMA DE GESTIÓN DE INVENTARIOS - CLASE INVENTARIO
Este archivo contiene la clase Inventario que gestiona los productos con persistencia en archivo.
Utiliza un diccionario para acceso rápido a los productos por ID.
"""

from producto import Producto
import json  # Para trabajar con archivos JSON
import os  # Para operaciones del sistema de archivos


class Inventario:
    """
    Clase que gestiona el inventario de productos.
    Utiliza un diccionario para acceso rápido por ID y maneja persistencia en archivo JSON.
    """

    def __init__(self, archivo: str = "inventario.json"):
        """
        Constructor de la clase Inventario.

        Args:
            archivo (str, optional): Ruta del archivo de almacenamiento. Default: "inventario.json"
        """
        self._productos = {}  # Diccionario para acceso rápido por ID: {id: Producto}
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
                print(f"📁 Archivo {self._archivo} creado exitosamente.")
                return

            # Leer y cargar datos del archivo existente
            with open(self._archivo, 'r') as f:
                datos = json.load(f)  # Carga datos JSON desde archivo

            # Reconstruir el diccionario de productos desde los datos
            # Usa dictionary comprehension para eficiencia
            self._productos = {
                producto_data['id']: Producto.from_dict(producto_data)
                for producto_data in datos
            }

            print(f"✅ Inventario cargado: {len(self._productos)} productos")

        except FileNotFoundError:
            print(f"❌ Error: Archivo {self._archivo} no encontrado")
        except PermissionError:
            print(f"❌ Error: Sin permisos para leer {self._archivo}")
        except json.JSONDecodeError:
            print(f"❌ Error: Archivo {self._archivo} corrupto o con formato inválido")
        except Exception as e:
            print(f"❌ Error inesperado al cargar: {e}")

    def _guardar_en_archivo(self) -> bool:
        """
        Método privado para guardar productos en el archivo de almacenamiento.

        Returns:
            bool: True si se guardó correctamente, False si hubo error
        """
        try:
            # Convertir todos los productos a diccionarios para serialización
            datos = [producto.to_dict() for producto in self._productos.values()]

            # Guardar en archivo con formato JSON legible
            with open(self._archivo, 'w') as f:
                json.dump(datos, f, indent=2)  # indent=2 para formato legible

            return True  # Indica éxito en la operación

        except PermissionError:
            print(f"❌ Error: Sin permisos para escribir en {self._archivo}")
            return False
        except Exception as e:
            print(f"❌ Error inesperado al guardar: {e}")
            return False

    # ========== OPERACIONES CRUD ==========

    def agregar_producto(self, producto: Producto) -> bool:
        """
        Agrega un nuevo producto al inventario.

        Args:
            producto (Producto): Producto a agregar

        Returns:
            bool: True si se agregó correctamente, False si hubo error
        """
        # Verificar que no exista producto con el mismo ID
        if producto.id in self._productos:
            print(f"❌ Error: Ya existe producto con ID {producto.id}")
            return False

        # Agregar producto al diccionario
        self._productos[producto.id] = producto

        # Intentar guardar en archivo
        if self._guardar_en_archivo():
            print(f"✅ Producto '{producto.nombre}' agregado exitosamente!")
            return True
        else:
            # REVERSIÓN: Si falla el guardado, eliminar del diccionario
            del self._productos[producto.id]
            print("❌ Error: No se pudo guardar en archivo")
            return False

    def eliminar_producto(self, id: int) -> bool:
        """
        Elimina un producto del inventario por su ID.

        Args:
            id (int): ID del producto a eliminar

        Returns:
            bool: True si se eliminó correctamente, False si hubo error
        """
        # Verificar que el producto exista
        if id not in self._productos:
            print(f"❌ Error: No existe producto con ID {id}")
            return False

        # Guardar referencia al producto para mensaje de confirmación
        producto = self._productos[id]

        # Eliminar producto del diccionario
        del self._productos[id]

        # Intentar guardar en archivo
        if self._guardar_en_archivo():
            print(f"✅ Producto '{producto.nombre}' eliminado exitosamente!")
            return True
        else:
            # REVERSIÓN: Si falla el guardado, restaurar el producto
            self._productos[id] = producto
            print("❌ Error: No se pudo guardar en archivo")
            return False

    def actualizar_producto(self, id: int, **kwargs) -> bool:
        """
        Actualiza los atributos de un producto existente.

        Args:
            id (int): ID del producto a actualizar
            **kwargs: Atributos a actualizar (nombre, cantidad, precio)

        Returns:
            bool: True si se actualizó correctamente, False si hubo error
        """
        # Verificar que el producto exista
        if id not in self._productos:
            print(f"❌ Error: No existe producto con ID {id}")
            return False

        producto = self._productos[id]

        # Guardar valores originales para posible reversión
        originales = {
            'nombre': producto.nombre,
            'cantidad': producto.cantidad,
            'precio': producto.precio
        }

        try:
            # Aplicar cambios solo a los campos proporcionados
            for attr, valor in kwargs.items():
                if valor is not None:
                    setattr(producto, attr, valor)

            # Intentar guardar en archivo
            if self._guardar_en_archivo():
                print(f"✅ Producto '{producto.nombre}' actualizado exitosamente!")
                return True
            else:
                # REVERSIÓN: Si falla el guardado, restaurar valores originales
                for attr, valor in originales.items():
                    setattr(producto, attr, valor)
                print("❌ Error: No se pudo guardar en archivo")
                return False

        except ValueError as e:
            # Manejar errores de validación
            print(f"❌ Error de validación: {e}")
            # Revertir cambios
            for attr, valor in originales.items():
                setattr(producto, attr, valor)
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

        # Usar list comprehension para búsqueda eficiente
        return [
            producto for producto in self._productos.values()
            if nombre_lower in producto.nombre.lower()
        ]

    def obtener_por_id(self, id: int) -> Producto:
        """
        Obtiene un producto por su ID.

        Args:
            id (int): ID del producto a obtener

        Returns:
            Producto: El producto encontrado o None si no existe
        """
        return self._productos.get(id)  # Retorna None si no existe

    def obtener_todos(self) -> list:
        """
        Obtiene todos los productos del inventario ordenados por ID.

        Returns:
            list: Lista de todos los productos ordenados por ID
        """
        # Ordenar productos por ID para consistencia en la visualización
        return sorted(self._productos.values(), key=lambda p: p.id)

    def existe_id(self, id: int) -> bool:
        """
        Verifica si existe un producto con el ID especificado.

        Args:
            id (int): ID a verificar

        Returns:
            bool: True si existe, False si no existe
        """
        return id in self._productos

    def __len__(self) -> int:
        """
        Devuelve la cantidad de productos en el inventario.

        Returns:
            int: Número de productos en el inventario
        """
        return len(self._productos)
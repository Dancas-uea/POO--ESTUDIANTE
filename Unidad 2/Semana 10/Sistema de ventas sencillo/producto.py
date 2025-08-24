"""
SISTEMA DE GESTIÓN DE INVENTARIOS - CLASE PRODUCTO
Archivo: producto.py
Descripción: Define la clase Producto con todos sus atributos y métodos
"""


class Producto:
    """
    Clase que representa un producto en el inventario.
    Cada producto tiene un ID único, nombre, cantidad disponible y precio.
    """

    def __init__(self, id: int, nombre: str, cantidad: int, precio: float):
        """
        Constructor de la clase Producto.
        Inicializa un nuevo producto con los atributos proporcionados.

        Args:
            id (int): Identificador único del producto (no se puede repetir)
            nombre (str): Nombre descriptivo del producto
            cantidad (int): Cantidad disponible en inventario (no puede ser negativa)
            precio (float): Precio unitario del producto (no puede ser negativo)
        """
        # Atributos privados para encapsulación
        self._id = id
        self._nombre = nombre
        self._cantidad = cantidad
        self._precio = precio

    # ========== GETTERS (PROPIEDADES DE SOLO LECTURA) ==========

    @property
    def id(self) -> int:
        """Devuelve el ID único del producto (solo lectura)"""
        return self._id

    @property
    def nombre(self) -> str:
        """Devuelve el nombre del producto (solo lectura)"""
        return self._nombre

    @property
    def cantidad(self) -> int:
        """Devuelve la cantidad disponible (solo lectura)"""
        return self._cantidad

    @property
    def precio(self) -> float:
        """Devuelve el precio unitario (solo lectura)"""
        return self._precio

    # ========== SETTERS (PROPIEDADES DE ESCRITURA) ==========

    @nombre.setter
    def nombre(self, nuevo_nombre: str):
        """
        Establece un nuevo nombre para el producto.

        Args:
            nuevo_nombre (str): Nuevo nombre a asignar
        """
        self._nombre = nuevo_nombre

    @cantidad.setter
    def cantidad(self, nueva_cantidad: int):
        """
        Establece una nueva cantidad para el producto.
        Valida que la cantidad no sea negativa.

        Args:
            nueva_cantidad (int): Nueva cantidad a asignar

        Raises:
            ValueError: Si la cantidad es negativa
        """
        if nueva_cantidad >= 0:
            self._cantidad = nueva_cantidad
        else:
            raise ValueError("La cantidad no puede ser negativa")

    @precio.setter
    def precio(self, nuevo_precio: float):
        """
        Establece un nuevo precio para el producto.
        Valida que el precio no sea negativo.

        Args:
            nuevo_precio (float): Nuevo precio a asignar

        Raises:
            ValueError: Si el precio es negativo
        """
        if nuevo_precio >= 0:
            self._precio = nuevo_precio
        else:
            raise ValueError("El precio no puede ser negativo")

    # ========== MÉTODOS ESPECIALES ==========

    def __str__(self) -> str:
        """
        Representación en string del producto para mostrar al usuario.

        Returns:
            str: Cadena formateada con todos los atributos del producto
        """
        return f"ID: {self._id}, Nombre: {self._nombre}, Cantidad: {self._cantidad}, Precio: ${self._precio:.2f}"

    # ========== MÉTODOS PARA PERSISTENCIA ==========

    def to_dict(self) -> dict:
        """
        Convierte el producto a un diccionario para facilitar el almacenamiento en archivo.
        Este método es crucial para la serialización de datos.

        Returns:
            dict: Diccionario con todos los atributos del producto
        """
        return {
            'id': self._id,
            'nombre': self._nombre,
            'cantidad': self._cantidad,
            'precio': self._precio
        }

    @classmethod
    def from_dict(cls, data: dict):
        """
        Crea un nuevo producto a partir de un diccionario.
        Este método es crucial para la deserialización de datos desde archivo.

        Args:
            data (dict): Diccionario con los datos del producto

        Returns:
            Producto: Nueva instancia de Producto con los datos proporcionados
        """
        return cls(data['id'], data['nombre'], data['cantidad'], data['precio'])
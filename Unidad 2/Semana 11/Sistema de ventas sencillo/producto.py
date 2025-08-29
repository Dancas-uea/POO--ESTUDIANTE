"""
SISTEMA DE GESTIÓN DE INVENTARIOS - CLASE PRODUCTO
Este archivo contiene la definición de la clase Producto con todas sus propiedades y métodos.
"""


class Producto:
    """
    Clase que representa un producto en el inventario.
    Utiliza propiedades (getters/setters) para garantizar la integridad de los datos.
    """

    def __init__(self, id: int, nombre: str, cantidad: int, precio: float):
        """
        Constructor de la clase Producto.

        Args:
            id (int): Identificador único del producto (debe ser único en el inventario)
            nombre (str): Nombre descriptivo del producto (no puede estar vacío)
            cantidad (int): Cantidad disponible en inventario (no puede ser negativa)
            precio (float): Precio unitario del producto (no puede ser negativo)
        """
        # Atributos privados para encapsulación
        self._id = id  # ID único, no cambia después de creado
        self.nombre = nombre  # Usa el setter para validación
        self.cantidad = cantidad  # Usa el setter para validación
        self.precio = precio  # Usa el setter para validación

    # ========== PROPIEDADES (GETTERS) ==========

    @property
    def id(self) -> int:
        """Devuelve el ID único del producto (solo lectura)"""
        return self._id

    @property
    def nombre(self) -> str:
        """Devuelve el nombre del producto"""
        return self._nombre

    @property
    def cantidad(self) -> int:
        """Devuelve la cantidad disponible en inventario"""
        return self._cantidad

    @property
    def precio(self) -> float:
        """Devuelve el precio unitario del producto"""
        return self._precio

    # ========== SETTERS CON VALIDACIÓN ==========

    @nombre.setter
    def nombre(self, valor: str):
        """
        Establece el nombre del producto con validación.

        Args:
            valor (str): Nuevo nombre para el producto

        Raises:
            ValueError: Si el nombre está vacío o solo contiene espacios
        """
        if not valor or not valor.strip():
            raise ValueError("El nombre no puede estar vacío")
        self._nombre = valor.strip()  # Elimina espacios extras

    @cantidad.setter
    def cantidad(self, valor: int):
        """
        Establece la cantidad disponible con validación.

        Args:
            valor (int): Nueva cantidad disponible

        Raises:
            ValueError: Si la cantidad es negativa
        """
        if valor < 0:
            raise ValueError("La cantidad no puede ser negativa")
        self._cantidad = valor

    @precio.setter
    def precio(self, valor: float):
        """
        Establece el precio unitario con validación.

        Args:
            valor (float): Nuevo precio unitario

        Raises:
            ValueError: Si el precio es negativo
        """
        if valor < 0:
            raise ValueError("El precio no puede ser negativo")
        self._precio = valor

    # ========== MÉTODOS ESPECIALES ==========

    def __str__(self) -> str:
        """
        Representación en string del producto para mostrar al usuario.

        Returns:
            str: Cadena formateada con todos los atributos del producto
        """
        return f"ID: {self._id} | {self._nombre} | Cant: {self._cantidad} | Precio: ${self._precio:.2f}"

    def __repr__(self) -> str:
        """
        Representación oficial del producto para debugging.

        Returns:
            str: Representación que puede ser usada para recrear el objeto
        """
        return f"Producto(id={self._id}, nombre='{self._nombre}', cantidad={self._cantidad}, precio={self._precio})"

    # ========== MÉTODOS PARA PERSISTENCIA ==========

    def to_dict(self) -> dict:
        """
        Convierte el producto a un diccionario para serialización.
        Esto permite guardar el producto en archivo JSON.

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
        Esto permite reconstruir productos desde archivo JSON.

        Args:
            data (dict): Diccionario con los datos del producto

        Returns:
            Producto: Nueva instancia de Producto con los datos proporcionados
        """
        return cls(data['id'], data['nombre'], data['cantidad'], data['precio'])
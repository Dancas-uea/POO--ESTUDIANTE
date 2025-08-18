from producto import Producto


class Inventario:
    """
    Clase que gestiona un inventario de productos.

    Atributos:
        productos (list): Lista de objetos Producto
    """

    def __init__(self):
        """Inicializa un inventario vacío"""
        self._productos = []

    def agregar_producto(self, producto: Producto) -> bool:
        """
        Agrega un nuevo producto al inventario.

        Args:
            producto: Producto a agregar

        Returns:
            bool: True si se agregó correctamente, False si ya existe un producto con ese ID
        """
        if self._buscar_por_id(producto.id) is None:
            self._productos.append(producto)
            return True
        return False

    def eliminar_producto(self, id: int) -> bool:
        """
        Elimina un producto del inventario por su ID.

        Args:
            id: ID del producto a eliminar

        Returns:
            bool: True si se eliminó correctamente, False si no se encontró el producto
        """
        producto = self._buscar_por_id(id)
        if producto:
            self._productos.remove(producto)
            return True
        return False

    def actualizar_producto(self, id: int, nombre: str = None, cantidad: int = None, precio: float = None) -> bool:
        """
        Actualiza los atributos de un producto.

        Args:
            id: ID del producto a actualizar
            nombre: Nuevo nombre (opcional)
            cantidad: Nueva cantidad (opcional)
            precio: Nuevo precio (opcional)

        Returns:
            bool: True si se actualizó correctamente, False si no se encontró el producto
        """
        producto = self._buscar_por_id(id)
        if producto:
            if nombre is not None:
                producto.nombre = nombre
            if cantidad is not None:
                producto.cantidad = cantidad
            if precio is not None:
                producto.precio = precio
            return True
        return False

    def buscar_por_nombre(self, nombre: str) -> list:
        """
        Busca productos por nombre (coincidencias parciales, insensible a mayúsculas).

        Args:
            nombre: Nombre o parte del nombre a buscar

        Returns:
            list: Lista de productos que coinciden con el criterio de búsqueda
        """
        nombre_lower = nombre.lower()
        return [p for p in self._productos if nombre_lower in p.nombre.lower()]

    def mostrar_inventario(self) -> list:
        """
        Devuelve todos los productos del inventario.

        Returns:
            list: Lista con todos los productos
        """
        return self._productos.copy()

    def _buscar_por_id(self, id: int) -> Producto:
        """
        Método interno para buscar un producto por su ID.

        Args:
            id: ID del producto a buscar

        Returns:
            Producto: El producto encontrado o None si no existe
        """
        for producto in self._productos:
            if producto.id == id:
                return producto
        return None
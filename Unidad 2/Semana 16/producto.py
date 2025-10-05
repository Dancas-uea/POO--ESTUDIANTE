class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        self._id = id_producto
        self._nombre = nombre
        self._cantidad = cantidad
        self._precio = precio

    # Getters
    @property
    def id(self):
        return self._id

    @property
    def nombre(self):
        return self._nombre

    @property
    def cantidad(self):
        return self._cantidad

    @property
    def precio(self):
        return self._precio

    # Setters
    @nombre.setter
    def nombre(self, valor):
        self._nombre = valor

    @cantidad.setter
    def cantidad(self, valor):
        if valor >= 0:
            self._cantidad = valor
        else:
            raise ValueError("La cantidad no puede ser negativa")

    @precio.setter
    def precio(self, valor):
        if valor >= 0:
            self._precio = valor
        else:
            raise ValueError("El precio no puede ser negativo")

    def __str__(self):
        return f"ID: {self._id}, Nombre: {self._nombre}, Cantidad: {self._cantidad}, Precio: ${self._precio:.2f}"

    def to_dict(self):
        """Convierte el producto a diccionario para guardar en archivo"""
        return {
            'id': self._id,
            'nombre': self._nombre,
            'cantidad': self._cantidad,
            'precio': self._precio
        }

    @classmethod
    def from_dict(cls, data):
        """Crea un producto desde un diccionario"""
        return cls(data['id'], data['nombre'], data['cantidad'], data['precio'])
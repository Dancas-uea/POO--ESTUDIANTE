import json
import os
from producto import Producto


class Inventario:
    def __init__(self, archivo='inventario.json'):
        self._productos = {}
        self._archivo = archivo
        self.cargar_desde_archivo()

    def agregar_producto(self, producto):
        if producto.id in self._productos:
            raise ValueError(f"El producto con ID {producto.id} ya existe")
        self._productos[producto.id] = producto
        self.guardar_en_archivo()

    def eliminar_producto(self, id_producto):
        if id_producto in self._productos:
            del self._productos[id_producto]
            self.guardar_en_archivo()
            return True
        return False

    def modificar_producto(self, id_producto, nombre=None, cantidad=None, precio=None):
        if id_producto not in self._productos:
            raise ValueError(f"Producto con ID {id_producto} no encontrado")

        producto = self._productos[id_producto]
        if nombre is not None:
            producto.nombre = nombre
        if cantidad is not None:
            producto.cantidad = cantidad
        if precio is not None:
            producto.precio = precio

        self.guardar_en_archivo()
        return producto

    def buscar_producto(self, id_producto):
        return self._productos.get(id_producto)

    def obtener_todos_productos(self):
        return list(self._productos.values())

    def guardar_en_archivo(self):
        try:
            datos = {id: producto.to_dict() for id, producto in self._productos.items()}
            with open(self._archivo, 'w') as archivo:
                json.dump(datos, archivo, indent=4)
        except Exception as e:
            print(f"Error al guardar en archivo: {e}")

    def cargar_desde_archivo(self):
        try:
            if os.path.exists(self._archivo):
                with open(self._archivo, 'r') as archivo:
                    datos = json.load(archivo)
                    self._productos = {id: Producto.from_dict(producto_data)
                                       for id, producto_data in datos.items()}
        except Exception as e:
            print(f"Error al cargar desde archivo: {e}")
            self._productos = {}
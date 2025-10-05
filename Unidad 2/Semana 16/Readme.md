1. Clase Producto (producto.py)

Implementación de la entidad principal con encapsulación de atributos:
- Atributos privados: _id, _nombre, _cantidad, _precio
- Properties para acceso controlado
- Métodos de serialización para persistencia

2. Clase Inventario (inventario.py)

Gestión de la colección de productos:
- Diccionario para almacenamiento en memoria
- Operaciones CRUD: agregar, eliminar, modificar, buscar
- Persistencia automática en archivo JSON
- Manejo de excepciones y validaciones

3. Interfaz Gráfica (gui_inventario.py)

Componente de presentación con Tkinter:
- Ventana principal con información del estudiante
- Formularios para gestión de productos
- TreeView para visualización tabular
- Manejo de eventos y atajos de teclado

4. Módulo Principal (main.py)

Punto de entrada de la aplicación:
- Inicialización del sistema
- Configuración de la ventana principal
- Coordinación entre componentes
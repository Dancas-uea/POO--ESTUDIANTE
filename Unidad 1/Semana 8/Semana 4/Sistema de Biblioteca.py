"""
Sistema de Biblioteca - Ejemplo de POO

Este programa modela un sistema de biblioteca con libros, usuarios y préstamos,
demostrando los principios de la Programación Orientada a Objetos.
"""

class Libro:
    """
    Clase que representa un libro en la biblioteca.

    Atributos:
        titulo (str): Título del libro
        autor (str): Autor del libro
        isbn (str): Número ISBN único del libro
        disponible (bool): Indica si el libro está disponible para préstamo
    """

    def __init__(self, titulo, autor, isbn):
        """
        Constructor de la clase Libro.

        Args:
            titulo (str): Título del libro
            autor (str): Autor del libro
            isbn (str): Número ISBN único del libro
        """
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.disponible = True

    def prestar(self):
        """Marca el libro como prestado si está disponible."""
        if self.disponible:
            self.disponible = False
            return True
        return False

    def devolver(self):
        """Marca el libro como disponible."""
        self.disponible = True

    def __str__(self):
        """Representación en string del libro."""
        return f"'{self.titulo}' por {self.autor} - {'Disponible' if self.disponible else 'Prestado'}"


class Usuario:
    """
    Clase que representa un usuario de la biblioteca.

    Atributos:
        nombre (str): Nombre del usuario
        id_usuario (str): ID único del usuario
        libros_prestados (list): Lista de libros actualmente prestados
    """

    def __init__(self, nombre, id_usuario):
        """
        Constructor de la clase Usuario.

        Args:
            nombre (str): Nombre del usuario
            id_usuario (str): ID único del usuario
        """
        self.nombre = nombre
        self.id_usuario = id_usuario
        self.libros_prestados = []

    def tomar_prestado(self, libro):
        """
        Intenta tomar prestado un libro.

        Args:
            libro (Libro): Libro a prestar

        Returns:
            bool: True si el préstamo fue exitoso, False si no
        """
        if libro.prestar():
            self.libros_prestados.append(libro)
            return True
        return False

    def devolver_libro(self, libro):
        """
        Devuelve un libro a la biblioteca.

        Args:
            libro (Libro): Libro a devolver
        """
        if libro in self.libros_prestados:
            libro.devolver()
            self.libros_prestados.remove(libro)

    def __str__(self):
        """Representación en string del usuario."""
        return f"Usuario: {self.nombre} (ID: {self.id_usuario}) - Libros prestados: {len(self.libros_prestados)}"


class Biblioteca:
    """
    Clase que representa la biblioteca y gestiona libros y usuarios.

    Atributos:
        libros (dict): Diccionario de libros (clave: ISBN)
        usuarios (dict): Diccionario de usuarios (clave: ID usuario)
    """

    def __init__(self):
        """Constructor de la clase Biblioteca."""
        self.libros = {}
        self.usuarios = {}

    def agregar_libro(self, libro):
        """Agrega un libro a la biblioteca."""
        self.libros[libro.isbn] = libro

    def registrar_usuario(self, usuario):
        """Registra un usuario en la biblioteca."""
        self.usuarios[usuario.id_usuario] = usuario

    def prestar_libro(self, isbn, id_usuario):
        """
        Gestiona el préstamo de un libro a un usuario.

        Args:
            isbn (str): ISBN del libro a prestar
            id_usuario (str): ID del usuario que pide el libro

        Returns:
            bool: True si el préstamo fue exitoso, False si no
        """
        if isbn in self.libros and id_usuario in self.usuarios:
            libro = self.libros[isbn]
            usuario = self.usuarios[id_usuario]
            return usuario.tomar_prestado(libro)
        return False

    def listar_libros(self):
        """Muestra todos los libros en la biblioteca."""
        print("\n--- Libros en la Biblioteca ---")
        for libro in self.libros.values():
            print(libro)

    def listar_usuarios(self):
        """Muestra todos los usuarios registrados."""
        print("\n--- Usuarios Registrados ---")
        for usuario in self.usuarios.values():
            print(usuario)


# Ejemplo de uso del sistema de biblioteca
if __name__ == "__main__":
    # Crear una biblioteca
    biblioteca = Biblioteca()

    # Agregar algunos libros
    libro1 = Libro("Cien años de soledad", "Gabriel García Márquez", "123456789")
    libro2 = Libro("El Principito", "Antoine de Saint-Exupéry", "987654321")
    libro3 = Libro("1984", "George Orwell", "567891234")

    biblioteca.agregar_libro(libro1)
    biblioteca.agregar_libro(libro2)
    biblioteca.agregar_libro(libro3)

    # Registrar algunos usuarios
    usuario1 = Usuario("Juan Pérez", "001")
    usuario2 = Usuario("María Gómez", "002")

    biblioteca.registrar_usuario(usuario1)
    biblioteca.registrar_usuario(usuario2)

    # Mostrar estado inicial
    biblioteca.listar_libros()
    biblioteca.listar_usuarios()

    # Realizar algunos préstamos
    print("\n--- Realizando préstamos ---")
    biblioteca.prestar_libro("123456789", "001")  # Juan toma Cien años de soledad
    biblioteca.prestar_libro("987654321", "001")  # Juan toma El Principito
    biblioteca.prestar_libro("567891234", "002")  # María toma 1984

    # Mostrar estado después de préstamos
    biblioteca.listar_libros()
    biblioteca.listar_usuarios()

    # Devolver un libro
    print("\n--- Devolviendo un libro ---")
    usuario1.devolver_libro(libro1)

    # Mostrar estado final
    biblioteca.listar_libros()
    biblioteca.listar_usuarios()

#SISTEMA BIBLIOTECARIO - FINALIDAD
# Este sistema avanzado resuelve problemas complejos de gestión bibliotecaria:

#Finalidad del Mundo Real:
#1. Implementar un sistema multiusuario con distintos niveles de acceso
#2. Gestionar préstamos con límites variables según tipo de usuario
#3. Controlar reservas y disponibilidad en tiempo real
#4. Generar informes administrativos completos
#5. Ofrecer búsquedas avanzadas en el catálogo

#Beneficios en el contexto real:
#- Cumple con normativas de bibliotecas académicas
#- Reduce conflictos por préstamos excesivos
#- Optimiza adquisición de nuevos materiales
#- Proporciona datos para acreditaciones
#- Interopera con sistemas de identificación universitaria
#- Genera alertas automáticas por atrasos
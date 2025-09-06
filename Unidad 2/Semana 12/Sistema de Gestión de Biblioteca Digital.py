"""
Sistema de Gestión de Biblioteca Digital - Biblioteca
Descripción: Sistema completo para gestionar una biblioteca digital especializada en literatura ecuatoriana.
"""

class Libro:
    """
    Clase que representa un libro en la biblioteca digital.
    Utiliza una tupla para almacenar autor y título, ya que son inmutables.
    """

    def __init__(self, titulo, autor, categoria, isbn, año_publicacion, editorial, descripcion=""):
        # Tupla para autor y título (inmutables)
        self.datos = (autor, titulo)
        self.categoria = categoria
        self.isbn = isbn
        self.año_publicacion = año_publicacion
        self.editorial = editorial
        self.descripcion = descripcion
        self.disponible = True
        self.veces_prestado = 0

    def __str__(self):
        estado = "Disponible" if self.disponible else "Prestado"
        return f"'{self.datos[1]}' por {self.datos[0]} - {self.categoria} ({self.año_publicacion}) - {estado} - ISBN: {self.isbn}"

    def info_completa(self):
        """Devuelve información completa del libro"""
        return f"""
Título: {self.datos[1]}
Autor: {self.datos[0]}
Categoría: {self.categoria}
ISBN: {self.isbn}
Año: {self.año_publicacion}
Editorial: {self.editorial}
Descripción: {self.descripcion}
Estado: {'Disponible' if self.disponible else 'Prestado'}
Veces prestado: {self.veces_prestado}
        """.strip()

    @property
    def titulo(self):
        return self.datos[1]

    @property
    def autor(self):
        return self.datos[0]


class Usuario:
    """
    Clase que representa a un usuario de la biblioteca.
    """

    def __init__(self, nombre, id_usuario, email, telefono, contraseña):
        self.nombre = nombre
        self.id_usuario = id_usuario
        self.email = email
        self.telefono = telefono
        self.contraseña = contraseña  # Contraseña para iniciar sesión
        self.libros_prestados = []  # Lista de libros actualmente prestados
        self.fecha_registro = "2024-05-20"  # Fecha actual simulada
        self.es_admin = (id_usuario == "admin")  # Usuario admin especial

    def __str__(self):
        return f"Usuario: {self.nombre} (ID: {self.id_usuario}) - Libros: {len(self.libros_prestados)}"

    def info_completa(self):
        """Devuelve información completa del usuario"""
        libros = ", ".join([libro.titulo for libro in self.libros_prestados]) if self.libros_prestados else "Ninguno"
        return f"""
Nombre: {self.nombre}
ID: {self.id_usuario}
Email: {self.email}
Teléfono: {self.telefono}
Fecha registro: {self.fecha_registro}
Libros prestados: {libros}
Tipo: {'Administrador' if self.es_admin else 'Usuario regular'}
        """.strip()

    def verificar_contraseña(self, contraseña):
        """Verifica si la contraseña es correcta"""
        return self.contraseña == contraseña


class BibliotecaEcuatoriana:
    """
    Clase principal que gestiona la biblioteca digital de literatura ecuatoriana.
    """

    def __init__(self, nombre="Biblioteca Digital Ecuatoriana"):
        self.nombre = nombre
        # Diccionario para libros (clave: ISBN, valor: objeto Libro)
        self.libros = {}

        # Conjunto para IDs de usuarios únicos
        self.ids_usuarios = set()

        # Diccionario para usuarios (clave: ID usuario, valor: objeto Usuario)
        self.usuarios = {}

        # Usuario actualmente logueado
        self.usuario_actual = None

        # Lista para historial de préstamos
        self.historial_prestamos = []

        # Inicializar con libros ecuatorianos
        self._inicializar_biblioteca()
        self._inicializar_usuario_admin()

    def _inicializar_biblioteca(self):
        """Inicializa la biblioteca con libros ecuatorianos"""
        libros_ecuatorianos = [
            # Novelas
            ("Huasipungo", "Jorge Icaza", "Novela", "978-9978-62-477-5", 1934, "Editorial Nacional",
             "Novela indigenista que denuncia la explotación de los indígenas en Ecuador"),

            ("Las cruces sobre el agua", "Joaquín Gallegos Lara", "Novela histórica", "978-9978-62-478-2", 1946,
             "Casa de la Cultura",
             "Novela sobre la matanza de trabajadores del 15 de noviembre de 1922 en Guayaquil"),

            ("El chulla Romero y Flores", "Jorge Icaza", "Novela", "978-9978-62-480-5", 1958, "Editorial Universitaria",
             "Novela que explora la identidad del mestizo ecuatoriano"),

            ("Siete lunas y siete serpientes", "Demetrio Aguilera Malta", "Novela", "978-9978-62-481-2", 1970,
             "Editorial Planeta",
             "Novela realista mágica ambientada en la costa ecuatoriana"),

            ("La dama tapada", "Alicia Yánez Cossío", "Novela", "978-9978-62-482-9", 1985, "Editorial El Conejo",
             "Novela histórica sobre la época colonial en Quito"),

            ("Polvo y ceniza", "Eliécer Cárdenas", "Novela", "978-9978-62-483-6", 1979, "Casa de la Cultura",
             "Novela sobre la vida en los Andes ecuatorianos"),

            # Cuentos
            ("Un día cualquiera", "José de la Cuadra", "Cuentos", "978-9978-62-479-9", 1936, "Editorial Ecuador",
             "Colección de cuentos costeños"),

            ("Cuando los guayacanes florecían", "José de la Cuadra", "Cuentos", "978-9978-62-484-3", 1933,
             "Editorial Ecuador",
             "Cuentos de la región costera del Ecuador"),

            ("Relatos de un náufrago", "Pedro Jorge Vera", "Cuentos", "978-9978-62-486-7", 1943, "Editorial Guayaquil",
             "Cuentos urbanos ambientados en Guayaquil"),

            # Poesía
            ("El espejo humeante", "Jorge Dávila Vázquez", "Poesía", "978-9978-62-485-0", 1984, "Casa de la Cultura",
             "Antología poética del autor ambateño"),
        ]

        for libro_info in libros_ecuatorianos:
            libro = Libro(*libro_info)
            self.libros[libro.isbn] = libro

        print(f"Biblioteca '{self.nombre}' inicializada con {len(self.libros)} libros ecuatorianos.")

    def _inicializar_usuario_admin(self):
        """Crea un usuario administrador por defecto"""
        admin = Usuario("Administrador", "admin", "admin@biblioteca.edu.ec", "0000000000", "admin123")
        self.ids_usuarios.add("admin")
        self.usuarios["admin"] = admin

    def iniciar_sesion(self):
        """Sistema de inicio de sesión"""
        print("\n🔐 INICIAR SESIÓN")
        id_usuario = input("ID de usuario: ")
        contraseña = input("Contraseña: ")

        if id_usuario in self.usuarios and self.usuarios[id_usuario].verificar_contraseña(contraseña):
            self.usuario_actual = self.usuarios[id_usuario]
            print(f"✅ Bienvenido/a, {self.usuario_actual.nombre}!")
            return True
        else:
            print("❌ ID de usuario o contraseña incorrectos.")
            return False

    def registrar_nuevo_usuario(self):
        """Registra un nuevo usuario en el sistema"""
        print("\n👤 REGISTRAR NUEVO USUARIO")

        while True:
            id_usuario = input("ID de usuario: ")
            if id_usuario in self.ids_usuarios:
                print("❌ Este ID ya existe. Por favor, elija otro.")
                continue

            nombre = input("Nombre completo: ")
            email = input("Email: ")
            telefono = input("Teléfono: ")
            contraseña = input("Contraseña: ")
            confirmar_contraseña = input("Confirmar contraseña: ")

            if contraseña != confirmar_contraseña:
                print("❌ Las contraseñas no coinciden.")
                continue

            nuevo_usuario = Usuario(nombre, id_usuario, email, telefono, contraseña)
            self.ids_usuarios.add(id_usuario)
            self.usuarios[id_usuario] = nuevo_usuario

            print(f"✅ Usuario '{nombre}' registrado exitosamente!")
            print("Ahora puede iniciar sesión con sus credenciales.")
            break

    def mostrar_lista_isbn(self):
        """Muestra una lista de ISBNs con los nombres de libros para facilitar la selección"""
        print("\n📋 LISTA DE LIBROS CON ISBN:")
        print("-" * 80)
        for i, (isbn, libro) in enumerate(self.libros.items(), 1):
            print(f"{i:2d}. ISBN: {isbn} - '{libro.titulo}' por {libro.autor}")
        print("-" * 80)

    def seleccionar_isbn_interactivo(self):
        """Permite seleccionar un ISBN de la lista mostrada"""
        self.mostrar_lista_isbn()
        try:
            opcion = int(input("\nSeleccione el número del libro: "))
            isbns = list(self.libros.keys())
            if 1 <= opcion <= len(isbns):
                return isbns[opcion - 1]
            else:
                print("❌ Opción inválida.")
                return None
        except ValueError:
            print("❌ Por favor, ingrese un número válido.")
            return None

    def listar_usuarios_registrados(self):
        """Muestra todos los usuarios registrados en el sistema"""
        print(f"\n👥 USUARIOS REGISTRADOS ({len(self.usuarios)}):")
        print("-" * 60)
        for i, (id_usuario, usuario) in enumerate(self.usuarios.items(), 1):
            print(f"{i:2d}. {usuario.nombre} (ID: {id_usuario}) - Tel: {usuario.telefono}")
        print("-" * 60)

    # Resto de métodos mantienen la misma estructura pero con mejoras en la interfaz
    def añadir_libro(self, titulo, autor, categoria, isbn, año_publicacion, editorial, descripcion=""):
        """Añade un nuevo libro a la biblioteca."""
        if isbn in self.libros:
            print(f"❌ El libro con ISBN {isbn} ya existe en la biblioteca.")
            return False

        libro = Libro(titulo, autor, categoria, isbn, año_publicacion, editorial, descripcion)
        self.libros[isbn] = libro
        print(f"✅ Libro '{titulo}' añadido correctamente.")
        return True

    def quitar_libro(self, isbn):
        """Elimina un libro de la biblioteca."""
        if isbn not in self.libros:
            print(f"❌ No existe ningún libro con ISBN {isbn}.")
            return False

        libro = self.libros[isbn]
        if not libro.disponible:
            print(f"❌ No se puede eliminar '{libro.titulo}' porque está prestado.")
            return False

        del self.libros[isbn]
        print(f"✅ Libro '{libro.titulo}' eliminado correctamente.")
        return True

    def prestar_libro(self, isbn, id_usuario):
        """Presta un libro a un usuario."""
        if isbn not in self.libros:
            print(f"❌ No existe ningún libro con ISBN {isbn}.")
            return False

        if id_usuario not in self.ids_usuarios:
            print(f"❌ No existe ningún usuario con ID {id_usuario}.")
            return False

        libro = self.libros[isbn]
        usuario = self.usuarios[id_usuario]

        if not libro.disponible:
            print(f"❌ '{libro.titulo}' no está disponible.")
            return False

        if len(usuario.libros_prestados) >= 5:
            print(f"❌ {usuario.nombre} ya tiene el máximo de 5 libros prestados.")
            return False

        # Realizar el préstamo
        libro.disponible = False
        libro.veces_prestado += 1
        usuario.libros_prestados.append(libro)

        # Registrar en el historial
        from datetime import datetime
        fecha_prestamo = datetime.now().strftime("%Y-%m-%d %H:%M")
        self.historial_prestamos.append((libro, usuario, "préstamo", fecha_prestamo))

        print(f"✅ '{libro.titulo}' prestado a {usuario.nombre}.")
        return True

    def devolver_libro(self, isbn, id_usuario):
        """Devuelve un libro prestado por un usuario."""
        if isbn not in self.libros:
            print(f"❌ No existe ningún libro con ISBN {isbn}.")
            return False

        if id_usuario not in self.ids_usuarios:
            print(f"❌ No existe ningún usuario con ID {id_usuario}.")
            return False

        libro = self.libros[isbn]
        usuario = self.usuarios[id_usuario]

        if libro not in usuario.libros_prestados:
            print(f"❌ {usuario.nombre} no tiene prestado '{libro.titulo}'.")
            return False

        # Realizar la devolución
        libro.disponible = True
        usuario.libros_prestados.remove(libro)

        # Registrar en el historial
        from datetime import datetime
        fecha_devolucion = datetime.now().strftime("%Y-%m-%d %H:%M")
        self.historial_prestamos.append((libro, usuario, "devolución", fecha_devolucion))

        print(f"✅ '{libro.titulo}' devuelto por {usuario.nombre}.")
        return True

    def buscar_por_titulo(self, titulo):
        """Busca libros por título."""
        return [libro for libro in self.libros.values() if titulo.lower() in libro.titulo.lower()]

    def buscar_por_autor(self, autor):
        """Busca libros por autor."""
        return [libro for libro in self.libros.values() if autor.lower() in libro.autor.lower()]

    def buscar_por_categoria(self, categoria):
        """Busca libros por categoría."""
        return [libro for libro in self.libros.values() if categoria.lower() in libro.categoria.lower()]

    def buscar_por_isbn(self, isbn):
        """Busca un libro por ISBN."""
        return self.libros.get(isbn, None)

    def listar_libros_prestados_usuario(self, id_usuario):
        """Lista los libros prestados a un usuario específico."""
        if id_usuario not in self.ids_usuarios:
            print(f"❌ No existe ningún usuario con ID {id_usuario}.")
            return []
        return self.usuarios[id_usuario].libros_prestados

    def listar_todos_libros_prestados(self):
        """Lista todos los libros actualmente prestados."""
        return [libro for usuario in self.usuarios.values() for libro in usuario.libros_prestados]

    def listar_libros_disponibles(self):
        """Lista todos los libros disponibles."""
        return [libro for libro in self.libros.values() if libro.disponible]

    def estadisticas(self):
        """Muestra estadísticas de la biblioteca."""
        total_libros = len(self.libros)
        libros_prestados = len(self.listar_todos_libros_prestados())
        libros_disponibles = total_libros - libros_prestados
        total_usuarios = len(self.usuarios)
        total_prestamos = len([p for p in self.historial_prestamos if p[2] == "préstamo"])

        libro_mas_popular = max(self.libros.values(), key=lambda x: x.veces_prestado, default=None)

        return f"""
📊 ESTADÍSTICAS DE LA BIBLIOTECA 📊
Total de libros: {total_libros}
Libros disponibles: {libros_disponibles}
Libros prestados: {libros_prestados}
Total de usuarios: {total_usuarios}
Total de préstamos: {total_prestamos}
Libro más popular: {libro_mas_popular.titulo if libro_mas_popular else 'Ninguno'} ({libro_mas_popular.veces_prestado if libro_mas_popular else 0} préstamos)
        """.strip()

    def mostrar_historial_prestamos(self, limite=10):
        """Muestra el historial reciente de préstamos."""
        if not self.historial_prestamos:
            print("No hay historial de préstamos.")
            return

        print(f"\n📋 HISTORIAL DE PRÉSTAMOS (últimos {limite}) 📋")
        for i, (libro, usuario, tipo, fecha) in enumerate(self.historial_prestamos[-limite:], 1):
            accion = "PRESTADO" if tipo == "préstamo" else "DEVUELTO"
            print(f"{i}. {fecha} - {usuario.nombre} {accion} '{libro.titulo}'")


# Función para mostrar menú interactivo
def menu_principal():
    """Menú interactivo para la biblioteca"""
    biblioteca = BibliotecaEcuatoriana()

    # Sistema de autenticación
    while True:
        print("\n" + "=" * 50)
        print("📚 BIBLIOTECA DIGITAL ECUATORIANA 📚")
        print("=" * 50)
        print("1. Iniciar sesión")
        print("2. Registrar nuevo usuario")
        print("0. Salir")
        print("=" * 50)

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            if biblioteca.iniciar_sesion():
                break
        elif opcion == "2":
            biblioteca.registrar_nuevo_usuario()
        elif opcion == "0":
            print("¡Hasta pronto!")
            return
        else:
            print("❌ Opción inválida.")

    # Menú principal después del login
    while True:
        print("\n" + "=" * 50)
        print(f"📚 BIBLIOTECA DIGITAL ECUATORIANA 📚")
        print(f"Usuario: {biblioteca.usuario_actual.nombre}")
        print("=" * 50)
        print("1. Buscar libros")
        print("2. Prestar libro")
        print("3. Devolver libro")
        print("4. Ver lista de libros con ISBN")
        print("5. Ver estadísticas")
        print("6. Ver historial de préstamos")
        print("7. Listar libros prestados")
        print("8. Listar libros disponibles")

        # Opciones solo para administrador
        if biblioteca.usuario_actual.es_admin:
            print("9. Añadir libro")
            print("10. Quitar libro")
            print("11. Ver usuarios registrados")

        print("0. Cerrar sesión")
        print("=" * 50)

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            print("\n🔍 BUSCAR LIBROS")
            print("1. Por título")
            print("2. Por autor")
            print("3. Por categoría")
            sub_opcion = input("Seleccione tipo de búsqueda: ")

            if sub_opcion == "1":
                termino = input("Ingrese título a buscar: ")
                resultados = biblioteca.buscar_por_titulo(termino)
            elif sub_opcion == "2":
                termino = input("Ingrese autor a buscar: ")
                resultados = biblioteca.buscar_por_autor(termino)
            elif sub_opcion == "3":
                termino = input("Ingrese categoría a buscar: ")
                resultados = biblioteca.buscar_por_categoria(termino)
            else:
                print("❌ Opción inválida")
                continue

            if resultados:
                print(f"\n📖 Se encontraron {len(resultados)} resultados:")
                for i, libro in enumerate(resultados, 1):
                    print(f"{i}. {libro}")
            else:
                print("❌ No se encontraron resultados.")

        elif opcion == "2":
            print("\n📥 PRESTAR LIBRO")
            biblioteca.mostrar_lista_isbn()
            isbn = input("Ingrese ISBN del libro: ")
            biblioteca.prestar_libro(isbn, biblioteca.usuario_actual.id_usuario)

        elif opcion == "3":
            print("\n📤 DEVOLVER LIBRO")
            prestados = biblioteca.listar_libros_prestados_usuario(biblioteca.usuario_actual.id_usuario)
            if prestados:
                print("Sus libros prestados:")
                for i, libro in enumerate(prestados, 1):
                    print(f"{i}. {libro.titulo} - ISBN: {libro.isbn}")
                isbn = input("Ingrese ISBN del libro a devolver: ")
                biblioteca.devolver_libro(isbn, biblioteca.usuario_actual.id_usuario)
            else:
                print("❌ No tiene libros prestados actualmente.")

        elif opcion == "4":
            biblioteca.mostrar_lista_isbn()
            input("\nPresione Enter para continuar...")

        elif opcion == "5":
            print("\n" + biblioteca.estadisticas())
            input("\nPresione Enter para continuar...")

        elif opcion == "6":
            biblioteca.mostrar_historial_prestamos()
            input("\nPresione Enter para continuar...")

        elif opcion == "7":
            print("\n📚 LIBROS PRESTADOS")
            prestados = biblioteca.listar_todos_libros_prestados()
            if prestados:
                for i, libro in enumerate(prestados, 1):
                    print(f"{i}. {libro}")
            else:
                print("No hay libros prestados actualmente.")
            input("\nPresione Enter para continuar...")

        elif opcion == "8":
            print("\n📗 LIBROS DISPONIBLES")
            disponibles = biblioteca.listar_libros_disponibles()
            if disponibles:
                for i, libro in enumerate(disponibles, 1):
                    print(f"{i}. {libro}")
            else:
                print("No hay libros disponibles actualmente.")
            input("\nPresione Enter para continuar...")

        # Opciones solo para administrador
        elif opcion == "9" and biblioteca.usuario_actual.es_admin:
            print("\n➕ AÑADIR LIBRO")
            titulo = input("Título: ")
            autor = input("Autor: ")
            categoria = input("Categoría: ")
            isbn = input("ISBN: ")
            año = input("Año de publicación: ")
            editorial = input("Editorial: ")
            descripcion = input("Descripción: ")
            biblioteca.añadir_libro(titulo, autor, categoria, isbn, año, editorial, descripcion)

        elif opcion == "10" and biblioteca.usuario_actual.es_admin:
            print("\n🗑️ QUITAR LIBRO")
            biblioteca.mostrar_lista_isbn()
            isbn = input("Ingrese ISBN del libro a eliminar: ")
            biblioteca.quitar_libro(isbn)

        elif opcion == "11" and biblioteca.usuario_actual.es_admin:
            biblioteca.listar_usuarios_registrados()
            input("\nPresione Enter para continuar...")

        elif opcion == "0":
            print(f"✅ Sesión cerrada. ¡Hasta pronto, {biblioteca.usuario_actual.nombre}!")
            break

        else:
            print("❌ Opción inválida o no tiene permisos para esta acción.")


if __name__ == "__main__":
    menu_principal()
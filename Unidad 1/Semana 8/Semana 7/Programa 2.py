
"""
Sistema de Gestión de Archivos y Conexiones
Demostración de Constructores y Destructores en Python

Descripción: Este programa demuestra el uso de constructores (__init__) y
destructores (__del__) en Python a través de un sistema de gestión de archivos
y conexiones simuladas.
"""

import os
import datetime
import time

class GestorArchivos:
    """
    Clase que simula un gestor de archivos con operaciones de apertura,
    escritura y cierre automático usando constructores y destructores.
    """

    # Variable de clase para contar instancias activas
    instancias_activas = 0

    def __init__(self, nombre_archivo, modo='w'):
        """
        CONSTRUCTOR: Se ejecuta automáticamente cuando se crea una instancia
        de la clase. Inicializa los atributos del objeto.

        Args:
            nombre_archivo (str): Nombre del archivo a gestionar
            modo (str): Modo de apertura del archivo ('w', 'r', 'a')
        """
        self.nombre_archivo = nombre_archivo
        self.modo = modo
        self.archivo_abierto = None
        self.fecha_creacion = datetime.datetime.now()
        self.operaciones_realizadas = 0

        # Incrementar contador de instancias
        GestorArchivos.instancias_activas += 1

        # Simular apertura del archivo
        try:
            self.archivo_abierto = open(self.nombre_archivo, self.modo, encoding='utf-8')
            print(f"✅ Constructor ejecutado: Archivo '{self.nombre_archivo}' abierto en modo '{self.modo}'")
            print(f"📊 Instancias activas: {GestorArchivos.instancias_activas}")

            # Escribir header si es modo escritura
            if self.modo in ['w', 'a']:
                self.archivo_abierto.write(f"# Archivo creado el {self.fecha_creacion}\n")
                self.archivo_abierto.write(f"# Gestor de archivos iniciado\n\n")

        except Exception as e:
            print(f"❌ Error al abrir archivo: {e}")
            self.archivo_abierto = None

    def escribir_linea(self, contenido):
        """
        Método para escribir una línea en el archivo.

        Args:
            contenido (str): Contenido a escribir
        """
        if self.archivo_abierto and self.modo in ['w', 'a']:
            timestamp = datetime.datetime.now().strftime("%H:%M:%S")
            self.archivo_abierto.write(f"[{timestamp}] {contenido}\n")
            self.archivo_abierto.flush()  # Forzar escritura
            self.operaciones_realizadas += 1
            print(f"📝 Línea escrita: {contenido}")
        else:
            print("❌ No se puede escribir: archivo cerrado o en modo lectura")

    def leer_contenido(self):
        """
        Método para leer el contenido del archivo.

        Returns:
            str: Contenido del archivo o None si hay error
        """
        if self.archivo_abierto and self.modo == 'r':
            try:
                self.archivo_abierto.seek(0)  # Volver al inicio
                contenido = self.archivo_abierto.read()
                self.operaciones_realizadas += 1
                print(f"📖 Archivo leído: {len(contenido)} caracteres")
                return contenido
            except Exception as e:
                print(f"❌ Error al leer archivo: {e}")
                return None
        else:
            print("❌ No se puede leer: archivo cerrado o en modo escritura")
            return None

    def obtener_estadisticas(self):
        """
        Método para obtener estadísticas del gestor.

        Returns:
            dict: Diccionario con estadísticas
        """
        return {
            'archivo': self.nombre_archivo,
            'modo': self.modo,
            'fecha_creacion': self.fecha_creacion,
            'operaciones': self.operaciones_realizadas,
            'estado': 'Abierto' if self.archivo_abierto else 'Cerrado'
        }

    def __del__(self):
        """
        DESTRUCTOR: Se ejecuta automáticamente cuando el objeto va a ser
        eliminado de la memoria por el garbage collector. Realiza limpieza
        de recursos.
        """
        print(f"🔄 Destructor ejecutado para '{self.nombre_archivo}'")

        # Cerrar archivo si está abierto
        if self.archivo_abierto:
            try:
                # Escribir footer si es modo escritura
                if self.modo in ['w', 'a']:
                    self.archivo_abierto.write(f"\n# Archivo cerrado el {datetime.datetime.now()}\n")
                    self.archivo_abierto.write(f"# Total de operaciones: {self.operaciones_realizadas}\n")

                self.archivo_abierto.close()
                print(f"📁 Archivo '{self.nombre_archivo}' cerrado correctamente")

            except Exception as e:
                print(f"❌ Error al cerrar archivo: {e}")

        # Decrementar contador de instancias
        GestorArchivos.instancias_activas -= 1
        print(f"📊 Instancias activas restantes: {GestorArchivos.instancias_activas}")
        print(f"💾 Recursos liberados para '{self.nombre_archivo}'")


class ConexionBaseDatos:
    """
    Clase que simula una conexión a base de datos para demostrar
    el uso de constructores y destructores en gestión de recursos.
    """

    # Contador estático de conexiones
    total_conexiones = 0

    def __init__(self, servidor, puerto=5432, usuario="admin"):
        """
        CONSTRUCTOR: Inicializa la conexión a la base de datos.

        Args:
            servidor (str): Dirección del servidor
            puerto (int): Puerto de conexión
            usuario (str): Usuario para la conexión
        """
        self.servidor = servidor
        self.puerto = puerto
        self.usuario = usuario
        self.conectado = False
        self.consultas_ejecutadas = 0
        self.tiempo_conexion = datetime.datetime.now()

        # Incrementar contador
        ConexionBaseDatos.total_conexiones += 1
        self.id_conexion = ConexionBaseDatos.total_conexiones

        # Simular proceso de conexión
        print(f"🔌 Constructor: Iniciando conexión #{self.id_conexion} a {servidor}:{puerto}")
        time.sleep(0.5)  # Simular tiempo de conexión

        self.conectado = True
        print(f"✅ Conexión establecida exitosamente")
        print(f"👤 Usuario: {self.usuario}")
        print(f"🕐 Hora de conexión: {self.tiempo_conexion.strftime('%H:%M:%S')}")

    def ejecutar_consulta(self, consulta):
        """
        Simula la ejecución de una consulta SQL.

        Args:
            consulta (str): Consulta SQL a ejecutar

        Returns:
            dict: Resultado simulado de la consulta
        """
        if not self.conectado:
            print("❌ No se puede ejecutar: conexión cerrada")
            return None

        print(f"🔍 Ejecutando consulta: {consulta}")
        time.sleep(0.2)  # Simular tiempo de ejecución

        self.consultas_ejecutadas += 1
        resultado = {
            'consulta': consulta,
            'filas_afectadas': 42,  # Resultado simulado
            'tiempo_ejecucion': '0.2s',
            'estado': 'exitoso'
        }

        print(f"✅ Consulta ejecutada. Filas afectadas: {resultado['filas_afectadas']}")
        return resultado

    def obtener_estado_conexion(self):
        """
        Obtiene el estado actual de la conexión.

        Returns:
            dict: Estado de la conexión
        """
        duracion = datetime.datetime.now() - self.tiempo_conexion
        return {
            'id': self.id_conexion,
            'servidor': self.servidor,
            'puerto': self.puerto,
            'usuario': self.usuario,
            'conectado': self.conectado,
            'consultas_ejecutadas': self.consultas_ejecutadas,
            'duracion_conexion': str(duracion).split('.')[0],
            'tiempo_conexion': self.tiempo_conexion.strftime('%Y-%m-%d %H:%M:%S')
        }

    def __del__(self):
        """
        DESTRUCTOR: Cierra la conexión y libera recursos automáticamente.
        """
        print(f"🔄 Destructor: Cerrando conexión #{self.id_conexion}")

        if self.conectado:
            # Simular cierre de conexión
            duracion = datetime.datetime.now() - self.tiempo_conexion
            print(f"📊 Estadísticas de la conexión:")
            print(f"   - Servidor: {self.servidor}:{self.puerto}")
            print(f"   - Usuario: {self.usuario}")
            print(f"   - Consultas ejecutadas: {self.consultas_ejecutadas}")
            print(f"   - Duración: {str(duracion).split('.')[0]}")

            self.conectado = False
            time.sleep(0.2)  # Simular tiempo de cierre

            print(f"🔐 Conexión #{self.id_conexion} cerrada correctamente")

        print(f"💾 Recursos de conexión liberados")


def demostrar_constructores_destructores():
    """
    Función principal que demuestra el uso de constructores y destructores.
    """
    print("=" * 60)
    print("DEMOSTRACIÓN DE CONSTRUCTORES Y DESTRUCTORES EN PYTHON")
    print("=" * 60)

    print("\n1. CREANDO INSTANCIAS DE GESTORES DE ARCHIVOS")
    print("-" * 50)

    # Crear instancias - se ejecutan los constructores
    gestor1 = GestorArchivos("log_sistema.txt", "w")
    gestor2 = GestorArchivos("datos_usuario.txt", "w")

    print("\n2. USANDO LOS GESTORES DE ARCHIVOS")
    print("-" * 50)

    # Usar los gestores
    gestor1.escribir_linea("Sistema iniciado correctamente")
    gestor1.escribir_linea("Usuario admin conectado")
    gestor1.escribir_linea("Procesando solicitudes...")

    gestor2.escribir_linea("Registro de nuevo usuario: Juan Pérez")
    gestor2.escribir_linea("Perfil actualizado: María González")

    # Mostrar estadísticas
    print("\n📊 Estadísticas del Gestor 1:")
    stats1 = gestor1.obtener_estadisticas()
    for key, value in stats1.items():
        print(f"   {key}: {value}")

    print("\n3. CREANDO CONEXIONES A BASE DE DATOS")
    print("-" * 50)

    # Crear conexiones - se ejecutan los constructores
    conexion1 = ConexionBaseDatos("localhost", 5432, "admin")
    conexion2 = ConexionBaseDatos("192.168.1.100", 3306, "usuario1")

    print("\n4. USANDO LAS CONEXIONES")
    print("-" * 50)

    # Usar las conexiones
    conexion1.ejecutar_consulta("SELECT * FROM usuarios")
    conexion1.ejecutar_consulta("UPDATE productos SET precio = 100 WHERE id = 1")

    conexion2.ejecutar_consulta("SELECT COUNT(*) FROM pedidos")

    # Mostrar estado de conexiones
    print("\n📊 Estado de Conexión 1:")
    estado1 = conexion1.obtener_estado_conexion()
    for key, value in estado1.items():
        print(f"   {key}: {value}")

    print("\n5. ELIMINANDO REFERENCIAS (ACTIVANDO DESTRUCTORES)")
    print("-" * 50)

    # Eliminar referencias - se ejecutarán los destructores
    print("Eliminando gestor1...")
    del gestor1  # Destructor se ejecuta inmediatamente

    print("\nEliminando conexion1...")
    del conexion1  # Destructor se ejecuta inmediatamente

    print("\n6. SALIENDO DEL ÁMBITO (DESTRUCTORES AUTOMÁTICOS)")
    print("-" * 50)
    print("Al finalizar la función, los objetos restantes serán")
    print("destruidos automáticamente por el garbage collector...")

    # gestor2 y conexion2 se destruirán automáticamente al salir del ámbito


def ejemplo_con_excepcion():
    """
    Demuestra cómo los destructores se ejecutan incluso cuando hay excepciones.
    """
    print("\n" + "=" * 60)
    print("DEMOSTRACIÓN CON MANEJO DE EXCEPCIONES")
    print("=" * 60)

    try:
        print("\n📁 Creando gestor de archivos...")
        gestor = GestorArchivos("archivo_temporal.txt", "w")

        print("📝 Escribiendo datos...")
        gestor.escribir_linea("Datos importantes")
        gestor.escribir_linea("Más información crítica")

        print("⚠️  Simulando error...")
        # Simular un error
        raise ValueError("Error simulado para demostrar destructores")

    except Exception as e:
        print(f"❌ Excepción capturada: {e}")
        print("🔄 Nota: El destructor se ejecutará automáticamente")

    print("✅ Manejo de excepción completado")


if __name__ == "__main__":
    # Ejecutar demostración principal
    demostrar_constructores_destructores()

    # Demostrar manejo de excepciones
    ejemplo_con_excepcion()

    print("\n" + "=" * 60)
    print("RESUMEN DE CONCEPTOS DEMOSTRADOS")
    print("=" * 60)
    print("✅ Constructores (__init__):")
    print("   - Se ejecutan automáticamente al crear objetos")
    print("   - Inicializan atributos del objeto")
    print("   - Pueden recibir parámetros")
    print("   - Gestionan recursos (archivos, conexiones)")
    print()
    print("✅ Destructores (__del__):")
    print("   - Se ejecutan automáticamente al destruir objetos")
    print("   - Liberan recursos y realizan limpieza")
    print("   - Se activan al salir del ámbito o usar 'del'")
    print("   - Funcionan incluso con excepciones")
    print()
    print("🎯 Programa completado exitosamente")

    # Limpiar archivos temporales
    import os
    archivos_temporales = ["log_sistema.txt", "datos_usuario.txt", "archivo_temporal.txt"]
    for archivo in archivos_temporales:
        if os.path.exists(archivo):
            os.remove(archivo)
            print(f"🗑️  Archivo temporal eliminado: {archivo}")
"""
Sistema de Gestión de Empleados
Programa que demuestra conceptos de POO en Python:
- Definición de Clase y Objeto
- Herencia
- Encapsulación
- Polimorfismo

Autor: [Tu Nombre]
Fecha: [Fecha actual]
"""

from abc import ABC, abstractmethod
from datetime import datetime


class Persona(ABC):
    """
    Clase base abstracta que representa una persona.
    Demuestra: Definición de clase, Encapsulación
    """

    def __init__(self, nombre, apellido, edad, dni):
        """
        Constructor de la clase Persona

        Args:
            nombre (str): Nombre de la persona
            apellido (str): Apellido de la persona
            edad (int): Edad de la persona
            dni (str): DNI de la persona
        """
        # Atributos públicos
        self.nombre = nombre
        self.apellido = apellido

        # Atributos protegidos (Encapsulación)
        self._edad = self._validar_edad(edad)
        self._dni = dni

        # Atributo privado (Encapsulación)
        self.__fecha_registro = datetime.now()

    def _validar_edad(self, edad):
        """
        Método protegido para validar la edad
        Demuestra: Encapsulación
        """
        if edad < 0 or edad > 120:
            raise ValueError("La edad debe estar entre 0 y 120 años")
        return edad

    # Propiedades para acceder a atributos encapsulados
    @property
    def edad(self):
        """Getter para el atributo edad"""
        return self._edad

    @edad.setter
    def edad(self, nueva_edad):
        """Setter para el atributo edad con validación"""
        self._edad = self._validar_edad(nueva_edad)

    @property
    def dni(self):
        """Getter para el atributo DNI"""
        return self._dni

    @property
    def fecha_registro(self):
        """Getter para la fecha de registro (solo lectura)"""
        return self.__fecha_registro

    def obtener_nombre_completo(self):
        """
        Método público que retorna el nombre completo
        """
        return f"{self.nombre} {self.apellido}"

    @abstractmethod
    def mostrar_informacion(self):
        """
        Método abstracto que debe ser implementado por las clases hijas
        Demuestra: Polimorfismo
        """
        pass


class Empleado(Persona):
    """
    Clase derivada de Persona que representa un empleado.
    Demuestra: Herencia, Polimorfismo
    """

    # Atributo de clase
    contador_empleados = 0

    def __init__(self, nombre, apellido, edad, dni, puesto, salario_base):
        """
        Constructor de la clase Empleado

        Args:
            nombre (str): Nombre del empleado
            apellido (str): Apellido del empleado
            edad (int): Edad del empleado
            dni (str): DNI del empleado
            puesto (str): Puesto de trabajo
            salario_base (float): Salario base del empleado
        """
        # Llamada al constructor de la clase padre (Herencia)
        super().__init__(nombre, apellido, edad, dni)

        self.puesto = puesto
        self._salario_base = self._validar_salario(salario_base)

        # Incrementar contador de empleados
        Empleado.contador_empleados += 1
        self._id_empleado = Empleado.contador_empleados

    def _validar_salario(self, salario):
        """
        Método protegido para validar el salario
        Demuestra: Encapsulación
        """
        if salario < 0:
            raise ValueError("El salario no puede ser negativo")
        return salario

    @property
    def salario_base(self):
        """Getter para el salario base"""
        return self._salario_base

    @salario_base.setter
    def salario_base(self, nuevo_salario):
        """Setter para el salario base con validación"""
        self._salario_base = self._validar_salario(nuevo_salario)

    @property
    def id_empleado(self):
        """Getter para el ID del empleado (solo lectura)"""
        return self._id_empleado

    def calcular_salario(self):
        """
        Método base para calcular el salario
        Puede ser sobrescrito por clases hijas (Polimorfismo)
        """
        return self._salario_base

    def mostrar_informacion(self):
        """
        Implementación del método abstracto de la clase padre
        Demuestra: Polimorfismo
        """
        return (f"Empleado ID: {self._id_empleado}\n"
                f"Nombre: {self.obtener_nombre_completo()}\n"
                f"Edad: {self.edad} años\n"
                f"DNI: {self.dni}\n"
                f"Puesto: {self.puesto}\n"
                f"Salario: ${self.calcular_salario():,.2f}\n"
                f"Fecha de registro: {self.fecha_registro.strftime('%d/%m/%Y %H:%M')}")


class EmpleadoTiempoCompleto(Empleado):
    """
    Clase que representa un empleado de tiempo completo.
    Demuestra: Herencia múltiple, Polimorfismo
    """

    def __init__(self, nombre, apellido, edad, dni, puesto, salario_base, bono_anual=0):
        """
        Constructor para empleado de tiempo completo

        Args:
            bono_anual (float): Bono anual adicional
        """
        super().__init__(nombre, apellido, edad, dni, puesto, salario_base)
        self._bono_anual = bono_anual

    @property
    def bono_anual(self):
        """Getter para el bono anual"""
        return self._bono_anual

    @bono_anual.setter
    def bono_anual(self, nuevo_bono):
        """Setter para el bono anual"""
        if nuevo_bono < 0:
            raise ValueError("El bono no puede ser negativo")
        self._bono_anual = nuevo_bono

    def calcular_salario(self):
        """
        Sobrescribe el método de la clase padre
        Demuestra: Polimorfismo
        """
        salario_mensual = self._salario_base + (self._bono_anual / 12)
        return salario_mensual

    def mostrar_informacion(self):
        """
        Extiende el método de la clase padre
        Demuestra: Polimorfismo
        """
        info_base = super().mostrar_informacion()
        return (f"{info_base}\n"
                f"Tipo: Tiempo Completo\n"
                f"Bono Anual: ${self._bono_anual:,.2f}")


class EmpleadoMedioTiempo(Empleado):
    """
    Clase que representa un empleado de medio tiempo.
    Demuestra: Herencia, Polimorfismo
    """

    def __init__(self, nombre, apellido, edad, dni, puesto, tarifa_por_hora, horas_semanales=20):
        """
        Constructor para empleado de medio tiempo

        Args:
            tarifa_por_hora (float): Tarifa por hora trabajada
            horas_semanales (int): Horas trabajadas por semana
        """
        # Calcular salario base mensual
        salario_mensual = tarifa_por_hora * horas_semanales * 4
        super().__init__(nombre, apellido, edad, dni, puesto, salario_mensual)

        self._tarifa_por_hora = tarifa_por_hora
        self._horas_semanales = horas_semanales

    @property
    def tarifa_por_hora(self):
        """Getter para la tarifa por hora"""
        return self._tarifa_por_hora

    @property
    def horas_semanales(self):
        """Getter para las horas semanales"""
        return self._horas_semanales

    def calcular_salario(self, horas_extras=0):
        """
        Calcula el salario incluyendo horas extras
        Demuestra: Polimorfismo (sobrecarga de métodos)

        Args:
            horas_extras (int): Horas extras trabajadas en el mes
        """
        salario_base = self._tarifa_por_hora * self._horas_semanales * 4
        pago_extras = horas_extras * self._tarifa_por_hora * 1.5  # 50% más por horas extras
        return salario_base + pago_extras

    def mostrar_informacion(self):
        """
        Sobrescribe el método de la clase padre
        Demuestra: Polimorfismo
        """
        info_base = super().mostrar_informacion()
        return (f"{info_base}\n"
                f"Tipo: Medio Tiempo\n"
                f"Tarifa por hora: ${self._tarifa_por_hora:,.2f}\n"
                f"Horas semanales: {self._horas_semanales}")


class GestorEmpleados:
    """
    Clase para gestionar una colección de empleados.
    Demuestra: Composición, Polimorfismo
    """

    def __init__(self):
        """Constructor del gestor de empleados"""
        self._empleados = []  # Lista privada de empleados

    def agregar_empleado(self, empleado):
        """
        Agrega un empleado a la lista

        Args:
            empleado (Empleado): Instancia de empleado a agregar
        """
        if isinstance(empleado, Empleado):
            self._empleados.append(empleado)
            print(f"Empleado {empleado.obtener_nombre_completo()} agregado exitosamente.")
        else:
            raise TypeError("Solo se pueden agregar objetos de tipo Empleado")

    def mostrar_todos_los_empleados(self):
        """
        Muestra información de todos los empleados
        Demuestra: Polimorfismo (mismo método, comportamientos diferentes)
        """
        if not self._empleados:
            print("No hay empleados registrados.")
            return

        print("=== LISTADO DE EMPLEADOS ===")
        for i, empleado in enumerate(self._empleados, 1):
            print(f"\n--- Empleado {i} ---")
            print(empleado.mostrar_informacion())

    def buscar_empleado_por_dni(self, dni):
        """
        Busca un empleado por su DNI

        Args:
            dni (str): DNI del empleado a buscar

        Returns:
            Empleado: El empleado encontrado o None
        """
        for empleado in self._empleados:
            if empleado.dni == dni:
                return empleado
        return None

    def calcular_nomina_total(self):
        """
        Calcula el total de la nómina
        Demuestra: Polimorfismo (diferentes tipos de empleados, mismo método)
        """
        total = sum(empleado.calcular_salario() for empleado in self._empleados)
        return total

    def obtener_estadisticas(self):
        """
        Obtiene estadísticas de los empleados
        """
        if not self._empleados:
            return "No hay empleados para mostrar estadísticas."

        total_empleados = len(self._empleados)
        tiempo_completo = sum(1 for emp in self._empleados if isinstance(emp, EmpleadoTiempoCompleto))
        medio_tiempo = sum(1 for emp in self._empleados if isinstance(emp, EmpleadoMedioTiempo))
        nomina_total = self.calcular_nomina_total()
        salario_promedio = nomina_total / total_empleados

        return (f"=== ESTADÍSTICAS ===\n"
                f"Total de empleados: {total_empleados}\n"
                f"Empleados tiempo completo: {tiempo_completo}\n"
                f"Empleados medio tiempo: {medio_tiempo}\n"
                f"Nómina total mensual: ${nomina_total:,.2f}\n"
                f"Salario promedio: ${salario_promedio:,.2f}")


def demostrar_polimorfismo(*empleados):
    """
    Función que demuestra polimorfismo usando argumentos variables

    Args:
        *empleados: Número variable de empleados
    """
    print("\n=== DEMOSTRACIÓN DE POLIMORFISMO ===")
    for empleado in empleados:
        print(f"\nProcesando empleado: {empleado.obtener_nombre_completo()}")
        print(f"Salario calculado: ${empleado.calcular_salario():,.2f}")
        print("-" * 50)


def main():
    """
    Función principal que demuestra todos los conceptos de POO
    """
    print("=== SISTEMA DE GESTIÓN DE EMPLEADOS ===")
    print("Demostrando conceptos de POO en Python\n")

    # Crear gestor de empleados
    gestor = GestorEmpleados()

    try:
        # Crear empleados de tiempo completo
        emp1 = EmpleadoTiempoCompleto(
            "Juan", "Pérez", 30, "12345678",
            "Desarrollador Senior", 5000, 12000
        )

        emp2 = EmpleadoTiempoCompleto(
            "María", "García", 28, "87654321",
            "Gerente de Proyectos", 7000, 18000
        )

        # Crear empleados de medio tiempo
        emp3 = EmpleadoMedioTiempo(
            "Carlos", "López", 25, "11111111",
            "Diseñador Gráfico", 25, 20
        )

        emp4 = EmpleadoMedioTiempo(
            "Ana", "Martínez", 22, "22222222",
            "Asistente de Marketing", 20, 15
        )

        # Agregar empleados al gestor
        for empleado in [emp1, emp2, emp3, emp4]:
            gestor.agregar_empleado(empleado)

        # Demostrar encapsulación
        print("\n=== DEMOSTRACIÓN DE ENCAPSULACIÓN ===")
        print(f"Empleado 1 - Edad actual: {emp1.edad}")
        emp1.edad = 31  # Usar setter con validación
        print(f"Empleado 1 - Nueva edad: {emp1.edad}")

        print(f"Empleado 1 - Salario actual: ${emp1.salario_base:,.2f}")
        emp1.salario_base = 5500  # Usar setter con validación
        print(f"Empleado 1 - Nuevo salario: ${emp1.salario_base:,.2f}")

        # Mostrar todos los empleados
        gestor.mostrar_todos_los_empleados()

        # Demostrar polimorfismo con argumentos variables
        demostrar_polimorfismo(emp1, emp2, emp3, emp4)

        # Demostrar polimorfismo con sobrecarga (empleado medio tiempo con horas extras)
        print(f"\nEmpleado medio tiempo sin horas extras: ${emp3.calcular_salario():,.2f}")
        print(f"Empleado medio tiempo con 10 horas extras: ${emp3.calcular_salario(10):,.2f}")

        # Mostrar estadísticas
        print(f"\n{gestor.obtener_estadisticas()}")

        # Demostrar búsqueda
        print("\n=== BÚSQUEDA DE EMPLEADO ===")
        empleado_encontrado = gestor.buscar_empleado_por_dni("12345678")
        if empleado_encontrado:
            print("Empleado encontrado:")
            print(empleado_encontrado.mostrar_informacion())

        # Mostrar información de clase
        print(f"\nTotal de empleados creados: {Empleado.contador_empleados}")

    except ValueError as e:
        print(f"Error de validación: {e}")
    except TypeError as e:
        print(f"Error de tipo: {e}")
    except Exception as e:
        print(f"Error inesperado: {e}")


if __name__ == "__main__":
    main()
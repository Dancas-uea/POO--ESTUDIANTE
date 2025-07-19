from abc import ABC, abstractmethod

# ---------------------------
# S - Single Responsibility Principle (Responsabilidad Única)
# Cada clase tiene UNA sola responsabilidad.
# ---------------------------

# Clase abstracta que define el contrato para cualquier tipo de notificación
# Aplica también LSP porque cualquier subclase debe comportarse como esta clase base.
class Notificacion(ABC):
    @abstractmethod
    def enviar(self, mensaje: str):
        pass

# Clase concreta que se encarga SOLO de enviar notificaciones por Email
class NotificacionEmail(Notificacion):
    def enviar(self, mensaje: str):
        print(f"Enviando email: {mensaje}")

# Clase concreta que se encarga SOLO de enviar notificaciones por SMS
class NotificacionSMS(Notificacion):
    def enviar(self, mensaje: str):
        print(f"Enviando SMS: {mensaje}")

# Clase concreta que se encarga SOLO de enviar notificaciones por WhatsApp
class NotificacionWhatsApp(Notificacion):
    def enviar(self, mensaje: str):
        print(f"Enviando WhatsApp: {mensaje}")

# ---------------------------
# D - Dependency Inversion Principle (Inversión de Dependencias)
# ServicioNotificacion depende de la abstracción (Notificacion), no de las clases concretas.
# ---------------------------

class ServicioNotificacion:
    def __init__(self, notificador: Notificacion):
        # Inyectamos una implementación de Notificacion, sin importar cuál.
        # Esto permite cambiar el tipo de notificación sin modificar esta clase.
        self.notificador = notificador

    def procesar_mensaje(self, mensaje: str):
        # Se llama al método enviar definido por la clase concreta que se haya inyectado.
        self.notificador.enviar(mensaje)

# ---------------------------
# Uso del sistema
# Demuestra también O - Open/Closed Principle (Abierto/Cerrado)
# El sistema está abierto para extender (añadir nuevas clases como Telegram)
# sin modificar las clases ya existentes.
# ---------------------------

# Creamos distintas instancias del servicio, inyectando diferentes notificaciones
email = ServicioNotificacion(NotificacionEmail())        # Email
sms = ServicioNotificacion(NotificacionSMS())            # SMS
whatsapp = ServicioNotificacion(NotificacionWhatsApp())  # WhatsApp

# ---------------------------
# Polimorfismo:
# Todas las clases Notificacion implementan el mismo método 'enviar'
# con comportamientos diferentes (sobreescritura).
# ---------------------------

# Se usa la misma interfaz, pero cada tipo se comporta diferente
email.procesar_mensaje("Tu suscripción fue activada.")
sms.procesar_mensaje("Código de verificación: 123456")
whatsapp.procesar_mensaje("¡Tu pedido está en camino!")
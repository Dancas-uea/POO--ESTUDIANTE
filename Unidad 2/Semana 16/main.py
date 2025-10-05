import tkinter as tk
from tkinter import ttk, messagebox
from gui_inventario import VentanaProductos


class SistemaInventario:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Sistema de Gestión de Inventario - UEA")
        self.root.geometry("600x400")
        self.root.configure(bg='#2c3e50')

        # Configurar atajo de teclado para salir
        self.root.bind('<Escape>', lambda e: self.salir())

        self.crear_interfaz_principal()

    def crear_interfaz_principal(self):
        # Frame principal
        main_frame = ttk.Frame(self.root, padding="20")
        main_frame.pack(fill=tk.BOTH, expand=True)

        # Información del estudiante
        info_frame = ttk.LabelFrame(main_frame, text="Información del Estudiante", padding="15")
        info_frame.pack(fill=tk.X, pady=(0, 20))

        datos_estudiante = [
            ("Integrantes:", "Carlos Castillo, Luis Gomez, Marcos Delgado"),
            ("Carrera:", "Ingeniería en Tecnologías de la Información"),
            ("Paralelo:", "A"),
            ("Asignatura:", "Programación Orientada a Objetos"),
            ("Práctica:", "Sistema de Gestión de Inventario")
        ]

        for i, (campo, valor) in enumerate(datos_estudiante):
            ttk.Label(info_frame, text=campo, font=('Arial', 10, 'bold')).grid(
                row=i, column=0, sticky=tk.W, padx=(0, 10), pady=2)
            ttk.Label(info_frame, text=valor, font=('Arial', 10)).grid(
                row=i, column=1, sticky=tk.W, pady=2)

        # Título del sistema
        titulo = ttk.Label(main_frame,
                           text="SISTEMA DE GESTIÓN DE INVENTARIO",
                           font=('Arial', 18, 'bold'),
                           foreground='#2c3e50')
        titulo.pack(pady=20)

        # Descripción
        descripcion = ttk.Label(main_frame,
                                text="Sistema desarrollado para la gestión eficiente de productos\n"
                                     "utilizando Programación Orientada a Objetos con Python",
                                font=('Arial', 11),
                                justify=tk.CENTER)
        descripcion.pack(pady=10)

        # Frame de botones
        btn_frame = ttk.Frame(main_frame)
        btn_frame.pack(pady=30)

        # Botón para abrir gestión de productos
        btn_productos = ttk.Button(btn_frame,
                                   text="Gestionar Productos",
                                   command=self.abrir_gestion_productos,
                                   style='Accent.TButton')
        btn_productos.pack(pady=10, ipadx=20, ipady=10)

        # Botón salir
        btn_salir = ttk.Button(btn_frame,
                               text="Salir (Esc)",
                               command=self.salir)
        btn_salir.pack(pady=5, ipadx=20, ipady=5)

        # Configurar estilo para botón destacado
        style = ttk.Style()
        style.configure('Accent.TButton', font=('Arial', 12, 'bold'))

    def abrir_gestion_productos(self):
        VentanaProductos(self.root)

    def salir(self):
        if messagebox.askyesno("Salir", "¿Está seguro de que desea salir del sistema?"):
            self.root.quit()

    def ejecutar(self):
        self.root.mainloop()


if __name__ == "__main__":
    app = SistemaInventario()
    app.ejecutar()
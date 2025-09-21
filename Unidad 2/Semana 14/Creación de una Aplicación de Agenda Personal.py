import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import DateEntry
from datetime import datetime


class AgendaPersonal:
    def __init__(self, root):
        self.root = root
        self.root.title("Agenda Personal")
        self.root.geometry("800x600")
        self.root.resizable(True, True)

        # Configuración de estilo
        self.style = ttk.Style()
        self.style.theme_use("clam")

        # Lista para almacenar eventos
        self.eventos = []

        # Crear la interfaz
        self.crear_interfaz()

    def crear_interfaz(self):
        # Frame principal
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # Configurar grid para que se expanda
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        main_frame.columnconfigure(1, weight=1)
        main_frame.rowconfigure(1, weight=1)

        # Título
        titulo = ttk.Label(main_frame, text="Agenda Personal", font=("Arial", 16, "bold"))
        titulo.grid(row=0, column=0, columnspan=3, pady=(0, 15))

        # Frame para entrada de datos
        input_frame = ttk.LabelFrame(main_frame, text="Nuevo Evento", padding="10")
        input_frame.grid(row=1, column=0, columnspan=3, sticky=(tk.W, tk.E), pady=(0, 10))
        input_frame.columnconfigure(1, weight=1)

        # Etiqueta y campo para fecha
        ttk.Label(input_frame, text="Fecha:").grid(row=0, column=0, sticky=tk.W, padx=(0, 5), pady=5)
        self.fecha_entry = DateEntry(input_frame, width=12, background='darkblue',
                                     foreground='white', borderwidth=2, date_pattern='yyyy-mm-dd')
        self.fecha_entry.grid(row=0, column=1, sticky=(tk.W, tk.E), padx=(0, 10), pady=5)

        # Etiqueta y campo para hora
        ttk.Label(input_frame, text="Hora:").grid(row=0, column=2, sticky=tk.W, padx=(0, 5), pady=5)
        self.hora_entry = ttk.Entry(input_frame, width=10)
        self.hora_entry.grid(row=0, column=3, sticky=(tk.W, tk.E), padx=(0, 10), pady=5)
        self.hora_entry.insert(0, "00:00")  # Valor por defecto

        # Etiqueta y campo para descripción
        ttk.Label(input_frame, text="Descripción:").grid(row=1, column=0, sticky=tk.W, padx=(0, 5), pady=5)
        self.descripcion_entry = ttk.Entry(input_frame, width=40)
        self.descripcion_entry.grid(row=1, column=1, columnspan=3, sticky=(tk.W, tk.E), pady=5)

        # Frame para botones
        button_frame = ttk.Frame(input_frame)
        button_frame.grid(row=2, column=0, columnspan=4, pady=(10, 0))

        # Botón para agregar evento
        agregar_btn = ttk.Button(button_frame, text="Agregar Evento", command=self.agregar_evento)
        agregar_btn.pack(side=tk.LEFT, padx=(0, 10))

        # Botón para limpiar campos
        limpiar_btn = ttk.Button(button_frame, text="Limpiar Campos", command=self.limpiar_campos)
        limpiar_btn.pack(side=tk.LEFT)

        # Frame para la lista de eventos
        list_frame = ttk.LabelFrame(main_frame, text="Eventos Programados", padding="10")
        list_frame.grid(row=2, column=0, columnspan=3, sticky=(tk.W, tk.E, tk.N, tk.S), pady=(10, 0))
        list_frame.columnconfigure(0, weight=1)
        list_frame.rowconfigure(0, weight=1)

        # Treeview para mostrar eventos
        columns = ('fecha', 'hora', 'descripcion')
        self.tree = ttk.Treeview(list_frame, columns=columns, show='headings')

        # Definir columnas
        self.tree.heading('fecha', text='Fecha')
        self.tree.heading('hora', text='Hora')
        self.tree.heading('descripcion', text='Descripción')

        # Ajustar anchos de columnas
        self.tree.column('fecha', width=100, anchor=tk.CENTER)
        self.tree.column('hora', width=80, anchor=tk.CENTER)
        self.tree.column('descripcion', width=400, anchor=tk.W)

        # Scrollbar para el treeview
        scrollbar = ttk.Scrollbar(list_frame, orient=tk.VERTICAL, command=self.tree.yview)
        self.tree.configure(yscroll=scrollbar.set)

        # Colocar treeview y scrollbar en la interfaz
        self.tree.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        scrollbar.grid(row=0, column=1, sticky=(tk.N, tk.S))

        # Frame para botones de acción
        action_frame = ttk.Frame(main_frame)
        action_frame.grid(row=3, column=0, columnspan=3, pady=(15, 0))

        # Botón para eliminar evento seleccionado
        eliminar_btn = ttk.Button(action_frame, text="Eliminar Evento Seleccionado", command=self.eliminar_evento)
        eliminar_btn.pack(side=tk.LEFT, padx=(0, 10))

        # Botón para salir
        salir_btn = ttk.Button(action_frame, text="Salir", command=self.root.quit)
        salir_btn.pack(side=tk.LEFT)

        # Bind para doble click en un evento
        self.tree.bind('<Double-1>', self.editar_evento)

    def agregar_evento(self):
        """Agrega un nuevo evento a la lista"""
        fecha = self.fecha_entry.get_date().strftime("%Y-%m-%d")
        hora = self.hora_entry.get()
        descripcion = self.descripcion_entry.get().strip()

        # Validar campos
        if not fecha:
            messagebox.showerror("Error", "Por favor, seleccione una fecha.")
            return

        if not self.validar_hora(hora):
            messagebox.showerror("Error", "Por favor, ingrese una hora válida en formato HH:MM.")
            return

        if not descripcion:
            messagebox.showerror("Error", "Por favor, ingrese una descripción.")
            return

        # Agregar evento a la lista
        self.eventos.append({
            'fecha': fecha,
            'hora': hora,
            'descripcion': descripcion
        })

        # Actualizar treeview
        self.actualizar_treeview()

        # Limpiar campos
        self.limpiar_campos()

        messagebox.showinfo("Éxito", "Evento agregado correctamente.")

    def eliminar_evento(self):
        """Elimina el evento seleccionado"""
        seleccion = self.tree.selection()
        if not seleccion:
            messagebox.showwarning("Advertencia", "Por favor, seleccione un evento para eliminar.")
            return

        # Confirmar eliminación
        if messagebox.askyesno("Confirmar", "¿Está seguro de que desea eliminar el evento seleccionado?"):
            # Obtener índice del elemento seleccionado
            index = int(seleccion[0].lstrip('I')) - 1

            # Eliminar evento de la lista
            if 0 <= index < len(self.eventos):
                del self.eventos[index]

            # Actualizar treeview
            self.actualizar_treeview()

    def editar_evento(self, event):
        """Permite editar un evento existente al hacer doble clic sobre él"""
        seleccion = self.tree.selection()
        if not seleccion:
            return

        # Obtener índice del elemento seleccionado
        index = int(seleccion[0].lstrip('I')) - 1

        if 0 <= index < len(self.eventos):
            evento = self.eventos[index]

            # Crear ventana de edición
            self.crear_ventana_edicion(evento, index)

    def crear_ventana_edicion(self, evento, index):
        """Crea una ventana para editar un evento existente"""
        ventana_edicion = tk.Toplevel(self.root)
        ventana_edicion.title("Editar Evento")
        ventana_edicion.geometry("400x200")
        ventana_edicion.resizable(False, False)
        ventana_edicion.transient(self.root)
        ventana_edicion.grab_set()

        # Frame principal
        frame = ttk.Frame(ventana_edicion, padding="10")
        frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # Configurar grid
        ventana_edicion.columnconfigure(0, weight=1)
        ventana_edicion.rowconfigure(0, weight=1)
        frame.columnconfigure(1, weight=1)

        # Etiqueta y campo para fecha
        ttk.Label(frame, text="Fecha:").grid(row=0, column=0, sticky=tk.W, padx=(0, 5), pady=5)
        fecha_entry = DateEntry(frame, width=12, background='darkblue',
                                foreground='white', borderwidth=2, date_pattern='yyyy-mm-dd')
        fecha_entry.grid(row=0, column=1, sticky=(tk.W, tk.E), padx=(0, 10), pady=5)
        fecha_entry.set_date(datetime.strptime(evento['fecha'], "%Y-%m-%d"))

        # Etiqueta y campo para hora
        ttk.Label(frame, text="Hora:").grid(row=1, column=0, sticky=tk.W, padx=(0, 5), pady=5)
        hora_entry = ttk.Entry(frame, width=10)
        hora_entry.grid(row=1, column=1, sticky=tk.W, padx=(0, 10), pady=5)
        hora_entry.insert(0, evento['hora'])

        # Etiqueta y campo para descripción
        ttk.Label(frame, text="Descripción:").grid(row=2, column=0, sticky=tk.W, padx=(0, 5), pady=5)
        descripcion_entry = ttk.Entry(frame, width=30)
        descripcion_entry.grid(row=2, column=1, sticky=(tk.W, tk.E), padx=(0, 10), pady=5)
        descripcion_entry.insert(0, evento['descripcion'])

        # Frame para botones
        button_frame = ttk.Frame(frame)
        button_frame.grid(row=3, column=0, columnspan=2, pady=(15, 0))

        # Botón para guardar cambios
        def guardar_cambios():
            nueva_fecha = fecha_entry.get_date().strftime("%Y-%m-%d")
            nueva_hora = hora_entry.get()
            nueva_descripcion = descripcion_entry.get().strip()

            # Validar campos
            if not self.validar_hora(nueva_hora):
                messagebox.showerror("Error", "Por favor, ingrese una hora válida en formato HH:MM.")
                return

            if not nueva_descripcion:
                messagebox.showerror("Error", "Por favor, ingrese una descripción.")
                return

            # Actualizar evento
            self.eventos[index] = {
                'fecha': nueva_fecha,
                'hora': nueva_hora,
                'descripcion': nueva_descripcion
            }

            # Actualizar treeview
            self.actualizar_treeview()

            # Cerrar ventana de edición
            ventana_edicion.destroy()

            messagebox.showinfo("Éxito", "Evento actualizado correctamente.")

        guardar_btn = ttk.Button(button_frame, text="Guardar Cambios", command=guardar_cambios)
        guardar_btn.pack(side=tk.LEFT, padx=(0, 10))

        # Botón para cancelar
        cancelar_btn = ttk.Button(button_frame, text="Cancelar", command=ventana_edicion.destroy)
        cancelar_btn.pack(side=tk.LEFT)

    def actualizar_treeview(self):
        """Actualiza el treeview con la lista actual de eventos"""
        # Limpiar treeview
        for item in self.tree.get_children():
            self.tree.delete(item)

        # Ordenar eventos por fecha y hora
        eventos_ordenados = sorted(self.eventos, key=lambda x: (x['fecha'], x['hora']))

        # Agregar eventos al treeview
        for evento in eventos_ordenados:
            self.tree.insert('', tk.END, values=(evento['fecha'], evento['hora'], evento['descripcion']))

    def limpiar_campos(self):
        """Limpia los campos de entrada"""
        self.descripcion_entry.delete(0, tk.END)

    def validar_hora(self, hora_str):
        """Valida que el formato de hora sea correcto (HH:MM)"""
        try:
            datetime.strptime(hora_str, "%H:%M")
            return True
        except ValueError:
            return False


def main():
    root = tk.Tk()
    app = AgendaPersonal(root)
    root.mainloop()


if __name__ == "__main__":
    main()
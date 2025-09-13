import tkinter as tk
from tkinter import ttk, messagebox


class AplicacionTareas:
    def __init__(self, root):
        """
        Inicializa la aplicación con todos sus componentes GUI.

        Args:
            root: La ventana principal de Tkinter
        """
        self.root = root
        self.root.title("Gestor de Tareas - Aplicación GUI")
        self.root.geometry("600x400")
        self.root.resizable(True, True)

        # Configurar estilo para los componentes
        self.style = ttk.Style()
        self.style.theme_use('clam')

        # Inicializar lista de tareas
        self.tareas = []

        # Configurar la interfaz
        self.configurar_interfaz()

    def configurar_interfaz(self):
        """Configura todos los componentes de la interfaz gráfica."""
        # Marco principal para organizar los elementos
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # Configurar expansión de filas y columnas
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        main_frame.columnconfigure(1, weight=1)
        main_frame.rowconfigure(3, weight=1)

        # Título de la aplicación
        titulo = ttk.Label(main_frame, text="Gestor de Tareas",
                           font=("Arial", 16, "bold"))
        titulo.grid(row=0, column=0, columnspan=2, pady=(0, 15))

        # Etiqueta y campo de texto para nueva tarea
        ttk.Label(main_frame, text="Nueva tarea:").grid(
            row=1, column=0, sticky=tk.W, pady=(0, 5))

        self.entrada_tarea = ttk.Entry(main_frame, width=40)
        self.entrada_tarea.grid(
            row=1, column=1, sticky=(tk.W, tk.E), pady=(0, 5))
        self.entrada_tarea.bind("<Return>", lambda e: self.agregar_tarea())

        # Marco para los botones
        botones_frame = ttk.Frame(main_frame)
        botones_frame.grid(row=2, column=0, columnspan=2, pady=(0, 10))
        botones_frame.columnconfigure(0, weight=1)
        botones_frame.columnconfigure(1, weight=1)
        botones_frame.columnconfigure(2, weight=1)

        # Botón para agregar tarea
        self.boton_agregar = ttk.Button(
            botones_frame, text="Agregar", command=self.agregar_tarea)
        self.boton_agregar.grid(row=0, column=0, padx=5)

        # Botón para limpiar
        self.boton_limpiar = ttk.Button(
            botones_frame, text="Limpiar", command=self.limpiar_todo)
        self.boton_limpiar.grid(row=0, column=1, padx=5)

        # Botón para eliminar tarea seleccionada
        self.boton_eliminar = ttk.Button(
            botones_frame, text="Eliminar Selección",
            command=self.eliminar_tarea)
        self.boton_eliminar.grid(row=0, column=2, padx=5)

        # Etiqueta para la lista de tareas
        ttk.Label(main_frame, text="Tareas:").grid(
            row=3, column=0, sticky=tk.W, pady=(0, 5))

        # Lista de tareas con scrollbar
        list_frame = ttk.Frame(main_frame)
        list_frame.grid(row=4, column=0, columnspan=2, sticky=(tk.W, tk.E, tk.N, tk.S))
        list_frame.columnconfigure(0, weight=1)
        list_frame.rowconfigure(0, weight=1)

        # Scrollbar para la lista
        scrollbar = ttk.Scrollbar(list_frame)
        scrollbar.grid(row=0, column=1, sticky=(tk.N, tk.S))

        # Listbox para mostrar las tareas
        self.lista_tareas = tk.Listbox(
            list_frame, yscrollcommand=scrollbar.set,
            selectmode=tk.SINGLE, height=15)
        self.lista_tareas.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # Configurar scrollbar
        scrollbar.config(command=self.lista_tareas.yview)

        # Contador de tareas
        self.contador_tareas = ttk.Label(main_frame, text="Total de tareas: 0")
        self.contador_tareas.grid(row=5, column=0, columnspan=2, pady=(10, 0))

    def agregar_tarea(self):
        """
        Agrega una nueva tarea a la lista a partir del texto en el campo de entrada.
        Valida que el campo no esté vacío antes de agregar.
        """
        tarea = self.entrada_tarea.get().strip()

        if tarea:
            self.tareas.append(tarea)
            self.actualizar_lista_tareas()
            self.entrada_tarea.delete(0, tk.END)  # Limpiar el campo de entrada
        else:
            messagebox.showwarning("Campo vacío", "Por favor, ingresa una tarea.")

    def eliminar_tarea(self):
        """
        Elimina la tarea seleccionada de la lista.
        Pide confirmación antes de eliminar.
        """
        seleccion = self.lista_tareas.curselection()

        if seleccion:
            indice = seleccion[0]
            tarea = self.tareas[indice]

            if messagebox.askyesno(
                    "Confirmar eliminación",
                    f"¿Estás seguro de que quieres eliminar la tarea: '{tarea}'?"):
                del self.tareas[indice]
                self.actualizar_lista_tareas()
        else:
            messagebox.showinfo(
                "Sin selección", "Por favor, selecciona una tarea para eliminar.")

    def limpiar_todo(self):
        """
        Limpia todas las tareas de la lista después de pedir confirmación.
        """
        if self.tareas:
            if messagebox.askyesno(
                    "Confirmar limpieza",
                    "¿Estás seguro de que quieres eliminar todas las tareas?"):
                self.tareas.clear()
                self.actualizar_lista_tareas()
        else:
            messagebox.showinfo("Lista vacía", "No hay tareas para limpiar.")

    def actualizar_lista_tareas(self):
        """
        Actualiza el Listbox con las tareas actuales y el contador.
        """
        self.lista_tareas.delete(0, tk.END)

        for tarea in self.tareas:
            self.lista_tareas.insert(tk.END, tarea)

        # Actualizar el contador
        self.contador_tareas.config(text=f"Total de tareas: {len(self.tareas)}")


def main():
    """
    Función principal que inicia la aplicación GUI.
    """
    root = tk.Tk()
    app = AplicacionTareas(root)
    root.mainloop()


if __name__ == "__main__":
    main()
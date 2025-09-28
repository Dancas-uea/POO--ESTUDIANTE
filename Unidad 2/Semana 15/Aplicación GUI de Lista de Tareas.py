import tkinter as tk
from tkinter import ttk, messagebox


class TodoApp:
    def __init__(self, root):
        """
        Inicializa la aplicación de lista de tareas.

        Args:
            root: Ventana principal de Tkinter
        """
        self.root = root
        self.root.title("Gestor de Tareas")
        self.root.geometry("500x400")
        self.root.resizable(True, True)

        # Lista para almacenar las tareas
        self.tasks = []

        # Configurar la interfaz
        self.setup_ui()

        # Vincular evento Enter en el campo de entrada
        self.entry_task.bind('<Return>', lambda event: self.add_task())

    def setup_ui(self):
        """Configura todos los elementos de la interfaz de usuario."""

        # Frame principal para organizar los elementos
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # Configurar grid weights para que sea responsive
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        main_frame.columnconfigure(1, weight=1)
        main_frame.rowconfigure(1, weight=1)

        # Campo de entrada para nuevas tareas
        ttk.Label(main_frame, text="Nueva Tarea:").grid(row=0, column=0, sticky=tk.W, pady=5)
        self.entry_task = ttk.Entry(main_frame, width=40)
        self.entry_task.grid(row=0, column=1, sticky=(tk.W, tk.E), pady=5, padx=(5, 0))

        # Botón para añadir tarea
        self.btn_add = ttk.Button(main_frame, text="Añadir Tarea", command=self.add_task)
        self.btn_add.grid(row=0, column=2, padx=(5, 0), pady=5)

        # Frame para la lista de tareas
        list_frame = ttk.Frame(main_frame)
        list_frame.grid(row=1, column=0, columnspan=3, sticky=(tk.W, tk.E, tk.N, tk.S), pady=10)
        list_frame.columnconfigure(0, weight=1)
        list_frame.rowconfigure(0, weight=1)

        # Listbox para mostrar las tareas con scrollbar
        self.listbox_tasks = tk.Listbox(
            list_frame,
            height=15,
            selectmode=tk.SINGLE,
            font=('Arial', 10)
        )

        # Scrollbar para la lista
        scrollbar = ttk.Scrollbar(list_frame, orient=tk.VERTICAL, command=self.listbox_tasks.yview)
        self.listbox_tasks.configure(yscrollcommand=scrollbar.set)

        self.listbox_tasks.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        scrollbar.grid(row=0, column=1, sticky=(tk.N, tk.S))

        # Vincular doble clic para marcar como completada
        self.listbox_tasks.bind('<Double-Button-1>', lambda event: self.mark_completed())

        # Frame para botones de acción
        button_frame = ttk.Frame(main_frame)
        button_frame.grid(row=2, column=0, columnspan=3, pady=10)

        # Botones de acción
        self.btn_mark = ttk.Button(
            button_frame,
            text="Marcar como Completada",
            command=self.mark_completed,
            state=tk.DISABLED
        )
        self.btn_mark.grid(row=0, column=0, padx=5)

        self.btn_delete = ttk.Button(
            button_frame,
            text="Eliminar Tarea",
            command=self.delete_task,
            state=tk.DISABLED
        )
        self.btn_delete.grid(row=0, column=1, padx=5)

        self.btn_clear = ttk.Button(
            button_frame,
            text="Limpiar Completadas",
            command=self.clear_completed
        )
        self.btn_clear.grid(row=0, column=2, padx=5)

        # Vincular selección de lista para habilitar/deshabilitar botones
        self.listbox_tasks.bind('<<ListboxSelect>>', self.on_task_select)

    def add_task(self):
        """
        Añade una nueva tarea a la lista.
        Se puede llamar desde el botón o presionando Enter.
        """
        task_text = self.entry_task.get().strip()

        if task_text:
            # Añadir tarea a la lista interna
            self.tasks.append({
                'text': task_text,
                'completed': False
            })

            # Actualizar la lista visual
            self.update_task_list()

            # Limpiar el campo de entrada
            self.entry_task.delete(0, tk.END)

            # Enfocar el campo de entrada para nueva tarea
            self.entry_task.focus()
        else:
            messagebox.showwarning("Advertencia", "Por favor, escribe una tarea.")

    def mark_completed(self):
        """
        Marca la tarea seleccionada como completada.
        Se puede llamar desde el botón o con doble clic.
        """
        selected_index = self.get_selected_index()

        if selected_index is not None:
            # Cambiar estado de completado
            self.tasks[selected_index]['completed'] = not self.tasks[selected_index]['completed']

            # Actualizar la lista visual
            self.update_task_list()

    def delete_task(self):
        """Elimina la tarea seleccionada de la lista."""
        selected_index = self.get_selected_index()

        if selected_index is not None:
            # Confirmar eliminación
            if messagebox.askyesno("Confirmar", "¿Estás seguro de que quieres eliminar esta tarea?"):
                # Eliminar tarea
                del self.tasks[selected_index]

                # Actualizar la lista visual
                self.update_task_list()

    def clear_completed(self):
        """Elimina todas las tareas marcadas como completadas."""
        # Filtrar solo las tareas no completadas
        self.tasks = [task for task in self.tasks if not task['completed']]

        # Actualizar la lista visual
        self.update_task_list()

    def update_task_list(self):
        """Actualiza el Listbox con las tareas actuales."""
        # Limpiar lista actual
        self.listbox_tasks.delete(0, tk.END)

        # Añadir cada tarea con formato según su estado
        for task in self.tasks:
            task_text = task['text']

            if task['completed']:
                # Tarea completada - tachada y en color gris
                task_text = f"✓ {task_text}"
                self.listbox_tasks.insert(tk.END, task_text)
                self.listbox_tasks.itemconfig(tk.END, {'fg': 'gray'})
            else:
                # Tarea pendiente - normal
                self.listbox_tasks.insert(tk.END, f"○ {task_text}")

        # Deshabilitar botones si no hay selección
        self.update_button_states()

    def get_selected_index(self):
        """
        Obtiene el índice de la tarea seleccionada.

        Returns:
            int or None: Índice de la tarea seleccionada o None si no hay selección
        """
        selection = self.listbox_tasks.curselection()
        return selection[0] if selection else None

    def on_task_select(self, event):
        """
        Maneja el evento de selección de tarea.
        Habilita/deshabilita botones según la selección.
        """
        self.update_button_states()

    def update_button_states(self):
        """Actualiza el estado de los botones según la selección actual."""
        has_selection = self.get_selected_index() is not None

        # Habilitar botones solo si hay una tarea seleccionada
        self.btn_mark.config(state=tk.NORMAL if has_selection else tk.DISABLED)
        self.btn_delete.config(state=tk.NORMAL if has_selection else tk.DISABLED)


def main():
    """
    Función principal que inicia la aplicación.
    """
    # Crear ventana principal
    root = tk.Tk()

    # Crear la aplicación
    app = TodoApp(root)

    # Iniciar el loop principal
    root.mainloop()


if __name__ == "__main__":
    main()
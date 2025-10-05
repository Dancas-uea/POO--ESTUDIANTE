import tkinter as tk
from tkinter import ttk, messagebox
from inventario import Inventario
from producto import Producto


class VentanaProductos:
    def __init__(self, parent):
        self.parent = parent
        self.inventario = Inventario()

        self.ventana = tk.Toplevel(parent)
        self.ventana.title("Gestión de Productos - Sistema de Inventario")
        self.ventana.geometry("800x600")
        self.ventana.configure(bg='#f0f0f0')
        self.ventana.transient(parent)  # Hacerla dependiente de la principal
        self.ventana.grab_set()  # Modal
        self.ventana.focus_set()  # Enfocar esta ventana

        # Configurar atajos de teclado
        self.ventana.bind('<Delete>', lambda e: self.eliminar_producto_seleccionado())
        self.ventana.bind('<d>', lambda e: self.eliminar_producto_seleccionado())
        self.ventana.bind('<Escape>', lambda e: self.ventana.destroy())

        self.crear_widgets()
        self.actualizar_lista()

    def crear_widgets(self):
        # Frame principal
        main_frame = ttk.Frame(self.ventana, padding="10")
        main_frame.pack(fill=tk.BOTH, expand=True)

        # Configurar grid weights
        self.ventana.columnconfigure(0, weight=1)
        self.ventana.rowconfigure(0, weight=1)
        main_frame.columnconfigure(1, weight=1)
        main_frame.rowconfigure(1, weight=1)

        # Título
        titulo = ttk.Label(main_frame, text="GESTIÓN DE PRODUCTOS",
                           font=('Arial', 16, 'bold'))
        titulo.grid(row=0, column=0, columnspan=2, pady=(0, 20))

        # Frame de formulario (IZQUIERDA)
        form_frame = ttk.LabelFrame(main_frame, text="Datos del Producto", padding="10")
        form_frame.grid(row=1, column=0, sticky=(tk.W, tk.E, tk.N, tk.S), padx=(0, 10))

        # Campos del formulario
        ttk.Label(form_frame, text="ID:").grid(row=0, column=0, sticky=tk.W, pady=5)
        self.entry_id = ttk.Entry(form_frame, width=20)
        self.entry_id.grid(row=0, column=1, sticky=(tk.W, tk.E), pady=5)

        ttk.Label(form_frame, text="Nombre:").grid(row=1, column=0, sticky=tk.W, pady=5)
        self.entry_nombre = ttk.Entry(form_frame, width=20)
        self.entry_nombre.grid(row=1, column=1, sticky=(tk.W, tk.E), pady=5)

        ttk.Label(form_frame, text="Cantidad:").grid(row=2, column=0, sticky=tk.W, pady=5)
        self.entry_cantidad = ttk.Entry(form_frame, width=20)
        self.entry_cantidad.grid(row=2, column=1, sticky=(tk.W, tk.E), pady=5)

        ttk.Label(form_frame, text="Precio:").grid(row=3, column=0, sticky=tk.W, pady=5)
        self.entry_precio = ttk.Entry(form_frame, width=20)
        self.entry_precio.grid(row=3, column=1, sticky=(tk.W, tk.E), pady=5)

        form_frame.columnconfigure(1, weight=1)

        # Botones del formulario
        btn_frame_form = ttk.Frame(form_frame)
        btn_frame_form.grid(row=4, column=0, columnspan=2, pady=(15, 0))

        ttk.Button(btn_frame_form, text="Agregar Producto",
                   command=self.agregar_producto).pack(side=tk.LEFT, padx=(0, 5))
        ttk.Button(btn_frame_form, text="Modificar Producto",
                   command=self.modificar_producto).pack(side=tk.LEFT, padx=5)
        ttk.Button(btn_frame_form, text="Limpiar Campos",
                   command=self.limpiar_formulario).pack(side=tk.LEFT, padx=5)

        # Frame de lista de productos (DERECHA)
        list_frame = ttk.LabelFrame(main_frame, text="Lista de Productos", padding="10")
        list_frame.grid(row=1, column=1, sticky=(tk.W, tk.E, tk.N, tk.S))

        # TreeView para mostrar productos
        columns = ('ID', 'Nombre', 'Cantidad', 'Precio')
        self.tree = ttk.Treeview(list_frame, columns=columns, show='headings', height=15)

        # Configurar columnas
        self.tree.heading('ID', text='ID')
        self.tree.heading('Nombre', text='Nombre')
        self.tree.heading('Cantidad', text='Cantidad')
        self.tree.heading('Precio', text='Precio ($)')

        self.tree.column('ID', width=80)
        self.tree.column('Nombre', width=150)
        self.tree.column('Cantidad', width=80)
        self.tree.column('Precio', width=100)

        # Scrollbar
        scrollbar = ttk.Scrollbar(list_frame, orient=tk.VERTICAL, command=self.tree.yview)
        self.tree.configure(yscrollcommand=scrollbar.set)

        self.tree.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        scrollbar.grid(row=0, column=1, sticky=(tk.N, tk.S))

        # Bind evento de selección
        self.tree.bind('<<TreeviewSelect>>', self.on_seleccion)

        # Botones de acción (ABAJO)
        action_frame = ttk.Frame(main_frame)
        action_frame.grid(row=2, column=0, columnspan=2, pady=(20, 0))

        ttk.Button(action_frame, text="Eliminar Producto Seleccionado (Delete/D)",
                   command=self.eliminar_producto_seleccionado).pack(side=tk.LEFT, padx=5)
        ttk.Button(action_frame, text="Actualizar Lista",
                   command=self.actualizar_lista).pack(side=tk.LEFT, padx=5)
        ttk.Button(action_frame, text="Cerrar Ventana (Esc)",
                   command=self.ventana.destroy).pack(side=tk.LEFT, padx=5)

        # Configurar pesos de grid
        list_frame.columnconfigure(0, weight=1)
        list_frame.rowconfigure(0, weight=1)
        main_frame.columnconfigure(1, weight=1)
        main_frame.rowconfigure(1, weight=1)

    # Los métodos restantes se mantienen igual...
    def agregar_producto(self):
        try:
            id_producto = self.entry_id.get().strip()
            nombre = self.entry_nombre.get().strip()
            cantidad = int(self.entry_cantidad.get())
            precio = float(self.entry_precio.get())

            if not id_producto or not nombre:
                messagebox.showerror("Error", "ID y Nombre son campos obligatorios")
                return

            producto = Producto(id_producto, nombre, cantidad, precio)
            self.inventario.agregar_producto(producto)
            self.actualizar_lista()
            self.limpiar_formulario()
            messagebox.showinfo("Éxito", "Producto agregado correctamente")

        except ValueError as e:
            messagebox.showerror("Error", f"Datos inválidos: {e}")
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo agregar el producto: {e}")

    def modificar_producto(self):
        seleccion = self.tree.selection()
        if not seleccion:
            messagebox.showwarning("Advertencia", "Seleccione un producto para modificar")
            return

        try:
            item = seleccion[0]
            id_actual = self.tree.item(item, 'values')[0]

            nombre = self.entry_nombre.get().strip()
            cantidad = int(self.entry_cantidad.get())
            precio = float(self.entry_precio.get())

            if not nombre:
                messagebox.showerror("Error", "El nombre es obligatorio")
                return

            self.inventario.modificar_producto(id_actual, nombre, cantidad, precio)
            self.actualizar_lista()
            self.limpiar_formulario()
            messagebox.showinfo("Éxito", "Producto modificado correctamente")

        except ValueError as e:
            messagebox.showerror("Error", f"Datos inválidos: {e}")
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo modificar el producto: {e}")

    def eliminar_producto_seleccionado(self):
        seleccion = self.tree.selection()
        if not seleccion:
            messagebox.showwarning("Advertencia", "Seleccione un producto para eliminar")
            return

        if messagebox.askyesno("Confirmar", "¿Está seguro de eliminar el producto seleccionado?"):
            item = seleccion[0]
            id_producto = self.tree.item(item, 'values')[0]

            if self.inventario.eliminar_producto(id_producto):
                self.actualizar_lista()
                self.limpiar_formulario()
                messagebox.showinfo("Éxito", "Producto eliminado correctamente")
            else:
                messagebox.showerror("Error", "No se pudo eliminar el producto")

    def on_seleccion(self, event):
        seleccion = self.tree.selection()
        if seleccion:
            item = seleccion[0]
            valores = self.tree.item(item, 'values')
            self.entry_id.delete(0, tk.END)
            self.entry_id.insert(0, valores[0])
            self.entry_nombre.delete(0, tk.END)
            self.entry_nombre.insert(0, valores[1])
            self.entry_cantidad.delete(0, tk.END)
            self.entry_cantidad.insert(0, valores[2])
            self.entry_precio.delete(0, tk.END)
            self.entry_precio.insert(0, valores[3])

    def actualizar_lista(self):
        # Limpiar treeview
        for item in self.tree.get_children():
            self.tree.delete(item)

        # Agregar productos
        productos = self.inventario.obtener_todos_productos()
        for producto in productos:
            self.tree.insert('', tk.END, values=(
                producto.id,
                producto.nombre,
                producto.cantidad,
                f"{producto.precio:.2f}"
            ))

    def limpiar_formulario(self):
        self.entry_id.delete(0, tk.END)
        self.entry_nombre.delete(0, tk.END)
        self.entry_cantidad.delete(0, tk.END)
        self.entry_precio.delete(0, tk.END)
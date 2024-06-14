# Archivo: filesystem_app.py

import tkinter as tk
from tkinter import ttk, messagebox
from filesystem import FileSystem
from comandos_basicos.mkdir import mkdir
from comandos_basicos.file import create_file
from comandos_basicos.cambiar_dir import change_directory
from comandos_basicos.listar_dir import list_directory
from comandos_basicos.mover import move
from comandos_basicos.copiar import copy
from comandos_basicos.find import find
from comandos_basicos.ver import view_file
from comandos_basicos.editar import edit_file
from comandos_basicos.tree import show_tree
from comandos_basicos.ver_propiedades import show_file_properties
from comandos_basicos.eliminar import delete_file, delete_directory

class FileSystemApp:
    def __init__(self, root):
        self.root = root
        self.root.title("File System")
        self.create_widgets()
        
    def create_widgets(self):
        # Configurar el estilo
        style = ttk.Style()
        style.configure('TButton', padding=6, relief='flat', background='#ccc')
        style.configure('TLabel', padding=5, background='#eee')
        style.configure('TFrame', background='#eee')
        
        # Frame principal
        main_frame = ttk.Frame(self.root, padding="10 10 10 10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Frame izquierdo para controles
        control_frame = ttk.Frame(main_frame, padding="10 10 10 10", borderwidth=2, relief='solid')
        control_frame.grid(row=0, column=0, sticky=(tk.N, tk.S, tk.W, tk.E))
        
        # Etiqueta y entrada para el número de sectores
        self.sectors_label = ttk.Label(control_frame, text="Número de Sectores:")
        self.sectors_label.grid(row=0, column=0, sticky=tk.W, pady=2)
        self.sectors_entry = ttk.Entry(control_frame)
        self.sectors_entry.grid(row=0, column=1, pady=2)

        # Etiqueta y entrada para el tamaño de los sectores
        self.sectorsize_label = ttk.Label(control_frame, text="Tamaño de los Sectores (bytes):")
        self.sectorsize_label.grid(row=1, column=0, sticky=tk.W, pady=2)
        self.sectorsize_entry = ttk.Entry(control_frame)
        self.sectorsize_entry.grid(row=1, column=1, pady=2)

        # Botón para crear el disco
        self.create_button = ttk.Button(control_frame, text="Crear Disco", command=self.create_disk)
        self.create_button.grid(row=2, column=0, columnspan=2, pady=5)

        # Botón para mostrar los sectores del disco
        self.show_sectors_button = ttk.Button(control_frame, text="Mostrar Sectores", command=self.show_sectors)
        self.show_sectors_button.grid(row=3, column=0, columnspan=2, pady=5)

        # Frame para los comandos básicos
        commands_frame = ttk.Frame(control_frame, padding="10 10 10 10", borderwidth=2, relief='solid')
        commands_frame.grid(row=4, column=0, columnspan=2, pady=10, sticky=(tk.W, tk.E, tk.N, tk.S))

        # Botones para los comandos básicos
        self.mkdir_button = ttk.Button(commands_frame, text="Crear Directorio (mkdir)", command=self.create_directory)
        self.mkdir_button.grid(row=0, column=0, pady=2, sticky=(tk.W, tk.E))

        self.create_file_button = ttk.Button(commands_frame, text="Crear Archivo (file)", command=self.create_new_file)
        self.create_file_button.grid(row=1, column=0, pady=2, sticky=(tk.W, tk.E))

        self.change_dir_button = ttk.Button(commands_frame, text="Cambiar Directorio (cd)", command=self.change_dir)
        self.change_dir_button.grid(row=2, column=0, pady=2, sticky=(tk.W, tk.E))

        self.list_dir_button = ttk.Button(commands_frame, text="Listar Directorio (ls)", command=self.list_dir)
        self.list_dir_button.grid(row=3, column=0, pady=2, sticky=(tk.W, tk.E))

        self.move_button = ttk.Button(commands_frame, text="Mover (mv)", command=self.move)
        self.move_button.grid(row=4, column=0, pady=2, sticky=(tk.W, tk.E))

        self.copy_button = ttk.Button(commands_frame, text="Copiar (cp)", command=self.copy)
        self.copy_button.grid(row=5, column=0, pady=2, sticky=(tk.W, tk.E))

        self.find_button = ttk.Button(commands_frame, text="Buscar (find)", command=self.find)
        self.find_button.grid(row=6, column=0, pady=2, sticky=(tk.W, tk.E))

        # Botón para ver archivos
        self.view_button = ttk.Button(commands_frame, text="Ver Archivo (view)", command=self.view_file)
        self.view_button.grid(row=0, column=1, pady=2, sticky=(tk.W, tk.E))

        # Botón para editar archivos
        self.edit_button = ttk.Button(commands_frame, text="Editar Archivo (edit)", command=self.edit_file)
        self.edit_button.grid(row=1, column=1, pady=2, sticky=(tk.W, tk.E))

        # Botón para ver propiedades de un archivo
        self.show_properties_button = ttk.Button(commands_frame, text="Ver Propiedades de Archivo", command=self.show_file_properties)
        self.show_properties_button.grid(row=2, column=1, pady=2, sticky=(tk.W, tk.E))
        
        # Botón para eliminar un archivo
        self.delete_button = ttk.Button(commands_frame, text="Eliminar (del)", command=self.delete_file)
        self.delete_button.grid(row=3, column=1, pady=2, sticky=(tk.W, tk.E))

        # Botón para mostrar el árbol
        self.show_tree_button = ttk.Button(commands_frame, text="Árbol (Tree)", command=self.show_directory_tree)
        self.show_tree_button.grid(row=4, column=1, pady=2, sticky=(tk.W, tk.E))

        # Botón para limpiar la pantalla de salida
        self.clear_output_button = ttk.Button(commands_frame, text="Limpiar Pantalla", command=self.clear_output)
        self.clear_output_button.grid(row=5, column=1, pady=2, sticky=(tk.W, tk.E))

        # Botón para regresar al root
        self.back_to_root_button = ttk.Button(commands_frame, text="Raíz (Root)", command=self.back_to_root)
        self.back_to_root_button.grid(row=6, column=1, pady=2, sticky=(tk.W, tk.E))

        # Botón para guardar el estado
        self.save_button = ttk.Button(commands_frame, text="Guardar Estado", command=self.save_state)
        self.save_button.grid(row=7, column=1, pady=2, sticky=(tk.W, tk.E))

        # Botón para cargar el estado
        self.load_button = ttk.Button(commands_frame, text="Cargar Estado", command=self.load_state)
        self.load_button.grid(row=7, column=0, pady=2, sticky=(tk.W, tk.E))

        # Frame derecho para resultados
        result_frame = ttk.Frame(main_frame, padding="10 10 10 10", borderwidth=2, relief='solid')
        result_frame.grid(row=0, column=1, sticky=(tk.N, tk.S, tk.W, tk.E))

        # Área de texto para mostrar los resultados
        self.result_text = tk.Text(result_frame, wrap=tk.WORD, width=80, height=30, bg="#f0f0f0", fg="#000")
        self.result_text.grid(row=0, column=0, pady=10, padx=10)

    def create_disk(self):
        try:
            num_sectors = int(self.sectors_entry.get())
            sector_size = int(self.sectorsize_entry.get())
            self.fs = FileSystem(num_sectors, sector_size)
            self.result_text.insert(tk.END, f"Disco creado con {num_sectors} sectores de {sector_size} bytes cada uno.\n")
        except ValueError:
            messagebox.showerror("Error", "Por favor ingrese valores válidos para los sectores y el tamaño de los sectores.")

    def show_sectors(self):
        if hasattr(self, 'fs'):
            sectors = self.fs.disk.read_all_sectors()
            self.result_text.insert(tk.END, "Contenido de los sectores:\n")
            for i, sector in enumerate(sectors):
                self.result_text.insert(tk.END, f"Sector {i}: {sector}\n")
        else:
            messagebox.showerror("Error", "Primero debe crear el disco.")

    def create_directory(self):
        if hasattr(self, 'fs'):
            dir_name = self.prompt_for_input("Ingrese el nombre del directorio:")
            if dir_name:
                success, message = mkdir(self.fs, dir_name)
                if success:
                    self.result_text.insert(tk.END, f"{message}\n")
                else:
                    overwrite = messagebox.askyesno("Sobrescribir directorio", f"{message} ¿Desea sobrescribirlo?")
                    if overwrite:
                        success, message = mkdir(self.fs, dir_name, overwrite=True)
                        self.result_text.insert(tk.END, f"{message}\n")
                    else:
                        self.result_text.insert(tk.END, "Operación cancelada.\n")
        else:
            messagebox.showerror("Error", "Primero debe crear el disco.")

    def create_new_file(self):
        if hasattr(self, 'fs'):
            file_name = self.prompt_for_input("Ingrese el nombre del archivo (sin extensión):")
            extension = self.prompt_for_input("Ingrese la extensión del archivo:")
            content = self.prompt_for_input("Ingrese el contenido del archivo:")
            if file_name and extension:
                success, message = create_file(self.fs, file_name, extension, content)
                if success:
                    self.result_text.insert(tk.END, f"{message}\n")
                else:
                    overwrite = messagebox.askyesno("Sobrescribir archivo", f"{message} ¿Desea sobrescribirlo?")
                    if overwrite:
                        success, message = create_file(self.fs, file_name, extension, content, overwrite=True)
                        self.result_text.insert(tk.END, f"{message}\n")
                    else:
                        self.result_text.insert(tk.END, "Operación cancelada.\n")
        else:
            messagebox.showerror("Error", "Primero debe crear el disco.")

    def change_dir(self):
        if hasattr(self, 'fs'):
            dir_name = self.prompt_for_input("Ingrese el nombre del directorio:")
            if dir_name:
                change_directory(self.fs, dir_name)
                self.result_text.insert(tk.END, f"Directorio actual: {self.fs.current_directory.name}\n")
        else:
            messagebox.showerror("Error", "Primero debe crear el disco.")

    def list_dir(self):
        if hasattr(self, 'fs'):
            result = list_directory(self.fs)
            self.result_text.insert(tk.END, result)
        else:
            messagebox.showerror("Error", "Primero debe crear el disco.")

    def move(self):
        if hasattr(self, 'fs'):
            src = self.prompt_for_input("Ingrese la ruta de origen:")
            dest = self.prompt_for_input("Ingrese la ruta de destino:")
            if src and dest:
                move(self.fs, src, dest)
                self.result_text.insert(tk.END, f"'{src}' movido a '{dest}'.\n")
        else:
            messagebox.showerror("Error", "Primero debe crear el disco.")

    def copy(self):
        if hasattr(self, 'fs'):
            src = self.prompt_for_input("Ingrese la ruta de origen:")
            dest = self.prompt_for_input("Ingrese la ruta de destino:")
            if src and dest:
                copy(self.fs, src, dest)
                self.result_text.insert(tk.END, f"'{src}' copiado a '{dest}'.\n")
        else:
            messagebox.showerror("Error", "Primero debe crear el disco.")

    def find(self):
        if hasattr(self, 'fs'):
            pattern = self.prompt_for_input("Ingrese el patrón de búsqueda:")
            if pattern:
                result = find(self.fs, pattern)
                self.result_text.insert(tk.END, "Resultados de la búsqueda:\n")
                for path in result:
                    self.result_text.insert(tk.END, f"{path}\n")
        else:
            messagebox.showerror("Error", "Primero debe crear el disco.")

    def view_file(self):
        if hasattr(self, 'fs'):
            file_path = self.prompt_for_input("Ingrese la ruta del archivo a ver:")
            if file_path:
                content = view_file(self.fs, file_path)
                self.result_text.insert(tk.END, f"Contenido del archivo '{file_path}':\n{content}\n")
        else:
            messagebox.showerror("Error", "Primero debe crear el disco.")

    def edit_file(self):
        if hasattr(self, 'fs'):
            file_path = self.prompt_for_input("Ingrese la ruta del archivo a editar:")
            new_content = self.prompt_for_input("Ingrese el nuevo contenido del archivo:")
            if file_path and new_content:
                result = edit_file(self.fs, file_path, new_content)
                self.result_text.insert(tk.END, f"{result}\n")
        else:
            messagebox.showerror("Error", "Primero debe crear el disco.")

    def clear_output(self):
        self.result_text.delete('1.0', tk.END)

    def delete_file(self):
        if hasattr(self, 'fs'):
            choice = messagebox.askquestion("Eliminar", "¿Desea eliminar un archivo o un directorio?", icon='warning')
            if choice == 'yes':
                item_type = self.prompt_for_input("Ingrese 1 para eliminar un archivo o 2 para eliminar un directorio:")
                if item_type == '1':
                    file_name = self.prompt_for_input("Ingrese el nombre del archivo (sin extensión):")
                    extension = self.prompt_for_input("Ingrese la extensión del archivo:")
                    if file_name and extension:
                        delete_file(self.fs, file_name, extension)
                        self.result_text.insert(tk.END, f"Archivo {file_name}.{extension} eliminado.\n")
                elif item_type == '2':
                    dir_name = self.prompt_for_input("Ingrese el nombre del directorio a eliminar:")
                    if dir_name:
                        delete_directory(self.fs, dir_name)
                        self.result_text.insert(tk.END, f"Directorio {dir_name} eliminado.\n")
                else:
                    messagebox.showerror("Error", "Entrada no válida. Debe ingresar 'archivo' o 'directorio'.")
        else:
            messagebox.showerror("Error", "Primero debe crear el disco.")

    def save_state(self):
        if hasattr(self, 'fs'):
            self.fs.save_state()
            self.result_text.insert(tk.END, "Estado del sistema de archivos guardado.\n")
        else:
            messagebox.showerror("Error", "Primero debe crear el disco.")

    def load_state(self):
        try:
            self.fs = FileSystem.load_state()
            self.result_text.insert(tk.END, "Estado del sistema de archivos cargado.\n")
        except FileNotFoundError:
            messagebox.showerror("Error", "No se encontró un estado guardado.")
        except Exception as e:
            messagebox.showerror("Error", f"Error al cargar el estado: {e}")

    def prompt_for_input(self, prompt):
        input_dialog = tk.Toplevel(self.root)
        input_dialog.title(prompt)
        ttk.Label(input_dialog, text=prompt).pack(pady=10, padx=10)
        input_entry = ttk.Entry(input_dialog)
        input_entry.pack(pady=10, padx=10)
        input_entry.focus_set()

        def on_ok(event=None):
            input_dialog.input_value = input_entry.get()
            input_dialog.destroy()

        input_entry.bind("<Return>", on_ok)
        ttk.Button(input_dialog, text="OK", command=on_ok).pack(pady=10, padx=10)
        self.root.wait_window(input_dialog)
        return getattr(input_dialog, 'input_value', None)
    
    # Función para mostrar el árbol
    def show_directory_tree(self):
        if hasattr(self, 'fs'):
            tree = show_tree(self.fs)
            self.result_text.insert(tk.END, "Árbol:\n")
            self.result_text.insert(tk.END, tree)
        else:
            messagebox.showerror("Error", "Primero debe crear el disco.")

    # Función para volver al root
    def back_to_root(self):
        if hasattr(self, 'fs'):
            self.fs.current_directory = self.fs.root
            self.result_text.insert(tk.END, "Regresando a la raíz... '/'\n")
        else:
            messagebox.showerror("Error", "Primero debe crear el disco.")

    # Función mostrar propiedades
    def show_file_properties(self):
        if hasattr(self, 'fs'):
            file_name = self.prompt_for_input("Ingrese el nombre del archivo (sin extensión):")
            extension = self.prompt_for_input("Ingrese la extensión del archivo:")
            if file_name and extension:
                show_file_properties(self.fs, file_name, extension)
        else:
            messagebox.showerror("Error", "Primero debe crear el disco.")

if __name__ == "__main__":
    root = tk.Tk()
    app = FileSystemApp(root)
    root.mainloop()

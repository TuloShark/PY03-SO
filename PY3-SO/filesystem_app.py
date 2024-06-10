# Archivo: filesystem_app.py

import tkinter as tk
from tkinter import messagebox
from filesystem import FileSystem
from comandos_basicos.mkdir import mkdir
from comandos_basicos.file import create_file
from comandos_basicos.cambiar_dir import change_directory
from comandos_basicos.listar_dir import list_directory

# Clase que representa la aplicación del sistema de archivos
class FileSystemApp:
    def __init__(self, root):
        self.root = root  # Ventana principal
        self.root.title("File System")  # Título de la ventana
        self.create_widgets()  # Crear los elementos de la interfaz

    # Crear los elementos de la interfaz gráfica
    def create_widgets(self):
        # Etiqueta y entrada para el número de sectores
        self.sectors_label = tk.Label(self.root, text="Número de Sectores:")
        self.sectors_label.pack()
        self.sectors_entry = tk.Entry(self.root)
        self.sectors_entry.pack()

        # Etiqueta y entrada para el tamaño de los sectores
        self.sectorsize_label = tk.Label(self.root, text="Tamaño de los Sectores (bytes):")
        self.sectorsize_label.pack()
        self.sectorsize_entry = tk.Entry(self.root)
        self.sectorsize_entry.pack()

        # Botón para crear el disco
        self.create_button = tk.Button(self.root, text="Crear Disco", command=self.create_disk)
        self.create_button.pack()

        # Botón para mostrar los sectores del disco
        self.show_sectors_button = tk.Button(self.root, text="Mostrar Sectores", command=self.show_sectors)
        self.show_sectors_button.pack()

        # Botones para los comandos básicos
        self.mkdir_button = tk.Button(self.root, text="Crear Directorio (mkdir)", command=self.create_directory)
        self.mkdir_button.pack()

        self.create_file_button = tk.Button(self.root, text="Crear Archivo (file)", command=self.create_new_file)
        self.create_file_button.pack()

        self.change_dir_button = tk.Button(self.root, text="Cambiar Directorio (cd)", command=self.change_dir)
        self.change_dir_button.pack()

        self.list_dir_button = tk.Button(self.root, text="Listar Directorio (ls)", command=self.list_dir)
        self.list_dir_button.pack()

        # Área de texto para mostrar los resultados
        self.result_text = tk.Text(self.root)
        self.result_text.pack()

    # Método para crear el disco
    def create_disk(self):
        try:
            num_sectors = int(self.sectors_entry.get())  # Obtener número de sectores
            sector_size = int(self.sectorsize_entry.get())  # Obtener tamaño de los sectores
            self.fs = FileSystem(num_sectors, sector_size)  # Crear el sistema de archivos
            self.result_text.insert(tk.END, f"Disco creado con {num_sectors} sectores de {sector_size} bytes cada uno.\n")
        except ValueError:
            messagebox.showerror("Error", "Por favor ingrese valores válidos para los sectores y el tamaño de los sectores.")

    # Método para mostrar los sectores del disco
    def show_sectors(self):
        if hasattr(self, 'fs'):
            sectors = self.fs.disk.read_all_sectors()
            self.result_text.insert(tk.END, "Contenido de los sectores:\n")
            for i, sector in enumerate(sectors):
                self.result_text.insert(tk.END, f"Sector {i}: {sector}\n")
        else:
            messagebox.showerror("Error", "Primero debe crear el disco.")

    # Método para crear un nuevo directorio
    def create_directory(self):
        if hasattr(self, 'fs'):
            dir_name = self.prompt_for_input("Ingrese el nombre del directorio:")
            if dir_name:
                mkdir(self.fs, dir_name)
                self.result_text.insert(tk.END, f"Directorio '{dir_name}' creado.\n")
        else:
            messagebox.showerror("Error", "Primero debe crear el disco.")

    # Método para crear un nuevo archivo
    def create_new_file(self):
        if hasattr(self, 'fs'):
            file_name = self.prompt_for_input("Ingrese el nombre del archivo (sin extensión):")
            extension = self.prompt_for_input("Ingrese la extensión del archivo:")
            content = self.prompt_for_input("Ingrese el contenido del archivo:")
            if file_name and extension:
                create_file(self.fs, file_name, extension, content)
                self.result_text.insert(tk.END, f"Archivo '{file_name}.{extension}' creado con contenido: {content}\n")
        else:
            messagebox.showerror("Error", "Primero debe crear el disco.")

    # Método para cambiar de directorio
    def change_dir(self):
        if hasattr(self, 'fs'):
            dir_name = self.prompt_for_input("Ingrese el nombre del directorio:")
            if dir_name:
                change_directory(self.fs, dir_name)
                self.result_text.insert(tk.END, f"Directorio actual: {self.fs.current_directory.name}\n")
        else:
            messagebox.showerror("Error", "Primero debe crear el disco.")

    # Método para listar el contenido del directorio actual
    def list_dir(self):
        if hasattr(self, 'fs'):
            result = list_directory(self.fs)
            self.result_text.insert(tk.END, result)
        else:
            messagebox.showerror("Error", "Primero debe crear el disco.")

    # Método para mostrar un cuadro de diálogo de entrada
    def prompt_for_input(self, prompt):
        input_dialog = tk.Toplevel(self.root)
        input_dialog.title(prompt)
        tk.Label(input_dialog, text=prompt).pack()
        input_entry = tk.Entry(input_dialog)
        input_entry.pack()
        input_entry.focus_set()

        def on_ok():
            input_dialog.input_value = input_entry.get()
            input_dialog.destroy()

        tk.Button(input_dialog, text="OK", command=on_ok).pack()
        self.root.wait_window(input_dialog)
        return getattr(input_dialog, 'input_value', None)

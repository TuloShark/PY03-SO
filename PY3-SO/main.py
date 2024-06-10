# Archivo: main.py

import tkinter as tk
from filesystem_app import FileSystemApp

# Método principal
if __name__ == "__main__":
    root = tk.Tk()  # Crear la ventana principal
    app = FileSystemApp(root)  # Crear la aplicación
    root.mainloop()  # Ejecutar la aplicación

# Archivo: comandos_basicos/ver_propiedades.py

import tkinter as tk
from tkinter import ttk, messagebox
from directory_and_file import File  # Importar la clase File
import time  # Importar el módulo time

def show_file_properties(fs, file_name, extension):
    """
    Muestra las propiedades de un archivo en el sistema de archivos.

    :param fs: Instancia del sistema de archivos.
    :param file_name: Nombre del archivo del cual se desea ver las propiedades.
    :param extension: Extensión del archivo.
    """
    result = find_file(fs.root, file_name, extension)
    if result:
        path, file_obj = result
        messagebox.showinfo("Propiedades del Archivo",
                            f"Nombre: {file_name}.{extension}\n"
                            f"Extensión: {extension}\n"
                            f"Tamaño: {file_obj.size} bytes\n"
                            f"Ruta: {path}\n"
                            f"Fecha de Creación: {format_timestamp(file_obj.creation_date)}\n"
                            f"Fecha de Modificación: {format_timestamp(file_obj.modification_date)}")
    else:
        messagebox.showerror("Error", f"El archivo '{file_name}.{extension}' no existe en el directorio actual.")

def format_timestamp(timestamp):
    """
    Formatea un timestamp de UNIX a una cadena de fecha y hora legible.

    :param timestamp: Timestamp de UNIX.
    :return: Cadena formateada de fecha y hora.
    """
    import time
    return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(timestamp))

def find_file(current_dir, file_name, extension):
    """
    Busca un archivo en el sistema de archivos recursivamente y devuelve su ruta y objeto File si se encuentra.

    :param current_dir: Directorio actual de búsqueda.
    :param file_name: Nombre del archivo a buscar.
    :param extension: Extensión del archivo a buscar.
    :return: Tupla (ruta, objeto File) si se encuentra el archivo, None si no se encuentra.
    """
    from fnmatch import fnmatch

    if file_name in current_dir.files:
        file_obj = current_dir.files[file_name]
        if file_obj.extension == extension:
            return f"{current_dir.name}/{file_name}.{extension}", file_obj

    for dir_name, dir_obj in current_dir.subdirectories.items():
        result = find_file(dir_obj, file_name, extension)
        if result:
            return f"{current_dir.name}/{result[0]}", result[1]

    return None

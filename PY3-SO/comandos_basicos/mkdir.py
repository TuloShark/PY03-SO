# Archivo: comandos_basicos/mkdir.py

from directory_and_file import Directory  # Importar la clase Directory
import time  # Importar el módulo time

def mkdir(fs, dir_name):
    """
    Crea un nuevo directorio en el directorio actual del sistema de archivos.
    
    :param fs: Instancia del sistema de archivos.
    :param dir_name: Nombre del nuevo directorio a crear.
    """
    if dir_name in fs.current_directory.subdirectories:
        print(f"Directory {dir_name} already exists.")
    else:
        new_dir = Directory(dir_name, fs.current_directory)  # Agregar referencia al directorio padre
        fs.current_directory.subdirectories[dir_name] = new_dir
        fs.current_directory.modification_date = time.time()
        print(f"Directory {dir_name} creado.")

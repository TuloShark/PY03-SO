# Archivo: comandos_basicos/mkdir.py

from directory_and_file import Directory
import time

def mkdir(fs, dir_name, overwrite=False):
    """
    Crea un nuevo directorio en el directorio actual del sistema de archivos.
    
    :param fs: Instancia del sistema de archivos.
    :param dir_name: Nombre del nuevo directorio a crear.
    :param overwrite: Indica si se debe sobrescribir un directorio existente.
    """
    if dir_name in fs.current_directory.subdirectories:
        if not overwrite:
            print(f"El directorio '{dir_name}' ya existe.")
            return False
    new_dir = Directory(dir_name, fs.current_directory)
    fs.current_directory.subdirectories[dir_name] = new_dir
    fs.current_directory.modification_date = time.time()
    print(f"Directorio '{dir_name}' creado.")
    return True

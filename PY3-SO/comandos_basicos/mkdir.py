from directory_and_file import Directory  # Importar la clase Directory
import time  # Importar el módulo time

def mkdir(fs, dir_name, overwrite=False):
    """
    Crea un nuevo directorio en el directorio actual del sistema de archivos.
    
    :param fs: Instancia del sistema de archivos.
    :param dir_name: Nombre del nuevo directorio a crear.
    :param overwrite: Indica si se debe sobrescribir un directorio existente.
    :return: Tuple indicando éxito y mensaje.
    """
    if dir_name in fs.current_directory.subdirectories:
        if not overwrite:
            return False, f"El directorio '{dir_name}' ya existe."
        else:
            del fs.current_directory.subdirectories[dir_name]
    new_dir = Directory(dir_name, fs.current_directory)  # Agregar referencia al directorio padre
    fs.current_directory.subdirectories[dir_name] = new_dir
    fs.current_directory.modification_date = time.time()
    return True, f"Directorio '{dir_name}' creado."

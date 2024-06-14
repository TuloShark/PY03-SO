# Archivo: comandos_basicos/ver.py

def view_file(fs, file_path):
    """
    Muestra el contenido de un archivo específico en el sistema de archivos.
    
    :param fs: Instancia del sistema de archivos.
    :param file_path: Ruta del archivo cuyo contenido se desea ver.
    :return: El contenido del archivo o un mensaje de error si no se encuentra.
    """
    file_path_parts = file_path.strip('/').split('/')
    file_name = file_path_parts[-1]

    dir = fs.root

    # Navegar a través del árbol de directorios para la ruta del archivo
    for part in file_path_parts[:-1]:
        if part in dir.subdirectories:
            dir = dir.subdirectories[part]
        else:
            return f"Ruta del archivo '{file_path}' no encontrada."

    if file_name in dir.files:
        file_obj = dir.files[file_name]
        return file_obj.content
    else:
        return f"Archivo '{file_path}' no encontrado."

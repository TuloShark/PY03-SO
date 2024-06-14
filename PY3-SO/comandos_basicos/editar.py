# Archivo: comandos_basicos/editar.py

def edit_file(fs, file_path, new_content):
    """
    Edita el contenido de un archivo específico en el sistema de archivos.
    
    :param fs: Instancia del sistema de archivos.
    :param file_path: Ruta del archivo cuyo contenido se desea editar.
    :param new_content: El nuevo contenido para el archivo.
    :return: Mensaje de éxito o de error si no se encuentra el archivo.
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
        file_obj.content = new_content
        file_obj.modification_date = time.time()
        return f"Contenido del archivo '{file_path}' actualizado."
    else:
        return f"Archivo '{file_path}' no encontrado."

# Archivo: comandos_basicos/eliminar.py

def delete_file(fs, file_path):
    """
    Elimina un archivo específico del sistema de archivos.
    
    :param fs: Instancia del sistema de archivos.
    :param file_path: Ruta del archivo a eliminar.
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
        file_obj = dir.files.pop(file_name)
        # Liberar los sectores ocupados por el archivo
        for sector in file_obj.sectors:
            fs.free_sectors.append(sector)
        return f"Archivo '{file_path}' eliminado."
    else:
        return f"Archivo '{file_path}' no encontrado."

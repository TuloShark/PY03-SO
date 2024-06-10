# Archivo: comandos_basicos/listar_dir.py

def list_directory(fs):
    """
    Lista los archivos y subdirectorios en el directorio actual del sistema de archivos.
    
    :param fs: Instancia del sistema de archivos.
    :return: Cadena con la lista de archivos y subdirectorios.
    """
    result = f"Listing directory: {fs.current_directory.name}\n"
    for dir_name in fs.current_directory.subdirectories:
        result += f"[DIR] {dir_name}\n"
    for file_name, file_obj in fs.current_directory.files.items():
        result += f"[FILE] {file_name}.{file_obj.extension}\n"
    return result

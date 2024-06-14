# Archivo: comandos_basicos/find.py

def find(fs, name_pattern):
    """
    Busca archivos y directorios por nombre o patrón en el sistema de archivos.
    
    :param fs: Instancia del sistema de archivos.
    :param name_pattern: Patrón de nombre a buscar.
    :return: Lista de rutas que coinciden con el patrón.
    """
    result = []
    _find_recursive(fs.root, name_pattern, "", result)
    return result

def _find_recursive(current_dir, name_pattern, current_path, result):
    """
    Función recursiva para buscar archivos y directorios.
    
    :param current_dir: Directorio actual.
    :param name_pattern: Patrón de nombre a buscar.
    :param current_path: Ruta actual.
    :param result: Lista de resultados.
    """
    from fnmatch import fnmatch

    for dir_name, dir_obj in current_dir.subdirectories.items():
        full_path = f"{current_path}/{dir_name}"
        if fnmatch(dir_name, name_pattern):
            result.append(full_path)
        _find_recursive(dir_obj, name_pattern, full_path, result)
    
    for file_name, file_obj in current_dir.files.items():
        full_path = f"{current_path}/{file_name}.{file_obj.extension}"
        if fnmatch(f"{file_name}.{file_obj.extension}", name_pattern):
            result.append(full_path)
        elif fnmatch(file_name, name_pattern) or fnmatch(file_obj.extension, name_pattern):
            result.append(full_path)


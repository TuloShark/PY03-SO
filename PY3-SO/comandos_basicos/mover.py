# Archivo: comandos_basicos/mover.py

def get_directory(fs, path_parts):
    """
    Navega a través de la estructura de directorios según las partes de la ruta proporcionada.

    :param fs: Instancia del sistema de archivos.
    :param path_parts: Lista de partes de la ruta.
    :return: Directorio al final de la ruta proporcionada.
    """
    directory = fs.root if path_parts[0] == '/' else fs.current_directory
    for part in path_parts:
        if part == '..':
            if directory.parent is not None:
                directory = directory.parent
        elif part in directory.subdirectories:
            directory = directory.subdirectories[part]
        else:
            return None
    return directory

def move(fs, src, dest):
    """
    Mueve un archivo o directorio de una ubicación a otra dentro del sistema de archivos.
    
    :param fs: Instancia del sistema de archivos.
    :param src: Ruta de origen del archivo o directorio.
    :param dest: Ruta de destino del archivo o directorio.
    """
    src_parts = src.split('/')
    dest_parts = dest.split('/')

    src_dir = get_directory(fs, src_parts[:-1])
    dest_dir = get_directory(fs, dest_parts[:-1])

    if src_dir is None:
        print(f"Source path '{src}' not found.")
        return

    if dest_dir is None:
        print(f"Destination path '{dest}' not found.")
        return

    src_name = src_parts[-1]
    dest_name = dest_parts[-1]

    if src_name in src_dir.files:
        file_obj = src_dir.files.pop(src_name)
        dest_dir.files[dest_name] = file_obj
        print(f"Archivo '{src}' movido a '{dest}'.")
    elif src_name in src_dir.subdirectories:
        dir_obj = src_dir.subdirectories.pop(src_name)
        dest_dir.subdirectories[dest_name] = dir_obj
        print(f"Directorio '{src}' movido a '{dest}'.")
    else:
        print(f"'{src}' no encontrado en el directorio actual.")

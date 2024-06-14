# Archivo: comandos_basicos/copiar.py

from directory_and_file import File, Directory

def copy(fs, src, dest):
    """
    Copia un archivo o directorio de una ubicación a otra dentro del sistema de archivos.
    
    :param fs: Instancia del sistema de archivos.
    :param src: Ruta de origen del archivo o directorio.
    :param dest: Ruta de destino del archivo o directorio.
    """
    src_path_parts = src.strip('/').split('/')
    dest_path_parts = dest.strip('/').split('/')

    src_name = src_path_parts[-1]
    dest_name = dest_path_parts[-1]

    src_dir = fs.root
    dest_dir = fs.root

    # Navegar a través del árbol de directorios para la ruta de origen
    for part in src_path_parts[:-1]:
        if part in src_dir.subdirectories:
            src_dir = src_dir.subdirectories[part]
        else:
            print(f"Source path '{src}' not found.")
            return

    # Navegar a través del árbol de directorios para la ruta de destino
    for part in dest_path_parts[:-1]:
        if part in dest_dir.subdirectories:
            dest_dir = dest_dir.subdirectories[part]
        else:
            print(f"Destination path '{dest}' not found.")
            return

    if src_name in src_dir.files:
        # Copiar archivo
        file_obj = src_dir.files[src_name]
        new_file_obj = File(file_obj.name, file_obj.extension, file_obj.content)
        dest_dir.files[dest_name] = new_file_obj
        print(f"Archivo '{src}' copiado a '{dest}'.")
    elif src_name in src_dir.subdirectories:
        # Copiar directorio
        dir_obj = src_dir.subdirectories[src_name]
        new_dir_obj = Directory(dir_obj.name, dir_obj.parent)
        new_dir_obj.files = dir_obj.files.copy()
        new_dir_obj.subdirectories = dir_obj.subdirectories.copy()
        dest_dir.subdirectories[dest_name] = new_dir_obj
        print(f"Directorio '{src}' copiado a '{dest}'.")
    else:
        print(f"'{src}' no encontrado en el directorio de origen.")

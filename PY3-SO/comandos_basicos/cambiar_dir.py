# Archivo: comandos_basicos/cambiar_dir.py

def change_directory(fs, dir_name):
    """
    Cambia el directorio actual en el sistema de archivos.
    
    :param fs: Instancia del sistema de archivos.
    :param dir_name: Nombre del directorio al que se desea cambiar.
    """
    if dir_name == "..":
        if fs.current_directory.parent is not None:
            fs.current_directory = fs.current_directory.parent
    elif dir_name in fs.current_directory.subdirectories:
        fs.current_directory = fs.current_directory.subdirectories[dir_name]
    else:
        print(f"Directory {dir_name} not found.")
    print(f"Current directory: {fs.current_directory.name}")

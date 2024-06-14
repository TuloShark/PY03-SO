# Archivo: comandos_basicos/eliminar.py

import time

def delete_file(fs, file_name, extension):
    """
    Elimina un archivo en el directorio actual del sistema de archivos.
    
    :param fs: Instancia del sistema de archivos.
    :param file_name: Nombre del archivo a eliminar.
    :param extension: Extensión del archivo a eliminar.
    """
    if file_name in fs.current_directory.files:
        file = fs.current_directory.files[file_name]
        if file.extension == extension:
            # Liberar los sectores ocupados por el archivo
            for sector in file.sectors:
                fs.disk.write_sector(sector, b'\x00' * fs.sector_size)  # Escribir sectores con bytes nulos
                fs.free_sectors.append(sector)
                fs.free_sectors.sort()
            del fs.current_directory.files[file_name]
            fs.current_directory.modification_date = time.time()
            print(f"Archivo {file_name}.{extension} eliminado.")
        else:
            print(f"El archivo {file_name} no tiene la extensión {extension}.")
    else:
        print(f"Archivo {file_name}.{extension} no encontrado.")

def delete_directory(fs, dir_name):
    """
    Elimina un directorio y su contenido de manera recursiva en el sistema de archivos.
    
    :param fs: Instancia del sistema de archivos.
    :param dir_name: Nombre del directorio a eliminar.
    """
    if dir_name in fs.current_directory.subdirectories:
        dir_to_delete = fs.current_directory.subdirectories[dir_name]
        _delete_directory_recursive(fs, dir_to_delete)
        del fs.current_directory.subdirectories[dir_name]
        fs.current_directory.modification_date = time.time()
        print(f"Directorio {dir_name} eliminado.")
    else:
        print(f"Directorio {dir_name} no encontrado.")

def _delete_directory_recursive(fs, directory):
    """
    Función recursiva para eliminar un directorio y su contenido.
    
    :param fs: Instancia del sistema de archivos.
    :param directory: Directorio a eliminar.
    """
    # Eliminar archivos en el directorio
    for file_name in list(directory.files.keys()):
        file = directory.files[file_name]
        for sector in file.sectors:
            fs.disk.write_sector(sector, b'\x00' * fs.sector_size)  # Escribir sectores con bytes nulos
            fs.free_sectors.append(sector)
            fs.free_sectors.sort()
        del directory.files[file_name]

    # Eliminar subdirectorios de manera recursiva
    for subdir_name in list(directory.subdirectories.keys()):
        _delete_directory_recursive(fs, directory.subdirectories[subdir_name])
        del directory.subdirectories[subdir_name]

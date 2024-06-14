# Archivo: comandos_basicos/eliminar.py

import os

def delete_file(fs, file_name, extension):
    """
    Elimina un archivo del directorio actual del sistema de archivos y libera los sectores del disco.

    :param fs: Instancia del sistema de archivos.
    :param file_name: Nombre del archivo a eliminar.
    :param extension: Extensión del archivo a eliminar.
    """
    if file_name in fs.current_directory.files:
        file_obj = fs.current_directory.files[file_name]
        if file_obj.extension == extension:
            # Liberar los sectores ocupados por el archivo
            for sector in file_obj.sectors:
                fs.free_sectors.append(sector)
                fs.free_sectors.sort()

            # Eliminar el archivo del directorio
            del fs.current_directory.files[file_name]
            fs.current_directory.modification_date = time.time()
            print(f"Archivo '{file_name}.{extension}' eliminado.")
        else:
            print(f"La extensión '{extension}' no coincide con el archivo '{file_name}'.")
    else:
        print(f"El archivo '{file_name}' no existe en el directorio actual.")

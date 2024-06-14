# Archivo: comandos_basicos/file.py

from directory_and_file import File  # Importar la clase File
import time  # Importar el módulo time

def create_file(fs, file_name, extension, content, overwrite=False):
    """
    Crea un nuevo archivo en el directorio actual del sistema de archivos y escribe su contenido en el disco.
    
    :param fs: Instancia del sistema de archivos.
    :param file_name: Nombre del archivo a crear.
    :param extension: Extensión del archivo.
    :param content: Contenido del archivo.
    :param overwrite: Indica si se debe sobrescribir un archivo existente.
    :return: Tuple indicando éxito y mensaje.
    """
    full_name = f"{file_name}"
    if full_name in fs.current_directory.files:
        if not overwrite:
            return False, f"El archivo '{full_name}' ya existe."
        else:
            del fs.current_directory.files[full_name]
    new_file = File(file_name, extension, content)
    sectors_needed = -(-len(content) // fs.sector_size)  # Ceiling division
    if len(fs.free_sectors) < sectors_needed:
        return False, "No hay suficiente espacio en el disco."
    for _ in range(sectors_needed):
        sector_index = fs.free_sectors.pop(0)
        data = content[:fs.sector_size].encode()
        fs.disk.write_sector(sector_index, data.ljust(fs.sector_size, b'\x00'))
        new_file.sectors.append(sector_index)
        content = content[fs.sector_size:]
    fs.current_directory.files[full_name] = new_file
    fs.current_directory.modification_date = time.time()
    return True, f"Archivo '{full_name}' creado con contenido: {content}"




# # Archivo: comandos_basicos/file.py

# from directory_and_file import File  # Importar la clase File
# import time  # Importar el módulo time

# def create_file(fs, file_name, extension, content):
#     """
#     Crea un nuevo archivo en el directorio actual del sistema de archivos y escribe su contenido en el disco.
    
#     :param fs: Instancia del sistema de archivos.
#     :param file_name: Nombre del archivo a crear.
#     :param extension: Extensión del archivo.
#     :param content: Contenido del archivo.
#     """
#     if file_name in fs.current_directory.files:
#         print(f"File {file_name} already exists.")
#     else:
#         new_file = File(file_name, extension, content)
#         sectors_needed = -(-len(content) // fs.sector_size)  # Ceiling division
#         if len(fs.free_sectors) < sectors_needed:
#             print("Not enough space on disk.")
#             return
#         for _ in range(sectors_needed):
#             sector_index = fs.free_sectors.pop(0)
#             data = content[:fs.sector_size].encode()
#             fs.disk.write_sector(sector_index, data.ljust(fs.sector_size, b'\x00'))
#             new_file.sectors.append(sector_index)
#             content = content[fs.sector_size:]
#         fs.current_directory.files[file_name] = new_file
#         fs.current_directory.modification_date = time.time()
#         print(f"File {file_name}.{extension} created with content: {content}")

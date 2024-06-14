# Archivo: comandos_basicos/copiar.py

import os
from directory_and_file import Directory, File
import time  # Importar el módulo time

def copy(fs, src, dest):
    """
    Copia un archivo o directorio de una ubicación a otra.

    :param fs: Instancia del sistema de archivos.
    :param src: Ruta de origen.
    :param dest: Ruta de destino.
    """
    # Ruta real a ruta virtual
    if os.path.isfile(src):
        copy_real_to_virtual(fs, src, dest)
    # Ruta virtual a ruta real
    elif dest.startswith("/"):
        copy_virtual_to_real(fs, src, dest)
    # Ruta virtual a ruta virtual
    else:
        copy_virtual_to_virtual(fs, src, dest)

def copy_real_to_virtual(fs, real_path, virtual_path):
    """
    Copia un archivo desde una ruta real de la máquina a una ruta virtual de MI File System.

    :param fs: Instancia del sistema de archivos.
    :param real_path: Ruta del archivo en el sistema de archivos real.
    :param virtual_path: Ruta del archivo en el sistema de archivos virtual.
    """
    if not os.path.isfile(real_path):
        print(f"File {real_path} does not exist.")
        return

    with open(real_path, "r") as f:
        content = f.read()

    path_parts = virtual_path.split('/')
    file_name = path_parts[-1]
    dir_path = path_parts[:-1]

    current_dir = fs.root
    for part in dir_path:
        if part in current_dir.subdirectories:
            current_dir = current_dir.subdirectories[part]
        else:
            print(f"Directory {part} does not exist.")
            return

    if file_name in current_dir.files:
        print(f"File {file_name} already exists in virtual path.")
        return

    new_file = File(file_name, os.path.splitext(file_name)[1][1:], content)
    sectors_needed = -(-len(content) // fs.sector_size)  # Ceiling division
    if len(fs.free_sectors) < sectors_needed:
        print("Not enough space on disk.")
        return
    for _ in range(sectors_needed):
        sector_index = fs.free_sectors.pop(0)
        data = content[:fs.sector_size].encode()
        fs.disk.write_sector(sector_index, data.ljust(fs.sector_size, b'\x00'))
        new_file.sectors.append(sector_index)
        content = content[fs.sector_size:]
    current_dir.files[file_name] = new_file
    current_dir.modification_date = time.time()
    print(f"File {file_name} copied to virtual path.")

def copy_virtual_to_real(fs, virtual_path, real_path):
    """
    Copia un archivo desde una ruta virtual de MI File System a una ruta real de la máquina.

    :param fs: Instancia del sistema de archivos.
    :param virtual_path: Ruta del archivo en el sistema de archivos virtual.
    :param real_path: Ruta del archivo en el sistema de archivos real.
    """
    path_parts = virtual_path.split('/')
    file_name = path_parts[-1]
    dir_path = path_parts[:-1]

    current_dir = fs.root
    for part in dir_path:
        if part in current_dir.subdirectories:
            current_dir = current_dir.subdirectories[part]
        else:
            print(f"Directory {part} does not exist.")
            return

    if file_name not in current_dir.files:
        print(f"File {file_name} does not exist in virtual path.")
        return

    file_obj = current_dir.files[file_name]

    with open(real_path, "w") as f:
        for sector_index in file_obj.sectors:
            data = fs.disk.read_sector(sector_index).decode().rstrip('\x00')
            f.write(data)
    
    print(f"File {file_name} copied to real path.")

def copy_virtual_to_virtual(fs, src, dest):
    """
    Copia un archivo desde una ruta virtual de MI File System a otra ruta virtual de MI File System.

    :param fs: Instancia del sistema de archivos.
    :param src: Ruta de origen en el sistema de archivos virtual.
    :param dest: Ruta de destino en el sistema de archivos virtual.
    """
    src_path_parts = src.split('/')
    src_file_name = src_path_parts[-1]
    src_dir_path = src_path_parts[:-1]

    dest_path_parts = dest.split('/')
    dest_file_name = dest_path_parts[-1]
    dest_dir_path = dest_path_parts[:-1]

    src_dir = fs.root
    for part in src_dir_path:
        if part in src_dir.subdirectories:
            src_dir = src_dir.subdirectories[part]
        else:
            print(f"Directory {part} does not exist.")
            return

    if src_file_name not in src_dir.files:
        print(f"File {src_file_name} does not exist in source path.")
        return

    dest_dir = fs.root
    for part in dest_dir_path:
        if part in dest_dir.subdirectories:
            dest_dir = dest_dir.subdirectories[part]
        else:
            print(f"Directory {part} does not exist.")
            return

    if dest_file_name in dest_dir.files:
        print(f"File {dest_file_name} already exists in destination path.")
        return

    file_obj = src_dir.files[src_file_name]
    new_file = File(dest_file_name, file_obj.extension, file_obj.content)
    new_file.sectors = file_obj.sectors[:]

    dest_dir.files[dest_file_name] = new_file
    dest_dir.modification_date = time.time()
    print(f"File {src_file_name} copied to {dest_file_name} in virtual path.")

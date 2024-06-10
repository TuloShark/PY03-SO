# Archivo: disk.py

import os

class Disk:
    def __init__(self, num_sectors, sector_size):
        self.num_sectors = num_sectors  # Número de sectores
        self.sector_size = sector_size  # Tamaño de cada sector
        self.disk_size = num_sectors * sector_size  # Tamaño total del disco
        self.disk_file = "virtual_disk.txt"  # Nombre del archivo que simula el disco
        self.create_disk_file()  # Crear el archivo del disco

    # Método para crear el archivo del disco
    def create_disk_file(self):
        with open(self.disk_file, "wb") as f:
            f.write(b'\x00' * self.disk_size)  # Llenar el archivo con ceros

    # Método para leer un sector del disco
    def read_sector(self, sector_index):
        with open(self.disk_file, "rb") as f:
            f.seek(sector_index * self.sector_size)  # Moverse al sector indicado
            return f.read(self.sector_size)  # Leer el sector

    # Método para escribir en un sector del disco
    def write_sector(self, sector_index, data):
        with open(self.disk_file, "r+b") as f:
            f.seek(sector_index * self.sector_size)  # Moverse al sector indicado
            f.write(data)  # Escribir los datos
    
    # Método para leer todos los sectores del disco
    def read_all_sectors(self):
        sectors = []
        with open(self.disk_file, "rb") as f:
            for i in range(self.num_sectors):
                f.seek(i * self.sector_size)
                sectors.append(f.read(self.sector_size))
        return sectors

# Archivo: filesystem.py

import pickle
from disk import Disk
from directory_and_file import Directory, File

# Clase que representa el sistema de archivos
class FileSystem:
    def __init__(self, num_sectors, sector_size):
        self.disk = Disk(num_sectors, sector_size)  # Crear el disco virtual
        self.root = Directory("/")  # Crear el directorio raíz
        self.current_directory = self.root  # Directorio actual es la raíz
        self.num_sectors = num_sectors  # Número de sectores
        self.sector_size = sector_size  # Tamaño de cada sector
        self.free_sectors = list(range(num_sectors))  # Lista de sectores libres

    # Guardar el estado del sistema de archivos
    def save_state(self):
        with open("filesystem_state.pkl", "wb") as f:
            pickle.dump(self, f)

    # Cargar el estado del sistema de archivos
    @staticmethod
    def load_state():
        with open("filesystem_state.pkl", "rb") as f:
            return pickle.load(f)

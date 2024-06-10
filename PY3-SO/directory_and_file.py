# Archivo: directory_and_file.py

import time

# Clase que representa un archivo
class File:
    def __init__(self, name, extension, content=""):
        self.name = name  # Nombre del archivo
        self.extension = extension  # Extensión del archivo
        self.content = content  # Contenido del archivo
        self.creation_date = time.time()  # Fecha de creación
        self.modification_date = self.creation_date  # Fecha de modificación
        self.size = len(content)  # Tamaño del archivo
        self.sectors = []  # Sectores ocupados por el archivo

# Clase que representa un directorio
class Directory:
    def __init__(self, name, parent=None):
        self.name = name  # Nombre del directorio
        self.files = {}  # Archivos en el directorio
        self.subdirectories = {}  # Subdirectorios en el directorio
        self.creation_date = time.time()  # Fecha de creación
        self.modification_date = self.creation_date  # Fecha de modificación
        self.parent = parent  # Directorio padre

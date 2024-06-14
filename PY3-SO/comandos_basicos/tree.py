# Archivo: comandos_basicos/tree.py

def show_tree(fs):
    """
    Muestra el árbol de directorios desde la raíz en el output.
    
    :param fs: Instancia del sistema de archivos.
    """
    result = _build_tree(fs.root, "", True)
    return result

def _build_tree(directory, indent, last):
    """
    Función recursiva para construir el árbol de directorios.
    
    :param directory: Directorio actual.
    :param indent: Indentación para mostrar la estructura.
    :param last: Indicador de si es el último elemento en el nivel actual.
    :return: Representación en cadena del árbol de directorios.
    """
    tree_representation = ""
    if indent:
        tree_representation += f"{indent[:-1]}{'└─ ' if last else '├─ '}{directory.name}/\n"
    else:
        tree_representation += f"/\n"
    
    indent += "   " if last else "│  "

    # Ordenar y recorrer subdirectorios
    subdirectories = list(directory.subdirectories.keys())
    subdirectories.sort()
    for i, subdirectory_name in enumerate(subdirectories):
        subdirectory_obj = directory.subdirectories[subdirectory_name]
        last_item = (i == len(subdirectories) - 1) and len(directory.files) == 0
        tree_representation += _build_tree(subdirectory_obj, indent, last_item)

    # Ordenar y recorrer archivos
    files = list(directory.files.keys())
    files.sort()
    for i, file_name in enumerate(files):
        file_obj = directory.files[file_name]
        last_item = i == len(files) - 1
        tree_representation += f"{indent[:-1]}{'└─ ' if last_item else '├─ '}{file_name}.{file_obj.extension}\n"

    return tree_representation

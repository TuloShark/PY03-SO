import os
import datetime

class File:
    def __init__(self, name, extension, content):
        self.name = name
        self.extension = extension
        self.content = content
        self.creation_date = datetime.datetime.now()
        self.last_modified = datetime.datetime.now()

class Directory:
    def __init__(self, name):
        self.name = name
        self.subdirectories = {}
        self.files = {}

class FileSystem:
    def __init__(self):
        self.root = None
        self.current_directory = None
        self.disk_size = 0
        self.sector_size = 0
        self.disk = []

    def create_disk(self, disk_size, sector_size):
        if self.root is None:
            self.disk_size = disk_size
            self.sector_size = sector_size
            self.disk = [None] * disk_size
            self.root = Directory("/")
            self.current_directory = self.root
            return True
        else:
            return False

    def file_create(self, name, extension, content):
        if name not in self.current_directory.files:
            file = File(name, extension, content)
            self.current_directory.files[name] = file
            return True
        else:
            return False

    def mkdir(self, name):
        if self.root is None:
            return False
        elif name not in self.current_directory.subdirectories:
            directory = Directory(name)
            self.current_directory.subdirectories[name] = directory
            return True
        else:
            return False

    def change_dir(self, path):
        if self.root is None:
            return False
        elif path == "..":
            if self.current_directory != self.root:
                self.current_directory = self.current_directory.parent
            return True
        elif path in self.current_directory.subdirectories:
            self.current_directory = self.current_directory.subdirectories[path]
            return True
        else:
            return False

    def list_dir(self):
        if self.root is None:
            return None
        contents = []
        for directory in self.current_directory.subdirectories:
            contents.append(directory)
        for file in self.current_directory.files:
            contents.append(file)
        return contents

    def mod_file(self, name, content):
        if name in self.current_directory.files:
            self.current_directory.files[name].content = content
            self.current_directory.files[name].last_modified = datetime.datetime.now()
            return True
        else:
            return False

    def view_properties(self, name):
        if name in self.current_directory.files:
            file = self.current_directory.files[name]
            return {
                "Name": file.name,
                "Extension": file.extension,
                "Creation Date": file.creation_date,
                "Last Modified": file.last_modified,
                "Size": len(file.content)
            }
        else:
            return None

    def view_file(self, name):
        if name in self.current_directory.files:
            return self.current_directory.files[name].content
        else:
            return None

    def copy_file(self, source_path, destination_path):
        if source_path in self.current_directory.files:
            if destination_path not in self.current_directory.files:
                self.file_create(destination_path, self.current_directory.files[source_path].extension, self.current_directory.files[source_path].content)
                return True
            else:
                return False
        else:
            return False

    def move_file(self, source_path, destination_path):
        if source_path in self.current_directory.files:
            if destination_path not in self.current_directory.files:
                self.file_create(destination_path, self.current_directory.files[source_path].extension, self.current_directory.files[source_path].content)
                del self.current_directory.files[source_path]
                return True
            else:
                return False
        else:
            return False

    def remove_file(self, name):
        if name in self.current_directory.files:
            del self.current_directory.files[name]
            return True
        else:
            return False

    def find_file(self, name):
        found_paths = []
        for directory in self.current_directory.subdirectories.values():
            for file in directory.files.values():
                if name in file.name:
                    found_paths.append(os.path.join(directory.name, file.name))
        return found_paths

    def tree(self, directory=None, indent=""):
        if directory is None:
            directory = self.root
        tree_structure = []
        tree_structure.append(indent + directory.name + "/")
        for subdirectory in directory.subdirectories.values():
            tree_structure.extend(self.tree(subdirectory, indent + "  "))
        for file in directory.files.values():
            tree_structure.append(indent + "|--" + file.name)
        return tree_structure

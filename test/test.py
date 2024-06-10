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
        self.root = Directory("/")
        self.current_directory = self.root
        self.disk_size = 0
        self.sector_size = 0
        self.disk = []

    def create_disk(self, disk_size, sector_size):
        self.disk_size = disk_size
        self.sector_size = sector_size
        self.disk = [None] * disk_size

    def file_create(self, name, extension, content):
        file = File(name, extension, content)
        self.current_directory.files[name] = file

    def mkdir(self, name):
        directory = Directory(name)
        self.current_directory.subdirectories[name] = directory

    def change_dir(self, path):
        if path == "..":
            if self.current_directory != self.root:
                self.current_directory = self.current_directory.parent
        elif path in self.current_directory.subdirectories:
            self.current_directory = self.current_directory.subdirectories[path]
        else:
            print("Directory not found.")

    def list_dir(self):
        print("Directories:")
        for directory in self.current_directory.subdirectories:
            print(directory)
        print("\nFiles:")
        for file in self.current_directory.files:
            print(file)

    def mod_file(self, name, content):
        if name in self.current_directory.files:
            self.current_directory.files[name].content = content
            self.current_directory.files[name].last_modified = datetime.datetime.now()
        else:
            print("File not found.")

    def view_properties(self, name):
        if name in self.current_directory.files:
            file = self.current_directory.files[name]
            print("Name:", file.name)
            print("Extension:", file.extension)
            print("Creation Date:", file.creation_date)
            print("Last Modified:", file.last_modified)
            print("Size:", len(file.content))
        else:
            print("File not found.")

    def view_file(self, name):
        if name in self.current_directory.files:
            print(self.current_directory.files[name].content)
        else:
            print("File not found.")

    def copy_file(self, source_path, destination_path):
        if source_path in self.current_directory.files:
            self.file_create(destination_path, self.current_directory.files[source_path].extension, self.current_directory.files[source_path].content)
        else:
            print("File not found.")

    def move_file(self, source_path, destination_path):
        if source_path in self.current_directory.files:
            self.file_create(destination_path, self.current_directory.files[source_path].extension, self.current_directory.files[source_path].content)
            del self.current_directory.files[source_path]
        else:
            print("File not found.")

    def remove_file(self, name):
        if name in self.current_directory.files:
            del self.current_directory.files[name]
        else:
            print("File not found.")

    def find_file(self, name):
        found = False
        for directory in self.current_directory.subdirectories.values():
            for file in directory.files.values():
                if name in file.name:
                    print(os.path.join(directory.name, file.name))
                    found = True
        if not found:
            print("File not found.")

    def tree(self, directory=None, indent=""):
        if directory is None:
            directory = self.root
        print(indent + directory.name + "/")
        for subdirectory in directory.subdirectories.values():
            self.tree(subdirectory, indent + "  ")
        for file in directory.files.values():
            print(indent + "|--" + file.name)

def get_integer_input(prompt):
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print("Please enter a valid integer.")

def main():
    fs = FileSystem()

    print("Welcome to Simple File System!")

    disk_size = get_integer_input("Enter disk size: ")
    sector_size = get_integer_input("Enter sector size: ")

    fs.create_disk(disk_size, sector_size)

    while True:
        print("\nCurrent Directory:", fs.current_directory.name)
        print("1. Create Directory")
        print("2. Create File")
        print("3. Change Directory")
        print("4. List Directory")
        print("5. Modify File")
        print("6. View Properties")
        print("7. View File")
        print("8. Copy File")
        print("9. Move File")
        print("10. Remove File")
        print("11. Find File")
        print("12. Tree")
        print("0. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter directory name: ")
            fs.mkdir(name)
        elif choice == "2":
            name = input("Enter file name: ")
            extension = input("Enter file extension: ")
            content = input("Enter file content: ")
            fs.file_create(name, extension, content)
        elif choice == "3":
            path = input("Enter directory path: ")
            fs.change_dir(path)
        elif choice == "4":
            fs.list_dir()
        elif choice == "5":
            name = input("Enter file name: ")
            content = input("Enter new content: ")
            fs.mod_file(name, content)
        elif choice == "6":
            name = input("Enter file name: ")
            fs.view_properties(name)
        elif choice == "7":
            name = input("Enter file name: ")
            fs.view_file(name)
        elif choice == "8":
            source_path = input("Enter source file path: ")
            destination_path = input("Enter destination file path: ")
            fs.copy_file(source_path, destination_path)
        elif choice == "9":
            source_path = input("Enter source file path: ")
            destination_path = input("Enter destination file path: ")
            fs.move_file(source_path, destination_path)
        elif choice == "10":
            name = input("Enter file name: ")
            fs.remove_file(name)
        elif choice == "11":
            name = input("Enter file name to search: ")
            fs.find_file(name)
        elif choice == "12":
            fs.tree()
        elif choice == "0":
            print("Exiting...")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()

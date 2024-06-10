import tkinter as tk
from tkinter import ttk, scrolledtext, simpledialog, messagebox
from filesystem import FileSystem

class FileSystemGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple File System")
        self.root.geometry("760x420")

        self.fs = FileSystem()

        self.create_disk_frame = ttk.LabelFrame(self.root, text="Create Disk")
        self.create_disk_frame.grid(column=0, row=0, padx=10, pady=10)

        ttk.Label(self.create_disk_frame, text="Disk Size:").grid(column=0, row=0, padx=5, pady=5)
        self.disk_size_entry = ttk.Entry(self.create_disk_frame)
        self.disk_size_entry.grid(column=1, row=0, padx=5, pady=5)

        ttk.Label(self.create_disk_frame, text="Sector Size:").grid(column=0, row=1, padx=5, pady=5)
        self.sector_size_entry = ttk.Entry(self.create_disk_frame)
        self.sector_size_entry.grid(column=1, row=1, padx=5, pady=5)

        ttk.Button(self.create_disk_frame, text="Create Disk", command=self.create_disk).grid(column=0, row=2, columnspan=2, padx=5, pady=5)

        self.action_frame = ttk.LabelFrame(self.root, text="Actions")
        self.action_frame.grid(column=0, row=1, padx=10, pady=10)

        ttk.Button(self.action_frame, text="Create Directory", command=self.create_directory).grid(column=0, row=0, padx=5, pady=5)
        ttk.Button(self.action_frame, text="Create File", command=self.create_file).grid(column=1, row=0, padx=5, pady=5)
        ttk.Button(self.action_frame, text="Change Directory", command=self.change_directory).grid(column=0, row=1, padx=5, pady=5)
        ttk.Button(self.action_frame, text="List Directory", command=self.list_directory).grid(column=1, row=1, padx=5, pady=5)
        ttk.Button(self.action_frame, text="Modify File", command=self.modify_file).grid(column=0, row=2, padx=5, pady=5)
        ttk.Button(self.action_frame, text="View Properties", command=self.view_properties).grid(column=1, row=2, padx=5, pady=5)
        ttk.Button(self.action_frame, text="View File", command=self.view_file).grid(column=0, row=3, padx=5, pady=5)
        ttk.Button(self.action_frame, text="Copy File", command=self.copy_file).grid(column=1, row=3, padx=5, pady=5)
        ttk.Button(self.action_frame, text="Move File", command=self.move_file).grid(column=0, row=4, padx=5, pady=5)
        ttk.Button(self.action_frame, text="Remove File", command=self.remove_file).grid(column=1, row=4, padx=5, pady=5)
        ttk.Button(self.action_frame, text="Find File", command=self.find_file).grid(column=0, row=5, padx=5, pady=5)
        ttk.Button(self.action_frame, text="Tree", command=self.tree).grid(column=1, row=5, padx=5, pady=5)
        ttk.Button(self.action_frame, text="Go to Root", command=self.go_to_root).grid(column=0, row=6, columnspan=2, padx=5, pady=5)

        self.output_frame = ttk.LabelFrame(self.root, text="Output")
        self.output_frame.grid(column=1, row=0, rowspan=3, padx=10, pady=10)

        self.output_text = scrolledtext.ScrolledText(self.output_frame, width=60, height=20)
        self.output_text.grid(column=0, row=0, padx=5, pady=5)

    def create_disk(self):
        disk_size = int(self.disk_size_entry.get())
        sector_size = int(self.sector_size_entry.get())
        if self.fs.create_disk(disk_size, sector_size):
            messagebox.showinfo("Info", "Disk created successfully.")
        else:
            messagebox.showwarning("Warning", "Disk already exists.")

    def create_directory(self):
        if self.fs.root is None:
            messagebox.showwarning("Warning", "Please create a disk first.")
        else:
            name = simpledialog.askstring("Input", "Enter directory name:")
            if name:
                if self.fs.mkdir(name):
                    self.show_output("Directory created successfully.")
                else:
                    self.show_output("Directory already exists.")

    def create_file(self):
        if self.fs.root is None:
            messagebox.showwarning("Warning", "Please create a disk first.")
        else:
            name = simpledialog.askstring("Input", "Enter file name:")
            extension = simpledialog.askstring("Input", "Enter file extension:")
            content = simpledialog.askstring("Input", "Enter file content:")
            if name and extension and content:
                if self.fs.file_create(name, extension, content):
                    self.show_output("File created successfully.")
                else:
                    self.show_output("File already exists.")

    def change_directory(self):
        if self.fs.root is None:
            messagebox.showwarning("Warning", "Please create a disk first.")
        else:
            path = simpledialog.askstring("Input", "Enter directory path:")
            if path:
                if self.fs.change_dir(path):
                    self.show_output(f"Changed to directory: {path}")
                else:
                    self.show_output("Directory not found.")

    def list_directory(self):
        if self.fs.root is None:
            messagebox.showwarning("Warning", "Please create a disk first.")
        else:
            contents = self.fs.list_dir()
            if contents:
                self.show_output("Directories and Files:")
                for item in contents:
                    self.show_output(item)
            else:
                self.show_output("Current directory is empty.")

    def modify_file(self):
        if self.fs.root is None:
            messagebox.showwarning("Warning", "Please create a disk first.")
        else:
            name = simpledialog.askstring("Input", "Enter file name:")
            if name:
                content = simpledialog.askstring("Input", "Enter new content:")
                if content:
                    if self.fs.mod_file(name, content):
                        self.show_output("File modified successfully.")
                    else:
                        self.show_output("File not found.")

    def view_properties(self):
        if self.fs.root is None:
            messagebox.showwarning("Warning", "Please create a disk first.")
        else:
            name = simpledialog.askstring("Input", "Enter file name:")
            if name:
                properties = self.fs.view_properties(name)
                if properties:
                    self.show_output("File Properties:")
                    for key, value in properties.items():
                        self.show_output(f"{key}: {value}")
                else:
                    self.show_output("File not found.")

    def view_file(self):
        if self.fs.root is None:
            messagebox.showwarning("Warning", "Please create a disk first.")
        else:
            name = simpledialog.askstring("Input", "Enter file name:")
            if name:
                content = self.fs.view_file(name)
                if content:
                    self.show_output("File Content:")
                    self.show_output(content)
                else:
                    self.show_output("File not found.")

    def copy_file(self):
        if self.fs.root is None:
            messagebox.showwarning("Warning", "Please create a disk first.")
        else:
            source_path = simpledialog.askstring("Input", "Enter source file path:")
            destination_path = simpledialog.askstring("Input", "Enter destination file path:")
            if source_path and destination_path:
                if self.fs.copy_file(source_path, destination_path):
                    self.show_output("File copied successfully.")
                else:
                    self.show_output("Copy failed. Source or destination file already exists.")

    def move_file(self):
        if self.fs.root is None:
            messagebox.showwarning("Warning", "Please create a disk first.")
        else:
            source_path = simpledialog.askstring("Input", "Enter source file path:")
            destination_path = simpledialog.askstring("Input", "Enter destination file path:")
            if source_path and destination_path:
                if self.fs.move_file(source_path, destination_path):
                    self.show_output("File moved successfully.")
                else:
                    self.show_output("Move failed. Source or destination file already exists.")

    def remove_file(self):
        if self.fs.root is None:
            messagebox.showwarning("Warning", "Please create a disk first.")
        else:
            name = simpledialog.askstring("Input", "Enter file name:")
            if name:
                if self.fs.remove_file(name):
                    self.show_output("File removed successfully.")
                else:
                    self.show_output("File not found.")

    def find_file(self):
        if self.fs.root is None:
            messagebox.showwarning("Warning", "Please create a disk first.")
        else:
            name = simpledialog.askstring("Input", "Enter file name:")
            if name:
                found_paths = self.fs.find_file(name)
                if found_paths:
                    self.show_output("Found file in the following paths:")
                    for path in found_paths:
                        self.show_output(path)
                else:
                    self.show_output("File not found.")

    def tree(self):
        if self.fs.root is None:
            messagebox.showwarning("Warning", "Please create a disk first.")
        else:
            tree_structure = self.fs.tree()
            if tree_structure:
                self.show_output("Directory Tree:")
                for item in tree_structure:
                    self.show_output(item)
            else:
                self.show_output("No directory structure found.")

    def go_to_root(self):
        if self.fs.root is None:
            messagebox.showwarning("Warning", "Please create a disk first.")
        else:
            self.fs.current_directory = self.fs.root
            self.show_output("Changed to root directory.")

    def show_output(self, message):
        self.output_text.insert(tk.END, message + "\n")

def main():
    root = tk.Tk()
    app = FileSystemGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()


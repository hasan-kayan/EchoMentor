import sys
import os
import tkinter as tk
from tkinter import filedialog, messagebox

# Get the parent directory of the src directory
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

# Add the lib directory to sys.path
sys.path.append(os.path.join(parent_dir, 'lib'))
# Now you can import the module
from file_finder.file_finder import *

class FileSearchApp:
    def __init__(self, root):
        self.root = root
        self.root.title("File Search")

        self.label1 = tk.Label(root, text="Root Folder:")
        self.label1.grid(row=0, column=0, padx=10, pady=10)

        self.root_folder_entry = tk.Entry(root, width=50)
        self.root_folder_entry.grid(row=0, column=1, padx=10, pady=10)

        self.browse_button = tk.Button(root, text="Browse...", command=self.browse_folder)
        self.browse_button.grid(row=0, column=2, padx=10, pady=10)

        self.label2 = tk.Label(root, text="File Extension:")
        self.label2.grid(row=1, column=0, padx=10, pady=10)

        self.extension_entry = tk.Entry(root, width=50)
        self.extension_entry.grid(row=1, column=1, padx=10, pady=10)

        self.search_button = tk.Button(root, text="Search", command=self.start_search)
        self.search_button.grid(row=2, column=1, padx=10, pady=20)

    def browse_folder(self):
        folder_selected = filedialog.askdirectory()
        if folder_selected:
            self.root_folder_entry.insert(0, folder_selected)

    def start_search(self):
        root_folder = self.root_folder_entry.get().strip()
        extension = self.extension_entry.get().strip()

        if not root_folder:
            # Set the root folder to the root of the file system based on the OS
            if os.name == 'nt':  # Windows
                root_folder = 'C:\\'
            else:  # Unix-based (Linux, macOS)
                root_folder = '/'

        if not os.path.isdir(root_folder):
            messagebox.showerror("Error", "Please select a valid root folder.")
            return

        if not extension.startswith('.'):
            messagebox.showerror("Error", "Please enter a valid file extension (e.g., .txt, .jpg).")
            return

        output_file = "found_files.txt"  # You can make this customizable too
        search_files(root_folder, extension, output_file)

        messagebox.showinfo("Search Completed", f"Search completed. Paths of all found files are saved in {output_file}.")

if __name__ == "__main__":
    root = tk.Tk()
    app = FileSearchApp(root)
    root.mainloop()

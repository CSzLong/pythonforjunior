import tkinter as tk
from tkinter import filedialog, messagebox

class TextEditor:
    def __init__(self, root):
        self.root = root
        self.root.title("Untitled - Simple Text Editor")
        self.root.geometry("800x600")

        self.current_file = None
        self.text_area = tk.Text(self.root, undo=True)
        self.text_area.pack(fill=tk.BOTH, expand=1)
        self.text_area.bind("<<Modified>>", self.on_modified)

        self.menu_bar = tk.Menu(self.root)
        self.root.config(menu=self.menu_bar)

        self.file_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="File", menu=self.file_menu)
        self.file_menu.add_command(label="New", command=self.new_file)
        self.file_menu.add_command(label="Open", command=self.open_file)
        self.file_menu.add_command(label="Save", command=self.save_file)
        self.file_menu.add_command(label="Save As", command=self.save_as_file)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Exit", command=self.exit_editor)

        self.edit_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="Edit", menu=self.edit_menu)
        self.edit_menu.add_command(label="Undo", command=self.text_area.edit_undo)
        self.edit_menu.add_command(label="Redo", command=self.text_area.edit_redo)
        self.edit_menu.add_separator()
        self.edit_menu.add_command(label="Cut", command=lambda: self.text_area.event_generate("<<Cut>>"))
        self.edit_menu.add_command(label="Copy", command=lambda: self.text_area.event_generate("<<Copy>>"))
        self.edit_menu.add_command(label="Paste", command=lambda: self.text_area.event_generate("<<Paste>>"))

        self.help_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="Help", menu=self.help_menu)
        self.help_menu.add_command(label="About", command=self.show_about)

        self.text_area.edit_modified(False)

    def new_file(self):
        if self.confirm_save_changes():
            self.text_area.delete(1.0, tk.END)
            self.current_file = None
            self.root.title("Untitled - Simple Text Editor")

    def open_file(self):
        if self.confirm_save_changes():
            file_path = filedialog.askopenfilename(defaultextension=".txt",
                                                   filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
            if file_path:
                with open(file_path, "r") as file:
                    self.text_area.delete(1.0, tk.END)
                    self.text_area.insert(tk.END, file.read())
                self.current_file = file_path
                self.root.title(f"{file_path} - Simple Text Editor")
                self.text_area.edit_modified(False)

    def save_file(self):
        if self.current_file:
            with open(self.current_file, "w") as file:
                file.write(self.text_area.get(1.0, tk.END))
            self.text_area.edit_modified(False)
        else:
            self.save_as_file()

    def save_as_file(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                                 filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
        if file_path:
            with open(file_path, "w") as file:
                file.write(self.text_area.get(1.0, tk.END))
            self.current_file = file_path
            self.root.title(f"{file_path} - Simple Text Editor")
            self.text_area.edit_modified(False)

    def confirm_save_changes(self):
        if self.text_area.edit_modified():
            response = messagebox.askyesnocancel("Save Changes",
                                                 "Do you want to save changes to your document?")
            if response:  # Yes
                self.save_file()
                return True
            elif response is None:  # Cancel
                return False
        return True

    def exit_editor(self):
        if self.confirm_save_changes():
            self.root.quit()

    def show_about(self):
        messagebox.showinfo("About", "Simple Text Editor\nBuilt with Python and Tkinter")

    def on_modified(self, event):
        if self.current_file:
            self.root.title(f"*{self.current_file} - Simple Text Editor")
        else:
            self.root.title("*Untitled - Simple Text Editor")
        self.text_area.edit_modified(False)

if __name__ == "__main__":
    root = tk.Tk()
    editor = TextEditor(root)
    root.protocol("WM_DELETE_WINDOW", editor.exit_editor)
    root.mainloop()

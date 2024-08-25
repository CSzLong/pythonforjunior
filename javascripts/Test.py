import tkinter as tk
from tkinter import filedialog, messagebox, simpledialog, font

class TextEditor:
    def __init__(self, root):
        self.root = root
        self.root.title("Untitled - Text Editor")
        self.root.geometry("800x600")

        self.current_file = None
        self.text_area = tk.Text(self.root, undo=True, wrap='word')
        self.text_area.pack(fill=tk.BOTH, expand=1)
        self.text_area.bind("<<Modified>>", self.on_modified)

        self.font_family = tk.StringVar(value="Arial")
        self.font_size = tk.IntVar(value=12)
        self.word_wrap = tk.BooleanVar(value=True)  # 自动换行的状态变量

        self.menu_bar = tk.Menu(self.root)
        self.root.config(menu=self.menu_bar)

        self.file_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="File", menu=self.file_menu)
        self.file_menu.add_command(label="New", command=self.new_file, accelerator="Ctrl+N")
        self.file_menu.add_command(label="Open", command=self.open_file, accelerator="Ctrl+O")
        self.file_menu.add_command(label="Save", command=self.save_file, accelerator="Ctrl+S")
        self.file_menu.add_command(label="Save As", command=self.save_as_file, accelerator="Ctrl+Shift+S")
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Exit", command=self.exit_editor, accelerator="Ctrl+Q")

        self.edit_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="Edit", menu=self.edit_menu)
        self.edit_menu.add_command(label="Undo", command=self.undo, accelerator="Ctrl+Z")
        self.edit_menu.add_command(label="Redo", command=self.redo, accelerator="Ctrl+Y")
        self.edit_menu.add_separator()
        self.edit_menu.add_command(label="Cut", command=lambda: self.text_area.event_generate("<<Cut>>"), accelerator="Ctrl+X")
        self.edit_menu.add_command(label="Copy", command=lambda: self.text_area.event_generate("<<Copy>>"), accelerator="Ctrl+C")
        self.edit_menu.add_command(label="Paste", command=lambda: self.text_area.event_generate("<<Paste>>"), accelerator="Ctrl+V")
        self.edit_menu.add_separator()
        self.edit_menu.add_command(label="Find", command=self.find_text, accelerator="Ctrl+F")
        self.edit_menu.add_command(label="Replace", command=self.replace_text, accelerator="Ctrl+H")

        self.format_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="Format", menu=self.format_menu)
        self.format_menu.add_command(label="Font", command=self.change_font)
        self.format_menu.add_command(label="Font Size", command=self.change_font_size)
        self.format_menu.add_checkbutton(label="Word Wrap", onvalue=True, offvalue=False, variable=self.word_wrap, command=self.toggle_word_wrap)  # 添加自动换行选项

        self.help_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="Help", menu=self.help_menu)
        self.help_menu.add_command(label="About", command=self.show_about, accelerator="F1")

        self.update_font()

        self.text_area.edit_modified(False)

        # Bind shortcuts
        self.root.bind('<Control-n>', lambda event: self.new_file())
        self.root.bind('<Control-o>', lambda event: self.open_file())
        self.root.bind('<Control-s>', lambda event: self.save_file())
        self.root.bind('<Control-S>', lambda event: self.save_as_file())
        self.root.bind('<Control-q>', lambda event: self.exit_editor())
        self.root.bind('<Control-z>', lambda event: self.undo())
        self.root.bind('<Control-y>', lambda event: self.redo())
        self.root.bind('<Control-x>', lambda event: self.text_area.event_generate("<<Cut>>"))
        self.root.bind('<Control-c>', lambda event: self.text_area.event_generate("<<Copy>>"))
        self.root.bind('<Control-v>', lambda event: self.text_area.event_generate("<<Paste>>"))
        self.root.bind('<Control-f>', lambda event: self.find_text())
        self.root.bind('<Control-h>', lambda event: self.replace_text())
        self.root.bind('<F1>', lambda event: self.show_about())

    def new_file(self):
        if self.confirm_save_changes():
            self.text_area.delete(1.0, tk.END)
            self.current_file = None
            self.root.title("Untitled - Text Editor")

    def open_file(self):
        if self.confirm_save_changes():
            file_path = filedialog.askopenfilename(defaultextension=".txt",
                                                   filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
            if file_path:
                with open(file_path, "r") as file:
                    self.text_area.delete(1.0, tk.END)
                    self.text_area.insert(tk.END, file.read())
                self.current_file = file_path
                self.root.title(f"{file_path} - Text Editor")
                self.text_area.edit_modified(False)

    def save_file(self):
        if self.current_file:
            with open(self.current_file, "w") as file:
                file.write(self.text_area.get(1.0, tk.END))
            self.text_area.edit_modified(False)
            self.root.title(f"{self.current_file} - Text Editor")
        else:
            self.save_as_file()

    def save_as_file(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                                 filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
        if file_path:
            with open(file_path, "w") as file:
                file.write(self.text_area.get(1.0, tk.END))
            self.current_file = file_path
            self.root.title(f"{file_path} - Text Editor")
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
        messagebox.showinfo("About", "Text Editor\nBuilt with Python and Tkinter")

    def on_modified(self, event=None):
        if self.current_file:
            title = f"{self.current_file} - Text Editor"
        else:
            title = "Untitled - Text Editor"
        if self.text_area.edit_modified():
            title = "*" + title
        self.root.title(title)

    def undo(self):
        self.text_area.edit_undo()
        self.on_modified()

    def redo(self):
        self.text_area.edit_redo()
        self.on_modified()

    def find_text(self):
        search_query = simpledialog.askstring("Find", "Enter text to find:")
        if search_query:
            start = "1.0"
            while True:
                start = self.text_area.search(search_query, start, stopindex=tk.END)
                if not start:
                    break
                end = f"{start}+{len(search_query)}c"
                self.text_area.tag_add("highlight", start, end)
                start = end
            self.text_area.tag_config("highlight", background="yellow")

    def replace_text(self):
        find_text = simpledialog.askstring("Replace", "Enter text to find:")
        replace_text = simpledialog.askstring("Replace", "Enter replacement text:")
        if find_text and replace_text:
            content = self.text_area.get(1.0, tk.END)
            new_content = content.replace(find_text, replace_text)
            self.text_area.delete(1.0, tk.END)
            self.text_area.insert(tk.END, new_content)

    def change_font(self):
        fonts = list(font.families())
        font_choice = simpledialog.askstring("Font", f"Choose font:\n{', '.join(fonts)}")
        if font_choice in fonts:
            self.font_family.set(font_choice)
            self.update_font()

    def change_font_size(self):
        size_choice = simpledialog.askinteger("Font Size", "Enter font size:")
        if size_choice:
            self.font_size.set(size_choice)
            self.update_font()

    def toggle_word_wrap(self):
        wrap_mode = "word" if self.word_wrap.get() else "none"
        self.text_area.config(wrap=wrap_mode)

    def update_font(self):
        current_font = font.Font(family=self.font_family.get(), size=self.font_size.get())
        self.text_area.configure(font=current_font)

if __name__ == "__main__":
    root = tk.Tk()
    editor = TextEditor(root)
    root.protocol("WM_DELETE_WINDOW", editor.exit_editor)
    root.mainloop()

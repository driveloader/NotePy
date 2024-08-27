import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfilename, asksaveasfilename
from tkinter.simpledialog import askstring
import os
#1.2
class NotePy:
    def __init__(self, **kwargs):
        self.__root = tk.Tk()
        self.__root.title("Untitled - NotePy")

        self.__thisWidth = kwargs.get('width', 600)
        self.__thisHeight = kwargs.get('height', 600)

        screenWidth = self.__root.winfo_screenwidth()
        screenHeight = self.__root.winfo_screenheight()
        left = (screenWidth / 2) - (self.__thisWidth / 2)
        top = (screenHeight / 2) - (self.__thisHeight / 2)
        self.__root.geometry(f'{self.__thisWidth}x{self.__thisHeight}+{int(left)}+{int(top)}')

        try:
            self.__root.iconbitmap("Notepad.ico")
        except tk.TclError:
            pass

        self.__mainFrame = ttk.Frame(self.__root)
        self.__mainFrame.grid(sticky='nsew')

        self.__statusFrame = ttk.Frame(self.__root)
        self.__statusFrame.grid(row=1, column=0, sticky='ew')

        self.__thisTextArea = tk.Text(self.__mainFrame, wrap='word', font=('Arial', 12))
        self.__thisScrollBar = ttk.Scrollbar(self.__mainFrame, orient='vertical', command=self.__thisTextArea.yview)
        self.__thisTextArea.config(yscrollcommand=self.__thisScrollBar.set)

        self.__thisTextArea.grid(row=0, column=0, sticky='nsew')
        self.__thisScrollBar.grid(row=0, column=1, sticky='ns')

        self.__mainFrame.grid_rowconfigure(0, weight=1)
        self.__mainFrame.grid_columnconfigure(0, weight=1)

        self.__statusBar = tk.Label(self.__statusFrame, text="Ln 1 | Col 1 | 100% | CRLF | UTF-8", anchor='w')
        self.__statusBar.grid(row=0, column=0, sticky='ew')

        self.__thisMenuBar = tk.Menu(self.__root)
        self.__root.config(menu=self.__thisMenuBar)

        self.__thisFileMenu = tk.Menu(self.__thisMenuBar, tearoff=0)
        self.__thisFileMenu.add_command(label="New", command=self.__newFile, accelerator="Ctrl+N")
        self.__thisFileMenu.add_command(label="Open", command=self.__openFile, accelerator="Ctrl+O")
        self.__thisFileMenu.add_command(label="Save", command=self.__saveFile, accelerator="Ctrl+S")
        self.__thisFileMenu.add_separator()
        self.__thisFileMenu.add_command(label="Exit", command=self.__quitApplication, accelerator="Ctrl+Q")
        self.__thisMenuBar.add_cascade(label="File", menu=self.__thisFileMenu)

        self.__thisEditMenu = tk.Menu(self.__thisMenuBar, tearoff=0)
        self.__thisEditMenu.add_command(label="Cut", command=self.__cut, accelerator="Ctrl+X")
        self.__thisEditMenu.add_command(label="Copy", command=self.__copy, accelerator="Ctrl+C")
        self.__thisEditMenu.add_command(label="Paste", command=self.__paste, accelerator="Ctrl+V")
        self.__thisEditMenu.add_command(label="Undo", command=self.__undo, accelerator="Ctrl+Z")
        self.__thisEditMenu.add_command(label="Redo", command=self.__redo, accelerator="Ctrl+Y")
        self.__thisEditMenu.add_command(label="Find", command=self.__findReplace, accelerator="Ctrl+F")
        self.__thisEditMenu.add_command(label="Replace", command=self.__findReplace, accelerator="Ctrl+H")
        self.__thisMenuBar.add_cascade(label="Edit", menu=self.__thisEditMenu)

        self.__thisFormatMenu = tk.Menu(self.__thisMenuBar, tearoff=0)
        self.__thisFormatMenu.add_command(label="Font Size", command=self.__setFontSize)
        self.__thisFormatMenu.add_command(label="Font Style", command=self.__setFontStyle)
        self.__thisMenuBar.add_cascade(label="Format", menu=self.__thisFormatMenu)

        self.__thisHelpMenu = tk.Menu(self.__thisMenuBar, tearoff=0)
        self.__thisHelpMenu.add_command(label="About NotePy", command=self.__showAbout)
        self.__thisMenuBar.add_cascade(label="Help", menu=self.__thisHelpMenu)

        self.__file = None
        self.__line_endings = "CRLF"
        self.__encoding = "UTF-8"

        self.__thisTextArea.bind('<KeyRelease>', self.__updateStatusBar)
        self.__root.bind_all('<Control-n>', lambda e: self.__newFile())
        self.__root.bind_all('<Control-o>', lambda e: self.__openFile())
        self.__root.bind_all('<Control-s>', lambda e: self.__saveFile())
        self.__root.bind_all('<Control-q>', lambda e: self.__quitApplication())
        self.__root.bind_all('<Control-x>', lambda e: self.__cut())
        self.__root.bind_all('<Control-c>', lambda e: self.__copy())
        self.__root.bind_all('<Control-v>', lambda e: self.__paste())
        self.__root.bind_all('<Control-z>', lambda e: self.__undo())
        self.__root.bind_all('<Control-y>', lambda e: self.__redo())
        self.__root.bind_all('<Control-f>', lambda e: self.__findReplace())
        self.__root.bind_all('<Control-h>', lambda e: self.__findReplace())

    def __quitApplication(self):
        self.__root.destroy()

    def __showAbout(self):
        showinfo("NotePy", "Having trust issue with Microsoft Products? Here you are, a FREE and OPEN SOURCE Notepad created in Python! Created by: Long Do (http://longdo.pythonanywhere.com/)")

    def __openFile(self):
        self.__file = askopenfilename(defaultextension=".txt", filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")])
        if self.__file:
            self.__root.title(os.path.basename(self.__file) + " - NotePy")
            self.__thisTextArea.delete(1.0, tk.END)
            with open(self.__file, "r", encoding=self.__encoding) as file:
                self.__thisTextArea.insert(1.0, file.read())
            self.__updateStatusBar()

    def __newFile(self):
        self.__root.title("Untitled - NotePy")
        self.__file = None
        self.__thisTextArea.delete(1.0, tk.END)
        self.__updateStatusBar()

    def __saveFile(self):
        if self.__file is None:
            self.__file = asksaveasfilename(initialfile='Untitled.txt', defaultextension=".txt", filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")])
        if self.__file:
            with open(self.__file, "w", encoding=self.__encoding) as file:
                file.write(self.__thisTextArea.get(1.0, tk.END))
            self.__root.title(os.path.basename(self.__file) + " - NotePy")
            self.__updateStatusBar()

    def __cut(self):
        self.__thisTextArea.event_generate("<<Cut>>")

    def __copy(self):
        self.__thisTextArea.event_generate("<<Copy>>")

    def __paste(self):
        self.__thisTextArea.event_generate("<<Paste>>")

    def __undo(self):
        self.__thisTextArea.event_generate("<<Undo>>")

    def __redo(self):
        self.__thisTextArea.event_generate("<<Redo>>")

    def __findReplace(self):
        findReplaceWindow = tk.Toplevel(self.__root)
        findReplaceWindow.title("Find and Replace")
        tk.Label(findReplaceWindow, text="Find:").grid(row=0, column=0, sticky='e')
        findEntry = tk.Entry(findReplaceWindow, width=30)
        findEntry.grid(row=0, column=1, padx=5, pady=5)
        tk.Label(findReplaceWindow, text="Replace with:").grid(row=1, column=0, sticky='e')
        replaceEntry = tk.Entry(findReplaceWindow, width=30)
        replaceEntry.grid(row=1, column=1, padx=5, pady=5)
        tk.Button(findReplaceWindow, text="Find", command=lambda: self.__find(findEntry.get())).grid(row=2, column=0, padx=5, pady=5)
        tk.Button(findReplaceWindow, text="Replace", command=lambda: self.__replace(findEntry.get(), replaceEntry.get())).grid(row=2, column=1, padx=5, pady=5)
        tk.Button(findReplaceWindow, text="Cancel", command=findReplaceWindow.destroy).grid(row=2, column=2, padx=5, pady=5)

    def __find(self, search_text):
        content = self.__thisTextArea.get(1.0, tk.END)
        index = content.find(search_text)
        if index != -1:
            self.__thisTextArea.mark_set("insert", f"1.0+{index}c")
            self.__thisTextArea.see("insert")

    def __replace(self, search_text, replace_text):
        content = self.__thisTextArea.get(1.0, tk.END)
        new_content = content.replace(search_text, replace_text)
        self.__thisTextArea.delete(1.0, tk.END)
        self.__thisTextArea.insert(1.0, new_content)

    def __setFontSize(self):
        size = askstring("Font Size", "Enter font size:")
        if size:
            try:
                size = int(size)
                current_font = self.__thisTextArea.cget("font")
                font_family, font_size = current_font.rsplit(' ', 1)
                self.__thisTextArea.config(font=(font_family, size))
            except ValueError:
                showinfo("Error", "Invalid font size.")

    def __setFontStyle(self):
        font_style = askstring("Font Style", "Enter font style (e.g., Arial, Courier):")
        if font_style:
            current_font = self.__thisTextArea.cget("font")
            font_family, font_size = current_font.rsplit(' ', 1)
            self.__thisTextArea.config(font=(font_style, font_size))

    def __updateStatusBar(self, event=None):
        content = self.__thisTextArea.get(1.0, tk.END)
        num_lines = int(self.__thisTextArea.index('end-1c').split('.')[0])
        num_cols = len(self.__thisTextArea.get(tk.INSERT + " linestart", tk.INSERT))
        num_words = len(content.split())

        line, col = map(int, self.__thisTextArea.index(tk.INSERT).split('.'))
        line_endings = self.__line_endings
        encoding = self.__encoding

        self.__statusBar.config(text=f"Ln {line} | Col {col} | {num_words} Words | {line_endings} | {encoding}")

    def run(self):
        self.__root.mainloop()

if __name__ == "__main__":
    app = NotePy(width=600, height=460)
    app.run()

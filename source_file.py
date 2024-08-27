import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfilename, asksaveasfilename
import os
from tkinter.simpledialog import askstring
import sys

class NotePy:
    def __init__(self, **kwargs):
        # Initialize main window
        self.__root = tk.Tk()
        self.__root.title("Untitled - NotePy")

        # Set window size
        self.__thisWidth = kwargs.get('width', 600)
        self.__thisHeight = kwargs.get('height', 460)

        # Center the window
        screenWidth = self.__root.winfo_screenwidth()
        screenHeight = self.__root.winfo_screenheight()
        left = (screenWidth / 2) - (self.__thisWidth / 2)
        top = (screenHeight / 2) - (self.__thisHeight / 2)
        self.__root.geometry(f'{self.__thisWidth}x{self.__thisHeight}+{int(left)}+{int(top)}')

        # Set icon (use a placeholder or remove if not available)
        try:
            self.__root.iconbitmap("NotePy.ico")
        except tk.TclError:
            pass

        # Create a frame for the text area and scrollbar
        self.__mainFrame = ttk.Frame(self.__root)
        self.__mainFrame.grid(sticky='nsew')

        # Create a frame for the status bar
        self.__statusFrame = ttk.Frame(self.__root)
        self.__statusFrame.grid(row=1, column=0, sticky='ew')

        # Create a text area with a scrollbar
        self.__thisTextArea = tk.Text(self.__mainFrame, wrap='word', font=('Arial', 12))
        self.__thisScrollBar = ttk.Scrollbar(self.__mainFrame, orient='vertical', command=self.__thisTextArea.yview)
        self.__thisTextArea.config(yscrollcommand=self.__thisScrollBar.set)

        # Pack widgets into the main frame
        self.__thisTextArea.grid(row=0, column=0, sticky='nsew')
        self.__thisScrollBar.grid(row=0, column=1, sticky='ns')

        # Configure row and column weights
        self.__mainFrame.grid_rowconfigure(0, weight=1)
        self.__mainFrame.grid_columnconfigure(0, weight=1)

        # Status bar elements
        self.__statusBar = tk.Label(self.__statusFrame, text="Ln 1 | Col 1 | 100% | CRLF | UTF-8", anchor='w')
        self.__statusBar.grid(row=0, column=0, sticky='ew')

        # Create menu bar
        self.__thisMenuBar = tk.Menu(self.__root)
        self.__root.config(menu=self.__thisMenuBar)

        # File menu
        self.__thisFileMenu = tk.Menu(self.__thisMenuBar, tearoff=0)
        self.__thisFileMenu.add_command(label="New", command=self.__newFile, accelerator="Ctrl+N")
        self.__thisFileMenu.add_command(label="New Window", command=self.__newWindow, accelerator="Ctrl+Shift+N")
        self.__thisFileMenu.add_command(label="Open", command=self.__openFile, accelerator="Ctrl+O")
        self.__thisFileMenu.add_command(label="Save", command=self.__saveFile, accelerator="Ctrl+S")
        self.__thisFileMenu.add_command(label="Save As", command=self.__saveAsFile, accelerator="Ctrl+Shift+S")
        self.__thisFileMenu.add_separator()
        self.__thisFileMenu.add_command(label="Exit", command=self.__quitApplication, accelerator="Ctrl+Q")
        self.__thisMenuBar.add_cascade(label="File", menu=self.__thisFileMenu)

        # Edit menu
        self.__thisEditMenu = tk.Menu(self.__thisMenuBar, tearoff=0)
        self.__thisEditMenu.add_command(label="Cut", command=self.__cut, accelerator="Ctrl+X")
        self.__thisEditMenu.add_command(label="Copy", command=self.__copy, accelerator="Ctrl+C")
        self.__thisEditMenu.add_command(label="Paste", command=self.__paste, accelerator="Ctrl+V")
        self.__thisEditMenu.add_command(label="Undo", command=self.__undo, accelerator="Ctrl+Z")
        self.__thisEditMenu.add_command(label="Redo", command=self.__redo, accelerator="Ctrl+Y")
        self.__thisEditMenu.add_command(label="Find", command=self.__findReplace, accelerator="Ctrl+F")
        self.__thisEditMenu.add_command(label="Replace", command=self.__findReplace, accelerator="Ctrl+H")
        self.__thisEditMenu.add_command(label="Select All", command=self.__selectAll, accelerator="Ctrl+A")
        self.__thisMenuBar.add_cascade(label="Edit", menu=self.__thisEditMenu)

        # Format menu
        self.__thisFormatMenu = tk.Menu(self.__thisMenuBar, tearoff=0)
        self.__thisFormatMenu.add_command(label="Font Size", command=self.__setFontSize)
        self.__thisFormatMenu.add_command(label="Font Style", command=self.__setFontStyle)
        self.__thisMenuBar.add_cascade(label="Format", menu=self.__thisFormatMenu)

        # Help menu
        self.__thisHelpMenu = tk.Menu(self.__thisMenuBar, tearoff=0)
        self.__thisHelpMenu.add_command(label="About NotePy", command=self.__showAbout)
        self.__thisMenuBar.add_cascade(label="Help", menu=self.__thisHelpMenu)

        # Initialize file variable
        self.__file = None
        self.__line_endings = "CRLF"
        self.__encoding = "UTF-8"

        # Bind events
        self.__thisTextArea.bind('<KeyRelease>', self.__updateStatusBar)
        self.__root.bind_all('<Control-n>', lambda e: self.__newFile())
        self.__root.bind_all('<Control-N>', lambda e: self.__newWindow())
        self.__root.bind_all('<Control-o>', lambda e: self.__openFile())
        self.__root.bind_all('<Control-s>', lambda e: self.__saveFile())
        self.__root.bind_all('<Control-S>', lambda e: self.__saveAsFile())
        self.__root.bind_all('<Control-q>', lambda e: self.__quitApplication())
        self.__root.bind_all('<Control-x>', lambda e: self.__cut())
        self.__root.bind_all('<Control-c>', lambda e: self.__copy())
        self.__root.bind_all('<Control-v>', lambda e: self.__paste())
        self.__root.bind_all('<Control-z>', lambda e: self.__undo())
        self.__root.bind_all('<Control-y>', lambda e: self.__redo())
        self.__root.bind_all('<Control-a>', lambda e: self.__selectAll())
        self.__root.bind_all('<Control-f>', lambda e: self.__findReplace())
        self.__root.bind_all('<Control-h>', lambda e: self.__findReplace())

        # Open file if provided as an argument (for "Open with NotePy" functionality)
        if len(sys.argv) > 1:
            self.__file = sys.argv[1]
            self.__openFile(initial_open=True)

    def __newWindow(self):
        os.system(f'python "{__file__}"')

    def __quitApplication(self):
        self.__root.destroy()

    def __showAbout(self):
        showinfo("NotePy", "Having trust issue with Microsoft Products? Here you are, a FREE and OPEN SOURCE Notepad created in Python! Created by: Long Do (http://longdo.pythonanywhere.com/)")

    def __openFile(self, initial_open=False):
        if not initial_open:
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
            self.__saveAsFile()
        else:
            with open(self.__file, "w", encoding=self.__encoding) as file:
                file.write(self.__thisTextArea.get(1.0, tk.END))
            self.__root.title(os.path.basename(self.__file) + " - NotePy")

    def __saveAsFile(self):
        self.__file = asksaveasfilename(initialfile='Untitled.txt', defaultextension=".txt", filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")])
        if self.__file:
            with open(self.__file, "w", encoding=self.__encoding) as file:
                file.write(self.__thisTextArea.get(1.0, tk.END))
            self.__root.title(os.path.basename(self.__file) + " - NotePy")

    def __cut(self):
        self.__thisTextArea.event_generate("<<Cut>>")

    def __copy(self):
        self.__thisTextArea.event_generate("<<Copy>>")

    def __paste(self):
        self.__thisTextArea.event_generate("<<Paste>>")

    def __undo(self):
        try:
            self.__thisTextArea.edit_undo()
        except tk.TclError:
            pass

    def __redo(self):
        try:
            self.__thisTextArea.edit_redo()
        except tk.TclError:
            pass

    def __findReplace(self):
        find_what = askstring("Find", "Enter text to find:")
        replace_with = askstring("Replace", "Replace with (leave empty to skip):")

        text_content = self.__thisTextArea.get(1.0, tk.END)
        self.__thisTextArea.delete(1.0, tk.END)

        if replace_with:
            text_content = text_content.replace(find_what, replace_with)

        self.__thisTextArea.insert(1.0, text_content)
        self.__updateStatusBar()

    def __selectAll(self):
        self.__thisTextArea.tag_add('sel', '1.0', 'end')

    def __setFontSize(self):
        size = askstring("Font Size", "Enter font size:")
        if size and size.isdigit():
            self.__thisTextArea.config(font=("Arial", int(size)))

    def __setFontStyle(self):
        style = askstring("Font Style", "Enter font style (e.g., bold, italic):")
        if style:
            current_font = self.__thisTextArea['font'].split()
            if len(current_font) > 1:
                current_font[-1] = style
            else:
                current_font.append(style)
            self.__thisTextArea.config(font=" ".join(current_font))

    def __updateStatusBar(self, event=None):
        line, column = self.__thisTextArea.index(tk.INSERT).split('.')
        self.__statusBar.config(text=f"Ln {line} | Col {column} | 100% | {self.__line_endings} | {self.__encoding}")

    def run(self):
        self.__root.mainloop()

if __name__ == '__main__':
    app = NotePy()
    app.run()

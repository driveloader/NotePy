<h1 align="center">NotePy 📓</h1>

<h3 align="center">— An Enhanced Version of Notepad (originally by pratyushjain122) Built with Python & Tkinter —</h3>

### 🔥 NotePy transforms the original notepad-python project by pratyushjain122 into a not-so-modern (but still nostalgic) yet fully-featured text editor designed for everyday use. It's a more efficient replacement for Notepad, but with a modern twist.

&nbsp;

## What is Tkinter?

#### 👉 Tkinter is Python's standard GUI (Graphical User Interface) toolkit.
#### 👉 While there are other GUI toolkits for Python, Tkinter is the go-to choice due to its simplicity and seamless integration with Python. It’s like the Swiss Army knife of Python GUI toolkits!

&nbsp;

## What is NotePy?

NotePy is an upgraded text editor based on the original notepad-python project. It boasts a sleek user interface and enhanced features, all built using Python and Tkinter. It’s like Notepad but with superpowers.

&nbsp;

## Features

### Original Features (from [pratyushjain122's notepad-python project](https://github.com/pratyushjain122/notepad-python)):

1. **New File**: Create a new, blank document. It’s like a fresh start for your thoughts.
2. **Open File**: Open and load an existing file. Perfect for revisiting your old masterpieces.
3. **Save File**: Save your document. Because who doesn’t want to keep their work?
4. **Cut**: Cut selected text. Time to trim the fat!
5. **Copy**: Copy selected text. Because good ideas deserve to be duplicated.
6. **Paste**: Paste text from the clipboard. Reuse like a pro.
7. **View Help**: Access help information for the application. Your guide to mastering NotePy.

### New Features in NotePy:

1. **Enhanced Edit Menu**: Now includes "Undo," "Redo," "Find," and "Replace" features. It's like having an editor’s undo button for life.
2. **Convenient Hotkeys**: Adds various hotkeys to streamline your workflow. For those who like to keep their hands on the keyboard and their eyes on the prize.
3. **Status Bar**: Displays real-time document information, including:
   - Cursor position (line and column number). Never lose your place again!
   - Word count. Because sometimes you just need to know how many words you’ve written.
   - Line endings (e.g., CRLF). For the technical wizards out there.
   - File encoding (e.g., UTF-8). Because encoding matters!
4. **Format Menu**: Adjust the global font style and size. Make your text look as good as it sounds.

&nbsp;

## What's Included in This Project

### Portable Version

- **Description**: A download-and-play version pre-compiled into an executable (.exe) that runs on any Windows machine without installation. It’s the software equivalent of a Swiss Army knife—versatile and always ready.
- **Use Case**: Perfect for those who prefer a plug-and-play application or want to keep it on a USB drive. No installation required, just run and go!

### Install Version

- **Description**: Install NotePy on your machine for a smoother workflow. One-click, and it’s on your device—no more searching for the portable file.
- **Use Case**: Ideal for those who want NotePy integrated into their system for everyday use. Installation makes it easy to access NotePy without the hassle of finding and running the portable version.

### Source Code

- **Description**: The complete source code for NotePy, available for download and compilation. Obviously, what would you expect more from a open source project? (lol) 
- **Use Case**: Perfect for those who prefer to compile the software themselves or need to run it on different operating systems. Great for the tryhards who compiles Gentoo 10 times a day. (Damn I really tried but my computer exploded)

&nbsp;

## GUI Overview 🧩

A GUI (Graphical User Interface) allows users to interact with software through visual elements like buttons, text fields, and menus. It’s what keeps your interactions with NotePy smooth and intuitive.

&nbsp;

## How It Works 👷‍♂️

#### ~ When you launch NotePy, a user-friendly GUI window will open, and you’ll be ready to write and edit text just like in any standard notepad application.

<p align="center">
<img src="https://github.com/driveloader/NotePy/blob/master/Extra/image.png" alt="Main Page" width="500px">
</p>

&nbsp;

### File Menu 👇

<br>
<img src="https://github.com/driveloader/NotePy/blob/master/Extra/image2.png" alt="File Menu">

#### ~ The File Menu lets you create a new file, open an existing one, save the current file, or exit the application. Plus, new keybindings to make life easier.

<hr>

&nbsp;

### Edit Menu 👇

<br>
<img src="https://github.com/driveloader/NotePy/blob/master/Extra/image3.png" alt="Edit Menu">

#### ~ The Edit Menu originally provided 'Cut,' 'Copy,' and 'Paste.' NotePy has added 'Undo,' 'Redo,' 'Find,' and 'Replace,' along with handy keybindings. Because text editing should be efficient and powerful!

&nbsp;

### Format Menu 👇

#### ~ The Format Menu allows you to adjust the 'Font Size' and 'Font Style' of your text. Make your text look just the way you want it!

&nbsp;

### Help Menu 👇

#### ~ The Help Menu provides an 'About NotePy' option for more information about the application and its creator. Because knowledge is power.

&nbsp;

## How to Use (Portable Version)

1. **Run the Application**: Launch the script or executable file to open NotePy.
2. **Create or Open Files**: Use the File Menu to start a new document or open an existing one.
3. **Edit Text**: Utilize the Edit Menu for text operations.
4. **Adjust Formatting**: Access the Format Menu to modify text size and style.
5. **Find and Replace**: Use the Find and Replace dialog to search and replace text.
6. **Check Status**: Monitor the status bar for real-time document details.

## For Installer Version

1. **Install The App**: Run the installer and follow the prompts to install NotePy on your machine.
2. **Launch NotePy**: Once installed, start NotePy from your desktop or start menu and begin using it. Easy peasy!

&nbsp;

## Code Overview

Here's a summary of the core functionalities:

- **Window Initialization**: Configures the main application window, including size, title, and alignment.
- **Menu Setup**: Creates menus for file operations, text editing, formatting, and help.
- **Text Area**: Provides a resizable text area with vertical scrolling. Perfect for those long writing sessions.
- **File Operations**:
  - **New File**: Clears the current text area and resets the file name. Fresh starts are great!
  - **Open File**: Opens a file dialog to load content into the editor. Revisit your previous work effortlessly.
  - **Save File**: Saves the current content to a file with options for naming and location. Because saving is caring.
- **Text Editing**:
  - **Cut, Copy, Paste**: Standard text editing functions. Basic but essential.
  - **Undo, Redo**: Reverses or re-applies recent changes. Because mistakes happen, and we like to fix them.
  - **Find and Replace**: Allows interactive text searching and replacement. Find what you need, replace what you don’t.
- **Formatting**:
  - **Font Size and Style**: Adjusts text appearance. Customize your text to match your mood.
- **Status Bar**: Displays real-time information about the document. Never lose track of what’s important.

&nbsp;

## Contributors 👨‍💻

<ul>
<li><a href="https://github.com/pratyushjain122">Pratyush Jain</a></li>
<li><a href="https://github.com/mansharamani-rahul">Rahul Mansharamani</a></li>
<li><a href="https://github.com/driveloader">Long Do (aka driveloader)</a></li>
</ul>

---

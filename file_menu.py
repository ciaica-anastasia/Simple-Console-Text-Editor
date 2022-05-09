from tkinter import *
from tkinter.filedialog import *
from tkinter.messagebox import *


class File():

    def newFile(self, button=""):
        answer = askyesno(title="Save File", message="Would you like to save this file?")
        if answer:
            self.saveFile()
        self.text.delete(0.0, END)
        self.filename = "Untitled"
        self.root.title(self.filename + " - Text Editor")

    def saveFile(self, button=""):
        try:
            if self.filename == "Untitled":
                path = asksaveasfilename(defaultextension='.txt')
                self.filename = path
            self.root.title(self.filename + " - Text Editor")
            t = self.text.get(0.0, END)
            f = open(self.filename, 'w')
            f.write(t)
            f.close()
        except:
            self.saveAs()

    def saveAs(self, button=""):
        if self.filename == "Untitled":
            self.saveFile()
            return "break"
        f = asksaveasfile(mode="w", defaultextension='.txt')
        self.filename = f.name
        t = self.text.get(0.0, END)
        try:
            self.root.title(self.filename + " - Text Editor")
            f.write(t.rstrip())
            f.close()
        except:
            showerror(title="Oops!", message="Unable to save file...")

    def openFile(self, button=""):
        f = askopenfile(mode='r')
        self.filename = f.name
        t = f.read()
        self.text.delete(0.0, END)
        self.text.insert(0.0, t)

    def quit(self, button=""):
        entry = askyesno(title="Quit", message="Are you sure you want to quit?")
        if entry == True:
            self.root.destroy()

    def __init__(self, text, root):
        self.filename = None
        self.text = text
        self.root = root


def main(root, text, menubar):
    root.bind("")
    filemenu = Menu(menubar)
    objFile = File(text, root)
    filemenu.add_command(label="New", command=objFile.newFile, accelerator="Ctrl+N")
    filemenu.add_command(label="Open", command=objFile.openFile, accelerator="Ctrl+O")
    filemenu.add_command(label="Save", command=objFile.saveFile, accelerator="Ctrl+S")
    filemenu.add_command(label="Save As...", command=objFile.saveAs, accelerator="Ctrl+A")
    filemenu.add_separator()
    filemenu.add_command(label="Quit", command=objFile.quit, accelerator="Ctrl+Q")
    menubar.add_cascade(label="File", menu=filemenu)
    root.config(menu=menubar)

    root.bind_all("<Control-s>", objFile.saveFile)
    root.bind_all("<Control-a>", objFile.saveAs)
    root.bind_all("<Control-q>", objFile.quit)
    root.bind_all("<Control-o>", objFile.openFile)


if __name__ == "__main__":
    print("Please run 'main.py'")

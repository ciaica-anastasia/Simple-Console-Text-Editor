import tkinter as tk
from tkinter import ttk
from tkinter.simpledialog import *


class _ReplaceWindow():
    def __init__(self, container, text):
        self.container = container
        self.text = text

    def create_input_frame(self, container):

        frame = ttk.Frame(container)

        # grid layout for the input frame
        frame.columnconfigure(0, weight=1)
        frame.columnconfigure(0, weight=3)

        # Find what
        ttk.Label(frame, text='Find what:').grid(column=0, row=0, sticky=tk.W)
        self.keyword = ttk.Entry(frame, width=30)
        self.keyword.focus()
        self.keyword.grid(column=1, row=0, sticky=tk.W)

        # Replace with:
        ttk.Label(frame, text='Replace with:').grid(column=0, row=1, sticky=tk.W)
        self.replacement = ttk.Entry(frame, width=30)
        self.replacement.grid(column=1, row=1, sticky=tk.W)

        for widget in frame.winfo_children():
            widget.grid(padx=0, pady=5)

        return frame

    def _find_and_replace(self):
        self.text.tag_remove('found', '1.0', END)
        s = self.keyword.get()
        r = self.replacement.get()

        if (s and r):
            idx = '1.0'
            while 1:
                idx = self.text.search(s, idx, nocase=1, stopindex=END)
                print(idx)
                if not idx: break
                lastidx = '% s+% dc' % (idx, len(s))
                self.text.delete(idx, lastidx)
                self.text.insert(idx, r)
                lastidx = '% s+% dc' % (idx, len(r))
                self.text.tag_add('found', idx, lastidx)
                idx = lastidx
            self.text.tag_config('found', background='blue', foreground='white')
        self.keyword.focus_set()

    def create_button_frame(self, container):
        frame = ttk.Frame(container)
        frame.columnconfigure(0, weight=1)
        self.btnReplace = ttk.Button(frame, text='Replace', command=self._find_and_replace).grid(column=0, row=0)

        for widget in frame.winfo_children():
            widget.grid(padx=0, pady=3)

        return frame

    def create_main_window(self):

        # root window
        root = tk.Tk()
        root.title('Replace')
        root.geometry('600x150')
        root.resizable(1, 0)

        # layout on the root window
        root.columnconfigure(0, weight=4)
        root.columnconfigure(1, weight=1)

        input_frame = self.create_input_frame(root)
        input_frame.grid(column=0, row=0)

        button_frame = self.create_button_frame(root)
        button_frame.grid(column=1, row=0)

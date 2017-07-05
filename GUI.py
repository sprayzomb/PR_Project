import sys
import os
import tkinter as tk
from tkinter import ttk
import csv

with open('compounds.csv', 'r') as f:
    reader = csv.reader(f)
    compound_list = list(reader)


LARGE_FONT= ("Verdana", 12)

class PR(tk.Tk):

    def __init__(self, *args, **kwargs):

        tk.Tk.__init__(self, *args, **kwargs)

        tk.Tk.iconbitmap(self, default="logo.ico")
        tk.Tk.wm_title(self, "Pr Project")

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand= True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, Properties, PageTwo):

            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()

class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Start Page", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1=ttk.Button(self, text="Visit Properties",
                          command=lambda: [controller.show_frame(Properties)])
        button1.pack()

        button2 = ttk.Button(self, text="Visit PageTwo",
                             command=lambda: [controller.show_frame(PageTwo)])
        button2.pack()


class Properties(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Properties", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1 = ttk.Button(self, text="Back to Home",
                            command=lambda: [controller.show_frame(StartPage)])
        button1.pack()

        button2 = ttk.Button(self, text="Page Two",
                            command=lambda: [controller.show_frame(PageTwo)])
        button2.pack()

        combo = AutocompleteCombobox(self)
        combo.set_completion_list(compound_list)
        combo.pack()
        combo.focus_set()

        #compound_1 = tk.StringVar()
        #box_1 = ttk.Combobox(self, textvariable = compound_1,
        #                   state='readonly', width=30)
        #box_1['values'] = (Properties.compound_list)
        #box_1.current(0)
        #box_1.bind("<Key>", Properties.findInBox)
        #box_1.focus()
        #box_1.pack()

        compound_2 = tk.StringVar()
        box_2 = ttk.Combobox(self, textvariable=compound_2,
                           state='readonly', width=30)
        box_2['values'] = (compound_list)
        box_2.current(0)
        box_2.pack()

        compound_3 = tk.StringVar()
        box_3 = ttk.Combobox(self, textvariable=compound_3,
                           state='readonly', width=30)
        box_3['values'] = (compound_list)
        box_3.current(0)
        box_3.pack()


class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Page Two", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1 = ttk.Button(self, text="Back to Home",
                            command=lambda: [controller.show_frame(StartPage)])
        button1.pack()

        button2 = ttk.Button(self, text="To Properties",
                            command=lambda: [controller.show_frame(Properties)])
        button2.pack()

class AutocompleteCombobox(ttk.Combobox):

        def set_completion_list(self, completion_list):
            """Use our completion list as our drop down selection menu, arrows move through menu."""
            #self._completion_list = sorted(completion_list, key=str.lower)  # Work with a sorted list
            self._hits = []
            self._hit_index = 0
            self.position = 0
            self.bind('<KeyRelease>', self.handle_keyrelease)
            self['values'] = self._completion_list  # Setup our popup menu

        def autocomplete(self, delta=0):
            """autocomplete the Combobox, delta may be 0/1/-1 to cycle through possible hits"""
            if delta:  # need to delete selection otherwise we would fix the current position
                self.delete(self.position, ttk.END)
            else:  # set position to end so selection starts where textentry ended
                self.position = len(self.get())
            # collect hits
            _hits = []
            for element in self._completion_list:
                if element.lower().startswith(self.get().lower()):  # Match case insensitively
                    _hits.append(element)
            # if we have a new hit list, keep this in mind
            if _hits != self._hits:
                self._hit_index = 0
                self._hits = _hits
            # only allow cycling if we are in a known hit list
            if _hits == self._hits and self._hits:
                self._hit_index = (self._hit_index + delta) % len(self._hits)
            # now finally perform the auto completion
            if self._hits:
                self.delete(0, ttk.END)
                self.insert(0, self._hits[self._hit_index])
                self.select_range(self.position, ttk.END)

        def handle_keyrelease(self, event):
            """event handler for the keyrelease event on this widget"""
            if event.keysym == "BackSpace":
                self.delete(self.index(ttk.INSERT), ttk.END)
                self.position = self.index(ttk.END)
            if event.keysym == "Left":
                if self.position < self.index(ttk.END):  # delete the selection
                    self.delete(self.position, ttk.END)
                else:
                    self.position = self.position - 1  # delete one character
                    self.delete(self.position, ttk.END)
            if event.keysym == "Right":
                self.position = self.index(ttk.END)  # go to end (no selection)
            if len(event.keysym) == 1:
                self.autocomplete()
                # No need for up/down, we'll jump to the popup
                # list at the position of the autocompletion


app = PR()
app.mainloop()

import tkinter as tk
from tkinter import ttk
import tkinter.font as tkfont
import csv

with open('compounds.csv', 'r') as f:
  reader = csv.reader(f)
  compound_list = list(reader)
  compound_list.sort()
  compound_list = [l[0] for l in compound_list]

#print(compound_list)

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

        #compound_1 = tk.StringVar()
        #box_1 = ttk.Combobox(self, textvariable=compound_1,
        #                     state='readonly', width=30)
        #box_1['values'] = (compound_list)
        #box_1.current(0)
        #box_1.pack()
        box_1 = AutocompleteCombobox(self, width=25)
        box_1.set_completion_list(compound_list)
        box_1.pack()
        box_1.focus_set()

        box_2 = AutocompleteCombobox(self, width=25)
        box_2.set_completion_list(compound_list)
        box_2.pack()
        box_2.focus_set()

        box_3 = AutocompleteCombobox(self, width=25)
        box_3.set_completion_list(compound_list)
        box_3.pack()
        box_3.focus_set()

        box_4 = AutocompleteCombobox(self, width=25)
        box_4.set_completion_list(compound_list)
        box_4.pack()
        box_4.focus_set()


class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Page Two", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        self.addButton = ttk.Button(self, text="Add")
                            #command=self.addOnDouble)
        self.addButton.pack()

        self.removeButton = ttk.Button(self, text="Remove",
                            command=self.removeWithButton)
        self.removeButton.pack()

        self.compound_box = tk.Listbox(self, width=45, height=15)
        self.compound_box.bind('<Double-Button-1>', self.removeOnDouble)
        self.compound_box.pack()

        #button2 = ttk.Button(self, text="To Properties",
        #                    command=lambda: [controller.show_frame(Properties)])
        #button2.pack()

        self.selected_compound_list=[]
        self.create_widgets()

    def removeOnDouble(self,event):
        widget = event.widget
        selection = widget.curselection()
        value = widget.get(selection[0])
        self.compound_box.delete(selection[0])
        self.selected_compound_list.remove(value)
        print(self.selected_compound_list)

    #def removeWithButton(self):
    #    selection = self.compound_box.curselection()
    #    value = widget.get(selection[0])
    #    self.compound_box.delete(selection[0])
    #    self.selected_compound_list.remove(selection[0])
    #    print(self.selected_compound_list)

    def addOnDouble(self,event):
        widget = event.widget
        selection = widget.curselection()
        value = widget.get(selection[0])
        self.compound_box.insert(tk.END, value)
        self.selected_compound_list.append(value)
        print(self.selected_compound_list)

    def create_widgets(self):
        self.search_var = tk.StringVar()
        self.search_var.trace("w", lambda name, index, mode: self.update_list())
        self.entry = tk.Entry(self, textvariable=self.search_var, width=13)
        self.lbox = tk.Listbox(self, width=45, height=15)
        self.lbox.bind('<Double-Button-1>', self.addOnDouble)
        self.entry.pack()
        self.lbox.pack()

        # Function for updating the list/doing the search.
        # It needs to be called here to populate the listbox.
        self.update_list()

    def update_list(self):
        search_term = self.search_var.get()

        # populate the listbox
        lbox_list = compound_list

        self.lbox.delete(0, tk.END)

        for item in lbox_list:
            if search_term.lower() in item.lower():
                self.lbox.insert(tk.END, item)

class AutocompleteCombobox(ttk.Combobox):

        def on_combo_configure(event):
            width = 20
            style = ttk.Style()
            style.configure('TCombobox', postoffset=(0, 0, width, 0))

        def set_completion_list(self, completion_list):
            """Use our completion list as our drop down selection menu, arrows move through menu."""
            self._completion_list = sorted(completion_list, key=str.lower)  # Work with a sorted list
            self._hits = []
            self._hit_index = 0
            self.position = 0
            self.bind('<KeyRelease>', self.handle_keyrelease)
            self['values'] = self._completion_list  # Setup our popup menu

        def autocomplete(self, delta=0):
            """autocomplete the Combobox, delta may be 0/1/-1 to cycle through possible hits"""
            if delta:  # need to delete selection otherwise we would fix the current position

                self.delete(self.position, tk.END)

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

                self.delete(0, tk.END)
                self.insert(0, self._hits[self._hit_index])

                self.select_range(self.position, tk.END)

        def handle_keyrelease(self, event):
            """event handler for the keyrelease event on this widget"""
            if event.keysym == "BackSpace":

                self.delete(self.index(tk.INSERT), tk.END)

                self.position = self.index(tk.END)
            if event.keysym == "Left":
                if self.position < self.index(tk.END):  # delete the selection

                    self.delete(self.position, tk.END)

                else:
                    self.position = self.position - 1  # delete one character

                    self.delete(self.position, tk.END)

            if event.keysym == "Right":
                self.position = self.index(tk.END)  # go to end (no selection)
            if len(event.keysym) == 1:
                self.autocomplete()
                # No need for up/down, we'll jump to the popup
                # list at the position of the autocompletion

app = PR()
app.mainloop()

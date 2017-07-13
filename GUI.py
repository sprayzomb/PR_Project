import tkinter as tk
from tkinter import ttk
import pandas as pd
import tkinter.font as tkfont
import csv
#import numpy as np

filename = "proptable.csv"

table_df = pd.read_csv(filename).set_index("Unnamed: 0")
table_df.index.name = None
table_df.columns = table_df.columns.astype(str)

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

class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        #label = tk.Label(self, text="Page Two", font=LARGE_FONT)
        #label.grid(column=1, row=1)

        self.addButton = ttk.Button(self, text="Add")
                            #command=self.addOnDouble)
        self.addButton.grid(column=6, row=3)

        self.removeButton = ttk.Button(self, text="Remove")
                            #command=self.removeWithButton)
        self.removeButton.grid(column=6, row=4)

        self.createButton = ttk.Button(self, text="Create", command=lambda: self.updateLabels())
        self.createButton.grid(column=11, row=7)

        self.compound_box = tk.Listbox(self, width=45, height=15)
        self.compound_box.bind('<Double-Button-1>', self.removeOnDouble)
        self.compound_box.grid(column=7, row=2, columnspan=5, rowspan=5)

        ttk.Separator(self, orient='horizontal').grid(column=1, row=8, columnspan=11, sticky='ew')

        label = tk.Label(self, text="Compound Name")
        label.grid(column=1, row=9)

        self.compound_1_label = tk.StringVar(value="")
        self.compound_1_label_box = tk.Entry(self, textvariable=self.compound_1_label)
        self.compound_1_label_box.config(state=tk.DISABLED)
        self.compound_1_label_box.config(disabledbackground='white')
        self.compound_1_label_box.config(disabledforeground='black')
        self.compound_1_label_box.grid(column=1, row=10)

        self.compound_2_label = tk.StringVar(value="")
        self.compound_2_label_box = tk.Entry(self, textvariable=self.compound_2_label)
        self.compound_2_label_box.config(state=tk.DISABLED)
        self.compound_2_label_box.config(disabledbackground='white')
        self.compound_2_label_box.config(disabledforeground='black')
        self.compound_2_label_box.grid(column=1, row=11)

        self.compound_3_label = tk.StringVar(value="")
        self.compound_3_label_box = tk.Entry(self, textvariable=self.compound_3_label)
        self.compound_3_label_box.config(state=tk.DISABLED)
        self.compound_3_label_box.config(disabledbackground='white')
        self.compound_3_label_box.config(disabledforeground='black')
        self.compound_3_label_box.grid(column=1, row=12)

        self.compound_4_label = tk.StringVar(value="")
        self.compound_4_label_box = tk.Entry(self, textvariable=self.compound_4_label)
        self.compound_4_label_box.config(state=tk.DISABLED)
        self.compound_4_label_box.config(disabledbackground='white')
        self.compound_4_label_box.config(disabledforeground='black')
        self.compound_4_label_box.grid(column=1, row=13)

        self.compound_5_label = tk.StringVar(value="")
        self.compound_5_label_box = tk.Entry(self, textvariable=self.compound_5_label)
        self.compound_5_label_box.config(state=tk.DISABLED)
        self.compound_5_label_box.config(disabledbackground='white')
        self.compound_5_label_box.config(disabledforeground='black')
        self.compound_5_label_box.grid(column=1, row=14)

        self.compound_6_label = tk.StringVar(value="")
        self.compound_6_label_box = tk.Entry(self, textvariable=self.compound_6_label)
        self.compound_6_label_box.config(state=tk.DISABLED)
        self.compound_6_label_box.config(disabledbackground='white')
        self.compound_6_label_box.config(disabledforeground='black')
        self.compound_6_label_box.grid(column=1, row=15)


        self.selected_compound_list=[]
        self.create_widgets()

    def updateLabels(self):
        self.compound_1_label_box.config(state=tk.NORMAL)
        self.compound_1_label_box.delete(0, tk.END)
        self.compound_1_label_box.insert(0, self.selected_compound_list[0])
        self.compound_1_label_box.config(state=tk.DISABLED)

        self.compound_2_label_box.config(state=tk.NORMAL)
        self.compound_2_label_box.delete(0, tk.END)
        self.compound_2_label_box.insert(0, self.selected_compound_list[1])
        self.compound_2_label_box.config(state=tk.DISABLED)

        self.compound_3_label_box.config(state=tk.NORMAL)
        self.compound_3_label_box.delete(0, tk.END)
        self.compound_3_label_box.insert(0, self.selected_compound_list[2])
        self.compound_3_label_box.config(state=tk.DISABLED)

        self.compound_4_label_box.config(state=tk.NORMAL)
        self.compound_4_label_box.delete(0, tk.END)
        self.compound_4_label_box.insert(0, self.selected_compound_list[3])
        self.compound_4_label_box.config(state=tk.DISABLED)

        self.compound_5_label_box.config(state=tk.NORMAL)
        self.compound_5_label_box.delete(0, tk.END)
        self.compound_5_label_box.insert(0, self.selected_compound_list[4])
        self.compound_5_label_box.config(state=tk.DISABLED)

        self.compound_6_label_box.config(state=tk.NORMAL)
        self.compound_6_label_box.delete(0, tk.END)
        self.compound_6_label_box.insert(0, self.selected_compound_list[5])
        self.compound_6_label_box.config(state=tk.DISABLED)
        return

    def pull_data(name, column):
        return table_df.loc[name, column]

    def removeOnDouble(self,event):
        widget = event.widget
        selection = widget.curselection()
        value = widget.get(selection[0])
        self.compound_box.delete(selection[0])
        self.selected_compound_list.remove(value)
        print(self.selected_compound_list)
        #print(self.selected_compound_list[0])

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
        self.entry.grid(column=2, row=1)
        self.lbox.grid(column=1, row=2, columnspan=5, rowspan=5)

        # Function for updating the list/doing the search.
        # It needs to be called here to populate the listbox.
        self.update_list()

    def update_list(self):
        search_term = self.search_var.get()

        # Populate the listbox
        self.lbox_list = compound_list

        self.lbox.delete(0, tk.END)

        for item in self.lbox_list:
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


#class TableReading():
#
#    def pull_data(name, column):
#        return table_df.loc[name, column]
#
#    omega = np.array([pull_data(f, "Tc(K)") for f in PageTwo.selected_compound_list])
#    print(omega)

app = PR()
app.mainloop()

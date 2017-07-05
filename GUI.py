import tkinter as tk
from tkinter import ttk
import csv


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

        with open('compounds.csv', 'r') as f:
            reader = csv.reader(f)
            compound_list = list(reader)

        compound = tk.StringVar()
        box = ttk.Combobox(self, textvariable = compound,
                           state='readonly', width=8)
        box['values'] = (compound_list)
        box.current(0)
        box.pack()


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


app = PR()
app.mainloop()

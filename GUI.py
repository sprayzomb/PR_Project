import tkinter as tk
from tkinter import ttk
import pandas as pd
import math
import tkinter.font as tkfont
import csv
import numpy as np

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

        for F in (StartPage, PageTwo):

            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(PageTwo)

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()

class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        #label = tk.Label(self, text="Start Page", font=LARGE_FONT)
        #label.pack(pady=10, padx=10)

        #button2 = ttk.Button(self, text="Visit PageTwo",
        #                     command=lambda: [controller.show_frame(PageTwo)])
        #button2.grid(row=5, column=5)

class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        #label = tk.Label(self, text="Page Two", font=LARGE_FONT)
        #label.grid(column=1, row=1)
        self.grid(padx=20, pady=20)

        self.addButton = ttk.Button(self, text="Add")
                            #command=self.addOnDouble)
        self.addButton.grid(column=6, row=3)

        self.removeButton = ttk.Button(self, text="Remove")
                            #command=self.removeWithButton)
        self.removeButton.grid(column=6, row=4)

        self.createButton = ttk.Button(self, text="Create", command=lambda: self.createWrapper())
        self.createButton.grid(column=11, row=7)

        self.createButton = ttk.Button(self, text="Calculate", command=lambda: self.calculator())
        self.createButton.grid(column=11, row=14)

        self.compound_box = tk.Listbox(self, width=45, height=15)
        self.compound_box.bind('<Double-Button-1>', self.removeOnDouble)
        self.compound_box.grid(column=7, row=2, columnspan=5, rowspan=5)

        ttk.Separator(self, orient='horizontal').grid(column=1, row=8, columnspan=11, sticky='ew')

        label = tk.Label(self, text="Search :")
        label.grid(column=1, row=1, sticky="W")
        label = tk.Label(self, text="Compound Name")
        label.grid(column=1, row=9)
        label = tk.Label(self, text="Mole Fraction")
        label.grid(column=2, row=9)
#Compound names will be transfered below boxes.
        self.compound_1_name = tk.StringVar(value="")
        self.compound_1_name_box = tk.Entry(self, textvariable=self.compound_1_name)
        self.compound_1_name_box.config(state=tk.DISABLED)
        self.compound_1_name_box.config(disabledbackground='white')
        self.compound_1_name_box.config(disabledforeground='black')
        self.compound_1_name_box.grid(column=1, row=10, sticky="E", padx=5, pady=5)

        self.compound_2_name = tk.StringVar(value="")
        self.compound_2_name_box = tk.Entry(self, textvariable=self.compound_2_name)
        self.compound_2_name_box.config(state=tk.DISABLED)
        self.compound_2_name_box.config(disabledbackground='white')
        self.compound_2_name_box.config(disabledforeground='black')
        self.compound_2_name_box.grid(column=1, row=11, sticky="E", padx=5, pady=5)

        self.compound_3_name = tk.StringVar(value="")
        self.compound_3_name_box = tk.Entry(self, textvariable=self.compound_3_name)
        self.compound_3_name_box.config(state=tk.DISABLED)
        self.compound_3_name_box.config(disabledbackground='white')
        self.compound_3_name_box.config(disabledforeground='black')
        self.compound_3_name_box.grid(column=1, row=12, sticky="E", padx=5, pady=5)

        self.compound_4_name = tk.StringVar(value="")
        self.compound_4_name_box = tk.Entry(self, textvariable=self.compound_4_name)
        self.compound_4_name_box.config(state=tk.DISABLED)
        self.compound_4_name_box.config(disabledbackground='white')
        self.compound_4_name_box.config(disabledforeground='black')
        self.compound_4_name_box.grid(column=1, row=13, sticky="E", padx=5, pady=5)

        self.compound_5_name = tk.StringVar(value="")
        self.compound_5_name_box = tk.Entry(self, textvariable=self.compound_5_name)
        self.compound_5_name_box.config(state=tk.DISABLED)
        self.compound_5_name_box.config(disabledbackground='white')
        self.compound_5_name_box.config(disabledforeground='black')
        self.compound_5_name_box.grid(column=1, row=14, sticky="E", padx=5, pady=5)

        self.compound_6_name = tk.StringVar(value="")
        self.compound_6_name_box = tk.Entry(self, textvariable=self.compound_6_name)
        self.compound_6_name_box.config(state=tk.DISABLED)
        self.compound_6_name_box.config(disabledbackground='white')
        self.compound_6_name_box.config(disabledforeground='black')
        self.compound_6_name_box.grid(column=1, row=15, sticky="E", padx=5, pady=5)
# Compound names will be transfered above boxes.

# Mole fractions will be entered below boxes.
        self.compound_1_mole_fraction = tk.StringVar(value="")
        self.compound_1_mole_fraction_box = tk.Entry(self, textvariable=self.compound_1_mole_fraction)
        self.compound_1_mole_fraction_box.config(state=tk.DISABLED)
        self.compound_1_mole_fraction_box.config(disabledbackground='white')
        self.compound_1_mole_fraction_box.config(disabledforeground='black')
        self.compound_1_mole_fraction_box.grid(column=2, row=10, sticky="E")

        self.compound_2_mole_fraction = tk.StringVar(value="")
        self.compound_2_mole_fraction_box = tk.Entry(self, textvariable=self.compound_2_mole_fraction)
        self.compound_2_mole_fraction_box.config(state=tk.DISABLED)
        self.compound_2_mole_fraction_box.config(disabledbackground='white')
        self.compound_2_mole_fraction_box.config(disabledforeground='black')
        self.compound_2_mole_fraction_box.grid(column=2, row=11, sticky="E")

        self.compound_3_mole_fraction = tk.StringVar(value="")
        self.compound_3_mole_fraction_box = tk.Entry(self, textvariable=self.compound_3_mole_fraction)
        self.compound_3_mole_fraction_box.config(state=tk.DISABLED)
        self.compound_3_mole_fraction_box.config(disabledbackground='white')
        self.compound_3_mole_fraction_box.config(disabledforeground='black')
        self.compound_3_mole_fraction_box.grid(column=2, row=12, sticky="E")

        self.compound_4_mole_fraction = tk.StringVar(value="")
        self.compound_4_mole_fraction_box = tk.Entry(self, textvariable=self.compound_4_mole_fraction)
        self.compound_4_mole_fraction_box.config(state=tk.DISABLED)
        self.compound_4_mole_fraction_box.config(disabledbackground='white')
        self.compound_4_mole_fraction_box.config(disabledforeground='black')
        self.compound_4_mole_fraction_box.grid(column=2, row=13, sticky="E")

        self.compound_5_mole_fraction = tk.StringVar(value="")
        self.compound_5_mole_fraction_box = tk.Entry(self, textvariable=self.compound_5_mole_fraction)
        self.compound_5_mole_fraction_box.config(state=tk.DISABLED)
        self.compound_5_mole_fraction_box.config(disabledbackground='white')
        self.compound_5_mole_fraction_box.config(disabledforeground='black')
        self.compound_5_mole_fraction_box.grid(column=2, row=14, sticky="E")

        self.compound_6_mole_fraction = tk.StringVar(value="")
        self.compound_6_mole_fraction_box = tk.Entry(self, textvariable=self.compound_6_mole_fraction)
        self.compound_6_mole_fraction_box.config(state=tk.DISABLED)
        self.compound_6_mole_fraction_box.config(disabledbackground='white')
        self.compound_6_mole_fraction_box.config(disabledforeground='black')
        self.compound_6_mole_fraction_box.grid(column=2, row=15, sticky="E")

# Mole fractions will be entered above boxes.

        self.temperature = tk.StringVar(value="")
        self.temperature_box = tk.Entry(self, textvariable=self.temperature)
        #self.temperature_box.config(state=tk.DISABLED)
        self.temperature_box.config(disabledbackground='white')
        self.temperature_box.config(disabledforeground='black')
        self.temperature_box.grid(column=7, row=10, sticky="E")

        self.pressure = tk.StringVar(value="")
        self.pressure_box = tk.Entry(self, textvariable=self.pressure)
        # self.pressure_box.config(state=tk.DISABLED)
        self.pressure_box.config(disabledbackground='white')
        self.pressure_box.config(disabledforeground='black')
        self.pressure_box.grid(column=8, row=10, sticky="E")

        self.selected_compound_list=[]
        self.selected_compound_fractions_list=[]
        self.selected_compound_fractions_list=[]
        self.create_widgets()

    def pull_data(self, name, column):
        return table_df.loc[name, column]

    def createWrapper(self):
        self.updateLabels()

    def fractionget(self):
        if len(self.selected_compound_list)>= 1:
            self.selected_compound_fractions_list.append(self.compound_1_mole_fraction_box.get())

        if len(self.selected_compound_list)>= 2:
            self.selected_compound_fractions_list.append(self.compound_2_mole_fraction_box.get())

        if len(self.selected_compound_list) >= 3:
            self.selected_compound_fractions_list.append(self.compound_3_mole_fraction_box.get())

        if len(self.selected_compound_list) >= 4:
            self.selected_compound_fractions_list.append(self.compound_4_mole_fraction_box.get())

        if len(self.selected_compound_list) >= 5:
            self.selected_compound_fractions_list.append(self.compound_5_mole_fraction_box.get())

        if len(self.selected_compound_list) >= 6:
            self.selected_compound_fractions_list.append(self.compound_6_mole_fraction_box.get())
        #print(self.selected_compound_fractions_list)

    def calculator(self):
        self.R=8.3145
        self.fractionget()
        self.temperature_entered = self.temperature_box.get()
        self.pressure_entered = self.pressure_box.get()
        self.TC_List = list()
        self.TR_List = list()
        self.PC_List = list()
        self.w_List = list()
        for i in self.selected_compound_list:
            self.TC_List.append(self.pull_data(i, "Tc(K)"))
            self.PC_List.append(self.pull_data(i, "Pc(MPa)")*1.01325)
            self.w_List.append(self.pull_data(i, "w"))
            #self.TR_List.append(self.temperature_entered / self.TC_List[i])

        print(self.TC_List)
        print(self.PC_List)
        print(self.w_List)

        numberOfCompunds = len(self.selected_compound_list)
        self.a_List = list()
        self.b_List = list()
        self.k_List = list()
        self.alpha_List = list()
        for i in range(0, numberOfCompunds):
            self.k_List.append(0.37464 + 1.54226 * self.w_List[i] - 0.26992*self.w_List[i]**2)

            self.alpha_List.append((1+self.k_List[i]*(1-(float(self.temperature_entered)/self.TC_List[i])**0.5))**2)

            self.a_List.append(0.45724*self.alpha_List[i]*(self.R**2)*(self.TC_List[i]**2)/(self.PC_List[i]*100000))

            self.b_List.append(0.07780*(self.R)*self.TC_List[i]/(self.PC_List[i]*100000))

        print(self.a_List)
        print(self.b_List)


#PROBLEM STARTS HERE
        self.aMix_List = list()
        self.bMix_List = list()
        for i in range(0, numberOfCompunds):
            self.bMix_List.append(float(self.selected_compound_fractions_list[i])*
                                  float(self.b_List[i]))
            for j in range(0, numberOfCompunds):
                self.aMix_List.append(float(self.selected_compound_fractions_list[i])*
                                      float(self.selected_compound_fractions_list[j])*
                                      math.sqrt(float(self.a_List[i])*float(self.a_List[j])))

        self.aM = sum(set(self.aMix_List))
        self.bM = sum(set(self.bMix_List))

        print(self.aM)
        print(self.bM)

        self.A = self.aM * float(self.pressure_entered) / ((self.R**2)*(float(self.temperature_entered)**2))
        self.B = self.bM * float(self.pressure_entered) / (self.R * float(self.temperature_entered))

        print(self.A)
        print(self.B)

        self.z3coef = 1
        self.z2coef = -(1-self.B)
        self.z1coef = self.A - 2*self.B - 3*(self.B**2)
        self.z0coef = -(self.A*self.B - 2*self.B - self.B**2)

        #p = P([self.z0coef, self.z1coef, self.z2coef, self.z3coef])
        p = [self.z3coef, self.z2coef, self.z1coef, self.z0coef]
        #print(self.z3coef)
        #print(self.z2coef)
        #print(self.z1coef)
        #print(self.z0coef)
        #roots=np.roots(p)
        #print(roots)
        #print(roots[~np.iscomplex(roots)])

    def updateLabels(self):

        self.compound_1_name_box.config(state=tk.NORMAL)
        self.compound_1_name_box.delete(0, tk.END)
        self.compound_2_name_box.config(state=tk.NORMAL)
        self.compound_2_name_box.delete(0, tk.END)
        self.compound_3_name_box.config(state=tk.NORMAL)
        self.compound_3_name_box.delete(0, tk.END)
        self.compound_4_name_box.config(state=tk.NORMAL)
        self.compound_4_name_box.delete(0, tk.END)
        self.compound_5_name_box.config(state=tk.NORMAL)
        self.compound_5_name_box.delete(0, tk.END)
        self.compound_6_name_box.config(state=tk.NORMAL)
        self.compound_6_name_box.delete(0, tk.END)
        self.compound_1_mole_fraction_box.config(state=tk.NORMAL)
        self.compound_1_mole_fraction_box.delete(0, tk.END)
        self.compound_2_mole_fraction_box.config(state=tk.NORMAL)
        self.compound_2_mole_fraction_box.delete(0, tk.END)
        self.compound_3_mole_fraction_box.config(state=tk.NORMAL)
        self.compound_3_mole_fraction_box.delete(0, tk.END)
        self.compound_4_mole_fraction_box.config(state=tk.NORMAL)
        self.compound_4_mole_fraction_box.delete(0, tk.END)
        self.compound_5_mole_fraction_box.config(state=tk.NORMAL)
        self.compound_5_mole_fraction_box.delete(0, tk.END)
        self.compound_6_mole_fraction_box.config(state=tk.NORMAL)
        self.compound_6_mole_fraction_box.delete(0, tk.END)


        numberOfCompunds = len(self.selected_compound_list)
        if numberOfCompunds >= 1:
            #self.compound_1_name_box.config(state=tk.NORMAL)
            #self.compound_1_name_box.delete(0, tk.END)
            self.compound_1_name_box.insert(0, self.selected_compound_list[0])
            self.compound_1_name_box.config(state=tk.DISABLED)
            self.compound_1_mole_fraction_box.config(state=tk.NORMAL)
            self.compound_1_mole_fraction_box.delete(0, tk.END)
            #self.name1 = self.compound_1_name_box.get()
            #self.compund1_TC = self.pull_data(self.name1, "Tc(K)")
            #self.compund1_PC = self.pull_data(self.name1, "Pc(MPa)")
            #self.compund1_w = self.pull_data(self.name1, "w")

        else:
            self.compound_1_name_box.config(state=tk.DISABLED)
            self.compound_1_mole_fraction_box.config(state=tk.DISABLED)
            self.compound_2_name_box.config(state=tk.DISABLED)
            self.compound_2_mole_fraction_box.config(state=tk.DISABLED)
            self.compound_3_name_box.config(state=tk.DISABLED)
            self.compound_3_mole_fraction_box.config(state=tk.DISABLED)
            self.compound_4_name_box.config(state=tk.DISABLED)
            self.compound_4_mole_fraction_box.config(state=tk.DISABLED)
            self.compound_5_name_box.config(state=tk.DISABLED)
            self.compound_5_mole_fraction_box.config(state=tk.DISABLED)
            self.compound_6_name_box.config(state=tk.DISABLED)
            self.compound_6_mole_fraction_box.config(state=tk.DISABLED)

        if numberOfCompunds >= 2:
            #self.compound_2_name_box.config(state=tk.NORMAL)
            #self.compound_2_name_box.delete(0, tk.END)
            self.compound_2_name_box.insert(0, self.selected_compound_list[1])
            self.compound_2_name_box.config(state=tk.DISABLED)
            self.compound_2_mole_fraction_box.config(state=tk.NORMAL)
            self.compound_2_mole_fraction_box.delete(0, tk.END)
            #self.name2 = self.compound_2_name_box.get()
            #self.compund2_TC = self.pull_data(self.name2, "Tc(K)")
            #self.compund2_PC = self.pull_data(self.name2, "Pc(MPa)")
            #self.compund2_w = self.pull_data(self.name2, "w")

        else:
            self.compound_2_name_box.config(state=tk.DISABLED)
            self.compound_2_mole_fraction_box.config(state=tk.DISABLED)
            self.compound_3_name_box.config(state=tk.DISABLED)
            self.compound_3_mole_fraction_box.config(state=tk.DISABLED)
            self.compound_4_name_box.config(state=tk.DISABLED)
            self.compound_4_mole_fraction_box.config(state=tk.DISABLED)
            self.compound_5_name_box.config(state=tk.DISABLED)
            self.compound_5_mole_fraction_box.config(state=tk.DISABLED)
            self.compound_6_name_box.config(state=tk.DISABLED)
            self.compound_6_mole_fraction_box.config(state=tk.DISABLED)

        if numberOfCompunds >= 3:
            #self.compound_3_name_box.config(state=tk.NORMAL)
            #self.compound_3_name_box.delete(0, tk.END)
            self.compound_3_name_box.insert(0, self.selected_compound_list[2])
            self.compound_3_name_box.config(state=tk.DISABLED)
            self.compound_3_mole_fraction_box.config(state=tk.NORMAL)
            self.compound_3_mole_fraction_box.delete(0, tk.END)
            #self.name3 = self.compound_3_name_box.get()
            #self.compund3_TC = self.pull_data(self.name3, "Tc(K)")
            #self.compund3_PC = self.pull_data(self.name3, "Pc(MPa)")
            #self.compund3_w = self.pull_data(self.name3, "w")
        else:
            self.compound_3_name_box.config(state=tk.DISABLED)
            self.compound_3_mole_fraction_box.config(state=tk.DISABLED)
            self.compound_4_name_box.config(state=tk.DISABLED)
            self.compound_4_mole_fraction_box.config(state=tk.DISABLED)
            self.compound_5_name_box.config(state=tk.DISABLED)
            self.compound_5_mole_fraction_box.config(state=tk.DISABLED)
            self.compound_6_name_box.config(state=tk.DISABLED)
            self.compound_6_mole_fraction_box.config(state=tk.DISABLED)

        if numberOfCompunds >= 4:
            #self.compound_4_name_box.config(state=tk.NORMAL)
            #self.compound_4_name_box.delete(0, tk.END)
            self.compound_4_name_box.insert(0, self.selected_compound_list[3])
            self.compound_4_name_box.config(state=tk.DISABLED)
            self.compound_4_mole_fraction_box.config(state=tk.NORMAL)
            self.compound_4_mole_fraction_box.delete(0, tk.END)
            #self.name4 = self.compound_4_name_box.get()
            #self.compund4_TC = self.pull_data(self.name4, "Tc(K)")
            #self.compund4_PC = self.pull_data(self.name4, "Pc(MPa)")
            #self.compund4_w = self.pull_data(self.name4, "w")
        else:
            self.compound_4_name_box.config(state=tk.DISABLED)
            self.compound_4_mole_fraction_box.config(state=tk.DISABLED)
            self.compound_5_name_box.config(state=tk.DISABLED)
            self.compound_5_mole_fraction_box.config(state=tk.DISABLED)
            self.compound_6_name_box.config(state=tk.DISABLED)
            self.compound_6_mole_fraction_box.config(state=tk.DISABLED)

        if numberOfCompunds >= 5:
            #self.compound_5_name_box.config(state=tk.NORMAL)
            #self.compound_5_name_box.delete(0, tk.END)
            self.compound_5_name_box.insert(0, self.selected_compound_list[4])
            self.compound_5_name_box.config(state=tk.DISABLED)
            self.compound_5_mole_fraction_box.config(state=tk.NORMAL)
            self.compound_5_mole_fraction_box.delete(0, tk.END)
            #self.name5 = self.compound_1_name_box.get()
            #self.compund5_TC = self.pull_data(self.name5, "Tc(K)")
            #self.compund5_PC = self.pull_data(self.name5, "Pc(MPa)")
            #self.compund5_w = self.pull_data(self.name5, "w")
        else:
            self.compound_5_name_box.config(state=tk.DISABLED)
            self.compound_5_mole_fraction_box.config(state=tk.DISABLED)
            self.compound_6_name_box.config(state=tk.DISABLED)
            self.compound_6_mole_fraction_box.config(state=tk.DISABLED)

        if numberOfCompunds >= 6:
            #self.compound_6_name_box.config(state=tk.NORMAL)
            #self.compound_6_name_box.delete(0, tk.END)
            self.compound_6_name_box.insert(0, self.selected_compound_list[5])
            self.compound_6_name_box.config(state=tk.DISABLED)
            self.compound_6_mole_fraction_box.config(state=tk.NORMAL)
            self.compound_6_mole_fraction_box.delete(0, tk.END)
            #self.name6 = self.compound_1_name_box.get()
            #self.compund6_TC = self.pull_data(self.name6, "Tc(K)")
            #self.compund6_PC = self.pull_data(self.name6, "Pc(MPa)")
            #self.compund6_w = self.pull_data(self.name6, "w")
        else:
            self.compound_6_name_box.config(state=tk.DISABLED)
            self.compound_6_mole_fraction_box.config(state=tk.DISABLED)

    def removeOnDouble(self,event):
        widget = event.widget
        selection = widget.curselection()
        value = widget.get(selection[0])
        self.compound_box.delete(selection[0])
        self.selected_compound_list.remove(value)
        #print(self.selected_compound_list)
        #print(len(self.selected_compound_list))
        self.lbox_list.append(value)
        self.update_list()

    def addOnDouble(self,event):
        widget = event.widget
        selection = widget.curselection()
        value = widget.get(selection[0])
        self.compound_box.insert(tk.END, value)
        self.selected_compound_list.append(value)
        #print(self.selected_compound_list)
        #print(len(self.selected_compound_list))
        self.lbox_list.remove(value)
        self.update_list()

    def create_widgets(self):
        self.search_var = tk.StringVar()
        self.search_var.trace("w", lambda name, index, mode: self.update_list())
        self.entry = tk.Entry(self, textvariable=self.search_var, width=13)
        self.lbox = tk.Listbox(self, width=45, height=15)
        self.lbox.bind('<Double-Button-1>', self.addOnDouble)
        self.entry.grid(column=2, row=1, sticky="W")
        self.lbox.grid(column=1, row=2, columnspan=5, rowspan=5, sticky="E")

        # Function for updating the list/doing the search.
        # It needs to be called here to populate the listbox.
        self.update_list()

    def update_list(self):
        search_term = self.search_var.get()

        # Populate the listbox
        self.lbox_list = compound_list
        self.lbox_list.sort()

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

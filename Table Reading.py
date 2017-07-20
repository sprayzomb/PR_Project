import pandas as pd
import numpy as np

filename = "proptable.csv"

table_df = pd.read_csv(filename).set_index("Unnamed: 0")
table_df.index.name = None
table_df.columns = table_df.columns.astype(str)

def pull_data(name, column):
    return table_df.loc[name, column]

name="METHANE"
print(pull_data(name, "Tc(K)"))

Kij_Array=np.zeros((2,3))
print(Kij_Array[1,2])
print(Kij_Array)
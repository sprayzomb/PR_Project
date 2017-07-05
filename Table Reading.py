import pandas as pd

filename = "proptable.csv"

table_df = pd.read_csv(filename).set_index("Unnamed: 0")
table_df.index.name = None
table_df.columns = table_df.columns.astype(str)

def pull_data(name, column):
    return table_df.loc[name, column]

print(pull_data("METHANE", "Tc(K)"))
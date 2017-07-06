import pandas as pd

filename = "compounds.csv"
table_df = pd.read_csv(filename).set_index("Unnamed: 0")

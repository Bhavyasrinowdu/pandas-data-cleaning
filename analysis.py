import pandas as pd
df = pd.read_csv("cleaned_data.csv")
print("Average Age:", df["Age"].mean())
print("City Distribution:\n", df["City"].value_counts())
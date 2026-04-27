import pandas as pd
df = pd.read_csv("data.csv")
df = df.drop_duplicates()
df.to_csv("cleaned_data.csv", index=False)
print("Data cleaned successfully ✅\")
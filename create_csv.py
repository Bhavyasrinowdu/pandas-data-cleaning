import pandas as pd
data = {
    "Name": ["Bhavya", "Anu", "Ravi"],
    "Age": [20, 21, 22],
    "City": ["Chennai", "Hyderabad", "Bangalore"]
}
df = pd.DataFrame(data)
df.to_csv("data.csv", index=False)
print("CSV file created successfully")

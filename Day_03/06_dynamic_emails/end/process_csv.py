import pandas as pd

# Read the CSV file
df = pd.read_csv("./sample.csv")

# Iterate through the rows of the DataFrame
for index, row in df.iterrows():
    print(row["Name"], row["Email"])

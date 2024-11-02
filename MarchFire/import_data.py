import pandas as pd

# Read the spreadsheet data
df = pd.read_csv('FireExt for project Apr 24.csv')  # replace with your file name

# Convert to JSON
json_data = df.to_json(orient='records')
print(json_data)

# Convert to tuples
tuple_data = list(df.itertuples(index=False, name=None))
print(tuple_data)
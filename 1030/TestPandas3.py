import pandas as pd
df = pd.read_json('Sample.json')
df.to_json('Sample_records.json',orient='records')
df.to_json('Sample_split.json',orient='split')
df.to_json('Sample_columns.json',orient='columns')
df.to_json('Sample_index.json',orient='index')
df.to_json('Sample_values.json',orient='values')
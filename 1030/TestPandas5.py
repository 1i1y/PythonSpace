#讀sql檔

import sqlalchemy
import pandas as pd

engine = sqlalchemy.create_engine('sqlite:///nobel_prize.db')
df     = pd.read_sql('winners',engine)

print(df.head())

import pandas as pd

df = pd.read_csv('8f7615b1-f6ed-41e6-871c-28129b7e9afa.csv')

cols = df.columns.tolist()

cols = sorted(cols)
cols.insert(0, cols.pop(cols.index('date')))
cols.insert(1, cols.pop(cols.index('time')))

df = df[cols]


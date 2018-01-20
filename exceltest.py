# exceltest.py
#
# Excel import test
# G Liu, 2018-Jan-16

import pandas as pd
file = 'testdata.xlsx'

# load the spreadsheet
x1 = pd.ExcelFile(file)

print(x1.sheet_names)

# load into a DataFrame
df = x1.parse('data')

#print(df)
print("\n\nColumns:\n")
cols = df.columns
print(cols)

print("\n\nIndex:\n")
index = df.index
print(index)

print("\n\nValues:\n")
val = df.values
print(val)

searchstr = 'fre'
print("\n\nSearch - contains..%s\n", searchstr)
print(df.loc[df['name'].str.contains(searchstr)])

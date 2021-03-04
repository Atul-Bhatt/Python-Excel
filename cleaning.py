import pandas as pd
import numpy as np
from openpyxl.workbook import Workbook

df = pd.read_csv('Names.csv', header=None)
df.columns = ['First', 'Last Name', 'Address',
              'City', 'State', 'Area Code', 'Income']

df.drop(columns='Address', inplace=True)
df.set_index('Area Code', inplace=True)
# print(df.loc[8074])
# print(df.iloc[1])

df.First = df.First.str.split(expand=True)
df.replace(np.nan, 'N/A', regex=True, inplace=True)
df.to_excel('modified.xlsx')

import pandas as pd
from openpyxl.workbook import Workbook

df = pd.read_csv('Names.csv')

df.columns = ['First Name', 'Last Name', 'Address',
              'City', 'State', 'Area Code', 'Unknown']

#print(df['First Name'])
#print(df[['Last Name', 'First Name', 'Area Code']][0:4])
# print(df.iloc[0:2])
#print(df['Last Name'][1])
#print(df.iloc[1, 1])
wanted_values = df[['First Name', 'Last Name', 'Area Code']]

wanted_values.to_excel('firstLastAreaCode.xlsx')

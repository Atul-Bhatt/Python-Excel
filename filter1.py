import pandas as pd
from openpyxl.workbook import Workbook

df = pd.read_csv('Names.csv', header=None)
df.columns = ['First Name', 'Last Name',
              'Address', 'City', 'State', 'Area Code', 'Income']

#print(df.loc[(df['City'] == 'Riverside') & (df['First Name'] == 'John')])

df['Tax %'] = df['Income'].apply(
    lambda x: .15 if 10000 < x < 40000 else .2 if 40000 < x < 80000 else .25)

df['Taxes Owed'] = df['Income'] * df['Tax %']

# Dropping columns from dataframe

to_drop = ['First Name', 'Address', 'Area Code']
df.drop(columns=to_drop, inplace=True)


# Setting columns true whose income is greater than 60000
# df['Test Col'] = df['Income'].apply(
#     lambda x: True if x > 60000 else False)

df['Test Col'] = False
df.loc[df['Income'] > 60000, 'Test Col'] = True

print(df.groupby(['Test Col']).mean().sort_values('Income'))

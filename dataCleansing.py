import pandas as pd
df = pd.read_csv('Data/edited_googleplaystore_dataset.csv')

columns = ['App', 'Raiting', 'Reviews', 'Size', 'Number of Installs', 'Type', 'Price', 'Last Update']

df = pd.read_csv('Data/edited_googleplaystore_dataset.csv', names = columns, header = None, na_values = '-1')

df.index = df['Last Update']

#print(df[columns[:-1]])

nameCSV = 'CleansedData.csv'

df.to_csv(nameCSV)

nameEx = 'CleansedData.xlsx'

df.to_excel(nameEx)

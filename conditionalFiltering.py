import pandas as pd

df = pd.read_csv('Data/intel.csv')

#print(df)

#close = df['Close'] > 40

#print(close)

#print(df[close])

#print(df[df['Close']>40])

#Using Loc

print(df.loc[(df['Close']>40) & (df['Close']<46)])

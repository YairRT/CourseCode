import pandas as pd
df = pd.read_csv("Data/intel.csv")

#Print dataFrame
#print(df)

#Type
#print(type(df))

#Shape
#print(df.shape)

#view columns
#print(df.columns)

#Show first n elements (default to 5)
#print(df.head())

#Show last n elements (default ro 5)
#print(df.tail())

#Show info
print(df.info())

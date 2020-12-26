import pandas as pd
import numpy as np

npArray = np.arange(0,10).reshape(2, 5)

#print(npArray)

df = pd.DataFrame(data = npArray, columns = ['A', 'B', 'C', 'D', 'E'])

print(df)

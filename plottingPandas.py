import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('Data/intel.csv', index_col = 'Date', parse_dates=True)

#closeVal = df['Close'].values

#print(type(closeVal))

#plt.plot(closeVal)

#plt.show()

#df.plot()
#plt.show()

#df['Close'].plot(color = 'g', style = '-', legend = True)
#plt.axis(('2017','2018', 0, 60))

df.plot(color = 'blue')

plt.title('Stock Price')

plt.xlabel('Date Range')

plt.ylabel('Price ($)')

#plt.show()

#plt.savefig('df.pdf')
#plt.save('df.jpg')
plt.save('df.png')

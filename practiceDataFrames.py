import pandas as pd

activities = ['Programmming', 'Dancing', 'Working out', ' Reading']

schedule = ['10:00', '12:00', '14:00', '16:00']

days = [5, 3, 6, 7]

newList = [activities, schedule, days]

headers = ['Activity', 'Hour', 'Days of the week']

masterList = list(zip(headers, newList))

masterDict = dict(masterList)

df = pd.DataFrame(data = masterDict)

df['Days (updated)'] = 5

print(df)

newHeaders = ['Activity', 'Hour', 'Days', 'New Days']

df.columns = newHeaders

print(df)

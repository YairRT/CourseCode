import pandas as pd

courseSales = {'course': ['Python', 'Ruby', 'Excel', 'C++'],
                'day': ['Mon', 'Tue', 'Wed ', 'Thu'],
                'price': [5, 10, 15 , 20],
                'sale': [2, 3, 5, 7]}

#print(courseSales)

#Converting to DataFrame

dfCourse = pd.DataFrame(courseSales)

print(dfCourse)

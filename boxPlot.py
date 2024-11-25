#DONE render box plot of columns 
#TODO GUI
#TODO allow user to select file then select row or column(s) 

#sample boxplot
#import pandas as pd

#data = {'values': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]}
#df = pd.DataFrame(data)

#df.boxplot(column='values')
#plt.show()
import csv
import pandas as pd
import matplotlib.pyplot as plt

selection = []
with open ('Real_Estate_Sales_2001-2022_GL.csv','r',newline='') as csvfile1:
    reader = csv.DictReader(csvfile1)
    for row in reader:
        if row != 0:
            selection.append(float(row['Sales Ratio']))
df = pd.DataFrame(selection)
df.boxplot(showfliers=False)
plt.ylabel('Sales Ratio')
plt.xlabel(' ')
plt.show()
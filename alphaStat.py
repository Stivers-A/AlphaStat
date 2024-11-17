import csv



#Project Goals
#Part 1 The Basics, I hope!
#Make a program that can get the mean median and mode of a column or row


#TODO make it so 'Assessed Value' can be renamed to any specific column
#make second column an option with that



confidence = input("Enter confidence (IE 0.95 will result in an alpha of 0.05)")
alpha = 1 - float(confidence)
# if p is less than alpha reject null hypothesis, statistical signifigance has been aquired
#if p value is greater or equal to alpha we fail to reject null hypothesis
twoTailed = 1 
#1 = true 0 = false
column1name = input('Col1 name')
column2name = input('Col2 name')

column1 = []
#a matrix that can be filled
with open ('Real_Estate_Sales_2001-2022_GL.csv','r',newline='') as csvfile1:
    reader = csv.DictReader(csvfile1)
    for row in reader:
        column1.append(float(row[column1name]))
        #appending the value of each row in the column of assesed value gives the
lencolumn1 = len(column1)
sumcolumn1 = sum(column1)
avgcolumn1 = sumcolumn1/lencolumn1

column2 = []
#a matrix that can be filled
with open ('Real_Estate_Sales_2001-2022_GL.csv','r',newline='') as csvfile1:
    reader = csv.DictReader(csvfile1)
    for row in reader:
        column2.append(float(row[column2name]))
        #appending the value of each row in the column of assesed value gives the
lencolumn2 = len(column2)
sumcolumn2 = sum(column2)
avgcolumn2= sumcolumn2/lencolumn2
import csv
#with open('Real_Estate_Sales_2001-2022_GL.csv','r') as csv_file:
   # csv_reader = csv.reader(csv_file)
    #reader method uses a dialect to detect csv format, IE expecting variables delinated by a comma
    #next(csv_reader) skips the first line
    #print(csv_reader)
    #all that shows up is 'csv.reader object at (location)

    #with open('new_vals.csv','w') as new_file:
       # csv_writer = csv.writer(new_file, delimiter='-')
       # for line in csv_reader:
        #    print(line)
            #csv_writer.writerow(line) commented out to prevent spam creation of new files
            #opens a file and and uses csv.reader, then uses csv.writer to copy the content of the original with the delimenter as a dash

    #for line in csv_reader:
      #  print(line)
        #this renders each line of the csv as a line in the terminal 
        #print(line[2]) 
        # would print the second line


assesedValues = []
#a matrix that can be filled
with open ('Real_Estate_Sales_2001-2022_GL.csv','r',newline='') as csvfile1:
    reader = csv.DictReader(csvfile1)
    for row in reader:
        assesedValues.append(float(row['Assessed Value']))
        #appending the value of each row in the column of assesed value gives the
lenAssessedValue = len(assesedValues)
sumAssessedValue = sum(assesedValues)
avgAssessedValue = sumAssessedValue/lenAssessedValue

#sum over total is mean
print('mean assessed value: ', avgAssessedValue)

#median
assesedValues.sort()
# % aka modulo returns the remainder after division thus divide by 2 will return 0 if its an even number
if lenAssessedValue % 2 == 0:
    median0 = assesedValues[lenAssessedValue//2]
    median1 = assesedValues[lenAssessedValue//2 - 1]
    median = (median0 + median1)/2
else:
    median = assesedValues[lenAssessedValue//2]
print("Median is: ", median)
#median 0 and 1 are the middlemost numbers assuming that the list is even // is used to keep the results a whole integer making it useful for checking a specific row
#sorts the values smallest to largest
 
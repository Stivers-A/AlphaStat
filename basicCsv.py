import csv
with open('apple_quality_unedited.csv','r') as csv_file:
    csv_reader = csv.reader(csv_file)
    #reader method uses a dialect to detect csv format, IE expecting variables delinated by a comma
    print(csv_reader)
    #all that shows up is 'csv.reader object at (location)
    for line in csv_reader:
        print(line)
    #this renders each line of the csv as a line in the terminal
import csv
with open('apple_quality_unedited.csv','r') as csv_file:
    csv_reader = csv.reader(csv_file)
    #reader method uses a dialect to detect csv format, IE expecting variables delinated by a comma
    #next(csv_reader) skips the first line
    print(csv_reader)
    #all that shows up is 'csv.reader object at (location)

    with open('new_vals.csv','w') as new_file:
        csv_writer = csv.writer(new_file, delimiter='-')
        for line in csv_reader:
            print(line)
            #csv_writer.writerow(line) commented out to prevent spam creation of new files
            #opens a file and and uses csv.reader, then uses csv.writer to copy the content of the original with the delimenter as a dash

    for line in csv_reader:
        print(line)
        #this renders each line of the csv as a line in the terminal 
        #print(line[2]) 
        # would print the second line

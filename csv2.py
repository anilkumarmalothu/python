import csv
with open("employee_details.csv","r") as csv_file:
    csv_reader=csv.reader(csv_file,delimiter=',')
    for row in csv_reader:
        print(row)
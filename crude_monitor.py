import requests, sys, csv, json
from prettytable import PrettyTable
#python requirements prettytable-2.1.0 wcwidth-0.2.5
#MSW, Mixed Sweet Blend, crudes

#setting up all variables to be used in the program
acronym = "none"
name = "none"
database = "none"
URL = "https://www.crudemonitor.ca/savePHPExcel.php"
start_date = "none"
end_date = "none"
#True is greater than and False is less than
operation = True
limit = 0

#checking all the different possible inputs and putting them into the right variables
if("--acronym" in sys.argv):
    acronym = sys.argv[sys.argv.index("--acronym")+1]
    
if("--start_date" in sys.argv):
    start_date = sys.argv[sys.argv.index("--start_date")+1]
    
if("--end_date" in sys.argv):
    end_date = sys.argv[sys.argv.index("--end_date")+1]
    
if("--operation" in sys.argv):
    if sys.argv[sys.argv.index("--operation")+1] == '<':
        operation = False
    else:
        operation = True

if("--limit" in sys.argv):
    limit = sys.argv[sys.argv.index("--limit")+1]

#reading CSV file to find the other 2 parameters 
with open('Crude Monitor Parameters.csv', newline = '') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        if acronym == row['acr']:
            acronym = row['acr']
            name = row['name']
            database = row['database']
            break
                        
 

form_data = {
    "date1noscript": "",
    "date2noscript": "",
    "trendProperty": "AbsoluteDensity",
    "acr": acronym,
    "name": name,
    "db": database,
    "basicanalysis[]": "AbsoluteDensity",
    "options": "on",
    "date1": start_date,
    "date2": end_date,
    "format": "Export .JSON",
    "daterangepicker_start": "",
    "daterangepicker_end": "",
}

data = requests.post(url=URL, data=form_data)

#putting the text data into a list of lists with the first list being the headers
lines = data.text.splitlines()
reader = csv.reader(lines)
parsed_csv = list(reader)

#initialize the the table to hold all the data except for the first two columns which are the acronym and name of the crude oil
mytable = PrettyTable()
mytable.field_names = parsed_csv[0][2:]

#filtering out the values that aren't within the limit
for row in parsed_csv:
    if operation == True:
        
        if row[5] > limit:
            mytable.add_row(row[2:])
    
    else:
        if row[5] < limit:
            mytable.add_row(row[2:])

print(mytable)


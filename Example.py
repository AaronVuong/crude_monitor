import requests, sys, csv, json
from prettytable import from_csv

#MSW, Mixed Sweet Blend, crudes
acronym = "none"
name = "none"
database = "none"
URL = "https://www.crudemonitor.ca/savePHPExcel.php"
start_date = "none"
end_date = "none"

if("--acronym" in sys.argv):
    acronym = sys.argv[sys.argv.index("--acronym")+1]
    
if("--start_date" in sys.argv):
    start_date = sys.argv[sys.argv.index("--start_date")+1]
    
if("--end_date" in sys.argv):
    end_date = sys.argv[sys.argv.index("--end_date")+1]
    


#reading CSV file to find the other 2 parameters 
with open('Crude Monitor Parameters.csv', newline = '') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        if acronym == row['acr']:
            acronym = row['acr']
            name = row['name']
            database = row['database']
            break
                        
 
# Date should be in DDMMYYYY form
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
#data.json()
#with open(data.text) as f:
    #data_pulled = [json.loads(line) for line in f]

lines = data.text.splitlines()

reader = csv.reader(lines)
parsed_csv = list(reader)
with open(parsed_csv) as fp:
    mytable = from_csv(fp)

print(mytable)


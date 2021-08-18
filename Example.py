import requests, sys, csv


#MSW, Mixed Sweet Blend, crudes
acronym = "none"
name = "none"
database = "none"
URL = "https://www.crudemonitor.ca/savePHPExcel.php"


if("--acronym" in sys.argv):
    acronym = sys.argv[sys.argv.index("--acronym")+1]


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
    "date1": "13072019",
    "date2": "13072021",
    "format": "Export .JSON",
    "daterangepicker_start": "",
    "daterangepicker_end": "",
}

data = requests.post(url=URL, data=form_data)
print(data.text)
print(reader)


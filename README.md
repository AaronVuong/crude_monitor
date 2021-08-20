# crude_monitor
This application requires 5 inputs in the order of:

  1. acronym of the crude oil. Examples: MSW, P, CHN
  2. start date of the data. Examples: 12052011, 14122014,DDMMYYYY
  3. end date of the data.
  4. operation of the limit. Either a "<" to indicate less than or ">" to indicate greater than.
  5. Density of the crude oil in kg/m^3. A value less than or greater than the desired density. Examples: 820, 813
  
An example of how to run the program would be to use following inputs:
python crude_monitor.py --acronym MSW --start_date 17032012 --end_date 14022021 --operation "<" --limit 822

This application requires the CSV file Crude Monitor Parameters in the same folder as the application in order to run properly. 

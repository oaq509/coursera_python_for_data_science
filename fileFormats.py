import pandas as pd
import json
import xml.etree.ElementTree as etree

# CSV --------------------------------------------
# csv stand for Comma Separated Values
file = 'csv/noHeader.csv'
df = pd.read_csv(file)
df.columns = ['Name','Phone Number', 'Birthday']

# JSON -------------------------------------------
with open('json/employee.json','r') as openfile:
    json_object = json.load(openfile)
    
# XML --------------------------------------------
tree = etree.parse('example.xml')
root = tree.getroot()
columns = ['Name', 'Phone Number', 'Birthday']
df = pd.DataFrame(columns = columns)
# .....
# Then we create loop and assign each value to the data frame



# NOTES

# Comma-separated values (CSV) file format
# The Comma-separated values file format falls under a spreadsheet file format.
# In a spreadsheet file format, data is stored in cells. Each cell is organized in rows and columns. A column in the spreadsheet file can have different types. For example, a column can be of string type, a date type, or an integer type.
# Each line in CSV file represents an observation, or commonly called a record. Each record may contain one or more fields which are separated by a comma.
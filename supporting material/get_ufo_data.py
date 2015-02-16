"""
Get Data from the National UFO Reporting Center

Modified from example by Hideki Fujioka 
http://www.ccs.tulane.edu/~fuji/DataVisualization14/GetUFOReport.py
"""
import pandas as pd
import requests
from bs4 import BeautifulSoup

# Create list of states to loop through
#states = ['va', 'mo', 'az', 'pa', 'tx']

states =['AL','AK','AZ', 'AR','CA','CO','CT','DE','FL','GA','HI','ID','IL',
         'IN','IA','KS','KY','LA','ME','MD','MA','MI','MN','MS','MO','MT',
         'NE','NV','NH','NJ','NM','NY','NC','ND','OH','OK','OR','PA','RI',
         'SC','SD','TN','TX','UT','VT','VA','WA','WV','WI','WY']
         
# Initialize dataframe
df = pd.DataFrame()

for state in states:
    
    # Get HTML from URL
    #dat_url="http://www.nuforc.org/webreports/ndxl"+state+".html"
    dat_url = "ufo_" + "tx" + "_data.html"
    # http://www.crummy.com/software/BeautifulSoup/bs4/doc/#installing-a-parser
    #soup = BeautifulSoup(open(dat_url), "html.parser")     
    r = requests.get('http://www.nuforc.org/webreports/ndxl' + state + '.html')    
    soup = BeautifulSoup(r.text, "html.parser")
    table = soup.find("table", cellspacing=1)
    
    # Initialize the dictionary
    d = {'date_time': [],
         'city': [],
         'state': [],
         'shape': [],
         'duration': [],
         'summary': [],
         'posted': []}      
    
    # Read data row by row
    for i, row in enumerate(table.findAll('tr')[1:]):
        col = row.findAll('td')
        #print i
        d['date_time'].append(col[0].string)
        d['city'].append(col[1].string)
        d['state'].append(col[2].string)
        d['shape'].append(col[3].string)
        d['duration'].append(col[4].string)
        d['summary'].append(col[5].string)
        d['posted'].append(col[6].string)
    
    # Append to master dataframe                        
    df = df.append(pd.DataFrame(d))
    
    # Print message
    print state + " is complete"

# Validate number of records per state
df.state.value_counts()

# Convert all states to upper case 
df['state'] = df['state'].str.upper()

# Write to csv
df.to_csv('ufo_data.csv', index=False)
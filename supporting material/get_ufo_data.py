'''
Get Data from the National UFO Reporting Center

Author: Josiah Davis
Date:   February, 2015
'''

# For dataframes
import pandas as pd

# For collecting content from the web
import requests

# For isolating divs from an html file
from bs4 import BeautifulSoup

# Create list of states to loop through
states =['AL','AK','AZ', 'AR','CA','CO','CT','DE','FL','GA','HI','ID','IL',
         'IN','IA','KS','KY','LA','ME','MD','MA','MI','MN','MS','MO','MT',
         'NE','NV','NH','NJ','NM','NY','NC','ND','OH','OK','OR','PA','RI',
         'SC','SD','TN','TX','UT','VT','VA','WA','WV','WI','WY']
         
# Initialize dataframe to store results in
df = pd.DataFrame()

# Loop through each state
for state in states:

    '''
    To practice, recommend downloading a couple of web-pages first.
    Reference: http://lethain.com/an-introduction-to-compassionate-screenscraping/
    Example:
    soup = BeautifulSoup(open("ufo_data" + state + ".html"), "html.parser")
    '''
    
    # Get HTML from URL
    # http://www.crummy.com/software/BeautifulSoup/bs4/doc/#installing-a-parser
    r = requests.get('http://www.nuforc.org/webreports/ndxl' + state + '.html')    

    # Create a soup object
    soup = BeautifulSoup(r.text, "html.parser")
    
    # Find the table div
    table = soup.find("table", cellspacing=1)
    
    # Create an empty dictionary data-structure
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

# Convert all states to upper case 
df['state'] = df['state'].str.upper()

# Print out number of records per state
df.state.value_counts()

# Write to csv
df.to_csv('ufo_data.csv', index=False)
import pandas as pd
import json
import urllib.request as request

directory = 'some/directory'

# Download JSON file
# https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/vaccinations/vaccinations.json
with request.urlopen('https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/vaccinations/vaccinations.json') as response:
        if response.getcode() == 200:
            source = response.read()
            raw_data = pd.read_json(source, orient='records')
        else:
            print('An error occurred while attempting to retrieve data from the API.')

# Select only data of the last register of Spain
raw_data_spain = raw_data[(raw_data['country'] == 'Spain')]
raw_data_spain = raw_data_spain.reset_index(drop=True)
data_spain = raw_data_spain["data"].to_json()
data_spain_clean = pd.read_json(data_spain)
data_spain_last = data_spain_clean.tail(1)

# Save this data on JSON file
data_spain_last.to_json(directory, orient='records')

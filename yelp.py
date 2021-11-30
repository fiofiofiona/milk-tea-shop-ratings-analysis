import requests
import json
from yelpapi import YelpAPI
import csv
import pandas as pd

API_KEY = "3DeROj3ciBmId8IPCm5sivjBsoSGwwC0AtKzi4zkEYgdVIzApMwgPaiixoylJmEXwtr7tCC7FOFMOXb5fByNOt8WStir575lx__1ejKSy3LwPh6r2HcuwltxE62lYXYx"

yelp_api = YelpAPI(API_KEY)
url = 'https://api.yelp.com/v3/businesses/search'
headers = {'Authorization': 'Bearer %s' % API_KEY}

population_df = pd.read_csv('Chicago_Population_Counts.csv')
population_df = population_df[(population_df['Year'] == 2019) & (population_df['Geography Type'] == 'Zip Code')]
zip_codes = population_df['Geography'].astype(int).to_list()

data = []
data_file = open('yelp_data_file.csv', 'w')
csv_writer = csv.writer(data_file)
count = 0

for zipcode in zip_codes:
    location = 'chicago, il ' + str(zipcode)
    for offset in range(0, 1000, 20):
        params = {
            'limit': 20, 
            'categories': 'bubbletea',
            'location': location.replace(' ', '+'),
            'offset': offset
        }

        response = requests.get(url, headers=headers, params=params)
        if response.status_code == 200:
            data = response.json()['businesses']
            for business in data:
                if count == 0:
                # headers
                    header = business.keys()
                    csv_writer.writerow(header)
                    count += 1
                # data
                csv_writer.writerow(business.values())

        elif response.status_code == 400:
            print('400 Bad Request')
            break

data_file.close()
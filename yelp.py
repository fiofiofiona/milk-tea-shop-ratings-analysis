import requests
import json
from yelpapi import YelpAPI
import csv

API_KEY = "0PhzbmD6rrFbjzvULfvk8rjVv1TIy9v6WrSEn5K5xub26KPCyIXUJFnE4vhXHgPahyeTwdndBX5lWXtibRdTXRpgRd7z2Xih4q0tDheuAbA9O6F1Z3wQrouyjxCIYXYx"

yelp_api = YelpAPI(API_KEY)
url = 'https://api.yelp.com/v3/businesses/search'
headers = {'Authorization': 'Bearer %s' % API_KEY}
total = 0

data = []
for offset in range(0, 1000, 20):
    params = {
        'limit': 20, 
        'location': 'chicago, il'.replace(' ', '+'),
        'term': 'bubble tea'.replace(' ', '+'),
        'offset': offset
    }

    response = requests.get(url, headers=headers, params=params)
    if response.status_code == 200:
        data += response.json()['businesses']
        total = response.json()['total']
    elif response.status_code == 400:
        print('400 Bad Request')
        break


#search_results = yelp_api.search_query(term='bubble tea', location='chicago, il', limit = 50, offset=190)
#print(search_results)

#total = int(search_results["total"])
#business_data = search_results["businesses"]
#print(business_data)

print(data)
data_file = open('yelp_data_file.csv', 'w')
csv_writer = csv.writer(data_file)
count = 0
for business in data:
    if count == 0:
        # headers
        header = business.keys()
        csv_writer.writerow(header)
        count += 1
 
    # data
    csv_writer.writerow(business.values())
 
data_file.close()
print(total)

"""
Google Places API only returns 60 results. 
For more results, it seems to require an upgraded account that charges, so I would focus on data from Yelp.
"""

from os import error
import requests
import json
import time
import csv

API_KEY = "AIzaSyAN_iNp_YoVwLfJ6ncT6fuJiC9CTsS8YNA"
url = "https://maps.googleapis.com/maps/api/place/textsearch/json?query=bubble%20tea%20store%20Chicago&key=AIzaSyAN_iNp_YoVwLfJ6ncT6fuJiC9CTsS8YNA"
#url = 'https://maps.googleapis.com/maps/api/place/findplacefromtext/json?input=Bubble%20milk%20tea%20in%20Chicago&inputtype=textquery&fields=formatted_address%2Cname%2Cbusiness_status%2Crating%2Cuser_ratings_total%2Cprice_level%2Copening_hours&key=AIzaSyAN_iNp_YoVwLfJ6ncT6fuJiC9CTsS8YNA'

payload={}
headers = {}
data = []
response = requests.request("GET", url, headers=headers, data=payload)
#print(response.json())
data += response.json()['results']
page_token = ""
try :
    page_token = response.json()['next_page_token']
    print(page_token)
    while page_token:
        url = 'https://maps.googleapis.com/maps/api/place/textsearch/json?pagetoken=' + page_token + '&key=' + API_KEY
        time.sleep(2)
        response = requests.request("GET", url, headers=headers, data=payload)
        print(response)

        if response.status_code == 200:
            data += response.json()['results']
            print(response.json()['next_page_token'])
            page_token = response.json()['next_page_token']
        elif response.status_code == 400:
            print('400 Bad Request')
            break
except KeyError:
    print("Error")

finally:
    with open('google_map_data.json', 'w') as f:
        json.dump(response.json(), f, ensure_ascii=False)

    #search_results = yelp_api.search_query(term='bubble tea', location='chicago, il', limit = 50, offset=190)
    #print(search_results)

    #total = int(search_results["total"])
    #business_data = search_results["businesses"]
    #print(business_data)


    data_file = open('google_map_data_file.csv', 'w')
    csv_writer = csv.writer(data_file)
    count = 0
    for result in data:
        if count == 0:
            # headers
            header = result.keys()
            csv_writer.writerow(header)
            count += 1
    
        # data
        csv_writer.writerow(result.values())
    
    data_file.close()

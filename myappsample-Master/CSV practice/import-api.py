import requests
import csv

api_url = 'https://catfact.ninja/fact'
response = requests.get(api_url)  #this get the Json send by the Api

# check if the Api send us the data
if response.status_code == 200:
    api_data = response.json() # convert the data

    # save data in a CSV file
    with open('api_data.csv','w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)

else:
    print(f'API request fail - code: {response.status_code}')
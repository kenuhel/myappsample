

import requests
import csv

# Step 3: Make an API request
api_url = 'https://catfact.ninja/fact'  
response = requests.get(api_url)

# check if the API returns something
if response.status_code == 200:
    # convert
    api_data = response.json()

    with open('api_data.csv', 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
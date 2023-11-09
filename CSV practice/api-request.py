
import csv
import requests

url = "https://api.publicapis.org/entries"

headers = {
    'Accept': 'application/json', # specify the expected type of data for the response
    'Content-Type': 'application/json' # commonly used on post request - not necessary used in this example
}

# -- ('Type of request', api-URL, 'headers defined above for this request', used to send data on your request [not used in this example - empty dict.])
response = requests.request("GET",url,headers=headers,data={})
myjson = response.json() # convert

ourData = [] # empty list/array

csvHeader = ['Name','Descrip.','Link','Categ.'] # headers to print in the csv file

for x in myjson['entries']: # *entries to read  the index
    listing = [x['API'], x['Description'], x['Link'], x['Category']] # filter the data on "x"
    ourData.append(listing) # added to the list/array

with open('our_data.csv','w',encoding='UTF8', newline='') as public:
    writer = csv.writer(public)

    writer.writerow(csvHeader) # write titles
    writer.writerows(ourData) # write content


print('done') # indicate us the file is ready

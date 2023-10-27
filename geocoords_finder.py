from geopy.geocoders import GoogleV3
import google_maps_api_creds
import csv
import time

geolocator = GoogleV3(api_key=google_maps_api_creds.key)

school_geocoords = {}

with open('schoolnames.csv', newline='') as csvfile:
    csvreader = csv.reader(csvfile)
    for school_row in csvreader:
        if school_row[0] != "Name":
            school_geocoords[school_row[0]] = [0, 0]

count = 0
for school in school_geocoords:
    address = geolocator.geocode(f"{school} school Pennsylvania")
    if address:
        if address.latitude and address.longitude:
            school_geocoords[school] = [address.latitude, address.longitude]
    count += 1
    if count % 100 == 0:
        print(f"{count} completed")
    time.sleep(0.25)

with open('school_geocoords.csv', 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    for school in school_geocoords:
        csvwriter.writerow([school, school_geocoords[school][0], school_geocoords[school][1]])

print("DONE")

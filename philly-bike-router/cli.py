import json
import requests


API_ENDPOINT = "https://api.phila.gov/bike-share-stations/v1/"

def main():
    r = requests.get(API_ENDPOINT, headers={'User-Agent': 'curl/7.37.1'})
    data = json.loads(r.content)

    for station in data['features']:
        spaces = station['properties']['docksAvailable']
        name = station['properties']['name'].strip()
        if spaces == 0:
            print("%s is full" % name)
        elif spaces < 3:
            print("%s is nearly full - %d spaces left" % (name, spaces))

if __name__ == "__main__":
    main()

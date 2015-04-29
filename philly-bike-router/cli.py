import json
import requests


API_ENDPOINT = "https://api.phila.gov/bike-share-stations/v1/"

def main():
    r = requests.get(API_ENDPOINT, headers={'User-Agent': 'curl/7.37.1'})
    data = json.loads(r.content)

    for station in data['features']:
        if (station['properties']['docksAvailable'] < 3 and
           station['properties']['docksAvailable'] > 0):
            print("%s is nearly full - %d spaces left" %
                  (station['properties']['name'].strip(),
                   station['properties']['docksAvailable']))

if __name__ == "__main__":
    main()

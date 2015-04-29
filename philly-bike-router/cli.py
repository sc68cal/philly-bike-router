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
            plural = "space" if spaces == 1 else "spaces"
            print("%s is nearly full - %d %s left" % (name, spaces, plural))
        if not station['properties']['bikesAvailable']:
            print("%s has no bikes" % name)

if __name__ == "__main__":
    main()

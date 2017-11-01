#!/usr/bin/env python3
import httplib2
import json

def getGeocodeLocation(inputString):
    # Use Google Maps to convert a location into Latitute/Longitute coordinates
    # FORMAT: https://maps.googleapis.com/maps/api/geocode/json?address=1600+Amphitheatre+Parkway,+Mountain+View,+CA&key=API_KEY
    google_api_key = "google_map_api_key_here"
    locationString = inputString.replace(" ", "+")
    url = ('https://maps.googleapis.com/maps/api/geocode/json?address=%s&key=%s'% (locationString, google_api_key))
    h = httplib2.Http()
    #add decode method to avoid JSON type error
    result = json.loads(h.request(url,'GET')[1].decode('utf-8'))
    latitude = result['results'][0]['geometry']['location']['lat']
    longitude = result['results'][0]['geometry']['location']['lng']
    #return (latitude,longitude)
    print(latitude, longitude)
    return

if __name__ == '__main__':
	getGeocodeLocation("beijing")
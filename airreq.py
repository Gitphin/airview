import requests
import time

# TODO: Change this to be current location, add customizations
# to the request s.t you can change radius of search
lat = 44.8851
lon = -93.2144
dist = 10

url = f"https://api.adsb.lol/v2/closest/{lat}/{lon}/{dist}"
session = requests.Session()

# TODO: Maybe set up signals instead of hard-exiting program after
while True:
    try:
        response = session.get(url, timeout=5)
        if response.status_code == 200:
            data = response.json()
            aircraft_list = data.get("ac", [])
            if not aircraft_list:
                print("No aircraft found.")
            else:
                for aircraft in aircraft_list:
                    flight = aircraft.get("flight", "").strip()
                    alt = aircraft.get("alt_baro", 0)
                    speed = aircraft.get("gs", 0)
                    model = aircraft.get("type", "Unknown")
                    desc = aircraft.get("t", "Unknown")
                    reg = aircraft.get("r", "N/A")
                    lat = aircraft.get("lat", 0)
                    lon = aircraft.get("lon", 0)
                    # TODO: Given the flight number, run it through FlightStats and scrape
                    # for information on route such as airport, dest, airline, delays, gate etc.
                    print(f"Flight: {flight} | Reg: {reg}")
                    print(f"Model: {desc} ({model}) | Altitude: {alt} ft | Speed: {speed} kt")
                    print(f"Location: {lat}, {lon}\n")
        else:
            print(f"Error: ", response.status_code)
    except Exception as e:
        print("Error: ", e)

    time.sleep(5)



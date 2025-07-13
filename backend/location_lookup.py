import requests

"""
Looks up flight info using adsb.lol API, returns None
on failure or flight information on success
"""
def look_from_location(url):
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        data = response.json()
        aircrafts = data.get("ac", [])
        if not aircrafts:
            return
        aircraft = aircrafts[0]
        flight_num = aircraft.get("flight", "").strip()
        alt = aircraft.get("alt_baro", 0)
        speed = aircraft.get("gs", 0)
        reg = aircraft.get("r", "N/A")
        lat = aircraft.get("lat", 0)
        long = aircraft.get("long", 0)
        return flight_num, alt, speed, reg, lat, long

    except (requests.RequestException, ValueError, TypeError, KeyError):
        return None




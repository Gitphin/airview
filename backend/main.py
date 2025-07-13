import location_lookup


lat = 44.8851
lon = -93.2144
dist = 10

url = f"https://api.adsb.lol/v2/closest/{lat}/{lon}/{dist}"
result = location_lookup.look_from_location(url)
cur_flight_num = ""

if result:
    flight_num, alt, speed, reg, lat, long = result

    if flight_num != cur_flight_num:
        cur_flight_num = flight_num
        print(cur_flight_num)
        # Do our scraping function for each time we get a new flight num.
        # or just every minute or so if I want to.
        # Also we can store our cur_flight_num in some cache db later on for multiple
        # users. We could maybe use JWT for this part or something else or a hash of the user's login credentials?




 

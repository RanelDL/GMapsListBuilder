from loadLocations import Automaps
f = open("addresses_wrk_cpy.txt", 'rt')
GMAPS_URL ="https://www.google.com/maps/@32.0851663,34.8955189,15z?authuser=0&entry=ttu" 
auto = Automaps(GMAPS_URL)
auto.enter_address(f.readline())
f.close()


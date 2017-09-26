from __future__ import print_function

import sys
import json
try:
    import urllib2 as urllib
except ImportError:
    import urllib.request as urllib

if not len(sys.argv) == 3:
    print('Invalid number of arguments!\n' \
    + 'To run script: ' \
    + 'python show_bus_locations_uc288.py <MTA_KEY> <BUS_LINE>')
    sys.exit()

key = sys.argv[1]
bus_line = sys.argv[2]

mta_url = 'http://bustime.mta.info/api/siri/vehicle-monitoring.json?key=' \
          + key + '&VehicleMonitoringDetailLevel=calls&LineRef=' + bus_line

print('Bus Line : ' + bus_line)

try:
   response = urllib.urlopen(mta_url)
   data = response.read().decode('utf-8')
   data = json.loads(data)
except urllib.HTTPError:
    print('Invalid URL!!!')
    sys.exit()

try:
    bus_list = data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'] \
              [0]['VehicleActivity']
    bus_count = len(bus_list)
except KeyError:
    print('No bus activity found for bus line ' + bus_line)
    sys.exit()

print('Number of Active Buses : ' + str(bus_count))

for i in range(bus_count):
    bus_loc = bus_list[i]['MonitoredVehicleJourney']['VehicleLocation']
    print('Bus ' + str(i) + ' is at latitude ' + str(bus_loc['Latitude']) \
        + ' and longitude' + str(bus_loc['Longitude']))




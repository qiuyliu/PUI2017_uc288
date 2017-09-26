from __future__ import print_function

import sys
import json
try:
    import urllib2 as urllib
except ImportError:
    import urllib.request as urllib

if not len(sys.argv) == 4:
    print('Invalid number of arguments!\n' \
    + 'To run script: ' \
    + 'python get_bus_info_uc288.py <MTA_KEY> <BUS_LINE> <OUTPUT_FILENAME>.csv')
    sys.exit()

key = sys.argv[1]
bus_line = sys.argv[2]
output_file = sys.argv[3]

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

fout = open(output_file, 'w')

fout.write('Latitude,Longitude,Stop Name,Stop Status\n')

for i in range(bus_count):
    bus_loc = bus_list[i]['MonitoredVehicleJourney']['VehicleLocation']
    print('Bus ' + str(i) + ' is at latitude ' + str(bus_loc['Latitude']) \
        + ' and longitude' + str(bus_loc['Longitude']))

    try:
        next_stops = bus_list[i]['MonitoredVehicleJourney'] \
                    ['OnwardCalls']['OnwardCall']
    except KeyError:
        next_stops = []

    if len(next_stops) < 1:
        stop_name = 'N/A'
        stop_status = 'N/A'
    else:
        stop_name = next_stops[0]['StopPointName']
        stop_status = next_stops[0]['Extensions']['Distances']['PresentableDistance']

    fout.write(str(bus_loc['Latitude']) + ',' + str(bus_loc['Longitude']) + ',' \
               + stop_name + ',' + stop_status + '\n')

fout.write('\n')







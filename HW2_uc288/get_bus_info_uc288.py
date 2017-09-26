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

fout = open(output_file, 'w')

mta_url = 'http://bustime.mta.info/api/siri/vehicle-monitoring.json?key=' \
          + key + '&VehicleMonitoringDetailLevel=calls&LineRef=' + bus_line

print('Bus Line : ' + bus_line)

response = urllib.urlopen(mta_url)
data = response.read().decode('utf-8')
data = json.loads(data)

buslist = data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'] \
	      [0]['VehicleActivity']
bus_count = len(buslist)

print('Number of Active Buses : ' + str(bus_count))

fout.write('Latitude,Longitude,Stop Name,Stop Status\n')

for i in range(bus_count):
    busloc = buslist[i]['MonitoredVehicleJourney']['VehicleLocation']
    print('Bus ' + str(i) + ' is at latitude ' + str(busloc['Latitude']) \
        + ' and longitude' + str(busloc['Longitude']))

    try:
        next_stops = buslist[i]['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall']
    except KeyError:
        next_stops = []

    if len(next_stops) < 1:
        stop_name = 'N/A'
        stop_status = 'N/A'
    else:
        stop_name = next_stops[0]['StopPointName']
        stop_status = next_stops[0]['Extensions']['Distances']['PresentableDistance']

    fout.write(str(busloc['Latitude']) + ',' + str(busloc['Longitude']) + ',' \
               + stop_name + ',' + stop_status + '\n')

fout.write('\n')







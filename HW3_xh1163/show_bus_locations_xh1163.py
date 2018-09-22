#show_bus_locations_xh1163.py

import os
import json
import sys
try: 
	import urllib2 as urllib
except ImportError:
	import urllib.request as urllbib

if not len(sys.argv)==3:
	print """ Invalid Input. \n
	Please enter your API Key and Bus line after the file name as follow :\n
	show_bus_locations.py API_KEY BUS_LINE """


own_key=sys.argv[1]
BUS_LINE=sys.argv[2]

url = "http://api.prod.obanyc.com/api/siri/vehicle-monitoring.json?key=" + own_key
response = urllib.urlopen(url)
data = response.read().decode("utf-8")
data = json.loads(data)


# put the but positions into a list and print the output
positions=[]
for l in data[u'Siri'][u'ServiceDelivery'][ u'VehicleMonitoringDelivery'][0]['VehicleActivity']:
    if l['MonitoredVehicleJourney']['PublishedLineName']==BUS_LINE:
        p=l[u'MonitoredVehicleJourney'][u'VehicleLocation']
        if p not in positions:
            positions.append(p)
            
output='''Bus Line: %s 
Number of Active Buses : %d '''% (BUS_LINE, len(positions))
for bus in range(len(positions)):
    output+= '\n'+'Bus %d is at latitude %f and longtitude %f' %(bus,positions[bus]['Latitude'],positions[bus]['Longitude'])

print(output)

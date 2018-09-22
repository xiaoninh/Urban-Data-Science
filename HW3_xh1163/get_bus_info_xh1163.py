#get_bus_info_xh1163.py

import os
import json
import sys
try: 
    import urllib2 as urllib
except ImportError:
    import urllib.request as urllbib


own_key=sys.argv[1]
url = "http://api.prod.obanyc.com/api/siri/vehicle-monitoring.json?key=" + own_key
response = urllib.urlopen(url)
data = response.read().decode("utf-8")
data = json.loads(data)


# for each line, put the buses information in to a list, and create and write csv files for the line
for bus_line in sys.argv[2:]:
    buses=[]
    for l in data[u'Siri'][u'ServiceDelivery'][ u'VehicleMonitoringDelivery'][0]['VehicleActivity']:
	this_bus=""
        if l['MonitoredVehicleJourney']['PublishedLineName']==str(bus_line):
            latitude=str(l[u'MonitoredVehicleJourney'][u'VehicleLocation']['Latitude'])
            longitude=str(l[u'MonitoredVehicleJourney'][u'VehicleLocation']['Longitude'])
            if 'MonitoredCall'not in l[u'MonitoredVehicleJourney'].keys():
                stop_name="N/A"
                status="N/A"
                this_bus= latitude+","+longitude+","+stop_name+","+status
            else:
                stop_name=l[u'MonitoredVehicleJourney']['MonitoredCall']['StopPointName']
                status= l[u'MonitoredVehicleJourney']['MonitoredCall']['Extensions']['Distances']['PresentableDistance']
                this_bus= latitude+","+longitude+","+stop_name+","+status             
            buses.append(this_bus)
            
    file_name=bus_line+".csv"
    f = open(file_name, "w")
    f.write('Latitude,Longitude,Stop Name,Stop Status')
    for bus in buses:
        f.write("\n"+bus)

#%matplotlib tk
import urllib.request
import json
import matplotlib.pyplot as plt
from matplotlib import animation
import cartopy.crs as ccrs
from cartopy.io.img_tiles import OSM

#SET AXES
fig, ax = plt.subplots()
ax=plt.axes(projection=ccrs.PlateCarree())
ax.set_ylim(40.6051,40.6825)
ax.set_xlim(-73.8288,-73.7258)

#ADD OSM BASEMAP
osm_tiles=OSM()
ax.add_image(osm_tiles,13) #Zoom Level 13

#PLOT JFK INTL AIRPORT
ax.text(-73.778889,40.639722,'JFK Intl',horizontalalignment='right',size='large')
ax.plot([-73.778889],[40.639722],'bo')

#PLOT TRACK
track, = ax.plot([], [],'ro')

opener = urllib.request.build_opener()
opener.addheaders = [('User-agent', 'Mozilla/5.0')]

#UPDATE FUNCTION
def update(self):
    # Find possible query items:
    # http://www.virtualradarserver.co.uk/Documentation/Formats/AircraftList.aspx
    #SEND QUERY
    fp=opener.open('http://public-api.adsbexchange.com/VirtualRadar/AircraftList.json?lat=40.639722&lng=-73.778889&fDstL=0&fDstU=20')
    mybyte=fp.read()
    mystr=mybyte.decode("utf8")
    js_str=json.loads(mystr)
    fp.close()
    lat_list=[]
    long_list=[]
    #
    # Find flight description details:
    # https://www.adsbexchange.com/datafields/ 
    for num,flight_data in enumerate(js_str['acList']):
        lat=flight_data['Lat']
        lon=flight_data['Long']
        lat_list.append(lat)
        long_list.append(lon)
    track.set_data(long_list,lat_list)
    return track,
                         
#UPDATING EVERY SECOND
anim = animation.FuncAnimation(fig, update,interval=1000, blit=False)

plt.show()
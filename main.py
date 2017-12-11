import config, urllib.request, urllib.error, urllib.parse, json, webbrowser,os
import APIRequests
#Get data for each of the tabs:

#MapUrl with traffic?
import geocoder
g = geocoder.ip('me')
print(g.latlng)
print(g.lat)
print(g.lng)
userinput = APIRequests.UserCall(lat=float(g.lat), lon=float(g.lng))
googleMapUrl = "https://www.google.com/maps/embed/v1/view?key=%s&center=%s,%s&zoom=12"%(config.googleMapKey,g.lat,g.lng)
#Weather
UGWeather = APIRequests.wRefine(userinput.weather)

#Incidents
bing = APIRequests.dataPrint(APIRequests.bRefine(userinput.bing))
mapquest = APIRequests.mRefine(userinput.mapquest)
import jinja2

JINJA_ENVIRONMENT = jinja2.Environment(loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
                                       extensions=['jinja2.ext.autoescape'],
                                       autoescape=True)

tvals = {'location':g.city,'lat': g.lat,'lng':g.lng,'mapURL': googleMapUrl, 'bing' : bing, 'mapquest' : mapquest, 'weather' : UGWeather}
for a in tvals:
    print(tvals[a])
f = open("output.html", 'w')
template = JINJA_ENVIRONMENT.get_template('index.html')
f.write(template.render(tvals))
f.close()






# print(testusercall)

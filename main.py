import config, urllib.request, urllib.error, urllib.parse, json, webbrowser,os

#Get data for each of the tabs:

#MapUrl with traffic?
import geocoder
g = geocoder.ip('me')
print(g.latlng)
print(g.lat)
print(g.lng)

googleMapUrl = "https://www.google.com/maps/search/?api=1&query=%s,%s"%(g.lat,g.lng)
print(googleMapUrl)
#Weather

#Incidents


import jinja2

JINJA_ENVIRONMENT = jinja2.Environment(loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
                                       extensions=['jinja2.ext.autoescape'],
                                       autoescape=True)

tvals = {'mapURL': ''}

f = open("output.html", 'w')
template = JINJA_ENVIRONMENT.get_template('index.html')
f.write(template.render(tvals))
f.close()






# print(testusercall)

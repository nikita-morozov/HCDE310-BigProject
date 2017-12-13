import config, os, APIRequests, jinja2, webapp2

def mqLocs(info):
    if len(info) > 1:
        locs = [info[incident]['coordinates'] for incident in info]
    else:
        return None
    return locs

def bingLocs(info):
    if info == "This location has no traffic incidents or data.":
        return None
    else:
        locs = [incident['startCoordinates'] for incident in info]
    return locs

#MapUrl with traffic?
#print(g.latlng)


JINJA_ENVIRONMENT = jinja2.Environment(loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
                                       extensions=['jinja2.ext.autoescape'],
                                       autoescape=True)


# f = open("output.html", 'r+')
# f.write(template.render(tvals))
# f.close()
# print(mapquest)
# #print(bingLocs(bing))
# print(mqLocs(mapquest))


class MainHandler(webapp2.RequestHandler):
    def get(self):
        userinput = APIRequests.UserCall(lat=float(47.657), lon=float(-122.338))
        googleMapUrl = "https://www.google.com/maps/embed/v1/view?key=%s&center=%s,%s&zoom=12" % (
        config.googleMapKey, str(47.657), str(-122.338))
        UGWeather = APIRequests.wRefine(userinput.weather)

        # Incidents
        bing = APIRequests.dataPrint(APIRequests.bRefine(userinput.bing))
        mapquest = APIRequests.mRefine(userinput.mapquest)
        tvals = {'incidents': mqLocs(mapquest), 'location': 'Seattle', 'lat': 47.657, 'lng': -122.338,
                 'mapKey': config.googleMapKey, 'bing': bing, 'mapquest': mapquest, 'weather': UGWeather}
        template = JINJA_ENVIRONMENT.get_template('indexClean.html')
        self.response.write(template.render(tvals))


application = webapp2.WSGIApplication([('/.*', MainHandler)], debug=True)
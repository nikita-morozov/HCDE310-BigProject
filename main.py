import config, urllib.request, urllib.error, urllib.parse, json, webbrowser,os


def pretty(obj):
    return json.dumps(obj, sort_keys=True, indent=2)


def safeGet(url):
    try:
        return urllib.request.urlopen(url)
    except urllib.error.HTTPError as e:
        print("The server couldn't fulfill the request.")
        print("Error code: ", e.code)
    except urllib.error.URLError as e:
        print("We failed to reach a server")
        print("Reason: ", e.reason)
    return None


# method for making a request to mapquest
# http://www.mapquestapi.com/traffic/v2/incidents?key=KEY&boundingBox=39.95,-105.25,39.52,-104.71&filters=construction,incidents
def mapquest(baseurl = 'https://www.mapquestapi.com/traffic/v2/incidents',
    key=config.mapquestKey,
    lat=47.657265,
    lon=-122.307208,
    params={}
    ):
    # boundingBox = 39.95, -105.25, 39.52, -104.71
    params['boundingBox'] = str(lat+.05) + ',' + str(lon+.05) + ',' + str(lat-.05) + ',' + str(lon-.05)
    params['key'] = key
    url = baseurl + "?" + urllib.parse.urlencode(params)
    info = json.loads(safeGet(url).read())
    return info


# testmq = json.loads(mapquest().read())
# print(pretty(testmq))


# method for making a request to bing
# http://dev.virtualearth.net/REST/v1/Traffic/Incidents/mapArea/includeLocationCodes?severity=severity1,severity2,severityn&type=type1,type2,typen&key=BingMapsKey
def bing(baseurl = 'https://dev.virtualearth.net/REST/v1/Traffic/Incidents/',
    lat=47.657265,
    lon=-122.307208,
    params = {}
    ):

    mapArea = str(lat-.05) + ',' + str(lon-.05) + ',' + str(lat+.05) + ',' + str(lon+.05)
    params['t'] = '1,2,3,4,5,6,7,8,9,10,11'
    params['key'] = config.bingKey
    url = baseurl + mapArea + "?" + urllib.parse.urlencode(params)
    info = json.loads(safeGet(url).read())
    return info


# testbing = json.loads(bing().read())
# print(pretty(testbing))
#
# for report in testbing['resourceSets'][0]['resources']:
#     print(str(report['point']['coordinates'][0]) + ', ' + str(report['point']['coordinates'][1]))


# method for making a request to wsdot
def wsdot(baseurl = '',
    params = {}
    ):
    url = baseurl + "?" + urllib.parse.urlencode(params)
    return safeGet(url)


# testwsdot = json.loads(wsdot().read())
# print(pretty(testwsdot))


# method for creating our google map
def googlemap():
    print()

# method for making a request to weather underground
# http://api.wunderground.com/api/Your_Key/conditions/q/lat,lon.json

def wunderground(baseurl = 'https://api.wunderground.com/api/',
    lat=47.657265,
    lon=-122.307208,
    method = 'conditions',
    api_key = config.weatherKey,
    format = 'json'
    ):
    url = baseurl + api_key + '/' + method + '/q/' + str(lat) + ',' + str(lon) + '.' + format
    info = json.loads(safeGet(url).read())
    return info


# testwu = json.loads(wunderground().read())
# print(pretty(testwu))

class UserCall(object):
    def __init__(self, lat=47.657265, lon=-122.307208):
        self.bing = bing(lat=lat,lon=lon)
        self.mapquest = mapquest(lat=lat, lon=lon)
        self.weather = wunderground(lat=lat, lon=lon)


    def __str__(self):
        return "test text"


if __name__ == '__main__':
    testusercall = UserCall()

    #print('--__BING__--')
    #print(pretty(testusercall.bing))
    #print('--__MAPQUEST__--')
    #print(pretty(testusercall.mapquest))
    #print('--__WEATHER__--')
    #print(pretty(testusercall.weather))
    #print(testusercall)

import jinja2

JINJA_ENVIRONMENT = jinja2.Environment(loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
                                       extensions=['jinja2.ext.autoescape'],
                                       autoescape=True)

tvals = {'photos': [sortedByViews, sortedByTags, sortedByComments]}

f = open("output.html", 'w')
template = JINJA_ENVIRONMENT.get_template('index.html')
f.write(template.render(tvals))
f.close()
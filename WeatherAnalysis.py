import googlemaps
import json
import urllib.request
import datetime as dt
import pandas as pd
from decimal import Decimal

df2=pd.DataFrame()




place=(input('Please enter place:'))
year= int(input('Enter a year YYYY:'))
month= int(input('Enter a month MM:'))
day= int(input('Enter a day DD:'))
date=dt.datetime(year,month,day)
unixtime = int((date - dt.datetime(1970, 1, 1)).total_seconds())
unixtime = str(unixtime)
print(unixtime)



gmap_key= 'Google Maps API Key goes here' 

gm= googlemaps.Client(key=gmap_key)

geo_code= gm.geocode(place)[0]
lat= (geo_code['geometry']['location']['lat'])
lng= (geo_code['geometry']['location']['lng'])
lat= Decimal(lat)
lng= Decimal(lng)
lat=str(round(lat,3))
lng=str(round(lng,3))
print(lat, lng)


darksky_key= 'DarkSKy API Key goes here'
for i in range(1,365):
   darksky_url= 'https://api.darksky.net/forecast/'+darksky_key+'/'+lat+','+lng+','+unixtime+'?exclude=currently,hourly,flags'
   response= urllib.request.urlopen(darksky_url)
   content= response.read()
   data= json.loads(content.decode('utf8'))
   df1=pd.DataFrame(data["daily"]["data"])
   pd.concat([df2,df1])

       
        
    


    
                     
    
    
    
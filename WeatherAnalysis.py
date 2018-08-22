import googlemaps
import json
import urllib.request
import datetime as dt
import pandas as pd
from decimal import Decimal

df1=pd.DataFrame()
df2=pd.DataFrame()




place='PLACE NAME EG: GOA'
year= int(ENTER YEAR HERE. EG: 2017)
month= int(ENTER MONTH HERE, EG: FOR MARCH ENTER: 03)
day= int(ENTER DAY HERE)
date=dt.datetime(year,month,day)
unixtime = int((date - dt.datetime(1970, 1, 1)).total_seconds())  #Converts to unix timestamps needed for the Darksky link.
unixtime = str(unixtime)
print(unixtime)



gmap_key= 'GOOGLE MAPS API KEY ' 

gm= googlemaps.Client(key=gmap_key)

geo_code= gm.geocode(place)[0]  #Google Maps API is used to get the latitiude and longtitiude of entered place.
lat= (geo_code['geometry']['location']['lat'])
lng= (geo_code['geometry']['location']['lng'])
lat= Decimal(lat)
lng= Decimal(lng)
lat=str(round(lat,3)) # rounding up of the values to use in the link
lng=str(round(lng,3))
print(lat, lng)


darksky_key= 'DarkSKY API KEY' #Check the Dark Sky documentations. Link in ReadME file
for i in range(1,365):  #Change the last limit according number of days (max limit is 1,000)
   darksky_url= 'https://api.darksky.net/forecast/'+darksky_key+'/'+lat+','+lng+','+unixtime+'?exclude=currently,hourly,flags'
   response= urllib.request.urlopen(darksky_url)
   content= response.read()
   data= json.loads(content.decode('utf8')) #data is in JSON format
   df1=data['daily']['data']
   df2=df2.append(df1)
   unixtime=int(unixtime)
   unixtime=unixtime+86400  #changes the date to the next day
   unixtime=str(unixtime)
  
#changes all unix timestamps to human readable format
df2.time=pd.to_datetime(df2.time, unit='s')
df2.apparentTemperatureHighTime=pd.to_datetime(df2.apparentTemperatureHighTime, unit='s')
df2.apparentTemperatureLowTime=pd.to_datetime(df2.apparentTemperatureLowTime, unit='s')
df2.apparentTemperatureMaxTime=pd.to_datetime(df2.apparentTemperatureMaxTime, unit='s')
df2.apparentTemperatureMinTime=pd.to_datetime(df2.apparentTemperatureMinTime, unit='s')
df2.sunriseTime=pd.to_datetime(df2.sunriseTime, unit='s')
df2.sunsetTime=pd.to_datetime(df2.sunsetTime, unit='s')
df2.temperatureHighTime=pd.to_datetime(df2.temperatureHighTime, unit='s')
df2.temperatureLowTime=pd.to_datetime(df2.temperatureLowTime, unit='s')
df2.temperatureMaxTime=pd.to_datetime(df2.temperatureMaxTime, unit='s')
df2.temperatureMinTime=pd.to_datetime(df2.temperatureMinTime, unit='s')
df2.temperatureLowTime=pd.to_datetime(df2.temperatureLowTime, unit='s')

df2=df2.set_index('time', inplace=True) #sets the index of the data frame as the date of the day of reading.



       
        
    


    
                     
    
    
    

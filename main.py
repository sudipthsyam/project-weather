import requests
#import os
from datetime import datetime

api_key = 'cc1087d2cae498065526072ea15c5845'
location = input("Enter the city name: ")

complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+api_key
api_link = requests.get(complete_api_link)
api_data = api_link.json()

#create variables to store and display data
temp_city = ((api_data['main']['temp']) - 273.15)
weather_desc = api_data['weather'][0]['description']
hmdt = api_data['main']['humidity']
wind_spd = api_data['wind']['speed']
date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")

print ("-------------------------------------------------------------")
print ("Weather Stats for - {}  || {}".format(location.upper(), date_time))
print ("-------------------------------------------------------------")

print ("Current temperature is: {:.2f} deg C".format(temp_city))
print ("Current weather desc  :",weather_desc)
print ("Current Humidity      :",hmdt, '%')
print ("Current wind speed    :",wind_spd ,'kmph') 

tem=str(temp_city)
whe=str(weather_desc)
hm=str(hmdt)
Wnd=str(wind_spd)
dt=str(date_time)

def main():
  report=open('report.txt','w')
  report.write("Current climate details of " + location +'\n' )
  report.write("Current temperature is:" + tem + " deg c" +'\n')
  report.write("Current Humidity      :" + hm + " %"   + '\n')
  report.write("Current weather desc  :" + whe + '\n')
  report.write("Current wind speed    :" +Wnd + " kmph" + '\n')
  report.write("Current time and date :" +dt + '\n')

  report.close()
main()

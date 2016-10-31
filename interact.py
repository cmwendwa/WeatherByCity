# -*- coding: utf-8 -*-
import requests
from key import key

def interact():
	"""Returns the weather of the supplied city """

	print "Hello there am going to connect you to a public weather API\n"



	while True:

		city = raw_input("Enter A city of your choice to get its current weather\n")
       


		r = requests.get('http://api.openweathermap.org/data/2.5/weather?q='+city+',&appid='+ key)
		if r.status_code == 200:

			rj =r.json()
			temp_k = float(rj['main']['temp'])
			temp_celcius = temp_k -273
			pressure = float(rj['main']['pressure'])
			humidity = float(rj['main']['humidity'])
			wind_speed =float(rj['wind']['speed'])
			 
			print "\t\tCURRENT WEATHER IN " + city
			print "Temperature: " + str(temp_celcius) + " °C"
			print "   Pressure: " + str(pressure) + ""
			print "   Humidity: "  + str(humidity) + ""
			print " Wind Speed: "  + str(wind_speed) + ""
			print "\n"
			while True:
				choice = int(raw_input("Enter 1 to continue or 0 to exit\n"))
				if choice ==1:
					break
				elif choice ==0:
					return None
				else:
					print "Invalid choice"
					continue
		elif r.status_code == 500:
			print "City choice not available"

if __name__ == '__main__':
	interact()

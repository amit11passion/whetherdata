from pyowm import OWM
api_id='5f4cef08501ce2e191f42f1a4c5d0c08'
owm = OWM(api_id)
observation = owm.weather_at_place('Texas,usa')
w = observation.get_weather()
a = w.get_temperature()
print("Temperatures in Kelvin:")
print(a)
print("Temperature in Celcius:")
print(a['temp']-273.15)
b = w.get_humidity()
print("Humidity in % ")
print(b)


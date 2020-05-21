import pyowm
city = input("Какой город вас интересует?: ")
owm = pyowm.OWM('d069404c21018306a372846d446e18e3', language="RU")
observation = owm.weather_at_place(city)
w = observation.get_weather()

temperature = w.get_temperature('celsius')['temp']


print("В городе " + city + " сейчас температура: " +
      str(temperature) + " по Цельсию.")
print('Погода в указаном городе: ' + w.get_detailed_status())

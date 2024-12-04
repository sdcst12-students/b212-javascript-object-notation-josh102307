#Use the Weather API builder at https://open-meteo.com/en/docs to generate an API call for a city. We are going to make use of the REQUESTS.Request method to retrieve this data and unpack it with json.loads into a variable that we can use. Retrieve the data and present it in a more organized format. You may use text output or a window using Tkinter.  Our goal is to format the result in a reasonably organized format.
import json
import requests


req = requests.get('https://api.open-meteo.com/v1/forecast?latitude=49.2497&longitude=-123.1193&hourly=temperature_2m')
data = req.text
x = json.loads(data)
for i in x:
    print(i)

latitude = x["latitude"]
longitude = x["longitude"]
time = x["timezone"]
elevation = x["elevation"]


print("\n")
print(f"Weather statistics for Vancouver today: \nLatitude:{latitude}\nLongitude:{longitude}\nTimezone:{time}\nelevation:{elevation}\n{data}")

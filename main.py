import requests, json, os

def getcode(code):
  if code == 0:
    return "Clear sky ☀️"
  elif code >= 1 and code <= 3:
    return "Mainly clear, partly cloudy, overcast 🌤️☁️"
  elif code >= 45 and code <= 48:
    return "Fog and depositing rime fog 🌫️"
  elif code >= 51 and code <= 55:
    return "Drizzle: Light, moderate, and dense intensity 🌦️"
  elif code >= 61 and code <= 65:
    return "Rain: Slight, moderate, and heavy intensity 🌧️"
  elif code >= 95 and code <= 98:
    return "Thunderstorms: With or without hail ⛈️"
    
timezone = "GMT"
latitude = os.environ['latitude']
longitude = os.environ['longitude']

result = requests.get(f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&daily=weathercode,temperature_2m_max,temperature_2m_min&timezone={timezone.upper()}")

user = result.json()
#print(json.dumps(user, indent=2))

for i in range(len(user["daily"]["weathercode"])):
  weathercode = user["daily"]["weathercode"][i]
  min = user["daily"]["temperature_2m_min"][i]
  max = user["daily"]["temperature_2m_max"][i]
  
  print(f"{getcode(weathercode)}\nHigh of: {max}\t Low of {min}")

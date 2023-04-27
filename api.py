import requests

MY_LAT = 9.081999
MY_LNG = 8.675277
# response = requests.get(url="http://api.open-notify.org/iss-now.json")
# print(response)
# response.raise_for_status()
# data = response.json()
#
#
# longitude = data["iss_position"]["longitude"]
# latitude = data["iss_position"]["latitude"]
#
# iss_position = (longitude, latitude)
# print(iss_position)

parameters = {
    "lat": MY_LAT,
    "lng": MY_LNG
}

response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()







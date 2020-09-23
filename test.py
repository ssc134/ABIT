import requests

BASE_URL = "http://0.0.0.0:12345"

response = requests.get(BASE_URL + "/upload/request/1_4")
print(response.json())
response = requests.get(BASE_URL + "/upload/request/2_3")
print(response.json())
response = requests.get(BASE_URL + "/upload/request/2_-1")
print(response.json())
response = requests.get(BASE_URL + "/upload/request/2_5")
print(response.json())

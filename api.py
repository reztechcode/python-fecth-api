import requests
import json
headers = {
    'authority': 'cuaca-gempa-rest-api.vercel.app'
}

response = requests.get('https://cuaca-gempa-rest-api.vercel.app/quake', headers=headers);
response = response.content
response = json.loads(response)

# print(response)
print("======================================== ")
print("INFORMASI GEMPA BUMI TERKINI With Python ")
print("======================================== ")
print(" ")
print(f"Gempa Berkekuatan: {response['data']['magnitude']}, Dengan Kedalaman {response['data']['kedalaman']}")
print(f"Waktu Gempa: {response['data']['tanggal']}, {response['data']['jam']}")
print(f"Lokasi Gempa: {response['data']['wilayah']}")
print(f"Potensi: {response['data']['potensi']}")
print(f"Dirasakan: {response['data']['dirasakan']}")
print(" ")
print("======================================== ")
print("Powered By: Rezweb.my.id ")

print("Beta Version")

# Credit by: reztechcode
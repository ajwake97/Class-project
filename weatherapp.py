import requests
import json

#This is the API Key
API_KEY = "10b3ff178d347bb5e10cfee10deb2b63"

#This is the base URL 
baseUrl = "https://api.openweathermap.org/data/2.5/weather?"
#THis like prompts the user for the desired zipcdoe
zipCode = input("Enter the zipcode: ")

#Sends a request to the openweathermaps.org and uses my API key and zipcode to return data
response = requests.get((f'http://api.openweathermap.org/data/2.5/weather?zip={zipCode}&appid={API_KEY}'))

#Prints the response and displays the returned data
print(response.status_code)
print(response.json())

Y = input('\n\nWould you like to rerun this program? \nType "Yes" to input another zipcode. \ntype "Quit" to end program\n')

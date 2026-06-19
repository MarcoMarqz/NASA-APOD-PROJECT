import requests

API_KEY = "M3CCsNeHMKXdjJjzrkhwfx0SEsAEOR5MCe686jvp"
url = f"https://api.nasa.gov/planetary/apod?api_key={API_KEY}"

response = requests.get(url)

print(response.status_code)
print(response.json())




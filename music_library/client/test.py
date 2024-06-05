import requests

artist_id = 1
url = f'http://localhost:8000/api/artists/{artist_id}/songs/'

response = requests.get(url)

if response.status_code == 200:
    print("Canciones del Artista:")
    print(response.json())
else:
    print(f"Error: {response.status_code}")
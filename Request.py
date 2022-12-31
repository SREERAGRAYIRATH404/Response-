import requests

# Send a GET request to the API endpoint

response = requests.get("https://www.anapioficeandfire.com/api/houses/1")

# Parse the response

data = response.json()

# Print the name, region, and coat of arms

print("Name:", data["name"])

print("Region:", data["region"])

print("Coat of Arms:", data["coatOfArms"])

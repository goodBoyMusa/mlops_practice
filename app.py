import requests

print("Getting")
response = requests.get("https://www.google.com")
print(response.status_code)

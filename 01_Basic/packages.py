import requests

#import first web page
response = requests.get("https://api.github.com")
print(response.status_code)
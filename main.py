import urllib.request
opener = urllib.request.build_opener()
response  = opener.open('https://ranobehub.org/ranobe/696/1/555')
print(response.read())
print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
import requests
response = requests.get('https://ranobehub.org/ranobe/696/1/556')
print(type(response.content))
#import urllib.request
#opener = urllib.request.build_opener()
#response  = opener.open('https://ranobehub.org/ranobe/696/1/555')
#print(response.read())
#print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
import requests
res_parse_list = []
response = requests.get('https://coinmarketcap.com/')
response_text = response.text
response_parse = response.text.split('<span>')
for parse_elem_1 in response_parse:
    if parse_elem_1.startswith('$'):
       #print(parse_elem_1)
       for parse_elem_2 in parse_elem_1.split('</span>'):
           if parse_elem_2.startswith('$') and parse_elem_2[1].isdigit():
               #print(parse_elem_2)
               res_parse_list.append(parse_elem_2)
bitock = res_parse_list[0]
print(bitock)

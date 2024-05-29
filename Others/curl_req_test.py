import requests

url = 'https://wdn.varian.com:8443/ecc/ZFI_FARR_GET_FIN_BACKLOG'
payload = '{"IT_VBELN_RANGE": [{"SIGN": "I","OPTION": "EQ","LOW": "0420000015","HIGH": ""}]}'
headers = {'content-type': 'application/json', 'Accept-Charset': 'UTF-8', 'Authorization':'Basic ZmNqMTY0OTp2YXJpYW4uRUhRMDE='}
r = requests.post(url, data=payload, headers=headers)
print(r.status_code)
print(r.content)

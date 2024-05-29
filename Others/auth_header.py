import base64

username = "fcj1649"
password = "varian.EHQ01"
auth = username + ':' + password

print('Basic ' + base64.b64encode(auth.encode('ascii')).decode('ascii'))

username = "ISU_SAP_USERMASTER"
password = "Msn$nd&1209$kl90&$5#90"
auth = username + ':' + password

print('Basic ' + base64.b64encode(auth.encode('ascii')).decode('ascii'))
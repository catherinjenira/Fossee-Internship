import requests

URL = 'http://127.0.0.1:8000/api/upload/'
TOKEN = '74da50da9fa80f6319cb6b294bd5a8d22477c3a0'

with open('../sample_sensor_data.csv', 'rb') as f:
    files = {'file': f}
    headers = {'Authorization': f'Token {TOKEN}'}
    r = requests.post(URL, files=files, headers=headers)
    print('Status:', r.status_code)
    try:
        print('Response:', r.json())
    except Exception:
        print('Response text:', r.text)

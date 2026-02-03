import requests
import os

BASE = 'http://127.0.0.1:8000/api'
USERNAME = 'test'
PASSWORD = 'testpass'

print('Logging in...')
r = requests.post(f'{BASE}/login/', data={'username': USERNAME, 'password': PASSWORD})
print('Login status:', r.status_code)
if r.status_code != 200:
    print('Login failed:', r.text)
    raise SystemExit(1)

token = r.json().get('token')
print('Token:', token)
headers = {'Authorization': f'Token {token}'}

# Upload sample CSV
csv_path = os.path.join(os.path.dirname(__file__), '..', 'sample_sensor_data.csv')
print('Uploading', csv_path)
with open(csv_path, 'rb') as f:
    files = {'file': f}
    r = requests.post(f'{BASE}/upload/', files=files, headers=headers)
    print('Upload status:', r.status_code)
    if r.status_code == 200:
        print('Upload response:', r.json())
    else:
        print('Upload failed:', r.text)

# Get history
print('Fetching history...')
data = None
r = requests.get(f'{BASE}/history/', headers=headers)
print('History status:', r.status_code)
if r.status_code == 200:
    try:
        data = r.json()
    except Exception:
        data = None
    if data:
        print('History items:', len(data))
        print('Latest dataset id:', data[0].get('id'))
    else:
        print('No history items returned')
else:
    print('History failed:', r.text)

# Download report for latest if available
if data:
    dataset_id = data[0].get('id')
    print('Requesting PDF report for id', dataset_id)
    r = requests.get(f'{BASE}/report/{dataset_id}/', headers=headers)
    print('Report status:', r.status_code)
    if r.status_code == 200:
        out = os.path.join(os.path.dirname(__file__), f'report_{dataset_id}.pdf')
        with open(out, 'wb') as fh:
            fh.write(r.content)
        print('Saved report to', out)
    else:
        print('Report failed:', r.text)
else:
    print('No datasets available yet.')

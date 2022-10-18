import requests
from datetime import datetime
import os

CFG_PATH = os.path.join('CLIENTINFO.txt')

with open(CFG_PATH, 'r') as f:
    TO = f.readline()

def send_alert():
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    payload = {
        'to': TO,
        'timestamp': current_time
    }
    response = requests.post('http://localhost:8080/alert', json=payload)
    return response.status_code
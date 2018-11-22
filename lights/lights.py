import requests
from pathlib import Path
from pyyamlconfig import load_config
from sortedcontainers import SortedList

config = load_config(f'{Path.home()}/.config/lights.yaml')
ip = config.get('ip')
port = config.get('port')
token = config.get('token')
url = f'http://{ip}:{port}/api/{token}'

response = requests.get(f'{url}/lights')
lights = response.json()
light_status = SortedList()

for light in lights:
    light = lights.get(light)
    name = light.get('name')
    brightness = light.get('state', {}).get('bri')
    on = light.get('state', {}).get('on')
    status = 'on' if on else 'off'
    actual_brightness = brightness if on else 0
    light_status.add(f'{name}: {actual_brightness}')

for status in light_status:
    print(status)

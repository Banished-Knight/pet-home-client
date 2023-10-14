import json
import network
import urequests as requests

from machine import Timer

def connect(name, passwd):
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.scan()
    wlan.connect(name, passwd)
    return wlan.isconnected()


def report_boot_record(url):
    requests.post(url)
    
def read_client_config(url):
    response = requests.get(url)
    res_body = response.text
    return json.loads(res_body)
    
wifi_name = 'HomeDyy'
wifi_passwd = '01030115'
report_boot_record_url = ''
read_client_config_url = ''
default_heartbeat_interval = 5
default_monitor_interval = 30


f = connect(wifi_name, wifi_passwd)
print('wifi connect result: %s' % f)

report_boot_record(report_boot_record_url)

res_client_config = read_client_config(read_client_config_url)
print(res_client_config)
heartbeat_interval = default_heartbeat_interval
monitor_interval = default_monitor_interval
if res_client_config['success']:
    client_config = res_client_config['data']
    heartbeat_interval = client_config['heartbeatInterval']
    monitor_interval = client_config['monitorInterval']
print(heartbeat_interval)
print(monitor_interval)

# time1 = Timer(1)
# timer1.init(period=5000)
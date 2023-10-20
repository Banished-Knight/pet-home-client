import config
import json
import requests


def report_boot_record():
    requests.post(config.report_boot_record_url)


def find_client_config():
    response = requests.get(config.find_client_config_url)
    res_body = response.text
    return json.loads(res_body)


def report_heartbeat():
    requests.post(config.report_heartbeat_url)


def report_status(temperature, relative_humidity):
    body = {'temperature': temperature, 'relativeHumidity': relative_humidity}
    requests.post(config.report_status_url, data=json.dumps(body), headers={'Content-Type': 'application/json'})

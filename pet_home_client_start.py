import config
import pet_home_server as s
import schedule
import sensor


def report_heartbeat():
    try:
        s.report_heartbeat()
        print('Report Heartbeat Success')
    except Exception:
        print('Report Heartbeat Error')


def read_sensor_and_report():
    try:
        sensor_data = sensor.read()
        if sensor_data.is_valid:
            s.report_status(sensor_data.temperature, sensor_data.humidity)
        print('Report Status Success')
    except Exception:
        print('Report Status Error')


# 上报启动记录
try:
    s.report_boot_record()
    print('Report Boot Record Success')
except Exception:
    print('Report Boot Record Error')

# 查询客户端配置
heartbeat_interval = config.default_heartbeat_interval
monitor_interval = config.default_monitor_interval
try:
    client_config_response = s.find_client_config()
    if client_config_response['success']:
        heartbeat_interval = client_config_response['data']['heartbeatInterval']
        monitor_interval = client_config_response['data']['monitorInterval']
        print('Find Client Config Success')
    else:
        print('Find Client Config Failed')
except Exception:
    print('Find Client Config Error')

# 定时上报心跳
schedule.every(heartbeat_interval).seconds.do(report_heartbeat)
# 定时上报传感器状态
schedule.every(monitor_interval).seconds.do(read_sensor_and_report)

while True:
    schedule.run_pending()

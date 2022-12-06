from influxdb import InfluxDBClient
from datetime import datetime
import psutil

host='influxdb'
port=8086
user='admin'
password='123456789'
database='db'

client = InfluxDBClient(host=host, port=port, username=user, password=password, database=database)
client.switch_database('db')
cpu= str(psutil.cpu_percent(3))
json_payload = []
data = {
    "measurement":"cpu",
    "tags":{
        "pc": "PC_X"
    },
    "time": datetime.now(),
    "fields":{
        "cpu_percent": cpu
    }
}
json_payload.append(data)
print(json_payload)
client.write_points(json_payload)
print(client.query('select * from cpu;'))
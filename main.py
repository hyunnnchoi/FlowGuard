from mqtt.client import initialize_mqtt_client
from config.settings import BROKER_ADDRESS

# MQTT 클라이언트 초기화 및 연결
client = initialize_mqtt_client()
client.connect(BROKER_ADDRESS)
client.loop_start()

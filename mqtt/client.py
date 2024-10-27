import paho.mqtt.client as mqtt
from mqtt.handlers import on_message

def initialize_mqtt_client():
    client = mqtt.Client("server_listener")
    client.on_message = on_message
    client.subscribe("devices/+/measurements")
    client.subscribe("devices/+/status")
    client.subscribe("devices/+/logs")
    return client

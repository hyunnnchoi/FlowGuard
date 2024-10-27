import json
from models.measurement import save_measurement, update_device_status, save_log

def on_message(client, userdata, message):
    topic = message.topic
    payload = json.loads(message.payload.decode("utf-8"))

    if "measurements" in topic:
        save_measurement(payload)
    elif "status" in topic:
        update_device_status(payload)
    elif "logs" in topic:
        save_log(payload)

# Flowguard

### 📋 Overview
This project is an IoT-based storm drain blockage detection system that uses ESP32 devices with infrared sensors to monitor storm drains for blockages due to debris or foreign materials. The system operates in real-time, with each IoT device transmitting data to a central server three times a day via MQTT and NB-IoT. The server collects, processes, and stores this data in a PostgreSQL database, making it available for visualization and monitoring.

### 🚀 Features
- Real-time blockage detection using infrared sensors.
- Scalable architecture to support up to 550,000 devices.
- MQTT-based data transmission for efficient, low-power communication.
- PostgreSQL database storage for structured data handling.
- Integration-ready for visualization tools like Grafana.

---

### 📂 Project Structure
```plaintext
FlowGuard/
│
├── main.py                 # Application entry point
├── config/                 
│   └── settings.py         # Configuration for MQTT and DB
├── db/                     
│   ├── __init__.py
│   └── database.py         # Database connection and setup
├── mqtt/
│   ├── __init__.py
│   ├── client.py           # MQTT client and subscription setup
│   └── handlers.py         # MQTT message handlers
└── models/
    ├── __init__.py
    └── measurement.py      # Database interaction logic

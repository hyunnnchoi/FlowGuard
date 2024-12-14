from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
import sqlite3
import uvicorn
from datetime import datetime

# FastAPI 앱 생성
app = FastAPI()

# SQLite3 DB 연결 함수
def get_db_connection():
    conn = sqlite3.connect("flowguard.sqlite")
    conn.row_factory = sqlite3.Row
    return conn

# 새로운 IoT 기기 등록용 데이터 모델
class Device(BaseModel):
    latitude: float = Field(..., description="Device's latitude")
    longitude: float = Field(..., description="Device's longitude")
    address: str = Field(default=None, description="Optional device address")

# IoT 센서 데이터 모델
class IoTData(BaseModel):
    device_id: int
    ir_sensor: float
    trash_detection: bool
    battery_percent: float

# 새로운 IoT 기기 등록 API
@app.post("/api/devices/")
def register_device(device: Device):
    try:
        conn = get_db_connection()
        cursor = conn.cursor()

        # 새로운 기기 삽입
        cursor.execute(
            """
            INSERT INTO devices (latitude, longitude, address, created_at, maintained_at)
            VALUES (?, ?, ?, ?, ?)
            """,
            (device.latitude, device.longitude, device.address, datetime.now(), datetime.now())
        )
        conn.commit()

        # 생성된 device_id 반환
        device_id = cursor.lastrowid
        return {"message": "Device registered successfully", "device_id": device_id}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        conn.close()

# IoT 센서 데이터 전송 API
@app.post("/api/sensor-data/")
def add_sensor_data(data: IoTData):
    try:
        conn = get_db_connection()
        cursor = conn.cursor()

        # 디바이스 존재 여부 확인
        cursor.execute("SELECT * FROM devices WHERE device_id = ?", (data.device_id,))
        device = cursor.fetchone()
        if not device:
            raise HTTPException(status_code=404, detail="Device not found")

        # 데이터 삽입
        cursor.execute(
            """
            INSERT INTO sensor_data (device_id, ir_sensor, trash_detection, battery_percent, timestamp)
            VALUES (?, ?, ?, ?, ?)
            """,
            (data.device_id, data.ir_sensor, data.trash_detection, data.battery_percent, datetime.now())
        )
        conn.commit()
        return {"message": "Data successfully added"}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        conn.close()

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)

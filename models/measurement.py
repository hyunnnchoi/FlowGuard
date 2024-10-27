from db.database import get_db_connection

def save_measurement(data):
    conn = get_db_connection()
    cursor = conn.cursor()
    query = """
    INSERT INTO measurements (device_id, measurement_time, debris_height, is_blocked)
    VALUES (%s, %s, %s, %s)
    """
    cursor.execute(query, (data['device_id'], data['measurement_time'], data['debris_height'], data['is_blocked']))
    conn.commit()
    cursor.close()
    conn.close()

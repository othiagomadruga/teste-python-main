import os
from flask import Flask, request, jsonify
import mysql.connector
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

def get_db_connection():
    return mysql.connector.connect(
        host=os.getenv('DB_HOST'),
        user=os.getenv('DB_USER'),
        password=os.getenv('DB_PASSWORD'),
        database=os.getenv('DB_NAME'),
        port=int(os.getenv('DB_PORT'))
    )

@app.route('/device/android', methods=['POST'])
def insert_device_info():
    data = request.get_json()
    if not data:
        return jsonify({'error': 'No data provided'}), 400

    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS device_data (
                id INT AUTO_INCREMENT PRIMARY KEY,
                manufacturer TEXT NOT NULL,
                model TEXT NOT NULL,
                os_version TEXT NOT NULL,
                apps LONGTEXT NOT NULL,
                network TEXT NOT NULL,
                storage TEXT NOT NULL,
                users TEXT NOT NULL,
                timestamp TEXT NOT NULL
            )
        ''')
        cursor.execute('''
            INSERT INTO device_data
            (manufacturer, model, os_version, apps, network, storage, users, timestamp)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        ''', (
            data.get("manufacturer", ""),
            data.get("model", ""),
            data.get("os_version", ""),
            data.get("apps", ""),
            data.get("network", ""),
            data.get("storage", ""),
            data.get("users", ""),
            data.get("timestamp", "")
        ))
        conn.commit()
        cursor.close()
        conn.close()
        return jsonify({'status': 'success'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
@app.route('/devices/android', methods=['GET'])
def get_all_devices():
    try:
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute('SELECT * FROM device_data')
        rows = cursor.fetchall()
        cursor.close()
        conn.close()
        return jsonify(rows), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
@app.route('/device/android/<int:device_id>', methods=['GET'])
def get_device_by_id(device_id):
    try:
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute('SELECT * FROM device_data WHERE id = %s', (device_id,))
        row = cursor.fetchone()
        cursor.close()
        conn.close()
        if row:
            return jsonify(row), 200
        else:
            return jsonify({'error': 'Device not found'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
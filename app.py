
from flask import Flask, request, jsonify
import psycopg2
from psycopg2.extras import RealDictCursor

app = Flask(__name__)






def get_db_connection():
    try:
        conn = psycopg2.connect(
            host="dpg-cpkch3nsc6pc73er0mi0-a",
            port=5432,
            database="sensor_csmt",
            user="sensor_csmt_user",
            password="hFOCXl45t2bEoj28CKFxvwwWLmpS3tyq"
        )
        return conn
    except Exception as e:
        return None
    
    
def create_table():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS sensor (
            id SERIAL PRIMARY KEY,
            temperature REAL,
            humidity REAL,
            date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    conn.commit()
    cursor.close()
    conn.close()
# Endpoint pour insérer des données
@app.route('/add_data', methods=['POST'])
def add_data():
    create_table()
    data = request.get_json()
    temperature = data.get('temperature')
    humidity = data.get('humidity')

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        'INSERT INTO DHT (temperature, humidity) VALUES (%s, %s)',
        (temperature, humidity)
    )
    conn.commit()
    cursor.close()
    conn.close()

    return jsonify({"status": "success"}), 201

# Endpoint pour récupérer des données
@app.route('/get_data', methods=['GET'])
def get_data():
    conn = get_db_connection()
    cursor = conn.cursor(cursor_factory=RealDictCursor)
    cursor.execute('SELECT * FROM DHT')
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(rows), 200

if __name__ == '__main__':
    app.run(debug=True)

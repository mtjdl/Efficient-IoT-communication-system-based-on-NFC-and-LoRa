# database.py
import pymysql

class MySQLConnector:
    def __init__(self, host="mysql", user="iotuser", passwd="iotpass", db="iotdb"):
        self.conn = pymysql.connect(
            host=host, user=user, password=passwd, database=db,
            charset="utf8mb4", cursorclass=pymysql.cursors.DictCursor)
    
    def insert_sensor_data(self, node_id, temperature, humidity):
        with self.conn.cursor() as cursor:
            sql = "INSERT INTO sensor_data(node_id, temperature, humidity, ts) VALUES (%s, %s, %s, NOW())"
            cursor.execute(sql, (node_id, temperature, humidity))
        self.conn.commit()
    
    def close(self):
        self.conn.close()

# Cloud Service (MQTT + MySQL)

This directory contains:

1. `mqtt_listener.py`: Subscribes to the `iot/sensor/node1` topic, parses data, and stores it in MySQL  
2. `data_processor.py`: Implements the decompression (Algorithm B) and CRC checks (Algorithm C)  
3. `database.py`: MySQL connection and insertion helpers  
4. `requirements.txt`: Python dependencies  

## Environment Setup

- **MySQL** database with a `iotdb` schema. For example:
  ```sql
  CREATE DATABASE iotdb;
  USE iotdb;
  CREATE TABLE sensor_data(
    id INT AUTO_INCREMENT PRIMARY KEY,
    node_id VARCHAR(50),
    temperature FLOAT,
    humidity FLOAT,
    ts DATETIME
  );

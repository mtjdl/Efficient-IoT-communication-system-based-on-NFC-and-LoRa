#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import paho.mqtt.client as mqtt
from data_processor import verify_crc, decode_packet, BATCH_SIZE
from database import MySQLConnector

BROKER_HOST = "localhost"
BROKER_PORT = 1883
TOPIC = "iot/sensor/node1"

last_seq = 0
db = MySQLConnector(host="mysql", user="iotuser", passwd="iotpass", db="iotdb")

def on_connect(client, userdata, flags, rc):
    print("Connected to MQTT broker, subscribing to topic:", TOPIC)
    client.subscribe(TOPIC)

def on_message(client, userdata, msg):
    global last_seq
    packet_bytes = msg.payload

    # 1. Verify CRC (Algorithm C)
    if not verify_crc(packet_bytes):
        print("CRC check FAILED.")
        return

    # 2. Decode the packet (Algorithm B)
    seq, initT, initH, diffsT, diffsH = decode_packet(packet_bytes)
    if seq != last_seq + 1:
        print(f"Potential packet loss? expected={last_seq + 1}, got={seq}")
    last_seq = seq

    # Reconstruct the data points
    temps = [initT]
    hums = [initH]
    for i in range(BATCH_SIZE - 1):
        temps.append(temps[-1] + diffsT[i])
        hums.append(hums[-1] + diffsH[i])

    # 3. Store in MySQL
    for i in range(BATCH_SIZE):
        db.insert_sensor_data("node1", temps[i], hums[i])
    print(f"Stored packet seq={seq}, {BATCH_SIZE} records.")

def main():
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message
    client.connect(BROKER_HOST, BROKER_PORT, 60)
    client.loop_forever()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        db.close()
        print("Exiting...")

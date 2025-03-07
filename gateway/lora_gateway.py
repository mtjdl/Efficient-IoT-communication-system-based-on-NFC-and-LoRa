#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
lora_gateway.py
A sample Python script for a Raspberry Pi + SX1302 gateway:
- Receives LoRa packets (via packet forwarder or HAL)
- Forwards them to a cloud MQTT broker
"""

import socket
import time
import paho.mqtt.client as mqtt

MQTT_BROKER = "your-cloud-server-ip"
MQTT_PORT = 1883
MQTT_TOPIC = "iot/sensor/node1"

def main():
    # 1. Create a local UDP socket to listen to SX1302 packet forwarder output
    local_addr = ("0.0.0.0", 1700)  # typical packet forwarder port
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(local_addr)

    # 2. Connect to the MQTT broker
    client = mqtt.Client()
    client.connect(MQTT_BROKER, MQTT_PORT, 60)

    print("LoRa Gateway running... listening on UDP:1700")
    while True:
        data, addr = sock.recvfrom(1024)
        if not data:
            continue
        print(f"Received {len(data)} bytes from {addr}, forwarding to MQTT...")
        client.publish(MQTT_TOPIC, payload=data)
        time.sleep(0.1)

if __name__ == "__main__":
    main()

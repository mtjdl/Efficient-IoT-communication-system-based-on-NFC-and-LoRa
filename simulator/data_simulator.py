
---

## 4. `simulator/`: Data Simulator

### `data_simulator.py`

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
data_simulator.py
Simulate a device that generates temperature/humidity data periodically,
implements Algorithm B/C packing, attaches sequence & CRC, and sends via MQTT.
"""
import math
import random
import time
import paho.mqtt.client as mqtt
import struct

BROKER_HOST = "localhost"
BROKER_PORT = 1883
TOPIC = "iot/sensor/node1"

BATCH_SIZE = 10
seq_number = 0

def compute_crc(data):
    crc = 0xFFFF
    for b in data:
        crc ^= b
        for _ in range(8):
            if (crc & 1):
                crc >>= 1
                crc ^= 0xA001
            else:
                crc >>= 1
    return crc

def main():
    client = mqtt.Client()
    client.connect(BROKER_HOST, BROKER_PORT, 60)
    client.loop_start()
    
    temp_buffer = []
    hum_buffer = []

    global seq_number
    print("Starting simulator. Sending to MQTT broker:", BROKER_HOST)

    while True:
        # Generate cyclical temperature/humidity (1-hour sinus wave for demo)
        t = 25 + 5 * math.sin(time.time() / 3600 * 2*math.pi)
        h = 60 + 10 * math.sin(time.time() / 3600 * 2*math.pi + math.pi)
        # Add random noise
        t += random.uniform(-0.5, 0.5)
        h += random.uniform(-1, 1)

        temp_buffer.append(round(t, 2))
        hum_buffer.append(round(h, 2))

        if len(temp_buffer) >= BATCH_SIZE:
            seq_number += 1
            initT = temp_buffer[0]
            initH = hum_buffer[0]
            diffsT = []
            diffsH = []
            for i in range(1, BATCH_SIZE):
                diffsT.append(temp_buffer[i] - temp_buffer[i - 1])
                diffsH.append(hum_buffer[i] - hum_buffer[i - 1])

            # Pack: <Hff(9f)(9f)H
            packet_without_crc = struct.pack(
                "<Hff" + "f"*(BATCH_SIZE-1) + "f"*(BATCH_SIZE-1),
                seq_number, initT, initH, *diffsT, *diffsH
            )
            crc_val = compute_crc(packet_without_crc)
            packet = packet_without_crc + struct.pack("<H", crc_val)

            # Publish via MQTT
            client.publish(TOPIC, packet)
            print(f"Sim: seq={seq_number}, sent {BATCH_SIZE} records")

            temp_buffer.clear()
            hum_buffer.clear()

        time.sleep(60)  # 1 data point per minute

if __name__ == "__main__":
    main()

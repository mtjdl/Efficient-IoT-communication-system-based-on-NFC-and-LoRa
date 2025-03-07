# Efficient-IoT-communication-system-based-on-NFC-and-LoRa
# IoT-NFC-LoRa-Project

This project demonstrates how to use an **ESP32 + SX1276 + PN532 (NFC) + DHT22** as a LoRa node, combined with a **Raspberry Pi + SX1302** as the LoRa gateway, to upload sensor data via LoRa to a cloud server (Python + MySQL + Mosquitto MQTT). It also implements three algorithms described in the paper (A: adaptive frequency, B: differential compression and aggregation, C: packet loss detection and retransmission). A Python-based simulator is also provided to generate daytime/nighttime-like temperature and humidity data and send them via MQTT for testing.

## Feature Overview

1. **LoRa Device Node**  
   - Reads temperature/humidity from a DHT22 sensor  
   - Uses a PN532 module for NFC storage  
   - Sends data via SX1276 LoRa  
   - Implements Algorithm A (adaptive frequency), B (differential compression), C (data integrity check & retransmission)

2. **LoRa Gateway (Raspberry Pi + SX1302)**  
   - Captures LoRa packets via SX1302  
   - Publishes data to the cloud through MQTT (paho-mqtt)

3. **Cloud Server (Python + MySQL + MQTT)**  
   - Runs Mosquitto as an MQTT broker  
   - Listens to sensor data, decompresses and stores them into MySQL  
   - Implements algorithms B and C for data reconstruction and validation  
   - (Optional) can serve a REST API if needed

4. **Python Data Simulator**  
   - Periodically generates temperature/humidity data with diurnal (day-night) fluctuations  
   - Publishes data via MQTT to test the cloud pipeline

5. **Docker Support**  
   - Docker Compose can quickly deploy Mosquitto, MySQL, and the Python service  
   - Simplifies local or remote setup

## Quick Start

1. **Hardware Setup**  
   - Refer to [docs/hardware_setup.md](docs/hardware_setup.md) for wiring instructions of ESP32 with PN532, DHT22, SX1276, and Raspberry Pi with SX1302

2. **Compile & Upload Node**  
   - In `node/node_main.ino`, adjust any LoRa or pin definitions as necessary  
   - Use Arduino IDE or PlatformIO to flash the code to an ESP32

3. **Configure Gateway**  
   - On your Raspberry Pi, install the SX1302 packet forwarder/HAL  
   - Run `gateway/lora_gateway.py` (update MQTT server address if needed)

4. **Deploy Cloud Services**  
   - Go to the `docker/` folder and run `docker-compose up -d` to launch Mosquitto, MySQL, and the Python cloud service in containers  
   - (Or manually install MySQL, Mosquitto, Python, then run `cloud/mqtt_listener.py`)

5. **Simulator (Optional)**  
   - In `simulator/`, run `python data_simulator.py` to generate test data and publish it via MQTT

## Documentation

- [docs/hardware_setup.md](docs/hardware_setup.md) - Hardware and wiring instructions
- [docs/algorithms_explanation.md](docs/algorithms_explanation.md) - Detailed explanation of Algorithms A/B/C
- [docs/testing_guide.md](docs/testing_guide.md) - Tips for testing and validation

For further details, see individual subdirectory READMEs and the documentation under `docs/`.

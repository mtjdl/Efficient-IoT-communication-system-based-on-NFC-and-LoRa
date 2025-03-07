# LoRa Gateway (Raspberry Pi + SX1302)

This directory contains `lora_gateway.py`, a sample Python script to run on a Raspberry Pi equipped with an SX1302 LoRa concentrator board. It listens for LoRa data (via Semtech's packet forwarder) on UDP port 1700 and relays the data to a cloud MQTT broker.

## Prerequisites

1. Raspberry Pi OS (Bullseye or later)
2. [SX1302 HAL & packet forwarder](https://github.com/Lora-net/sx1302_hal) installed
3. Python 3.x, plus `paho-mqtt`:
   ```bash
   sudo apt-get install python3 python3-pip
   pip3 install paho-mqtt

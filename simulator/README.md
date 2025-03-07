# Data Simulator

The script `data_simulator.py` allows you to test the cloud data-processing pipeline without actual hardware. It:

1. Generates cyclical temperature/humidity data, mimicking day/night fluctuations  
2. Implements Algorithm B/C: batches of 10, differential encoding plus CRC  
3. Publishes binary packets via MQTT to the `iot/sensor/node1` topic

## Usage

```bash
pip install paho.mqtt
python data_simulator.py

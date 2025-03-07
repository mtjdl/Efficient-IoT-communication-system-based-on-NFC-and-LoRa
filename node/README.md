# LoRa Node (ESP32 + SX1276 + PN532 + DHT22)

This directory contains the Arduino/PlatformIO sketch `node_main.ino` for the ESP32 node. Main functionalities:

1. DHT22 sensor for temperature/humidity data  
2. PN532 NFC module for reading/writing data  
3. SX1276 for LoRa transmission  
4. Implements Algorithm A/B/C  

## Hardware Connections

- **ESP32** to **SX1276**: SCK, MISO, MOSI, NSS(SS), RST, and DIO0 pins must match the code definitions  
- **ESP32** to **PN532**: Example uses I2C mode (SDA=21, SCL=22)  
- **ESP32** to **DHT22**: Data pin -> GPIO4, plus power (3.3V/5V) and GND

## Compilation & Upload

1. Install [Arduino IDE](https://www.arduino.cc/en/software) or [PlatformIO](https://platformio.org/).  
2. Install the following libraries:
   - `DHT sensor library`
   - `LoRa by Sandeep Mistry`
   - `Adafruit PN532`
3. In Arduino IDE, select your ESP32 board type and proper COM port  
4. Compile and upload. Open the serial monitor to check the logs.

## Parameter Tuning

- `threshold` in the code (Algorithm A)  
- `maxInterval`, `minInterval` define the adaptive interval range  
- `BATCH_SIZE` defines how many data samples to batch (Algorithm B)

For more details, see the main [README.md](../README.md) and the [docs/](../docs) folder.

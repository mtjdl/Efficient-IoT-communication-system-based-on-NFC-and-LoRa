# Hardware Setup and Deployment

## ESP32 Node

- Refer to `node_main.ino` for pin definitions
- DHT22 -> GPIO4
- PN532 (I2C mode) -> SDA=21, SCL=22
- SX1276 -> SPI pins (SCK=5, MOSI=27, MISO=19, NSS=18, etc.)

## Raspberry Pi Gateway

- Connect SX1302 board via USB/SPI to the Pi
- Install SX1302 HAL & packet_forwarder
- Configure frequency band for your region (US915, EU868, etc.)

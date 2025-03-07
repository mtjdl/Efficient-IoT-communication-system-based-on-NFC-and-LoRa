# Testing Guide

1. **Functional Testing**  
   - Run the ESP32 node and watch logs in the gateway script to see if LoRa packets arrive.
   - Check the cloud `mqtt_listener.py` console to see if data is stored in the database.
   - Alternatively, run `data_simulator.py` to test your cloud pipeline without real hardware.

2. **Parameter Testing**  
   - Adjust Algorithm A threshold to see changes in sampling frequency.
   - Change BATCH_SIZE in Algorithm B to see how the data volume changes.
   - Force an error in CRC or skip a sequence number to test Algorithm C’s detection.

3. **Performance Testing**  
   - Observe the end-to-end latency (ESP32 -> Gateway -> MQTT -> Cloud).
   - Check insertion rate in the database.
   - Use Docker to spin up multiple container instances for concurrency tests.

4. **Real Hardware**  
   - Evaluate LoRa coverage at different distances, tweak SF/BW/TxPower.
   - Test NFC read/write for storing multiple data samples.

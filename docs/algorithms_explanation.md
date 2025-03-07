# Algorithms A/B/C Explanation

1. **Algorithm A (Adaptive Acquisition and Transmission Frequency)**
   - Monitors changes in sensor data (temperature/humidity).
   - Increases the sampling/transmission rate if changes exceed a threshold, reduces when stable.
   - Goal: save energy when data is stable while providing real-time updates on significant changes.

2. **Algorithm B (Compression and Aggregation)**
   - Uses differential encoding: store the first data point in full, then subsequent data as deltas.
   - Aggregates multiple readings (e.g., 10) into one packet, reducing transmission overhead.
   - On the cloud side, reconstruct the full data by summing the initial value and the deltas.

3. **Algorithm C (Packet Loss Detection and Retransmission)**
   - Appends sequence numbers and CRC checks.
   - If a sequence gap or CRC error is detected, the system identifies lost or corrupted packets, and can request retransmission.

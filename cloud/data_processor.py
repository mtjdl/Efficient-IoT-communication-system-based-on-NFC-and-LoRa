
### `data_processor.py`

Implements the decompression (Algorithm B) and CRC check (Algorithm C):

```python
# data_processor.py
import struct

BATCH_SIZE = 10

def verify_crc(packet_bytes):
    """Check the final two bytes for CRC16 correctness."""
    crc_calc = 0xFFFF
    for b in packet_bytes[:-2]:
        crc_calc ^= b
        for _ in range(8):
            if (crc_calc & 1):
                crc_calc >>= 1
                crc_calc ^= 0xA001
            else:
                crc_calc >>= 1
    # Extract the CRC from the packet
    crc_in_packet = packet_bytes[-2] | (packet_bytes[-1] << 8)
    return (crc_calc == crc_in_packet)

def decode_packet(packet_bytes):
    """
    Matches the DataPacket structure from the node code:
    typedef struct {
      uint16_t seq;
      float initTemp;
      float initHum;
      float diffsTemp[BATCH_SIZE-1];
      float diffsHum[BATCH_SIZE-1];
      uint16_t crc;
    } DataPacket;

    Using struct format: <Hff(9f)(9f)H for BATCH_SIZE=10
    """
    format_str = "<Hff" + "f"*(BATCH_SIZE-1) + "f"*(BATCH_SIZE-1) + "H"
    unpacked = struct.unpack(format_str, packet_bytes)
    seq = unpacked[0]
    initT = unpacked[1]
    initH = unpacked[2]
    diffsT = unpacked[3:3 + (BATCH_SIZE-1)]
    diffsH = unpacked[3 + (BATCH_SIZE-1):3 + 2*(BATCH_SIZE-1)]
    return seq, initT, initH, diffsT, diffsH

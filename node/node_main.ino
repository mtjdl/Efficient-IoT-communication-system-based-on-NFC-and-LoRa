/*****************************************************
 * node_main.ino
 * ESP32 + SX1276 + PN532 + DHT22
 * Performs temperature/humidity collection, NFC storage,
 * LoRa transmission, and implements algorithms A/B/C.
 *****************************************************/

#include <Arduino.h>
#include <DHT.h>         // DHT library
#include <SPI.h>
#include <Wire.h>
#include <LoRa.h>        // SX1276 LoRa library
#include "Adafruit_PN532.h" // PN532 NFC library

// ---------- Pin Definitions (example) ----------
#define DHTPIN 4
#define DHTTYPE DHT22

// LoRa pins (adjust based on your SX1276 board)
#define LORA_SS  18
#define LORA_RST 14
#define LORA_DIO0 26

// PN532 I2C
#define PN532_I2C_SDA 21
#define PN532_I2C_SCL 22

// ---------- Global Objects & Variables ----------
DHT dht(DHTPIN, DHTTYPE);
Adafruit_PN532 nfc(PN532_I2C_SDA, PN532_I2C_SCL);

float prevTemp = 0.0, prevHum = 0.0;  
float threshold = 0.5;             // Algorithm A threshold
int maxInterval = 60;              // 60s
int minInterval = 300;             // 300s
int currentInterval = 60;

// Algorithm B buffers
static const int BATCH_SIZE = 10;
float tempBuffer[BATCH_SIZE];
float humBuffer[BATCH_SIZE];
int bufferIndex = 0;

// Algorithm C
int seqNumber = 0;

// Simple CRC16
uint16_t computeCRC(const uint8_t* data, size_t len) {
  uint16_t crc = 0xFFFF;
  for (size_t i = 0; i < len; i++) {
    crc ^= data[i];
    for (int j = 0; j < 8; j++) {
      if (crc & 1) {
        crc >>= 1;
        crc ^= 0xA001;
      } else {
        crc >>= 1;
      }
    }
  }
  return crc;
}

// Data packet structure
typedef struct __attribute__((packed)) {
  uint16_t seq;
  float initTemp;
  float initHum;
  float diffsTemp[BATCH_SIZE - 1];
  float diffsHum[BATCH_SIZE - 1];
  uint16_t crc;
} DataPacket;

void setup() {
  Serial.begin(115200);
  dht.begin();

  // Initialize NFC
  nfc.begin();
  uint32_t versiondata = nfc.getFirmwareVersion();
  if (!versiondata) {
    Serial.println("PN532 not found!");
  } else {
    Serial.println("Found PN532 NFC module");
    nfc.SAMConfig(); // Initialize secure access module
  }

  // Initialize LoRa
  SPI.begin(5, 19, 27, LORA_SS); // Adjust pins as needed
  LoRa.setPins(LORA_SS, LORA_RST, LORA_DIO0);
  if (!LoRa.begin(915E6)) {  // Example frequency: 915MHz
    Serial.println("LoRa init failed!");
    while (1);
  }
  Serial.println("LoRa init OK");

  currentInterval = maxInterval;
}

void loop() {
  float t = dht.readTemperature();
  float h = dht.readHumidity();
  if (isnan(t) || isnan(h)) {
    Serial.println("Failed to read from DHT sensor!");
    delay(2000);
    return;
  }

  // Algorithm A: adjust interval based on data change
  float delta = fabs(t - prevTemp) + fabs(h - prevHum);
  if (delta > threshold) {
    currentInterval = maxInterval;
  } else {
    currentInterval = minInterval;
  }
  prevTemp = t;
  prevHum = h;

  // NFC write example (omitted actual PN532 write for brevity)
  char nfcMsg[32];
  snprintf(nfcMsg, sizeof(nfcMsg), "T=%.2f,H=%.2f", t, h);
  Serial.print("NFC write: ");
  Serial.println(nfcMsg);

  // Algorithm B: buffer data for batch sending
  tempBuffer[bufferIndex] = t;
  humBuffer[bufferIndex] = h;
  bufferIndex++;

  if (bufferIndex >= BATCH_SIZE) {
    seqNumber++;
    float initT = tempBuffer[0];
    float initH = humBuffer[0];
    float diffsT[BATCH_SIZE - 1];
    float diffsH[BATCH_SIZE - 1];
    for (int i = 1; i < BATCH_SIZE; i++) {
      diffsT[i - 1] = tempBuffer[i] - tempBuffer[i - 1];
      diffsH[i - 1] = humBuffer[i] - humBuffer[i - 1];
    }

    DataPacket packet;
    packet.seq = seqNumber;
    packet.initTemp = initT;
    packet.initHum = initH;
    for (int i = 0; i < BATCH_SIZE - 1; i++) {
      packet.diffsTemp[i] = diffsT[i];
      packet.diffsHum[i] = diffsH[i];
    }

    // Compute CRC (Algorithm C)
    packet.crc = 0;
    uint16_t c = computeCRC((uint8_t*)&packet, sizeof(packet));
    packet.crc = c;

    // Send via LoRa
    Serial.printf("Sending LoRa packet, seq=%d\n", seqNumber);
    LoRa.beginPacket();
    LoRa.write((uint8_t*)&packet, sizeof(packet));
    LoRa.endPacket();

    bufferIndex = 0;
  }

  delay(currentInterval * 1000);
}

#include <SPI.h>
#include <MFRC522.h>

#define RST_PIN         9          // Configurable, see typical pin layout above
#define SS_PIN          10         // Configurable, see typical pin layout above

MFRC522 mfrc522(SS_PIN, RST_PIN);  // Create MFRC522 instance

void setup() {
  Serial.begin(9600);   // Initialize serial communications with the PC
  while (!Serial);    // Do nothing if no serial port is opened (added for Arduinos based on ATMEGA32U4)
  SPI.begin();      // Init SPI bus
  mfrc522.PCD_Init();   // Init MFRC522
  // mfrc522.PCD_DumpVersionToSerial(); // Show details of PCD - MFRC522 Card Reader details
  // Serial.println(F("Scan PICC to see UID, SAK, type, and data blocks..."));
}

void loop() {

  // Look for new cards
  if ( ! mfrc522.PICC_IsNewCardPresent()) {
    return;
  }

  // Select one of the cards
  if ( ! mfrc522.PICC_ReadCardSerial()) {
    return;
  }

  // Dump debug info about the card; PICC_HaltA() is automatically called
 Serial.print("7,");
   // mfrc522.PICC_DumpToSerial(&(mfrc522.uid));
 // Serial.print(String((char *)mfrc522.uid.uidByte));
 // Serial.print(String((char *)mfrc522.uidString), HEX);
    for (byte i = 0; i < mfrc522.uid.size; i++) {
       // if(mfrc522.uid.uidByte[i] < 0x10)
        //    Serial.print(F(" 0"));
     //   else
       //     Serial.print(F(" "));
        Serial.print(mfrc522.uid.uidByte[i], HEX);
  }
  Serial.println();
  delay(5000);
}

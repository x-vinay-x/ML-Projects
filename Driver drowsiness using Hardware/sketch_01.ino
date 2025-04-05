#include <Wire.h>
#include <LiquidCrystal_I2C.h>
#include <SoftwareSerial.h>

// LCD and GSM Configuration
LiquidCrystal_I2C lcd(0x27, 16, 2);
SoftwareSerial gsm(2, 3); // RX, TX (Connect GSM TX to pin 2, RX to pin 3)

// Pins for buzzer and LED
const int buzzer_Pin = 8;
const int led_Pin = 9;

// State tracking
char sleep_status = 'b'; // Default state (Active)

// GSM task queue
bool send_sms = false;
bool make_call = false;
String emergencyNumber = "9380013335";
String alertMessage = "";

void setup() {
  Serial.begin(115200); // Match baud rate with Python script
  gsm.begin(115200);    // GSM Module baud rate

  pinMode(buzzer_Pin, OUTPUT);
  pinMode(led_Pin, OUTPUT);

  lcd.init();
  lcd.backlight();
  lcd.setCursor(0, 0);
  lcd.print("Driver Sleep ");
  lcd.setCursor(0, 1);
  lcd.print("Detection SYSTEM");

  digitalWrite(buzzer_Pin, LOW);
  digitalWrite(led_Pin, LOW);

  Serial.println("Initializing GSM...");
  gsm.println("AT");
  delay(500);
  gsm.println("AT+CMGF=1"); // Set SMS to Text Mode
  delay(500);
}

// Function to send SMS (non-blocking)
void sendSMS() {
  if (send_sms) {
    gsm.println("AT+CMGF=1");  
    delay(500);
    
    gsm.print("AT+CMGS=\"");
    gsm.print(emergencyNumber);
    gsm.println("\"");
    delay(500);

    gsm.println(alertMessage);
    delay(500);
    
    gsm.write(26); // Ctrl+Z to send SMS
    delay(1000); // Short delay to allow sending
    Serial.println("SMS Sent to " + emergencyNumber);
    
    send_sms = false; // Reset flag
  }
}

// Function to make a call (non-blocking)
void makeCall() {
  if (make_call) {
    gsm.print("ATD");
    gsm.print(emergencyNumber);
    gsm.println(";");
    Serial.println("Calling " + emergencyNumber);

    delay(10000); // Let it ring for 10 seconds
    gsm.println("ATH"); // Hang up the call
    Serial.println("Call Ended.");

    make_call = false; // Reset flag
  }
}

void loop() {
  sendSMS();  // Process pending SMS task
  makeCall(); // Process pending call task

  if (Serial.available() > 0) {
    char new_status = Serial.read(); // Read a single character
    if (new_status == 'a' || new_status == 'b' || new_status == 'y' || new_status == 'p') {
      if (new_status != sleep_status) {
        sleep_status = new_status;

        // **Instantly Update LCD and Buzzer**
        switch (sleep_status) {
          case 'a': // Drowsy
            digitalWrite(buzzer_Pin, HIGH);
            digitalWrite(led_Pin, HIGH);
            lcd.clear();
            lcd.print("Driver is Sleepy!");

            alertMessage = "Drowsy detected! Wake up!";
            send_sms = true;  // Trigger SMS sending
            make_call = true; // Trigger call
            break;

          case 'b': // Active (Instant Reset)
            digitalWrite(buzzer_Pin, LOW);
            digitalWrite(led_Pin, LOW);
            lcd.clear();
            lcd.print("All Okay");
            lcd.setCursor(0, 1);
            lcd.print("Driver Awake!");
            break;

          case 'y': // Yawning
            digitalWrite(buzzer_Pin, HIGH);
            digitalWrite(led_Pin, HIGH);
            lcd.clear();
            lcd.print("Yawning Detected!");

            alertMessage = "Yawning detected! Wake up!";
            send_sms = true;
            make_call = true;
            break;

          case 'p': // Head Pose Alert
            digitalWrite(buzzer_Pin, HIGH);
            digitalWrite(led_Pin, HIGH);
            lcd.clear();
            lcd.print("Head Pose Alert!");

            alertMessage = "Head pose alert! Focus on road.";
            send_sms = true;
            make_call = true;
            break;
        }
      }
    }
  }
}

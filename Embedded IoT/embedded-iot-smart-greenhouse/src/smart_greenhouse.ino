#include <Keypad.h>
#include <Wire.h>
#include <LiquidCrystal_I2C.h>

// Sensor pins
const byte LDR_PIN = A2;
const byte SOIL_MOISTURE_PIN = A1;

// Output pins
const byte LED_PIN_1 = 10;
const byte LED_PIN_2 = 11;
const byte RELAY_PIN = 13;

// Sensor threshold values
const int SOIL_MOISTURE_THRESHOLD = 700;
const int LDR_THRESHOLD = 300;

// Sensor values
int ldrValue = 0;
int soilMoistureValue = 0;

// Keypad configuration
const byte ROWS = 4;
const byte COLS = 4;

char keys[ROWS][COLS] = {
  {'1', '2', '3', 'a'},
  {'4', '5', '6', 'b'},
  {'7', '8', '9', 'c'},
  {'*', '0', '#', 'd'}
};

byte rowPins[ROWS] = {5, 4, 3, 2};
byte colPins[COLS] = {9, 8, 7, 6};

Keypad keypad = Keypad(makeKeymap(keys), rowPins, colPins, ROWS, COLS);

// LCD I2C configuration
LiquidCrystal_I2C lcd(0x27, 16, 2);

void setup() {
  Serial.begin(9600);

  lcd.init();
  lcd.backlight();

  pinMode(LED_PIN_1, OUTPUT);
  pinMode(LED_PIN_2, OUTPUT);
  pinMode(RELAY_PIN, OUTPUT);
}

void loop() {
  char key = keypad.getKey();

  // Read sensor values
  ldrValue = analogRead(LDR_PIN);
  soilMoistureValue = analogRead(SOIL_MOISTURE_PIN);

  // Display selected sensor value based on keypad input
  if (key) {
    handleKeypadInput(key);
  }

  // Print sensor values to Serial Monitor
  printSensorValues();

  // Control water pump based on soil moisture
  controlWaterPump();

  // Control LED based on light intensity
  controlLedLighting();

  delay(50);
}

void handleKeypadInput(char key) {
  if (key == '1') {
    lcd.clear();
    lcd.print("S Kelembaban");
    lcd.setCursor(0, 1);
    lcd.print("Nilai = ");
    lcd.print(soilMoistureValue);
  } 
  else if (key == '3') {
    lcd.clear();
    lcd.print("Sensor LDR");
    lcd.setCursor(0, 1);
    lcd.print("Nilai = ");
    lcd.print(ldrValue);
  } 
  else {
    Serial.print("Keypad: ");
    Serial.println(key);
  }
}

void printSensorValues() {
  Serial.print("Sensor Kelembaban: ");
  Serial.println(soilMoistureValue);

  Serial.print("Nilai LDR: ");
  Serial.println(ldrValue);
}

void controlWaterPump() {
  if (soilMoistureValue <= SOIL_MOISTURE_THRESHOLD) {
    digitalWrite(RELAY_PIN, LOW);
  } 
  else {
    digitalWrite(RELAY_PIN, HIGH);
  }
}

void controlLedLighting() {
  if (ldrValue < LDR_THRESHOLD) {
    digitalWrite(LED_PIN_1, HIGH);
    digitalWrite(LED_PIN_2, HIGH);
  } 
  else {
    digitalWrite(LED_PIN_1, LOW);
    digitalWrite(LED_PIN_2, LOW);
  }
}

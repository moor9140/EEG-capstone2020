int LED = LED_BUILTIN;
int numPins = 5;
int pinOffset = 14;
int i;

void setup() {
  Serial.begin(9600);
}

void loop() {
  for (i = 0; i < numPins; i++){
    Serial.print("A");
    Serial.print(i);
    Serial.print(": ");
    Serial.print(analogRead(i+pinOffset));
    Serial.print("\t");
  }
  Serial.print("\n");
  delay(500);
}

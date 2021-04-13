int LED = LED_BUILTIN;
int numPins = 8;
int pinOffset = 14;
int i;

void setup() {
  Serial.begin(9600);
}

void loop() {
  for (i = 0; i < numPins-1; i++){
    //Serial.print(analogRead(i+pinOffset));
    Serial.print(random(200,400));
    Serial.print(",");
  }
  //Serial.print(analogRead(pinOffset-1));
  Serial.print(random(200,400));
  //Serial.print(analogRead(14));
  
  Serial.print("\n");
  //delay(120);
}

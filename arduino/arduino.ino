/* 
 *  Prints the analog values from pins in a sequence
 */
int numPins = 8;  // How many pins are being printed?
int pinOffset = 14;  // Where does first pin begin?
int baudRate = 9600;  // See serial monitor for values to choose
//bool TESTING = true;  // print random values if true
bool TESTING = false;
int delayVal = 0;  // how long between new lines?

void setup() {
  Serial.begin(baudRate);  
  while (TESTING){
      testloop();  
  }
}

void loop() {
  for (int i = 0; i < numPins-1; i++){
    Serial.print(analogRead(i+pinOffset));  
    Serial.print(",");
  }
  Serial.print(analogRead(pinOffset-1));
  Serial.print("\n");
  delay(delayVal);
}

void testloop(){
  for (int i = 0; i < numPins-1; i++){
    Serial.print(random(200,400));  
    Serial.print(",");
  }
  Serial.print(random(200,400));
  Serial.print("\n");
  delay(delayVal);  
}

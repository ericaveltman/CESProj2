int xyzPins[] = {13, 12, 14}; //x,y,z pins
int blueButton = 25;
int redButton = 33;
int switch1 = 18;
int blueButtonOld = 1;
int redButtonOld = 1;

void setup() {
Serial.begin(9600);
pinMode(xyzPins[2], INPUT_PULLUP); //z axis is a button.
pinMode(blueButton, INPUT_PULLUP);
pinMode(redButton, INPUT_PULLUP);
pinMode(switch1, INPUT_PULLUP);

}

void loop() {
int xVal = analogRead(xyzPins[0]);
int yVal = analogRead(xyzPins[1]);
int zVal = digitalRead(xyzPins[2]);

if(blueButtonOld == 0 && digitalRead(blueButton) == 1){
  blueButtonOld = 1;
}else if(redButtonOld == 0 && digitalRead(redButton) == 1){
  redButtonOld = 1;
}

if(blueButtonOld == 1 && digitalRead(blueButton) == 0){ 
  Serial.print(0);
  blueButtonOld = 0;
}else{
  Serial.print(1);
}

Serial.print('\n');

if(redButtonOld == 1 && digitalRead(redButton) == 0){ 
  Serial.print(0);
  redButtonOld = 0;
}else{
  Serial.print(1);
}

Serial.print('\n');
Serial.print(digitalRead(switch1));
Serial.print('\n');
Serial.print(yVal);
Serial.print('\n');
delay(100);
}

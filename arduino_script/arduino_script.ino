#include <Servo.h>
Servo servo;
int buff[4];
int loc = 0;
int digital_listeners[14];
int datum;

void process_instruction(int mode, int pin, int val) {
  switch (mode) {
    case 1: // digitalRead
      if(digital_listeners[pin] != 1){
        digital_listeners[pin] = 1;
        pinMode(pin, INPUT);
      }
      if(val == 1){
        Serial.write(digitalRead(pin));
      }
      break;
    case 2: // digitalWrite
      break;
    case 3: // servo
      digital_listeners[pin] = 3;
      servo.attach(pin);
      servo.write(val);
      break;
    case 4: // pwm
      break;
    case 5: // analogRead
      break;
  }
}

int listen_to_digital(){ // I'm really beginning to doubt the utility of this...
  int sensors[14];
  for(int i = 0; i < 14; i++){
    if(digital_listeners[i] == 1){
      Serial.write(digitalRead(i) + 16);
    } else {
      Serial.write(0);
    }
  }
  return(sensors);
}

void setup() {
  Serial.begin(9600);
}

void loop() {
  if (Serial.available() > 0) {
    datum = Serial.read();
    if(datum == 255){
      listen_to_digital();
    } else {
      buff[loc] = datum;
      loc += 1;
      if (loc == 4) {
        process_instruction(buff[0], buff[1], buff[2] * 256 + buff[3]);
        loc = 0;
      }
    }
  }
}

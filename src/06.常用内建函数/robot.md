## 超声波测距

```cpp
const int TrigPin = 2; //引脚号自行更新
const int EchoPin = 3; //引脚号自行更新

int distance;

void getDistance(){
    digitalWrite(TrigPin, LOW);
    delayMicroseconds(2);
    digitalWrite(TrigPin, HIGH);
    delayMicroseconds(10);
    digitalWrite(TrigPin, LOW);
    distance = pulseIn(EchoPin, HIGH) / 58.0;
}
```

## 呼吸灯

```cpp
const int potPin = A0;
const int ledPin = 6;

void setup(){
    Serial.begin(9600);
}

void loop(){
    int potVal = analogRead(potPin);
    potVal = potVal/10;
    Serial.println(potVal);
    for (int i = 0; i <= 255; i++){
        analogWrite(ledPin, i);
        delay(potVal);
    }

    for (int i = 255; i >= 0; i--){
        analogWrite(ledPin, i);
        delay(potVal);
    }
}
```

## 红外线遥控

```cpp
#include <IRremote.h>

const int irPin = 12;

IRrecv irRecv(irPin);
decode_results results;

void setup(){
    irRecv.enableIRIn();
    Serial.begin(9600);
}

void loop(){
    if (irRecv.decode(&results)){
        Serial.println(results.value, HEX);

        switch (results.value){
            case 0xFF18E7:
            {
                Serial.println(1);
                break;
            }
            case 0xFF38C7:
            {
                Serial.println(2);
                break;
            }
        }
        irRecv.resume();
    }
}
```

## 舵机

```cpp
#include <Servo.h>

const int serPin = 3;

Servo myServo;

void setup(){
    myServo.attach(serPin);
}

void setup(){
    myServo.write(90);
    delay(1000);
    myServo.write(135);
}
```

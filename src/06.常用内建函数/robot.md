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

## 红外线智能小车

```cpp
#include <IRremote.h>

const int leftPin1 = 8; //AIN1连接引脚8
const int leftPin2 = 7; //AIN2连接引脚9
const int rightPin3 = 4; //BIN1连接引脚4
const int rightPin4 = 3; //BIN2连接引脚3
const int leftSpeed = 6; //PWA连接引脚6
const int rightSpeed = 5; //PWB连接引脚5
const int irPin = A0;//红外遥控传感器信号引脚连接主板引脚 A0
const int maxspeedPwm = 255;//PWM最大值
const int minspeedPwm = 90; //PWM最小值
const int speedStep = 10; //加速或减速时 PWM 的增减幅度

int intSpeedPwm = 130; //设置小车运行的初始速度
IRrecv irRecv(irPin); 
decode_results irResults;

void setup(){
    pinMode(leftPin1, OUTPUT);
    pinMode(leftPin2, OUTPUT);
    pinMode(rightPin1, OUTPUT);
    pinMode(rightPin2, OUTPUT);
    irRecv.enableIRIn();
    Serial.begin(9600);
}

void loop(){
    if (irRecv.decode(&irResults)){
        Serial.println(irResults.value, HEX);
        switch (irResult.value){
            case 0xFF10EF:{ //左转
                turnLeft();
                break;
            }
            case 0xFF5AA5:{ //右转
                turnRight();
                break;
            }
            case 0xFF18E7:{ //前进
                forward();
                break;
            }
            case 0xFF4AB5:{ //后退
                backward();
                break;
            }
            case 0xFF38C7:{ //停止
                pause();
                break;
            }
            case 0xFFA25D:{ //减速
                if(intSpeedPwm - speedStep < minSpeedPwm){
                    intSpeedPwm = minSpeedPwm;
                }else{
                    intSpeedPwm -= speedStep;
                }
                break;
            }
            case 0xFF629D:{ //加速
                if(intSpeedPwm + speedStep < maxSpeedPwm){
                    intSpeedPwm = maxSpeedPwm;
                }else{
                    intSpeedPwm += speedStep;
                }
                break;
            }
            case 0xFFE21D:{ //全速
                intSpeedPwm = maxSpeedPwm;
                break;
            }
        }
        analogWrite(leftSpeed, intSpeedPwm);
        analogWrite(rightSpeed, intSpeedPwm);
        irRecv.resume();
    }
}

/*前进*/
void forward(){
    digitalWrite(leftPin1, 1);
    digitalWrite(leftPin2, 0);
    digitalWrite(rightPin3, 1);
    digitalWrite(rightPin4, 0);
}

/*后退*/
void backward(){
    digitalWrite(leftPin1, 0);
    digitalWrite(leftPin2, 1);
    digitalWrite(rightPin3, 0);
    digitalWrite(rightPin4, 1);
}

/*左转*/
void turnLeft(){
    digitalWrite(leftPin1, 0);
    digitalWrite(leftPin2, 0);
    digitalWrite(rightPin3, 1);
    digitalWrite(rightPin4, 0);
}

/*右转*/
void turnRight(){
    digitalWrite(leftPin1, 1);
    digitalWrite(leftPin2, 0);
    digitalWrite(rightPin3, 0);
    digitalWrite(rightPin4, 0);
}

/*停止*/
void pause(){
    digitalWrite(leftPin1, 0);
    digitalWrite(leftPin2, 0);
    digitalWrite(rightPin3, 0);
    digitalWrite(rightPin4, 0);
}

/*原地左转*/
void  rotateLeft(){
    digitalWrite(leftPin1, 0);
    digitalWrite(leftPin2, 1);
    digitalWrite(rightPin3, 1);
    digitalWrite(rightPin4, 0);
}

/*原地右转*/
void  rotateLeft(){
    digitalWrite(leftPin1, 1);
    digitalWrite(leftPin2, 0);
    digitalWrite(rightPin3, 0);
    digitalWrite(rightPin4, 1);
}
```
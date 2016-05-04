#include <MsTimer2.h>
#include <Wire.h>

unsigned long time;
//距離センサの値を格納
unsigned int val0,val1,val2,val3;
//加速度センサの値を格納
//int x,y,z;

#define DEVICE_ADDR (0x53) // スレーブデバイスのアドレス
byte axis_buff[6];

void ad(){
  interrupts();
  //if ( Serial.available() > 0 ) {
    time = micros();
    uint8_t length = 6;
    readI2c(0x32, length, axis_buff); //レジスターアドレス 0x32から6バイト読む
    //x = (((int)axis_buff[1]) << 8) | axis_buff[0];   
    //y = (((int)axis_buff[3]) << 8) | axis_buff[2];
    //z = (((int)axis_buff[5]) << 8) | axis_buff[4];
    val0 = analogRead(0);
    val1 = analogRead(1);
    val2 = analogRead(2);
    val3 = analogRead(3);
    //Serial.print(time);
    Serial.print(",");
    Serial.print(" ");
    Serial.print(val0);
    Serial.print(" ");
    Serial.print(val1);
    Serial.print(" ");
    Serial.print(val2);
    Serial.print(" ");
    Serial.print(val3);
    //Serial.print(" ");
    //Serial.print( x );
    //Serial.print(" ");
    //Serial.print( y );
    //Serial.print(" ");
    //Serial.println( z );
    Serial.read();
    //delay(50);
  //}   
}

void setup() {
  Serial.begin(9600);
  Wire.begin();       // I2Cの開始
  Serial.write("init");
  // DATA_FORMAT
  writeI2c(0x31, 0x00);
  // POWER_TCL
  writeI2c(0x2d, 0x08);
  MsTimer2::set(100, ad);
  MsTimer2::start();
}

void loop() {
  //
}


// I2Cへの書き込み
void writeI2c(byte register_addr, byte value) {
  Wire.beginTransmission(DEVICE_ADDR);  
  Wire.write(register_addr);         
  Wire.write(value);                 
  Wire.endTransmission();        
}

// I2Cへの読み込み
void readI2c(byte register_addr, int num, byte buffer[]) {
  Wire.beginTransmission(DEVICE_ADDR); 
  Wire.write(register_addr);           
  Wire.endTransmission();         

  Wire.beginTransmission(DEVICE_ADDR); 
  Wire.requestFrom(DEVICE_ADDR, num);   

  int i = 0;
  while(Wire.available())        
  { 
    buffer[i] = Wire.read();   
    i++;
  }
  Wire.endTransmission();         
}

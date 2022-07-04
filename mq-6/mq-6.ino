
#include <MQUnifiedsensor.h>

//Definitions
#define placa "Arduino UNO"
#define Voltage_Resolution 5
#define pin A0 //Analog input 0 of your arduino
#define type "MQ-6" //MQ6
#define ADC_Bit_Resolution 10 // For arduino UNO/MEGA/NANO
#define RatioMQ6CleanAir 10   //RS / R0 = 10 ppm 


//Declare Sensor
MQUnifiedsensor MQ6(placa, Voltage_Resolution, ADC_Bit_Resolution, pin, type);

void setup() {
  //Init the serial port communication - to debug the library
  Serial.begin(9600); //Init serial port

  //Set math model to calculate the PPM concentration and the value of constants
  MQ6.setRegressionMethod(1); //_PPM =  a*ratio^b
  MQ6.setA(2127.2); MQ6.setB(-2.526); // Configure the equation to to calculate CH4 concentration
  /*
    Exponential regression:
  GAS     | a      | b
  H2      | 88158  | -3.597
  LPG     | 1009.2 | -2.35
  CH4     | 2127.2 | -2.526
  CO      | 1000000000000000 | -13.5
  Alcohol | 50000000 | -6.017
  */
  
 
  MQ6.init();   

  float calcR0 = 0;
  for(int i = 1; i<=10; i ++)
  {
    MQ6.update(); // Update data, the arduino will read the voltage from the analog pin
    calcR0 += MQ6.calibrate(RatioMQ6CleanAir);
  }
  MQ6.setR0(calcR0/10);
  Serial.println("  done!.");
  
  if(isinf(calcR0)) {Serial.println("Warning: Conection issue, R0 is infinite (Open circuit detected) please check your wiring and supply"); while(1);}
  if(calcR0 == 0){Serial.println("Warning: Conection issue found, R0 is zero (Analog pin shorts to ground) please check your wiring and supply"); while(1);}
  MQ6.serialDebug(true);
}

void loop() {
  MQ6.update(); // Update data, the arduino will read the voltage from the analog pin
  MQ6.readSensor(); // Sensor will read PPM concentration using the model, a and b values set previously or from the setup
  MQ6.serialDebug(); // Will print the table on the serial port
  delay(3000); //Sampling frequency
}

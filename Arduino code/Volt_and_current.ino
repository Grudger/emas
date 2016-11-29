
int sensorIn = A7;
int mVperAmp = 100 ; // use 100 for 20A Module and 66 for 30A Module10


double Voltage = 0;
double VRMS = 0;
double AmpsRMS = 0;



void setup(){ 
 Serial.begin(9600);
}

void loop(){
 //volt read
  int sensorValue = analogRead(A0);
  float volt = (sensorValue * (250.0 / 1024.0)) * 0.447761194;
  
  //Serial.println(" Volts");
 
  //current read
  Voltage = getVPP();
  VRMS = (Voltage/2.0) * 0.447761194; 
  AmpsRMS = (VRMS * 1000)/mVperAmp;
  //int sensorIn = analogRead(A7);
  //float AmpsRms = (sensorIn * (30.0 / 1024.
  Serial.print("{");
  Serial.print(" \"volt1\":");
  Serial.print(volt);
  Serial.print(" , ");
  Serial.print(" \"volt2\":");
  Serial.print(volt);
  Serial.print(" , ");
  Serial.print(" \"volt3\":");
  Serial.print(volt);
  Serial.print(" , ");
  Serial.print(" \"cur1\":");
  Serial.print(AmpsRMS);
  Serial.print(" , ");
  Serial.print(" \"cur2\":");
  Serial.print(AmpsRMS);
  Serial.print(" , ");
  Serial.print(" \"cur3\":");
  Serial.print(AmpsRMS);
  //Serial.print(analogRead(A7));
  Serial.print("}");
  Serial.println();
  delay(1500);
}

float getVPP()
{
  float result;
  
  int readValue;             //value read from the sensor
  int maxValue = 0;          // store max value here
  int minValue = 1024;          // store min value here
  
   uint32_t start_time = millis();
   while((millis()-start_time) < 1000) //sample for 1 Sec
   {
       readValue = analogRead(sensorIn);
       // see if you have a new maxValue
       if (readValue > maxValue) 
       {
           /*record the maximum sensor value*/
           maxValue = readValue;
       }
       if (readValue < minValue) 
       {
           /*record the maximum sensor value*/
           minValue = readValue;
       }
   }
   
   // Subtract min from max
   result = ((maxValue - minValue) * 5.0)/1024.0;
      
   return result;
 }


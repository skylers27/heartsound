#include <ezLCDLib.h>
ezLCD3 lcd;
float x = 0;
float timescale = .1; //seconds per frame
float high = 5; //max voltage displayed
float low = -1; //min voltage displayed
//int data[320];

void setup() {
  // put your setup code here, to run once:
  lcd.begin( EZM_BAUD_RATE );
  lcd.cls();
}

void loop() {
  // put your main code here, to run repeatedly:
  //range x:(319, 0) y:(239, 0)
  x = 0;
  lcd.color(WHITE);
  lcd.font(1);
  
  lcd.print("\\[5x\\[235yV = ");
  lcd.print(low);
  lcd.print(" & T = 0");

  lcd.print("\\[5x\\[5yV = ");
  lcd.print(high);

  lcd.print("\\[265x\\[225yT = ");
  lcd.print(timescale);
  
  for(int i=0; i < 319; i++){
    float value = analogRead(0);
    float volts = (5.00 * value) / 1023;
    float y = 240-((volts - low)*(240/(high-low)));
    x = x + 1; 
  }
    lcd.plot(x,y);  
    //delay((timescale*1000) / 320); //update every 1/10 second 
  
  delay(1000); 
  lcd.cls(); 

}

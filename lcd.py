import socket                                                      
import struct                                                      
import time                                                        
import pyupm_i2clcd as lcd                                         
import mraa

                                                                   
# Initialize Jhd1313m1 at 0x3E (LCD_ADDRESS) and 0x62 (RGB_ADDRESS)
                                            
while True:                                 
        myLcd = lcd.Jhd1313m1(0, 0x3E, 0x62)
        
        myLcd.clear()          
	      myLcd.setColor(0, 255 , 0)                                 
        myLcd.setCursor(0,0)                                       
        myLcd.write("Ola")                            
        time.sleep(10)
        myLcd.clear()
	      myLcd.setCursor(0,0)
	      myLcd.write("Ola de novo")                       
	      time.sleep(10)                               
           
         



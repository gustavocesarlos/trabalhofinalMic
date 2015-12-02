import time, sys, signal, atexit                                   
import pyupm_uln200xa as upmULN200XA                                 
      
# Instantiate a Stepper motor on a ULN200XA Darlington Motor Driver  
# This was tested with the Grove Geared Step Motor with Driver
 
# Instantiate a ULN2003XA stepper object                             
myUln200xa = upmULN200XA.ULN200XA(4096, 8, 9, 10, 11)                

## Exit handlers ##               
# This stops python from printing a stacktrace when you hit control-C
def SIGINTHandler(signum, frame):                                    
        raise SystemExit                                             
 
# This lets you run code on exit,          
# including functions from myUln200xa                                      
def exitHandler():                                                         
        print "Exiting"                                              
        sys.exit(0)                                                  

# Register exit handlers                   
atexit.register(exitHandler)                                               
signal.signal(signal.SIGINT, SIGINTHandler) 
###########################################
#Setando a velocidade e a direcao:                                   
myUln200xa.setSpeed(5) # 5 RPMs                                      
myUln200xa.setDirection(upmULN200XA.ULN200XA.DIR_CW) #sentido horario

print "Abrindo o portao..."                                          
myUln200xa.stepperSteps(300)                                         

print "Sleeping for 3 seconds..."                                    
time.sleep(3)                                                        
###########################################                          
#Setando a velocidade e a direcao:                                   
myUln200xa.setSpeed(5) # 5 RPMs                                      
myUln200xa.setDirection(upmULN200XA.ULN200XA.DIR_CCW) #sentido anti-horario
 
print "Fechando o portao..."                                               
myUln200xa.stepperSteps(300)                                               
time.sleep(1)                                                              
########################################### 
# release                                                            
myUln200xa.release()                                                 
 
# exitHandler is called automatically 

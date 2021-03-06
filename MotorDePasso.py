import time, sys, signal, atexit
import pyupm_uln200xa as upmULN200XA
import pyupm_i2clcd as lcd 
import mraa

#Funcao para interrupcao: Abre o portao
def abrePortao(args):
        #Setando a velocidade e a direcao do motor:
        myUln200xa.setSpeed(5) # 5 RPMs, eh a velocidade de rotacao do motor
        myUln200xa.setDirection(upmULN200XA.ULN200XA.DIR_CW) #sentido horario
        
        #Para escrever no lcd e fazer o motor rodar
        myLcd.clear()
        myLcd.setCursor(0,0)
        myLcd.write("Abrindo o portao...")
        myUln200xa.stepperSteps(300)    #setando os passos do motor. Nessa forma, o motor dara 3 voltas completas
        myLcd.clear()
        myLcd.setCursor(0,0)
        myLcd.write("Portao aberto.")

        time.sleep(1) #programa "dorme" por 1 segundo
##Fim abrePortao

#Funcao para interrupcao: Fecha o portao
def fechaPortao(args):
        #Setando a velocidade e a direcao do motor:
        myUln200xa.setSpeed(5) # 5 RPMs, eh a velocidade de rotacao do motor
        myUln200xa.setDirection(upmULN200XA.ULN200XA.DIR_CCW) #sentido anti-hora

        #Para escrever no lcd e fazer o motor rodar
        myLcd.clear()
        myLcd.setCursor(0,0)
        myLcd.write("Fechando o portao...")
        myUln200xa.stepperSteps(300)   #setando os passos do motor. Nessa forma, o motor dara 3 voltas completas  
        myLcd.clear()
        myLcd.setCursor(0,0)
        myLcd.write("Portao fechado.")
        
        time.sleep(1)    #programa "dorme" por 1 segundo                                                       
                                                                                
# Instantiate a Stepper motor on a ULN200XA Darlington Motor Driver             
# This was tested with the Grove Geared Step Motor with Driver                  
                                                                                
# Instantiate a ULN2003XA stepper object
#Os passos padroes do motor eh o primeiro parametro (4096).
#8, 9, 10 e 11 sao os pinos da Edson utilizados
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
                                                                                
#setando pinos para interrupcao:                                                
x = mraa.Gpio(2)        #Setando pino 1                                         
x.dir(mraa.DIR_IN)      #Setando como INPUT                                     
x.isr(mraa.EDGE_BOTH, abrePortao, abrePortao)   #setando a interrupcao. Ao apertar o botao, chamara a funcao abrePortao                                 
                                                                                
x = mraa.Gpio(3)        #Setando pino 1                                         
x.dir(mraa.DIR_IN)      #Setando como INPUT                                     
x.isr(mraa.EDGE_BOTH, fechaPortao, fechaPortao)  #setando a interrupcao. Ao apertar o botao, chamara a funcao fechaPortao  

#Inicializando o lcd
myLcd = lcd.Jhd1313m1(0, 0x3E, 0x62)
myLcd.setColor(0, 255 , 0) 
                                                                                
print "Esperando Interrupcao..."                                                
while(1):                                                                       
        time.sleep(1)                                                           
#FIM WHILE                                                                      

# release                                                                       
#myUln200xa.release()                                                
# exitHandler is called automatically 

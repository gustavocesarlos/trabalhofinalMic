import socket
import cv2
import numpy
import time, sys, signal, atexit
import pyupm_i2clcd as lcd
import mraa
import pyupm_uln200xa as upmULN200XA
 
# Variaveis para armazenar IP e porta de comunicacao
TCP_IP = '' # campo vario - vincula a todos os ips que a maquina possui na rede
TCP_PORT = 5052
 
# Criacao do socket de comunicacao para servidor
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Vincula o socket de servidor com o IP e Porta. IP = '' - rede
serverSocket.bind((TCP_IP,TCP_PORT))
# Habilita que socket de servidor ira escutar requisicoes
serverSocket.listen(True)

#Funcao para interrupcao: Abre o portao
def abrePortao(args):
        #Setando a velocidade e a direcao do motor:
        myUln200xa.setSpeed(5) # 5 RPMs, eh a velocidade de rotacao do motor
        myUln200xa.setDirection(upmULN200XA.ULN200XA.DIR_CW) #sentido horario
        
        #Para escrever no lcd e fazer o motor rodar
        myLcd.clear()
        myLcd.setCursor(0,0)
        myLcd.write("Abrindo o portao...")
        myUln200xa.stepperSteps(600)    #setando os passos do motor. Nessa forma, o motor dara 3 voltas complets
        myLcd.clear()
        myLcd.setCursor(0,0)
        myLcd.write("Portao aberto.")

        time.sleep(1) #programa "dorme" por 1 segundo
##Fim abrePortao

#Funcao para interrupcao: Fecha o portao
def fechaPortao(args):
        #Setando a velocidade e a direcao do motor:
        myUln200xa.setSpeed(5) # 5 RPMs, eh a velocidade de rotcao do motor
        myUln200xa.setDirection(upmULN200XA.ULN200XA.DIR_CCW) #sentido anti-hora

        #Para escrever no lcd e fazer o motor rodar
        myLcd.clear()
        myLcd.setCursor(0,0)
        
	myLcd.write("Fechando o portao...")
	myUln200xa.stepperSteps(600)
        myLcd.clear()
        myLcd.setCursor(0,0)
        myLcd.write("Portao fechado.")
        
        time.sleep(1)    #programa "dorme" por 1 segundo

# Instantiate a Stepper motor on a ULN200XA Darlington Motor Driver             
# This was tested with the Grove Geared Step Motor with Driver                  
                                                                                
# Instantiate a ULN2003XA stepper object
#Os passos padroes do motor eh o primeiro parametro (4096).
#8, 9, 10 e 11 sao os pinos da Edison utilizados
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
                                                                                
y = mraa.Gpio(3)        #Setando pino 1                                         
y.dir(mraa.DIR_IN)      #Setando como INPUT                                     
y.isr(mraa.EDGE_BOTH, fechaPortao, fechaPortao)  #setando a interrupcao. Ao apertar o botao, chamara a funcao fechaPortao  

#Inicializando o lcd
myLcd = lcd.Jhd1313m1(0, 0x3E, 0x62)
myLcd.setColor(0, 255 , 0) 
# Cria objeto de captura vinculado a device 0 - webcam
capture = cv2.VideoCapture(0)

#print "Default resolution: ( " + str(video_capture.get(3)) + " x " + str(video_capture.get(4)) + " )"
capture.set(3, 176)
capture.set(4, 144)
#print "Resolution set to: ( " + str(video_capture.get(3)) + " x " + str(video_capture.get(4)) + " )"
# Captura um quadro para verificar conexao
ret, frame = capture.read()
 
# Parametrizacao da codificacao de imagem a ser transmitirda
encode_param = [int(cv2.IMWRITE_JPEG_QUALITY),90]
 
print 'Aguardando conexoes...'
# Aguarda conexao com cliente e cria objeto "conn" - socket
conn, add = serverSocket.accept()
while ret:
    # codifica o quadro de imagem em formato jpg e grava em imgencode
    result, imgencode = cv2.imencode('.jpg', frame, encode_param)
    # tranforma imgencode em vetor - serializacao
    data = numpy.array(imgencode)
    # converte o vetor em string
    stringData = data.tostring()
    # Envia comprimento do quadro de imagem, com 16 caracteres justificado a esquerda
    conn.send(str(len(stringData)).ljust(16));
     # Envia quadro de imagem serializado em string
    conn.send(stringData)
    # Realiza leitura de quadro da webcam, grava em frame
    ret,frame = capture.read()
# Encerra conexao com camera usb - webcam
capture.release()
# Encerra motor
myUln200xa.release()
# Encerra o socket de comunicacao
serverSocket.close()

import cv2
import numpy
import socket
import os
from wamedia import*
from media2 import credential, Answer
#############
TCP_IP = ''
TCP_PORT = 5052
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSocket.bind((TCP_IP,TCP_PORT))
serverSocket.listen(True)

video_capture = cv2.VideoCapture(0)

print "Default resolution: ( " + str(video_capture.get(3)) + " x " + str(video_capture.get(4)) + " )"
video_capture.set(3, 176)
video_capture.set(4, 144)
print "Resolution set to: ( " + str(video_capture.get(3)) + " x " + str(video_capture.get(4)) + " )"

cascadePath = '/home/root/haarcascade_frontalface_alt.xml'
faceCascade = cv2.CascadeClassifier(cascadePath)

## encode_param = [int(cv2.IMWRITE_JPEG_QUALITY),40]
 
print '#IntelMaker'
print 'Tudo pronto, aguardando conexoes...'

conn, add = serverSocket.accept()
    

while True:
	
	encode_param = [int(cv2.IMWRITE_JPEG_QUALITY),90]	
	# capturar de quadro em quadro
	ret, frame =  video_capture.read()
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

	faces = faceCascade.detectMultiScale(gray, 1.3, 5)
	
	#if len(faces)>0:
		#cv2.imwrite('saida.png', frame)
	print "Encontrei {0} Rostos" .format(len(faces))

	# Desenhar retangulo em volta do rosto
	for (x,y,w,h) in faces:
		cv2.rectangle(frame, (x,y), (x+w, y+h), (0,255,0), 2)
		roi_gray = gray[y:y+h, x:x+w]
		roi_color = frame[y:y+h, x:x+w]

	if len(faces)>0:                                                        
                cv2.imwrite('saida.png', frame)
		os.system("yowsup-cli demos -s 55XXXXXXXXXXX \"Sua casa esta sendo invadida\" -c whatsapp.config")
		stack = SendMediaStack(credential(), [(["55XXXXXXXXXXX”, "saida.png"])])
            	stack.start()
		
	# Transformar imagem tratada em pacote e enviar

	result, imgencode = cv2.imencode('.jpg',frame, encode_param)
	data = numpy.array(imgencode)
	stringData = data.tostring()
	conn.send(str(len(stringData)).ljust(16));
	conn.send(stringData)

# Desliga a camera USB
video_capture.release()

# encerra o socket de comunicacao
serverSocket.close()

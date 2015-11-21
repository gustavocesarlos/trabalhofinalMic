import socket
import cv2
import numpy
 
# Variaveis para armazenar IP e porta de comunicacao
TCP_IP = '' # campo vario - vincula a todos os ips que a maquina possui na rede
TCP_PORT = 5052
 
# Criacao do socket de comunicacao para servidor
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Vincula o socket de servidor com o IP e Porta. IP = '' - rede
serverSocket.bind((TCP_IP,TCP_PORT))
# Habilita que socket de servidor ira escutar requisicoes
serverSocket.listen(True)
 
# Cria objeto de captura vinculado a device 0 - webcam
capture = cv2.VideoCapture(0)
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
# Encerra o socket de comunicacao
serverSocket.close()

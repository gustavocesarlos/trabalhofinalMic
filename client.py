# Esse código é o cliente usado nas aplicações com camera

import cv2
import numpy
import socket

# Rotina recvall - trata de receber informacao
def recvall(sock, count):
    buf = b''
    while count:
        newbuf = sock.recv(count)
        if not newbuf: return None
        buf += newbuf
        count -= len(newbuf)
    return buf

# Atribui IP da estacao servidora - Intel Edison
TCP_IP = ''
# Porta de comunicacao
TCP_PORT = 5052

# Cria objeto socket para comunicacao
conn = socket.socket()

# Faz conexao com estacao servidora
conn.connect((TCP_IP,TCP_PORT))

# Loop infinito: Recebe imagem, exibe. Se digitar q - sai.
while True:
    # Recebe tamanho da imagem
    length = recvall(conn,16)
    # Recebe imagem propriamente
    stringData = recvall(conn, int(length))
    # Recupera a imagem serializada em forma de string
    data = numpy.fromstring(stringData, dtype='uint8')
    # Decodifica a imagem
    decimg=cv2.imdecode(data,1)
    # Exibe a imagem
    cv2.imshow('EdisonCAM',decimg)
    # Se digitar 'q', encerra.
    if(cv2.waitKey(1) & 0xFF == ord('q')):
        break

# Fecha as janelas do OpenCV
cv2.destroyAllWindows()
# Encerra o socket
conn.close()

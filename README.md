#Desenvolvedores

* Gustavo Cesar Leite de Oliveira Santos RA: 558311
* Rodolfo Barcelar RA: 495921

# Trabalho Final Microcontroladores e Aplicações - 2015/s2

Este trabalho foi desenvolvido como parte da ementa da disciplina Microcontroladores e Aplicações.

Assim, este trabalho simula o uso de uma câmera de segurança para portões, ou seja, com o auxilio de uma filmadora, estaremos captando as imagens para que se possa fazer o reconhecimento de rostos humanos. Utilizamos uma placa da Intel chamada Edison para fazer o reconhecimento, e com o auxílio de uma rede de Internet, podemos enviar ao usuário uma foto da imagem captada.
Como dito anteriormente, este trabalho possui dois módulos.

No módulo 1, o monitoramento ocorre quando o usuário se encontra fora de casa. É feito o reconhecimento de rostos e, então, uma imagem é capturada e enviada via mensageiro eletrônico. As imagens vão sendo capturadas e enviadas sequencialmente até que a câmera não detecte mais rostos.
No módulo 2, o monitoramento ocorre quando o usuário está dentro de casa. Uma pessoa toca uma campainha e o usuário inicia a câmera para ver quem está tocando a campainha. E apertando um botão pode destravar o seu portão, que no caso é um motor de passo. Também existe um sensor no portão que detecta o fechamento do portão, ativando o motor de passo no sentido contrário, trancando o portão. Esse sensor será simulado por um botão.

O funcionamento desse motor de passo simulará a abertura de um portão. O motor de passo será acionado em um sentido e, ao terminar, funcionará no sentido inverso, simulando o fechamento do portão.

Para um melhor entendimento, veja os códigos contidos neste repositório, juntamente com os comentários inseridos nos códigos.

#Motor de Passo
Nesta parte do projeto, foi-se implementado um código (vide MotorDePasso.py) juntamente com um hardware para o funcionamento de um motor de Passo. Para tal, foram usados um protoboard, um chip ULN 2003, para que as ligações do motor sejam feitas de forma direta, e uma fonte de tensão de 5 Volts. Veja, nas figuras abaixo, como ocorreram as ligações, principalmente no que diz respeito ao motor com seus fios.

![Ligações do Motor de Passo com a fonte](https://github.com/gustavocesarlos/trabalhofinalMic/blob/master/Fotos%20e%20V%C3%ADdeos/20151202_144915.jpg)

![Ligação dos fios do motor ao chip UNL2003](https://github.com/gustavocesarlos/trabalhofinalMic/blob/master/Fotos%20e%20V%C3%ADdeos/20151202_144958.jpg)

Na pasta fotos e vídeos você poderá encontrar vídeos sobre o funcionamento do motor.

Implementado o motor, foi inserido dois botões para simular a abertura e fechamento do portão. Através desses dois botões, podemos criar interrupções para que, ao apertado, o portão seja aberto ou fechado (vide MotorDePasso.py).

Na pasta fotos e vídeos você poderá encontrar vídeos sobre o funcionamento do motor com interrupções.

#O Projeto

A seguir, uma foto do nosso projeto completo e funcionando, ou seja, servidor, cliente, camera para filmagem e captura de rostos, motor de passo, LCD, 2 botões e whatsapp funcionando corretamente:

![](https://github.com/gustavocesarlos/trabalhofinalMic/blob/master/Fotos%20e%20V%C3%ADdeos/20151204_165742.jpg)

Como já mencionado, os seguintes componentes são utilizados:

Placa Intel Edison;

Motor de passo simples, juntamente com o microcontrolador uln2003 para que as ligações sejam feitas;

Dois botões já inclusos no kit Intel Edison para ocasionar interrupções e, assim, abrir ou fechar o portão;

Um LCD, também incluso no kit Intel Edison;

Uma webcam para fazer a captura de vídeos e, também, a captura de imagens;

Um aplicativo whatssapp configurado para receber as imagens capturadas pela câmera;

Uma fonte de tensão contínua de 5 Volts.

Para ver nosso projeto funcionando, há vídeos na pasta Fotos e Vídeos mostrando o funcionamento. Como dito anteriormente, há duas maneiras diferentes de fazer o projeto funcionar.

### Modo 1

No primeiro modo, a câmera irá funcionar captando imagens do ambiente. Posicionada corretamente, ela irá captar rostos, capturar imagens e enviar essas imagens para o whatsapp configurado. Isso é feito utilizando sockets, código programado em python, e uma rede de internet. A qualidade de imagem e velocidade de resposta da webcam depende da conexão local. Uma conexão ruim gera imagens e um vídeo muito lento. A seguir, uma imagem demonstrando o envio duma imagem gerada e enviada para whatsapp. Observe o retângulo envolta da face. Posteriormente, explicaremos o que acontece:

![](https://github.com/gustavocesarlos/trabalhofinalMic/blob/master/Fotos%20e%20V%C3%ADdeos/rpovTWzy.jpg)

Para a execução desse modo, deverá ser executado o código detect3.py, que funcionará como servidor, e o arquivo client.py, que será o cliente. Nesse modo, o cliente se conectará ao servidor e, então, a câmera começará a detectar as imagens. Quando encontrar um rosto, uma foto será gerada e salvada como um arquivo de imagem. Este arquivo é o que será enviado para o whatapp configurado. Abaixo, alguns códigos para explicar melhor o funcionamento deste modo:

* detect3.py

```python
encode_param = [int(cv2.IMWRITE_JPEG_QUALITY),90]	
	# capturar de quadro em quadro
	ret, frame =  video_capture.read()
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

	faces = faceCascade.detectMultiScale(gray, 1.3, 5)
```

o código acima é o responsável por iniciar a câmera, ou seja, a captura de imagens e, além disso, iniciar a detecção de faces. 

```python
for (x,y,w,h) in faces:
		cv2.rectangle(frame, (x,y), (x+w, y+h), (0,255,0), 2)
		roi_gray = gray[y:y+h, x:x+w]
		roi_color = frame[y:y+h, x:x+w]

	if len(faces)>0:                                                        
                cv2.imwrite('saida.png', frame)
		os.system("yowsup-cli demos -s 55XXXXXXXXXXX \"Sua casa esta sendo invadida\" -c whatsapp.config")
		stack = SendMediaStack(credential(), [(["55XXXXXXXXXXX”, "saida.png"])])
            	stack.start()
```
O código acima é responsável por formar um retângulo em volta de um rosto, quando um é encontrado. Dessa forma, temos um indicativo de que uma face foi encontrada e que uma imagem foi gerada. Inclusive, na imagem salva, este retângulo estará presente, delimitando o rosto capturado.

```python
result, imgencode = cv2.imencode('.jpg',frame, encode_param)
	data = numpy.array(imgencode)
	stringData = data.tostring()
	conn.send(str(len(stringData)).ljust(16));
	conn.send(stringData)
```

E, finalmente, temos a parte do código responsável por enviar a imagem para o cliente. Observe que é necessário a formulação de um pacote, ou seja, a imagem é convertida em um vetor de string e este, por sua vez, será enviado pela conexão entre o cetect3.py e o client.py.

* client.py

Este código não tem nenhum segredo. Ele, basicamente, recebe o pacote gerado por detect3.py, o decodifica, uma vez que o pacote recebido é um vetor de strings, e então gera a imagem e a exibe:
```python
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
```
Apenas atente-se que, para sair do programa, basta digitar a letra "q".

* wamedia.py e whatsapp.config

Estes são os dois arquivos referentes à configuração do whatsapp que deve ser feita anteriormente à execução dos arquivos detect.py e cliente.py, para configurar o whatsapp que receberá as imagens e, também, como será a recepção e o salvamento da imagem que será enviada para o mesmo.

```python
cc=55
mcc=724
mnc=04
phone=55XXXXXXXXXXX
id=0000000000
password=VDdLcMfAkKV+TPxNOv+cRIoC7/M=
```
Este é o código do arquivo whatsapp.config. Observe o campo "phone". É neste campo que deve ser inserido o número de telefone para o qual receberá as imagens. 

### Modo 2

No segundo modo, novamente temos a webcam capturando as imagens do ambiente, mas, agora, um usuário poderá visualizar a imagem e, se quiser, apertar um botão para abrir ou fechar um portão, simulado pelo motor de passos. Executando o arquivo server.py e client.py, a câmera será iniciada, filmando o ambiente. Este programa ficará apenas captando imagens. Caso o usuário aperte algum botão, uma mensagem será msotrada no LCD correspondente à abertura ou fechamento do portão. Ao mostrar essa mensagem, o motor será acionado e, novamente, o LCD mostrará a condição em que se encontra o portão ("Aberto" ou "Fechado"). Para que o portão seja fechado, basta apertar o outro botão, correspondente ao fechamento do portão, ou seja, o motor de passos girará no sentido contrário ao da abertura. A seguir, a parte do código que corresponde à abertura e fechamento do portão, justamente com o acionamento do LCD:

```python
def fechaPortao(args):

        myUln200xa.setSpeed(5) # 5 RPMs, eh a velocidade de rotcao do motor
        myUln200xa.setDirection(upmULN200XA.ULN200XA.DIR_CCW) #sentido anti-hora


        myLcd.clear()
        myLcd.setCursor(0,0)
        
	myLcd.write("Fechando o portao...")
	myUln200xa.stepperSteps(600)
        myLcd.clear()
        myLcd.setCursor(0,0)
        myLcd.write("Portao fechado.")
        
        time.sleep(1)    #programa "dorme" por 1 segundo
```

```python
def abrePortao(args):

        myUln200xa.setSpeed(5) 
        myUln200xa.setDirection(upmULN200XA.ULN200XA.DIR_CW) 
        
        myLcd.clear()
        myLcd.setCursor(0,0)
        myLcd.write("Abrindo o portao...")
        myUln200xa.stepperSteps(600)    
        myLcd.clear()
        myLcd.setCursor(0,0)
        myLcd.write("Portao aberto.")
        time.sleep(1)
```

Observe que foram utilizadas funções para tal. Como mencionado anteriormente, o acionamento dos botões gera uma interrupção no programa, não afetando a captura de imagens. De acordo com o botão acionado, a interrupção levará o programa a executar a função correspondente. Para maiores detalhes de código e de ligações, vide client.py, server.py e a pasta Fotos e Vídeos. 

A foto a seguir mostra os botões, o LCD, o arduino e os fios em suas ligações:
![](https://github.com/gustavocesarlos/trabalhofinalMic/blob/master/Fotos%20e%20V%C3%ADdeos/20151204_165738.jpg)

A foto a seguir mostra o uso do chip uln2003 para o correto funcionamento do motor de passo:
![](https://github.com/gustavocesarlos/trabalhofinalMic/blob/master/Fotos%20e%20V%C3%ADdeos/20151204_165703.jpg)

E, a seguir, o uso de uma fonte, com uma tensão fixa de 5 Volts e corrente fixa de 3 Ampères:
![](https://github.com/gustavocesarlos/trabalhofinalMic/blob/master/Fotos%20e%20V%C3%ADdeos/20151204_165752.jpg)

## Algumas Observações
* O nosso código foi desenvolvido passo a passo. Por exemplo, no modo 2, primeiro desenvolveu-se um código para o LCD, depois um código para o motor de passos e, por fim, o programa servidor. Ao terminar o programa servidor, todos esses três códigos foram unidos, gerando o código final. Para visualizar os códigos referentes a alguns desses passos, vide os códigos postados, como o lcd.py e o MotorDePasso.py.
* Aconselhamos não utilizar um número comum, uma vez que as configurações padrões do aplicativo serão modificados. Em nossos experimentos, utilizamos um chip telefônico em desuso para os testes, uma vez que seria necessário a desinstalação e reinstalação do aplicativo em seu telefone para que o mesmo volte às configurações iniciais.
* O arquivo haarcascade_frontalface_alt.xml faz parte da bilbioteca openCV e é responsável pela detecção de faces quando a câmera estiver ativa. Uma parte do código detect3.py faz uso deste arquivo, e foi especificado no tópico Modo 1, detect3.py.
* A biblioteca utilizada para a configuração do whatsapp, yowsup, deve estar atualizada juntamente com a última versão do aplicativo. Caso o aplicativo for atualizado e a biblioteca não, então o envio da imagem não será possível, mas o salvamaneto da imagem ocorrerá sempre.

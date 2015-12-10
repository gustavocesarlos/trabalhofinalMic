# Trabalho Final Microcontroladores e Aplicações - 2015/s2

Este trabalho foi desenvolvido como parte da ementa da disciplina Microcontroladores e Aplicações.

Assim, este trabalho simula o uso de uma câmera de segurança para portões, ou seja, com o auxilio de uma filmadora, estaremos captando as imagens para que se possa fazer o reconhecimento de rostos humanos. Utilizamos uma placa da Intel chamada Edison para fazer o reconhecimento, e com o auxílio de uma rede de Internet, podemos enviar ao usuário uma foto da imagem captada.
Como dito anteriormente, este trabalho possui dois módulos.

No módulo 1, o monitoramento ocorre quando o usuário se encontra fora de casa. É feito o reconhecimento de rostos e, então, uma imagem é capturada e enviada via mensageiro eletrônico. As imagens vão sendo capturadas e enviadas sequencialmente até que a câmera não detecte mais rostos.
No módulo 2, o monitoramento ocorre quando o usuário está dentro de casa. Uma pessoa toca uma campainha que é simulada por um beep eletrônico, o usuário inicia a câmera para ver quem está tocando a campainha. E apertando um botão pode destravar o seu portão, que no caso é um motor de passo. Também existe um sensor no portão que detecta o fechamento do portão, ativando o motor de passo no sentido contrário, trancando o portão. Esse sensor será simulado por um botão.

Nos dois módulos, o usuário poderá ou não acionar um motor de passo implementado à placa através de um botão. O funcionamento desse motor simulará a abertura de um portão. O motor de passo será acionado em um sentido e, ao terminar, funcionará no sentido inverso, simulando o fechamento do portão.

Para um melhor entendimento, veja os códigos contidos neste repositório, juntamente com os comentários inseridos nos códigos.

#Motor de Passo
Nesta parte do projeto, foi-se implementado um código (vide MotorDePasso.py) juntamente com um hardware para o funcionamento de um motor de Passo. Para tal, foram usados um protoboard, um chip ULN 2003 para que as ligações do motor seja feita de forma direta e uma fonte de tensão de 5 Volts. Veja, nas figuras abaixo, como ocorreram as ligações, principalmente no que diz respeito ao motor com seus fios.

![Ligações do Motor de Passo com a fonte](https://github.com/gustavocesarlos/trabalhofinalMic/blob/master/Fotos%20e%20V%C3%ADdeos/20151202_144915.jpg)

![Ligação dos fios do motor ao chip UNL2003](https://github.com/gustavocesarlos/trabalhofinalMic/blob/master/Fotos%20e%20V%C3%ADdeos/20151202_144958.jpg)

Na pasta fotos e vídeos você poderá encontrar vídeos sobre o funcionamento do motor.

Implementado o motor, foi inserido dois botões para simular a abertura e fechamento do portão. Através desses dois botões, pudemos criar interrupções para que, ao apertado, o portão seja aberto ou fechado (vide MotorDePasso.py).

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

* ### Modo 1

No primeiro modo, a câmera irá funcionar captando imagens do ambiente. Posicionada corretamente, ela irá captar rostos, capturar imagens e enviar essas imagens para o whatsapp configurado. Isso é feito utilizando sockets, código programado em python, e uma rede de internet. A qualidade de imagem e velocidade de resposta da webcam depende da conexão local. Uma conexão ruim gera imagens e um vídeo muito lento.

* ### Modo 2

No segundo modo, novamente temos a webcam capturando as imagens do ambiente, mas, agora, um usuário poderá visualizar a imagem e, se quiser, apertar um botão para abrir ou fechar um portão, simulado pelo motor de passos. Executando o arquivo server.py e cliente.py, a câmera será iniciada, filmando o ambiente. Este programa ficará apenas captando imagens. Caso o usuário aperte algum botão, uma mensagem será msotrada no LCD correspondente à abertura ou fechamento do portão. Ao mostrar essa mensagem, o motor será acionado e, novamente, o LCD mostrará a condição em que se encontra o portão ("Aberto" ou "Fechado"). Para que o portão seja fechado, basta apertar o outro botão, correspondente ao fechamento do portão, ou seja, o motor de passos girará no sentido contrário ao da abertura. A seguir, a parte do código que corresponde à abertura e fechamento do portão, justamente com o acionamento do LCD:

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

Observe que foram utilizadas funções para tal. Como mencionado anteriormente, o acionamento dos botões gera uma interrupção no programa, não afetando a captura de imagens. De acordo com o botão acionado, a interrupção levará o programa a executar a função correspondente. Para maiores detalhes de código e de ligações, vide cliente.py, server.py e a pasta Fotos e Vídeos. 

#Desenvolvedores
Gustavo Cesar Leite de Oliveira Santos RA: 558311

Rodolfo Barcelar RA: 495921

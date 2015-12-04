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

#Desenvolvedores
Gustavo Cesar Leite de Oliveira Santos RA: 558311

Rodolfo Barcelar RA: 495921

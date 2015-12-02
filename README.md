# trabalhofinalMic

Este trabalho foi desenvolvido como parte da ementa da disciplina Microcontroladores e Aplicações.

Assim, este trabalho simula o uso de uma câmera de segurança para portões, ou seja, com o auxilio de uma filmadora, estaremos captando as imagens para que se possa fazer o reconhecimento de rostos humanos. Utilizamos uma placa da Intel chamada Edison para fazer o reconhecimento, e com o auxílio de uma rede de Internet, podemos enviar ao usuário uma foto da imagem captada.
Como dito anteriormente, este trabalho possui dois módulos.

No módulo 1, o monitoramento ocorre quando o usuário se encontra fora de casa. É feito o reconhecimento de rostos e de olhos e, então, uma imagem é capturada e enviada via mensageiro eletrônico com o auxílio de uma rede de Internet ao usuário.
No módulo 2, o monitoramento ocorre quando o usuário está dentro de casa. Uma pessoa toca uma campainha que é simulada por um beep eletrônico, o usuário inicia a câmera para ver quem está tocando a campainha.

Nos dois módulos, o usuário poderá ou não acionar um motor de passo implementado à placa através de um botão. O funcionamento desse motor simulará a abertura de um portão. O motor de passo será acionado em um sentido e, ao terminar, funcionará no sentido inverso, simulando o fechamento do portão.

#Videos e Imagens
Imagens das ligações do motor sem botões e posterior vídeo mostrando seu funcionamento

file:///home/enc2012/rodolfo.barcelar/Desktop/20151202_144915.jpg

file:///home/enc2012/rodolfo.barcelar/Desktop/20151202_144958.jpg

file:///home/enc2012/rodolfo.barcelar/Desktop/20151202_145305.mp4

A seguir, um video mostrando o funcionamento do motor através de interrupções, e com o uso de dois botões:

file:///home/enc2012/rodolfo.barcelar/Desktop/20151202_163022.mp4

#Desenvolvedores
Gustavo Cesar Leite de Oliveira Santos RA: 558311

Rodolfo Barcelar RA: 495921

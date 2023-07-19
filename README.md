# FloodGet
Flood de solicitações HTTP (Script Simples)

Script simples que envia solicitações TCP
infinitamente a um servidor alvo.
Ao ser iniciado você deve fornecer o IP do serv
alvo e a porta que sera utilizada.

(IMPORTANTE!)
CASO VOCÊ ESCOLHA UMA PORTA QUE ESTA FECHADA, O
PROGRAMA FICARÁ "PARADO" APÓS INSERIR OS DADOS (IP, PORTA)
ENTÃO CERTIFIQUE-SE DE QUE A PORTA SELECIONADA ESTEJA ABERTA

Em seguida, o programa criara um socket e enviara para 
o servidor alvo em um laço de repetição infinito (While)

Embora não seja considerado uma ataque DoS, os sockets enviados no
são fechados corretamente, oque pode causar uma sobrecarga os recursos do
site e causar indisponibilidade.

Como já falei, é um script simples e eu ainda sou um estudante, então 
caso tenha algo errado no meu código me avisem!

# FloodGet
**Flood de solicitações HTTP GET**

Script simples que envia solicitações TCP
infinitamente a um servidor alvo.
Ao ser iniciado você deve fornecer o IP do servidor
alvo e a porta que sera utilizada.

**(Importante!)**

**Caso você escolha uma porta que esteja fechada, o programa ficará "parado" ou dará um erro de conexão recusada após inserir os dados (IP, Porta). Então certifique-se de que a porta selecionada esteja aberta.**

Em seguida, o programa criara um socket e enviara para 
o servidor alvo em um laço de repetição infinito (While)

Embora não seja considerado uma ataque DoS, os sockets enviados no
são fechados corretamente, oque pode causar uma sobrecarga os recursos do
site e causar indisponibilidade.

É um script simples e eu ainda sou um estudante, então 
caso tenha algo errado no meu código me avisem!

# Linux / Termux
```Python
git clone https://github.com/MirrorWF/FloodGet
cd FloodGet
python3 FLOODGET.py

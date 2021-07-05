# TrabalhoRedes

#Trabalho foi feito em 2 arquivos, onde no servidor.py são dados os comando para criar a conexão em si, assim o servidor fica em modo listening e cria uma nova thread, que permanece ativa até que o cliente se desconecte com a mensagem quit, se a mensagem for diferente, o servidor pega a mensagem que recebeu e devolve para o cliente, sendo assim um servidor de echo.

#Detalhamento e explicação de blocos funcionais estão comentados no código.

#Trabalho foi desenvolvido no VisualStudio Code usando a linguagem python 3, para a execução é necessário alguma IDE que entenda python, pois os arquivos são .py

#Para a execução dos arquivos basta abrir primeiro o servidor.py pelo prompt, digitando seu caminho, uma vez na pasta basta digitar python3 server.py, se for no visualCode, é só executar o arquivo, ou o comando python3 server.py no prompt do VSC.

#Com o servidor conectado, deve-se abrir outro prompt e ir na pasta onde está o client.py, uma vez na pasta, o cliente se conecta com o seguinte comando, que possui 4 argumentos, a linguagem python3, a pasta client.py, o nome do cliente, que pode ser qualquer um, e o servidor, que foi chamado de localhost, com isso o cliente se conectará ao servidor.
Ex: "python3 client.py henrique localhost".Isso pode se repetir quantas vezes quiser, basta só abrir outro prompt e mudar o nome do client, para terminar a conexão basta digitar "quit" no terminal do cliente e depois matar o prompt.

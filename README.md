# docassemble-server-setup
###Arquivos de configuração do servidor docassemble

Essa instalação simplificada do Docassemble configura as variáveis essenciais usadaas na instalação e foi feita para Ubuntu Server 18.04.

Ela deve funcionar sem maiores problemas em outras versões do Ubuntu.

Com o usuário **root**:

1. Clone o repositório no local se sua preferência.
2. Acesse a pasta do repositório e digite:

```
$ python3 docassemble_setup.py
```
Assim que perguntado:

3. Digite o domínio do seu servidor com subdomínio (e.g. docassemble.meusitesensacional.com.br)
4. Digite o e-mail do administrador do sistema. Se você está seguindo esse tutorial, provavelmente você é o adminstrador do sistema :)

Após a execução completa do script, o container do Docassemble será criado.

Para verificar se o container está em execução:

```
$ docker ps 
```

Você deverá ver a seguinte mensagem:

```
6c3475a13664 jhpyle/docassemble:latest "/usr/bin/supervisor…" 5 minutes ago Up About a minute 0.0.0.0:80->80/tcp, 25/tcp, 465/tcp, 514/tcp, 4369/tcp, 5432/tcp, 5671-5672/tcp, 6379/tcp, 8080-8082/tcp, 9001/tcp, 25672/tcp, 0.0.0.0:443->443/tcp docassemble
```

O container pode levar vários minutos até estar completamente configurado e disponível para uso.

Se você desejar acompanhar o que está ocorrendo dentro do container digite:

```
docker logs -f docassemble
```

Você verá o log do container em andamento. Enquanto você não visualisar as linhas:

```
2020-08-02 19:02:17,036 INFO success: uwsgi entered RUNNING state, process has stayed up for > than 15 seconds (startsecs)
2020-08-02 19:02:17,214 INFO spawned: 'nginx' with pid 1380
```

O container não estará disponível.

Após o término da instalação acesse o endereço do servidor, preenchido no passo **3**.

No primeiro acesso, use:

Email: admin@admin.com
Password: password

A senha deverá ser trocada no primeiro acesso. 

Seu servidor do Docassemble está prontinho para uso!



# docassemble-server-setup
###Arquivos de configuração do servidor docassemble

Essa instalação simplificada do Docassemble configura as variáveis essenciais usadaas na instalação e foi feita para Ubuntu Server 18.04.

Ela deve funcionar sem maiores problemas em outras versões do Ubuntu.

Com o usuário **root**

1. Clone o repositório no local se sua preferência.
2. Acesse a pasta do repositório e digite:

```
$ python3 docassemble_setup.py
```
3. Digite o domínio do seu servidor com subdomínio (e.g. docassemble.meusitesensacional.com.br)
4. Digite o e-mail do administrador do sistema. Se você está seguindo esse tutorial, provavelmente você é o adminstrador do sistema :)
5. Acesse a pasta docassemble_generator_server
6. Digite:
```
$ make run 
```

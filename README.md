# API de Validação para Registros Nacionais
Desenvolvimento de uma API Restful em Flask para validação de registros nacionais (CEP, RG, CPF e CNPJ)

## Pré-requisitos

- [Python](http://www.python.org/ "Python")
- [Postman](https://www.postman.com/ "Postman")
- Interpretador de texto à sua escolha ([VS Code](https://code.visualstudio.com/ "VS Code"), [PyCharm](https://www.jetbrains.com/pt-br/pycharm/ "PyCharm"), etc)

## Iniciando a aplicação

### Clonando o Repositório
Comece o projeto clonando este repositório. Na sua pasta de preferencia, abra o BASH e digite:

`git clone https://github.com/Anderson-Couto/API-Flask_RegistrosNacionais.git`

### Criando o Ambiente Virtual
Dentro do seu diretório clonado, crie um ambiente virtual para a instalação dos pacotes.

`pip install virtualenv`

Selecione um nome para a sua virtualenv. Para o exemplo, usaremos **venv**

`virtualenv venv`

Agora, acesse o seu ambiente virtual com o comando:

`venv\Scripts\activate`

### Instalando os Pacotes
Dentro do seu ambiente virtual, digite:

`pip install -r requirements.txt`

### Acessando o Servidor
Execute o arquivo **run_restful.py**. Se não existirem erros, já terá acesso à aplicação.

## Executando a API
Com o Postman aberto, acesse a url de desejo, de acordo com o documento a ser validado, enviando os dados no formato JSON. Se estiver tudo em ordem, o retorno será um JSON com o dado formatado e validado. Se nao estiver de acordo, aparecerá uma mensagem de erro.

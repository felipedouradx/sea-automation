# SEA -  Test Automation Challenge - Python

## Informações Iniciais
Para execução dos testes é necessário instalar os seguintes recursos:
* Behave
* Docker
* Selenium
* VncViewer(opcional)

## Descrição
Execução de testes funcionais utilizando Behave, Selenium e Python.

## Utilização
A automação permite a execução de toda a suite de testes, sendo possível também a execução de forma individual ou
através de TAG's (para uso de determinado filtro). De acordo com os seguintes parâmetros:

* All-tests:

    
    behave -D browser=chrome -D headless=false -D remote=false -D base_url=sea -D device=desktop -f allure_behave.formatter:AllureFormatter -o allure-results ./features

* TAG's:

Para executar os testes utilizando uma tag, basta informá-la diretamente na feature(@example) e fazer a seguinte 
indicação na linha de comando.

    behave --tags=@example


Os testes podem ser executados em ambiente local e/ou remoto. Outras opções como, seleção do browser, seleção de 
ambiente, seleção de dispositivo e o modo headless, podem ser definidas através dos seguintes parâmetros:

* Remoto:

Tendo em conta a instalação do docker, vá até a pasta do projeto e execute o comando a seguir para a inicialização 
do serviço:
        
    docker-compose up --build

Desse modo, os serviços serão iniciados de acordo com as configurações do selenium hub e seus nós, dispostos no arquivo 
docker-compose.yml localizado na raiz do projeto.

Para verificar o status dos serviços basta utilizar o código a seguir:
    
    docker-compose -ps

Durante a execução dos testes é possível monitorar todos os processo através do Selenium Grid, tais como o status da 
operação, execução simultânea do driver nos navegadores e concorrência de testes em fila. Para isso, basta
acessar o seguinte endereço:

    http://localhost:4444/

Outro recurso disponível em ambiente remoto é a visualização da automação através das portas configuradas de acordo com
o browser em questão, podendo ser utilizado através de um software (ex: VncViewer).

Após subir o ambiente remoto basta iniciar o VncViewer informando a porta do browser desejado e a senha de acesso.
Por exemplo:
    
    localhost:    5901
    senha:      secret

Por padrão os nós são configurados da seguinte forma:

    Google Chrome:      localhost:5901
    Mozilla Firefox:    localhost:5902
    Microsoft Edge:     localhost:5903
    senha:                      secret

Podendo ser gerenciados no arquivo docker-compose.yml na raiz do projeto.

Após a execução dos testes em ambiente remoto os serviços permanecerão ativos, para finalizar a sessão no docker 
basta executar o seguinte código:

    docker-compose down


* Browser:

A automação oferece suporte para os principais browser's: Google Chrome, Mozilla Firefox e Microsoft Edge.
Para indicar o navegador desejado, basta adicionar o argumento ao comando de execução. De acordo com o exemplo abaixo:

        -D browser=chrome

Assim, podendo apenas substituir o nome do navegador de acordo com o interesse em questão. Para a execução através de 
uma IDE basta indicar a variável no arquivo 'behave.ini';


* Headless:

O modo headless pode ser utilizado da seguinte forma:

        -D headless=true

Por padrão a execução dos testes é definida em ambiente local, utilizando o navegador Google Chrome no modo headless.


## Reports
A partir da integração do Allure ao projeto é possível gerar relatórios detalhados de cada teste, incluindo detalhes de
cada step com a geração da evidência (screenshot), para fácil controle e manutenção do código.

Para gerar os relatórios é necessário adicionar os seguintes parâmetros ao comando de execução dos testes:

    allure_behave.formatter:AllureFormatter -o allure-results

Como o exemplo a seguir:

    behave -D browser=chrome -D headless=false -D remote=false -D base_url=sea -D device=desktop -f allure_behave.formatter:AllureFormatter -o allure-results ./features

Onde temos a chamada do behave e os argumentos seguidos da referência -D para seleção do browser, modo
headless, ambiente remoto, o dispositivo e a seleção URL para o teste em questão, junto com a referência do Allure e o diretório 
das features.

Após a conclusão dos testes o relatório do Allure pode ser gerado através de um link, a partir do comando a seguir:

    allure serve allure-results


## Suporte
Se precisar, entre em contato através do email:
josephfeliped@gmail.com


# desafio-django

**Desafio Django**

link: https://sistema-vacina-desafio.herokuapp.com/

## Urls do Sistema no Heroku

#### Clique no link acima e após a barra adicione qualquer trecho a seguir para utilizar o sistema: 

##### Modulo Adminstrativo

* `modulo_adm/estabelecimento`

* `modulo_adm/fabricante` 
   
* `modulo_adm/vacina`

* `modulo_adm/estoque`

* `modulo_adm/estoque_item`

* `modulo_adm/profissional`

* `modulo_adm/coordenador`

##### Modulo Cartão de Vacina

* `modulo_cartao_vacina/paciente`

* `modulo_cartao_vacina/cartao`

##### Modulo Agendamento

* `modulo_agendamento/agenda`

* `modulo_agendamento/fila`

## Ambiente de desenvolvimento

* Python 3.9
* PostgreSQL 12
* Docker
* docker-compose

## Pré requisito para roda o projeto: docker e docker-compose

#### Tutorial para instalação do docker no ubuntu

* [Tutorial oficial](https://docs.docker.com/engine/install/ubuntu/)

#### Tutorial para instalar o docker-compose no linux

* [Tutorial oficial](https://docs.docker.com/compose/install/)

## Passos para roda o projeto

#### Clonar o projeto

* Abra o terminal, entre na pasta onde deseja clonar o projeto e cole o seguinte comando: 

`https://github.com/isaquekaio/desafio-django.git`

#### Depois entre na pasta do projeto

* Digite no terminal: 

`cd desafio-django`

#### Para roda o projeto

* Dentro da pasta desafio-django, digite o seguinte comando:

`docker-compose up -d`

#### Para usar o sistema

* Abra o seu navegador de internet e digite: 

`localhost:8000`
